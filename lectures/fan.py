"""Shu nusxadagi darslik (fan) ma'lumotlari.

Boshqa fan uchun sayt yasashda loyiha nusxalanadi va faqat shu fayl hamda data/maruza.docx almashtiriladi:
bo'limlar, har bir mavzuning 3D ko'rgazmasi, muallif, YouTube video darslari va materiallar shu yerda.
Bu fanning ma'ruza matnlari data/manba/ papkasida yozilgan (ishchi dasturda faqat mavzular ro'yxati bor edi).
"""
from pathlib import Path

SLUG = 'axborot-xavfsizligi'   # docx dagi fan nomidan: «KM.1. Axborot xavfsizligi»
AUTHOR = 'Oydin Tashtemirova'

IMG = Path(__file__).resolve().parent / 'static' / 'lectures' / 'img'
PHOTO = IMG / 'muallif.jpg'   # ustoz (portret)
COVER = IMG / 'muqova.jpg'    # bosh sahifa foni: ustoz dars o'tayotgan payt

# docx muqovasida yo'q ma'lumotlar (modul, yo'nalish va soatlar docx'dan olinadi: 22 nazariy, 28 amaliy mavzu)
COURSE = {
    'subtitle': 'Interaktiv elektron darslik: 50 ta ma’ruza, 3D ko‘rgazmalar, video darslar, taqdimotlar, '
                '250 ta test va amaliy topshiriqlar.',
}

# (bo'lim nomi, birinchi mavzu, oxirgi mavzu, rang, belgi) — ishchi dasturdagi o'qitish natijalari bo'yicha
PARTS = [
    ('Axborot xavfsizligi tushunchalari va tamoyillari', 1, 6, '#0E7C7B', 'shield'),
    ('Kiberhujumlar, tahdidlar va xavflarni baholash', 7, 14, '#9E2A3A', 'alert'),
    ('Parol, autentifikatsiya va 2FA', 15, 21, '#B07D1E', 'key'),
    ('Internetda xavfsiz ishlash va phishing', 22, 27, '#C2562D', 'mail'),
    ('Tarmoq, Wi-Fi va shaxsiy ma’lumotlar himoyasi', 28, 32, '#24508F', 'wifi'),
    ('Antivirus, shifrlash va himoya vositalari', 33, 39, '#3F7D4E', 'lock'),
    ('Huquqiy me’yorlar va kiberetika', 40, 45, '#2F68B8', 'scale'),
    ('Himoya choralarini tanlash va baholash', 46, 50, '#D86A3E', 'target'),
]

# mavzu raqami -> 3D ko'rgazma (lectures/scenes.py)
SCENES = {
    1: 'shield', 2: 'pulse', 3: 'layers', 4: 'flow', 5: 'gear', 6: 'monitor', 7: 'bug', 8: 'siren', 9: 'safety',
    10: 'pulse', 11: 'tools', 12: 'siren', 13: 'layers', 14: 'flow', 15: 'password', 16: 'password', 17: 'lock',
    18: 'lock', 19: 'gear', 20: 'password', 21: 'lock', 22: 'network', 23: 'monitor', 24: 'shield', 25: 'phish',
    26: 'phish', 27: 'bug', 28: 'network', 29: 'shield', 30: 'wifi', 31: 'lock', 32: 'monitor', 33: 'shield',
    34: 'os', 35: 'bug', 36: 'lock', 37: 'disk', 38: 'layers', 39: 'chip', 40: 'law', 41: 'law', 42: 'law',
    43: 'monitor', 44: 'siren', 45: 'network', 46: 'shield', 47: 'flow', 48: 'tools', 49: 'pulse', 50: 'lock',
}

# mavzu raqami -> [(YouTube video ID, tili)]   tanlov: mavzuga mosligi, o'zbek tilidagilar birinchi
VIDEOS = {
    1: [('ESeGmFZsnXw', 'uz'), ('unTavenYgDo', 'uz'), ('BtNg2wbo--Q', 'uz')],
    2: [('oNgr1RBCmQc', 'uz'), ('eO7FffcsudQ', 'uz'), ('2DBB2TXwU-E', 'uz')],
    3: [('XXZww2DpHrg', 'uz'), ('thwAtrAR4ng', 'uz'), ('Uo38pEKrQ4k', 'uz')],
    4: [('C8C4ae-BWyQ', 'uz'), ('1ExsjKcNd-A', 'uz'), ('0CGpAlJt7nQ', 'uz')],
    5: [('N7bzLps0e6s', 'uz'), ('deEZvxMx3Ag', 'uz'), ('2OWkRUPCfdI', 'uz')],
    6: [('lo6KEcbnqGs', 'uz'), ('DiVWeUC7Nmg', 'uz'), ('c-_YlWcBZUs', 'uz')],
    7: [('MGcAHkCfhMA', 'uz'), ('MeBqe8WK9zc', 'uz'), ('nNsUIqY7ErQ', 'uz')],
    8: [('hYucr9ZnET0', 'uz'), ('oItvaetxexs', 'uz'), ('ZcwNuN_CSp8', 'uz')],
    9: [('9t4qjZu4tdM', 'uz'), ('kAU1Pj8cp5k', 'uz'), ('D1wnIoQsOEs', 'uz')],
    10: [('TIImXaRztLM', 'uz'), ('ylZHT20wUv8', 'en'), ('x-JMCUN9sIQ', 'en')],
    11: [('9YMx2xfJ6HU', 'uz'), ('G8iys9PqnBw', 'uz'), ('8UZFpCQeXnM', 'en')],
    12: [('cMms2YHAoAU', 'uz'), ('KhB6yilSG6E', 'uz'), ('4CUqbn7TYYs', 'uz')],
    13: [('suKO1ljdUdA', 'uz'), ('itu2nf9zgIM', 'uz'), ('Hjik8rssprw', 'uz')],
    14: [('k91v4zPI9aY', 'uz'), ('Cf2-BKS6-JE', 'uz'), ('6x-2qsE8NKo', 'uz')],
    15: [('aONrCMaLyTs', 'uz'), ('yGqnzugayTQ', 'uz'), ('03s7GGIJbBk', 'uz')],
    16: [('Km0SOKXVY50', 'uz'), ('f_x3ft5DY-8', 'uz'), ('BBt0lBldnLQ', 'uz')],
    17: [('wtWNSAAXOIs', 'uz'), ('_eLq8jO1T9o', 'uz'), ('mblWYKLNXcY', 'uz')],
    18: [('nod6knE-T0o', 'uz'), ('Y9c0_E-rqCY', 'uz'), ('IEYU_MetC3I', 'uz')],
    19: [('hK9Snkwe6Lc', 'uz'), ('D31t8Jg_AHU', 'uz'), ('TWf5mHwhjBQ', 'uz')],
    20: [('oLVkcQikKc0', 'uz'), ('GhuHqjr6jPk', 'uz'), ('mTTpBcRIAN8', 'uz')],
    21: [('dYIdBHJOBBg', 'uz'), ('gCZkZ8HMZ14', 'uz'), ('f7cZywbJabw', 'uz')],
    22: [('fUgTf3ProxA', 'uz'), ('R59EupSOlqI', 'uz'), ('AVmi5sWIJGc', 'uz')],
    23: [('NxM8Xz20Uf8', 'uz'), ('FCUQG4hwa5o', 'uz'), ('SaMau86QZfc', 'uz')],
    24: [('rsYxqHdERuw', 'uz'), ('7ngTyWu_1-0', 'uz'), ('-ElfMo6rSGg', 'uz')],
    25: [('F83JyH8d2Ps', 'uz'), ('tXXfryySj0c', 'uz'), ('uWCNnIw7aoM', 'uz')],
    26: [('-2GTuWnBSNU', 'uz'), ('PNDBXpjo0cs', 'uz'), ('q-2bKS2NrKo', 'uz')],
    27: [('4bb59b4ImNM', 'uz'), ('OcI-_k-JhCY', 'uz'), ('GsAbdGZAqyY', 'uz')],
    28: [('aiJCpXMo_h0', 'uz'), ('AEHK_2RT30c', 'uz'), ('JIz1FDJ2uGM', 'uz')],
    29: [('EdkhyXP7jp4', 'uz'), ('XCyC6skaaJg', 'ru'), ('VBxunkRH3X0', 'ru')],
    30: [('CcEGght-IeQ', 'uz'), ('lcjjI9tezMA', 'uz'), ('1cPGR17nnRQ', 'uz')],
    31: [('JD8m6T7tv7c', 'uz'), ('epI7NANklQA', 'uz'), ('iljpueGUhkY', 'uz')],
    32: [('U9CQqCUpR8E', 'uz'), ('T8zNebKq1gM', 'uz'), ('AcALDnXdRwQ', 'uz')],
    33: [('rOC7-_NLJZc', 'uz'), ('6MywbJGudCI', 'uz'), ('EXxJtCYjOsg', 'uz')],
    34: [('yZAFzAGPyDA', 'uz'), ('8O8N6ukuvfI', 'uz'), ('Dw9tPdLvQkc', 'uz')],
    35: [('1mzYjZtj7dg', 'uz'), ('dnEuULuGrB0', 'uz'), ('Ds8qp8U1H0g', 'uz')],
    36: [('dXbEzhWHmOc', 'uz'), ('SHfj41HWa_0', 'uz'), ('DukDIU7hP0w', 'uz')],
    37: [('QW8nuRTJRN0', 'uz'), ('Oc03-ri70yQ', 'uz'), ('pQzKnLOF6OY', 'uz')],
    38: [('uuLu4A9iDVI', 'uz'), ('-9P_z2GcKl4', 'uz'), ('KluTFZc-1Zs', 'uz')],
    39: [('mjfYfBUuEnE', 'uz'), ('rdeyK5skYe4', 'uz'), ('7ng_tA4_Jn8', 'ru')],
    40: [('k1F7FMihP18', 'uz'), ('ORWA9JpKFqQ', 'uz'), ('wJMIDoGKu00', 'uz')],
    41: [('p_9Ci-poYNU', 'uz'), ('ZUf41HyPnKs', 'uz'), ('2XomOrc24_o', 'uz')],
    42: [('zf0q6CTE8Lo', 'uz'), ('L1G9QPnLr0A', 'uz'), ('OHJVyegWgRU', 'uz')],
    43: [('WpQhfDV6zgY', 'uz'), ('K8_w1SJhKRg', 'uz'), ('lA8_LaQNs54', 'uz')],
    44: [('LovRfgPXcqE', 'uz'), ('bDqoJ-ExZeA', 'uz'), ('y76hswVOhuk', 'uz')],
    45: [('fHMGbgP53Qk', 'uz'), ('Cy1VDhb5OVk', 'uz'), ('jMZ5G2LXmow', 'uz')],
    46: [('ZQvnu13pxJs', 'uz'), ('rfU2KUjbhN8', 'uz'), ('mKT4KHX2HR4', 'uz')],
    47: [('JUspWldNQ6g', 'uz'), ('pjfQ_MkVKSc', 'uz'), ('wMuY81uUWUw', 'uz')],
    48: [('8cL7Lw2VAdE', 'uz'), ('iEbkTrVyRds', 'uz'), ('_Y-ffkJkq7Y', 'uz')],
    49: [('5rrz5rx6pQA', 'uz'), ('Acat_yzHacc', 'uz'), ('kUQwtMJunA8', 'uz')],
    50: [('4hICFLlKVog', 'uz'), ('7Q1ZqC4DptQ', 'uz'), ('YzmVmxENiok', 'uz')],
}

# fanga oid foydali havolalar (Materiallar bo'limi): (nomi, havola, izoh, mavzu raqami yoki None)
MATERIALS = [
    ('«Kiberxavfsizlik to‘g‘risida»gi Qonun (O‘RQ-764, 15.04.2022)', 'https://lex.uz/docs/5960604',
     'Qonunning rasmiy matni · lex.uz', 40),
    ('«Shaxsga doir ma’lumotlar to‘g‘risida»gi Qonun (O‘RQ-547, 02.07.2019)', 'https://lex.uz/docs/4396419',
     'Qonunning rasmiy matni · lex.uz', 31),
    ('«Axborotlashtirish to‘g‘risida»gi Qonun (560-II, 11.12.2003)', 'https://lex.uz/docs/82956',
     'Qonunning rasmiy matni · lex.uz', 40),
    ('«Mualliflik huquqi va turdosh huquqlar to‘g‘risida»gi Qonun (O‘RQ-42, 20.07.2006)', 'https://lex.uz/docs/1022944',
     'Qonunning rasmiy matni · lex.uz', 41),
    ('O‘zbekiston Respublikasining Jinoyat kodeksi', 'https://lex.uz/docs/111453',
     'Axborot texnologiyalari sohasidagi jinoyatlar bobi · lex.uz', 40),
    ('Kiberxavfsizlik markazi', 'https://csec.uz', 'Rasmiy tavsiyalar, ogohlantirishlar va statistika', 6),
    ('UZCERT — kompyuter hodisalariga javob berish xizmati', 'https://uzcert.uz',
     'Zaifliklar va tahdidlar haqida ogohlantirishlar', 12),
    ('VirusTotal — fayl va havolalarni tekshirish', 'https://www.virustotal.com',
     '70 ga yaqin antivirus bilan onlayn tekshiruv', 27),
    ('Have I Been Pwned — pochta sizib chiqqanini tekshirish', 'https://haveibeenpwned.com',
     'Ma’lumotlar sizib chiqishida qatnashganini aniqlash', 16),
    ('Google xavfsizlik tekshiruvi', 'https://myaccount.google.com/security-checkup',
     'Google hisobi himoyasini bosqichma-bosqich tekshirish', 21),
    ('Google Safe Browsing — sayt holati', 'https://transparencyreport.google.com/safe-browsing/search',
     'Saytning xavfli yoki xavfsizligini tekshirish', 24),
    ('ZiyoNET ta’lim portali', 'https://ziyonet.uz', 'O‘quv materiallari va elektron kutubxona', None),
]
