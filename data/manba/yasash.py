"""data/manba/*.py dagi ma'ruza matnlaridan data/maruza.docx yasaydi (o'quv-uslubiy majmua formatida).

    python data/manba/yasash.py

Ishchi dastur (PDF) da faqat mavzular ro'yxati bor edi — ma'ruza matnlari, testlar va savollar shu papkada yozilgan.
Matnni o'zgartirsangiz: shu buyruq -> python manage.py import_docx -> taqdimotlar -> sayt_yasash.
Tayyor docx'ni Word'da ochib chop etish ham mumkin.
"""
import html
import re
import sys
import zipfile
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

import kurs  # noqa: E402  (muqova, reja, mustaqil ta'lim)
from mavzular_1 import MAVZULAR as M1  # noqa: E402
from mavzular_2 import MAVZULAR as M2  # noqa: E402
from mavzular_3 import MAVZULAR as M3  # noqa: E402
from mavzular_4 import MAVZULAR as M4  # noqa: E402
from mavzular_5 import MAVZULAR as M5  # noqa: E402

MAVZULAR = M1 + M2 + M3 + M4 + M5


def _spread(topics):
    """To'g'ri javobi «a» bo'lgan savollarda javobni boshqa o'ringa surib, a/b/c/d ni tekis taqsimlaydi."""
    for n, t in enumerate(topics, 1):
        fixed = []
        for i, (q, opts, ans) in enumerate(t['testlar']):
            if ans == 'a' and (n + i) % 3 == 0:  # «a» javoblarining uchdan biri b/c/d ga
                k = 1 + (n + i) // 3 % 3
                opts = opts[1:k + 1] + [opts[0]] + opts[k + 1:]
                ans = 'abcd'[k]
            fixed.append((q, opts, ans))
        t['testlar'] = fixed


_spread(MAVZULAR)
OUT = HERE.parent / 'maruza.docx'

W_NS = 'http://schemas.openxmlformats.org/wordprocessingml/2006/main'
BLUE = '2E75B6'
TYPE = {'N': 'Nazariy', 'A': 'Amaliy'}


# ------------------------------------------------------------------ XML bo'laklari
def esc(s):
    return html.escape(s, quote=False)


def runs(text, bold=False, color=None, size=None):
    """'**qalin**' va '`kod`' belgilarini Word run'lariga aylantiradi."""
    out = []
    for part in re.split(r'(\*\*.+?\*\*|`[^`]+`)', text):
        if not part:
            continue
        b, mono = bold, False
        if part.startswith('**') and part.endswith('**'):
            part, b = part[2:-2], True
        elif part.startswith('`') and part.endswith('`'):
            part, mono = part[1:-1], True
        rpr = ''
        if mono:
            rpr += '<w:rFonts w:ascii="Courier New" w:hAnsi="Courier New" w:cs="Courier New"/>'
        if b:
            rpr += '<w:b/>'
        if color:
            rpr += f'<w:color w:val="{color}"/>'
        if size:
            rpr += f'<w:sz w:val="{size}"/>'
        out.append(f'<w:r>{f"<w:rPr>{rpr}</w:rPr>" if rpr else ""}<w:t xml:space="preserve">{esc(part)}</w:t></w:r>')
    return ''.join(out)


def p(text, *, bold=False, color=None, size=None, lst=None, align=None, style=None):
    ppr = ''
    if style:
        ppr += f'<w:pStyle w:val="{style}"/>'
    if lst:
        ppr += f'<w:numPr><w:ilvl w:val="0"/><w:numId w:val="{1 if lst == "bullet" else 2}"/></w:numPr>'
    if align:
        ppr += f'<w:jc w:val="{align}"/>'
    return f'<w:p>{f"<w:pPr>{ppr}</w:pPr>" if ppr else ""}{runs(text, bold, color, size)}</w:p>'


def cell(text, header=False, width=None):
    lines = text.split('\n') if isinstance(text, str) else text
    shade = '<w:shd w:val="clear" w:color="auto" w:fill="DEEAF6"/>' if header else ''
    tw = f'<w:tcW w:w="{width}" w:type="dxa"/>' if width else ''
    paras = ''.join(p(x, bold=header) for x in lines) or '<w:p/>'
    return f'<w:tc><w:tcPr>{tw}{shade}</w:tcPr>{paras}</w:tc>'


def table(rows, header=True, widths=None):
    border = ''.join(f'<w:{s} w:val="single" w:sz="4" w:space="0" w:color="8EAADB"/>'
                     for s in ('top', 'left', 'bottom', 'right', 'insideH', 'insideV'))
    trs = ''.join(
        '<w:tr>' + ''.join(cell(c, header and i == 0, widths[j] if widths else None) for j, c in enumerate(r)) + '</w:tr>'
        for i, r in enumerate(rows))
    return (f'<w:tbl><w:tblPr><w:tblW w:w="5000" w:type="pct"/><w:tblBorders>{border}</w:tblBorders></w:tblPr>'
            f'{trs}</w:tbl>{p("")}')


def heading(text):
    return p(text, bold=True, color=BLUE, size=30, align='center')


# ------------------------------------------------------------------ ma'ruza matni (sodda belgilash)
def body(text):
    """Bo'lim matni: '## sarlavha', '- ro'yxat bandi', '| jadval | qatori', qolgani — xatboshi."""
    out, rows = [], []

    def flush():
        if rows:
            out.append(table(rows))
            rows.clear()

    for line in text.strip().split('\n'):
        line = line.strip()
        if not line:
            continue
        if line.startswith('|'):
            rows.append([c.strip() for c in line.strip('|').split('|')])
            continue
        flush()
        if line.startswith('## '):
            out.append(p(line[3:], bold=True, color=BLUE))
        elif line.startswith('- '):
            out.append(p(line[2:], lst='bullet'))
        else:
            out.append(p(line))
    flush()
    return ''.join(out)


# ------------------------------------------------------------------ dars modeli va texnologik xarita
def model_table(t):
    kind = TYPE[t['type']]
    reja = '\n'.join(f'{i}. {r}.' for i, r in enumerate(t['reja'], 1))
    vaz = ['Pedagogik vazifalar:'] + [f'{i}. «{r}» bo‘yicha tushuncha berish;' for i, r in enumerate(t['reja'], 1)]
    vaz += ['O‘quv faoliyati natijalari:'] + [f'{i}. {r} bo‘yicha bilim va ko‘nikmaga ega bo‘ladilar;'
                                             for i, r in enumerate(t['reja'], 1)]
    shakl = ('Nazariy — yangi bilimlarni o‘zlashtirish bo‘yicha o‘quv mashg‘uloti' if kind == 'Nazariy'
             else 'Amaliy — ko‘nikma va malakalarni shakllantirish bo‘yicha o‘quv mashg‘uloti')
    sharoit = ('Multimedia vositalari bilan jihozlangan o‘quv xonasi' if kind == 'Nazariy'
               else 'Internetga ulangan kompyuterlar bilan jihozlangan laboratoriya')
    rows = [
        ['Ko‘rsatkich parametrlari', 'Tavsifi va mazmuni'],
        ['Mashg‘ulot vaqti va o‘quvchilar soni', 'Mashg‘ulot vaqti: **80 daqiqa** | O‘quvchilar soni: **26–30 gacha**'],
        ['Mashg‘ulot shakli va turi', shakl],
        ['O‘quv mashg‘ulot rejasi', reja],
        ['O‘quv mashg‘ulotining maqsadi', t['maqsad']],
        ['Mashg‘ulotdan kutilayotgan natijalar', t['natija']],
        ['Pedagogik vazifalar va natijalar', '\n'.join(vaz)],
        ['O‘qitish metodlari', t.get('metod') or ('Ma’ruza, aqliy hujum, savol-javob, «Klaster», namoyish'
                                                 if kind == 'Nazariy' else
                                                 'Instruktaj, namoyish etish, amaliy topshiriq, juftlikda ishlash, o‘zaro baholash')],
        ['O‘qitish vositalari', t.get('vosita') or 'O‘MT, ma’ruzalar matni, proyektor, kompyuter, taqdimot slaydlari, internet'],
        ['O‘quv faoliyatini tashkil etish', 'Jamoaviy, guruhli, juftlikda, yakka tartibda'],
        ['O‘qitish sharoiti', sharoit],
        ['Qaytar aloqaning yo‘l va vositalari', 'Kuzatish, savol-javob, test, o‘zaro baholash'],
    ]
    return table(rows, widths=[3200, 6400])


def xarita_table(t):
    amaliy = t['type'] == 'A'
    asosiy = ['Tayanch bilimlarni faollashtirish:',
              '1. Uyga berilgan vazifani nazorat qiladi, o‘tilgan mavzu bo‘yicha savollar beradi (1-ilova).',
              'Maqsad va vazifalarni belgilash:',
              '2. Mashg‘ulotning nomi, rejasi, maqsadi va kutilayotgan natijalari bilan tanishtiradi.',
              '3. Baholash mezonlari bilan tanishtiradi (2-ilova).']
    if amaliy:
        asosiy += ['Yo‘riqnoma va namoyish:', '4. Ishni bajarish tartibini kompyuterda bosqichma-bosqich ko‘rsatadi.',
                   'Amaliy ish:', '5. O‘quvchilarni juftliklarga bo‘lib, topshiriqni beradi va bajarilishini kuzatadi.',
                   '6. Xatolarni tuzatadi, natijalarni nazorat varag‘i asosida baholaydi.']
    else:
        asosiy += ['Yangi mavzu bayoni:', '4. Mavzuni reja asosida taqdimot va video yordamida tushuntiradi.',
                   '5. Real hayotdan misollar keltiradi, «Klaster» usulida asosiy tushunchalarni yozdiradi.']
    asosiy += ['Mustahkamlash:', f'{7 if amaliy else 6}. Mustahkamlash savollari va test topshiriqlarini beradi (3-ilova).']
    rows = [
        ['Ta’lim shakli, ish bosqichlari va vaqti', 'O‘qituvchining faoliyati mazmuni', 'O‘quvchining faoliyati mazmuni'],
        ['**1. O‘quv mashg‘ulotiga kirish** (5 daqiqa)',
         'Tashkiliy qism:\n• Davomat va o‘quvchilarning mashg‘ulotga tayyorgarligini tekshiradi.\n'
         '• Kompyuter xonasida ishlash qoidalarini eslatadi.',
         '• Mashg‘ulotga tayyorlanadilar.\n• Navbatchilar axborot beradilar.'],
        ['**2. Asosiy bosqich** (65 daqiqa)', '\n'.join(asosiy),
         '• Savollarga javob beradilar.\n• Asosiy tushunchalarni yozib oladilar.\n'
         + ('• Topshiriqni kompyuterda bajaradilar.\n• Bir-birini nazorat varag‘i asosida baholaydilar.\n'
            if amaliy else '• Klaster tuzadilar, misollar keltiradilar.\n')
         + '• Test topshiriqlarini bajaradilar.'],
        ['**3. Yakuniy bosqich** (10 daqiqa)',
         'Mashg‘ulot yakuni:\n1. Mavzuni umumlashtiradi, faol o‘quvchilarni baholaydi va rag‘batlantiradi.\n'
         'Uyga vazifa berilishi:\n2. Mustaqil ta’lim topshirig‘ini va uni bajarish yo‘riqnomasini beradi.',
         '• O‘z-o‘zini va o‘zaro baholashni o‘tkazadilar.\n• Topshiriqni yozib oladilar.'],
    ]
    return table(rows, widths=[2400, 4400, 2800])


GRADING = {
    'N': [['Baho', 'Mezon'],
          ['5 (a’lo)', 'Mavzu bo‘yicha savollarga to‘liq va asoslab javob beradi, real hayotdan misollar keltiradi'],
          ['4 (yaxshi)', 'Savollarga to‘g‘ri javob beradi, ayrim kichik noaniqliklarga yo‘l qo‘yadi'],
          ['3 (qoniqarli)', 'Asosiy tushunchalarni qisman biladi, misollar keltirishda qiynaladi'],
          ['2 (qoniqarsiz)', 'Asosiy tushunchalarni bilmaydi yoki noto‘g‘ri tushuntiradi']],
    'A': [['Baho', 'Mezon'],
          ['5 (a’lo)', 'Amaliy topshiriqni xatosiz, to‘g‘ri ketma-ketlikda mustaqil bajaradi va natijani izohlaydi'],
          ['4 (yaxshi)', 'Topshiriqni bajaradi, 1–2 ta kichik xatoga yo‘l qo‘yadi va ularni o‘zi tuzatadi'],
          ['3 (qoniqarli)', 'Topshiriqni o‘qituvchi yordamida bajaradi, ketma-ketlikda xatolar bor'],
          ['2 (qoniqarsiz)', 'Topshiriqni bajara olmaydi yoki xavfsizlik talablarini buzadi']],
}


def topic_xml(t):
    x = [p(f'Mavzu: {TYPE[t["type"]]}. {t["title"]}', bold=True, color=BLUE, size=28),
         p('O‘QUV MASHG‘ULOTINING TA’LIM TEXNOLOGIYASI MODELI', bold=True, align='center'),
         model_table(t),
         p('O‘QUV MASHG‘ULOTINING TEXNOLOGIK XARITASI', bold=True, align='center'),
         xarita_table(t),
         p('REJA:', bold=True)]
    x += [p(r + '.', lst='num') for r in t['reja']]
    assert len(t['reja']) == len(t['bolimlar']), t['title']
    for i, (r, matn) in enumerate(zip(t['reja'], t['bolimlar']), 1):
        x.append(p(f'{i}-REJA BO‘YICHA: {r.upper()}', bold=True))
        x.append(body(matn))
    x.append(p('1-ILOVA. Tayanch bilimlarni faollashtirish uchun savollar', bold=True))
    x += [p(q, lst='bullet') for q in t['oldingi']]
    x.append(p('2-ILOVA. Baholash mezonlari', bold=True))
    x.append(table(GRADING[t['type']], widths=[2400, 7200]))
    x.append(p('3-ILOVA. Mustahkamlash uchun savollar', bold=True))
    x += [p(q, lst='bullet') for q in t['savollar']]
    x.append(p('Test topshiriqlari', bold=True))
    for i, (q, opts, _) in enumerate(t['testlar'], 1):
        assert len(opts) == 4, (t['title'], q)
        x.append(p(f'{i}. {q}'))
        x += [p(f'{ch}) {o}') for ch, o in zip('abcd', opts)]
    x.append(p('MUSTAQIL TA’LIM UCHUN TOPSHIRIQLAR', bold=True))
    x += [p(f'**Topshiriq {i}:** {m}') for i, m in enumerate(t['mustaqil'], 1)]
    x.append(p('Adabiyotlar', bold=True))
    x += [p(a) for a in kurs.ADABIYOT]
    return ''.join(x)


def head_xml():
    x = [p(s, bold=True, align='center') for s in kurs.MUQOVA]
    x.append(p(''))
    x.append(p('O‘QUV-TEMATIK REJA', bold=True, align='center'))
    rows = [['№', 'Mavzu nomi', 'Turi', 'Soat']]
    rows += [[str(i), t['title'], TYPE[t['type']], '2'] for i, t in enumerate(MAVZULAR, 1)]
    x.append(table(rows, widths=[700, 6500, 1400, 1000]))
    x.append(p('MUSTAQIL TA’LIM MAVZULARI', bold=True, align='center'))
    rows = [['№', 'Mustaqil ta’lim mavzusi', 'Mavzular', 'Soat']]
    rows += [[str(i), title, rng, str(h)] for i, (title, rng, h) in enumerate(kurs.MUSTAQIL, 1)]
    x.append(table(rows, widths=[700, 6500, 1400, 1000]))
    x.append(p('ISHLAB CHIQARISH AMALIYOTI', bold=True, align='center'))
    rows = [['№', 'Ishlab chiqarish amaliyoti mavzusi', 'Soat']]
    rows += [[str(i), title, str(h)] for i, (title, h) in enumerate(kurs.AMALIYOT, 1)]
    x.append(table(rows, widths=[700, 7900, 1000]))
    return ''.join(x)


def answers_xml():
    x = [p('TEST TOPSHIRIQLARINING JAVOBLARI', bold=True, align='center')]
    rows = [[f'{i}-mavzu'] + [a for _, _, a in t['testlar']] for i, t in enumerate(MAVZULAR, 1)]
    width = max(len(r) for r in rows)
    rows = [r + [''] * (width - len(r)) for r in rows]
    x.append(table(rows, header=False))
    return ''.join(x)


# ------------------------------------------------------------------ docx paketi
CONTENT_TYPES = (
    '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
    '<Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types">'
    '<Default Extension="rels" ContentType="application/vnd.openxmlformats-package.relationships+xml"/>'
    '<Default Extension="xml" ContentType="application/xml"/>'
    '<Override PartName="/word/document.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.document.main+xml"/>'
    '<Override PartName="/word/styles.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.styles+xml"/>'
    '<Override PartName="/word/numbering.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.numbering+xml"/>'
    '</Types>')
RELS = ('<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
        '<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">'
        '<Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/officeDocument" Target="word/document.xml"/>'
        '</Relationships>')
DOC_RELS = ('<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
            '<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">'
            '<Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/styles" Target="styles.xml"/>'
            '<Relationship Id="rId2" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/numbering" Target="numbering.xml"/>'
            '</Relationships>')
STYLES = (f'<?xml version="1.0" encoding="UTF-8" standalone="yes"?><w:styles xmlns:w="{W_NS}">'
          '<w:docDefaults><w:rPrDefault><w:rPr><w:rFonts w:ascii="Times New Roman" w:hAnsi="Times New Roman" w:cs="Times New Roman"/>'
          '<w:sz w:val="26"/></w:rPr></w:rPrDefault><w:pPrDefault><w:pPr><w:spacing w:after="80" w:line="264" w:lineRule="auto"/>'
          '<w:jc w:val="both"/></w:pPr></w:pPrDefault></w:docDefaults>'
          '<w:style w:type="paragraph" w:default="1" w:styleId="Normal"><w:name w:val="Normal"/></w:style></w:styles>')


def numbering():
    def abstract(i, fmt, text):
        return (f'<w:abstractNum w:abstractNumId="{i}"><w:lvl w:ilvl="0"><w:start w:val="1"/><w:numFmt w:val="{fmt}"/>'
                f'<w:lvlText w:val="{text}"/><w:lvlJc w:val="left"/><w:pPr><w:ind w:left="720" w:hanging="360"/></w:pPr>'
                '</w:lvl></w:abstractNum>')
    return (f'<?xml version="1.0" encoding="UTF-8" standalone="yes"?><w:numbering xmlns:w="{W_NS}">'
            + abstract(0, 'bullet', '•') + abstract(1, 'decimal', '%1.')
            + '<w:num w:numId="1"><w:abstractNumId w:val="0"/></w:num><w:num w:numId="2"><w:abstractNumId w:val="1"/></w:num>'
            '</w:numbering>')


def build(out=OUT):
    page = ('<w:sectPr><w:pgSz w:w="11906" w:h="16838"/>'
            '<w:pgMar w:top="1134" w:right="850" w:bottom="1134" w:left="1418" w:header="708" w:footer="708"/></w:sectPr>')
    brk = '<w:p><w:r><w:br w:type="page"/></w:r></w:p>'
    doc = (f'<?xml version="1.0" encoding="UTF-8" standalone="yes"?><w:document xmlns:w="{W_NS}"><w:body>'
           + head_xml() + brk + brk.join(topic_xml(t) for t in MAVZULAR) + brk + answers_xml() + page
           + '</w:body></w:document>')
    with zipfile.ZipFile(out, 'w', zipfile.ZIP_DEFLATED) as z:
        z.writestr('[Content_Types].xml', CONTENT_TYPES)
        z.writestr('_rels/.rels', RELS)
        z.writestr('word/_rels/document.xml.rels', DOC_RELS)
        z.writestr('word/document.xml', doc)
        z.writestr('word/styles.xml', STYLES)
        z.writestr('word/numbering.xml', numbering())
    return out


if __name__ == '__main__':
    path = build()
    n_test = sum(len(t['testlar']) for t in MAVZULAR)
    print(f'{path}: {len(MAVZULAR)} ta mavzu, {n_test} ta test')
