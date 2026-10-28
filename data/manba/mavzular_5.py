"""41–50-mavzular: mualliflik huquqi, kiberetika, himoya choralarini tanlash, qo'llash va baholash."""

MAVZULAR = [
    # ------------------------------------------------------------------ 41
    {
        'type': 'A',
        'title': 'Axborotdan foydalanishda mualliflik huquqi va plagiatni aniqlash',
        'reja': ['Mualliflik huquqi va dasturiy ta’minot litsenziyalari',
                 'Amaliy ish: plagiatni aniqlash usullari',
                 'Manbalarga to‘g‘ri havola berish va qonuniy foydalanish'],
        'maqsad': 'O‘quvchilarda dasturiy ta’minot litsenziyalarini farqlash, matn va rasm plagiatini aniqlash hamda '
                  'manbalarga to‘g‘ri havola berish ko‘nikmasini shakllantirish.',
        'natija': 'O‘quvchilar litsenziya turlarini aniqlaydi, qidiruv tizimi va teskari rasm qidiruvi orqali '
                  'plagiatni topadi, Creative Commons litsenziyali materiallardan to‘g‘ri foydalanadi va iqtibos keltiradi.',
        'vosita': 'Internetga ulangan kompyuterlar, o‘qituvchi tayyorlagan matn va rasm namunalari, brauzer, proyektor',
        'bolimlar': [
            """
## Mualliflik huquqi
- **Mualliflik huquqi** — fan, adabiyot va san’at asarlari, jumladan kompyuter dasturlari va ma’lumotlar bazalari mualliflariga ularning asarlaridan foydalanish yuzasidan beriladigan huquqlar.
- **Plagiat** — birovning asari yoki uning bir qismini muallifini ko‘rsatmasdan o‘z nomidan taqdim etish.
## Dasturiy ta’minot litsenziyalari
| Litsenziya turi | Mazmuni | Misollar |
| Tijoriy (proprietar) | Pullik, nusxalash va tarqatish taqiqlangan | Windows, MS Office, Photoshop |
| Freeware | Bepul foydalanish, lekin kodi yopiq | 7-Zip, Google Chrome |
| Shareware | Sinov muddati yoki cheklangan versiya | WinRAR, ba’zi antiviruslar |
| Ochiq kodli (open source) | Bepul, kodini ko‘rish va o‘zgartirish mumkin | Linux, LibreOffice, Firefox |
| Creative Commons | Rasm, matn, musiqa uchun shartli bepul foydalanish | Wikimedia Commons materiallari |
- **Ochiq kodli dastur** — manba kodi hammaga ochiq bo‘lib, uni ko‘rish, o‘zgartirish va tarqatish ruxsat etilgan dastur.
- **Piratlik** — litsenziyalangan dastur, film yoki musiqani egasining ruxsatisiz nusxalash va tarqatish.
""",
            """
## Ishni bajarish tartibi
- **Matn plagiatini tekshirish.** O‘qituvchi bergan referatdan bitta noodatiy gapni nusxalab, qidiruv tizimida qo‘shtirnoq ichida qidiring: `"gapning aniq matni"`. Aynan shu gap uchragan saytlar topiladi.
- **Bir nechta gapni sinash.** Matnning turli qismlaridan 3–4 ta gapni tekshirib, qaysi qismi ko‘chirilganini aniqlang.
- **Teskari rasm qidiruvi.** images.google.com yoki Google Lens orqali rasmni yuklang — rasmning asl manbai va boshqa nusxalari topiladi.
- **Litsenziyani aniqlash.** Dastur yoki rasm sahifasida «License», «Лицензия», «CC BY» kabi belgilarni toping.
- **Qonuniy rasm topish.** Google rasmlar qidiruvida «Инструменты» → «Права на использование» → «Лицензии Creative Commons» filtrini qo‘llang.
- **Teskari rasm qidiruvi** — rasmni namuna sifatida berib, internetda aynan shu yoki o‘xshash rasmlarni topish usuli.
""",
            """
## Manbaga havola berish
Birovning fikri, matni yoki rasmidan foydalanilsa, albatta manba ko‘rsatiladi:
| Manba turi | Havola namunasi |
| Kitob | G‘aniyev S.K. va boshq. Axborot xavfsizligi. — Toshkent. — 45-bet. |
| Veb-sahifa | Kiberxavfsizlik markazi. Parol xavfsizligi bo‘yicha tavsiyalar. — csec.uz (murojaat sanasi: 2026-yil 20-oktyabr) |
| Rasm (CC BY) | Rasm muallifi: Ism Familiya, Wikimedia Commons, CC BY 4.0 |
## Creative Commons belgilari
| Belgi | Ma’nosi |
| BY | Muallifni ko‘rsatish shart |
| NC | Tijoriy maqsadda foydalanish mumkin emas |
| ND | O‘zgartirish mumkin emas |
| SA | O‘zgartirilgan asar ham xuddi shu litsenziyada tarqatiladi |
Manbani ko‘rsatib iqtibos keltirish plagiat hisoblanmaydi; plagiat bu manbani yashirishdir. Referat va loyiha ishlarida manbalar ro‘yxati albatta beriladi.
""",
        ],
        'oldingi': ['Axborot sohasidagi asosiy qonunlarni sanang.',
                    'Qanday javobgarlik turlari bor?',
                    'Mualliflik huquqi qaysi qonun bilan tartibga solinadi?'],
        'savollar': ['Freeware va ochiq kodli dasturning farqi nimada?',
                     'Plagiat deganda nimani tushunasiz?',
                     'Matn plagiatini qidiruv tizimida qanday tekshirish mumkin?',
                     'Teskari rasm qidiruvi qanday ishlaydi?',
                     'Creative Commons «BY» va «NC» belgilari nimani bildiradi?'],
        'testlar': [
            ('Manba kodi hammaga ochiq, bepul tarqatiladigan dastur:',
             ['Tijoriy', 'Shareware', 'Ochiq kodli (open source)', 'Trial'], 'c'),
            ('Birovning asarini muallifini ko‘rsatmasdan o‘z nomidan taqdim etish:',
             ['Plagiat', 'Iqtibos', 'Tahrir', 'Annotatsiya'], 'a'),
            ('Creative Commons litsenziyasidagi «NC» belgisi:',
             ['Muallifni ko‘rsatish shart', 'Tijoriy maqsadda foydalanish mumkin emas', 'O‘zgartirish mumkin', 'Bepul sotish mumkin'], 'b'),
            ('Aniq gapni qidirish uchun qidiruv so‘rovi qanday yoziladi?',
             ['Qavs ichida', 'Katta harflarda', 'Nuqta bilan', 'Qo‘shtirnoq ichida'], 'd'),
            ('Litsenziyali dasturni ruxsatsiz nusxalash va tarqatish:',
             ['Piratlik', 'Arxivlash', 'Zaxiralash', 'Yangilash'], 'a'),
        ],
        'mustaqil': ['Kompyuteringizdagi 10 ta dasturning litsenziya turini aniqlab, jadval tuzing.',
                     'Mustaqil ish referatingiz uchun manbalar ro‘yxatini namunaga mos rasmiylashtiring.'],
    },
    # ------------------------------------------------------------------ 42
    {
        'type': 'N',
        'title': 'Axborotdan mas’uliyatli foydalanish va kiberetika',
        'reja': ['Axborotdan mas’uliyatli foydalanish tamoyillari',
                 'Kiberetika tushunchasi va netiket qoidalari',
                 'Raqamli fuqarolik va raqamli obro‘'],
        'maqsad': 'O‘quvchilarga axborotdan mas’uliyatli foydalanish tamoyillari, kiberetika, netiket qoidalari va raqamli '
                  'fuqarolik tushunchalarini tushuntirish.',
        'natija': 'O‘quvchilar mas’uliyatli foydalanish tamoyillarini biladi, netiket qoidalariga amal qiladi va raqamli '
                  'obro‘ning ahamiyatini izohlaydi.',
        'bolimlar': [
            """
## Mas’uliyatli foydalanish nima?
- **Axborotdan mas’uliyatli foydalanish** — axborotni qonun, axloq va boshqalarning huquqlarini hurmat qilgan holda qidirish, tekshirish, saqlash va tarqatish.
Mas’uliyatli foydalanuvchi quyidagi tamoyillarga amal qiladi:
- **Haqqoniylik.** Tekshirilmagan ma’lumotni haqiqat deb tarqatmaydi.
- **Hurmat.** Boshqalarning shaxsiy hayoti, fikri va mualliflik huquqini hurmat qiladi.
- **Xavfsizlik.** O‘zi va boshqalarning ma’lumotlarini himoya qiladi.
- **Qonuniylik.** Litsenziyasiz dastur, piratlik kontenti va taqiqlangan materiallardan foydalanmaydi.
- **Oqibatni o‘ylash.** Har bir post, izoh va rasm boshqalarga qanday ta’sir qilishini oldindan o‘ylaydi.
Bitta noto‘g‘ri xabar bir necha daqiqada minglab odamga yetib boradi va vahima yoki zarar keltirishi mumkin. Shuning uchun har bir foydalanuvchi o‘zi tarqatgan axborot uchun javobgar.
""",
            """
## Kiberetika
- **Kiberetika** — kompyuter, internet va raqamli texnologiyalardan foydalanishda insonlar amal qilishi kerak bo‘lgan axloqiy me’yorlar va qoidalar majmui.
- **Netiket** — internetda muloqot qilish odobi: xat, chat va izohlarda o‘zini to‘g‘ri tutish qoidalari.
## Netiket qoidalari
| Qoida | Izoh |
| Hurmat bilan yozing | Ekran ortida ham tirik inson borligini unutmang |
| KATTA HARFLARDA yozmang | Bu baqirish deb qabul qilinadi |
| Shaxsiy xabarni ruxsatsiz tarqatmang | Skrinshot ham shaxsiy yozishma hisoblanadi |
| Guruhga mavzuga oid xabar yozing | Keraksiz reklama va zanjir xabarlar yubormang |
| Kechasi ishga oid xabar yubormang | Boshqalarning vaqtini hurmat qiling |
| Xatoni tan oling | Noto‘g‘ri ma’lumot tarqatgan bo‘lsangiz, tuzatish yozing |
Rasmiy xatlarda salomlashish, aniq mavzu satri va imzo bo‘lishi kerak. O‘qituvchiga «salom» va ismsiz bir so‘zli xabar yuborish — netiket buzilishi.
""",
            """
## Raqamli fuqarolik
- **Raqamli fuqarolik** — raqamli texnologiyalardan xavfsiz, qonuniy, axloqiy va mas’uliyatli foydalanish qobiliyati.
- **Raqamli obro‘** — inson haqida internetda shakllangan tasavvur; u postlar, izohlar, rasmlar va boshqalarning sharhlari asosida yuzaga keladi.
Ish beruvchilar va o‘quv yurtlari nomzodni tanlashda uning ijtimoiy tarmoqlardagi sahifalarini ko‘rib chiqadi. Bir necha yil oldin yozilgan qo‘pol izoh yoki nomaqbul rasm yaxshi ishga kirishga to‘sqinlik qilishi mumkin.
## Raqamli farovonlik
Mas’uliyat faqat boshqalarga emas, o‘zimizga ham tegishli:
- ekran oldida o‘tkaziladigan vaqtni nazorat qilish;
- kechasi telefondan foydalanishni cheklash;
- internetdagi «ideal hayot» rasmlari bilan o‘zini solishtirmaslik;
- kiberbullingga duch kelsa, yolg‘iz qolmay, kattalarga murojaat qilish.
""",
        ],
        'oldingi': ['Plagiat nima?',
                    'Litsenziyaning qanday turlari bor?',
                    'Manbaga havola qanday beriladi?'],
        'savollar': ['Axborotdan mas’uliyatli foydalanishning qanday tamoyillari bor?',
                     'Kiberetika nima?',
                     'Netiketning asosiy qoidalarini sanang.',
                     'Raqamli obro‘ qanday shakllanadi?',
                     'Raqamli farovonlik uchun nimalarga e’tibor berish kerak?'],
        'testlar': [
            ('Internetda muloqot qilish odobi:',
             ['Netiket', 'Phishing', 'Striming', 'Spam'], 'a'),
            ('Internetda butun xabarni KATTA HARFLARDA yozish nimani bildiradi?',
             ['Hurmatni', 'Rasmiylikni', 'Baqirishni', 'Shoshilishni'], 'c'),
            ('Inson haqida internetda shakllangan tasavvur:',
             ['Raqamli iz', 'Raqamli obro‘', 'Raqamli imzo', 'Raqamli kalit'], 'b'),
            ('Tekshirilmagan ma’lumotni tarqatmaslik qaysi tamoyilga kiradi?',
             ['Qonuniylik', 'Xavfsizlik', 'Tezkorlik', 'Haqqoniylik'], 'd'),
            ('Raqamli texnologiyalardan xavfsiz, qonuniy va axloqiy foydalanish qobiliyati:',
             ['Raqamli fuqarolik', 'Dasturlash', 'Kiberhujum', 'Avtorizatsiya'], 'a'),
        ],
        'mustaqil': ['Guruhingizning Telegram chati uchun 10 banddan iborat netiket qoidalarini yozing.',
                     '«Mening raqamli obro‘yim» mavzusida qisqa esse yozing.'],
    },
    # ------------------------------------------------------------------ 43
    {
        'type': 'A',
        'title': 'Axborotdan mas’uliyatli foydalanish',
        'reja': ['Axborotni tekshirish (fakt-cheking) usullari',
                 'Amaliy ish: xabarlarning haqqoniyligini tekshirish',
                 'Mas’uliyatli tarqatish qarorini qabul qilish'],
        'maqsad': 'O‘quvchilarda internetdagi xabarlarni manba, sana, rasm va boshqa manbalar bilan solishtirish orqali '
                  'tekshirish hamda tarqatish bo‘yicha mas’uliyatli qaror qabul qilish ko‘nikmasini shakllantirish.',
        'natija': 'O‘quvchilar xabarni fakt-cheking algoritmi bo‘yicha tekshiradi, soxta yoki buzib ko‘rsatilgan '
                  'ma’lumotni aniqlaydi va tarqatish yoki tarqatmaslik qarorini asoslaydi.',
        'vosita': 'Internetga ulangan kompyuterlar, o‘qituvchi tayyorlagan xabarlar namunalari, brauzer, tekshirish varag‘i',
        'bolimlar': [
            """
## Fakt-cheking
- **Fakt-cheking** — xabar yoki da’voning to‘g‘riligini ishonchli manbalar asosida tekshirish jarayoni.
## Tekshirish algoritmi
- **Manba kim?** Xabar rasmiy tashkilotdanmi yoki noma’lum kanaldan? Kanal qachon yaratilgan?
- **Sana qachon?** Eski voqea yangi deb tarqatilayotgan bo‘lishi mumkin.
- **Boshqa manbalar nima deydi?** Muhim voqea haqida kamida 2–3 ta ishonchli manba yozgan bo‘lishi kerak.
- **Rasm haqiqiymi?** Teskari rasm qidiruvi bilan rasmning asl manbai va sanasini aniqlang.
- **His-tuyg‘u qanday?** Xabar kuchli qo‘rquv yoki g‘azab uyg‘otsa, ehtiyot bo‘ling — manipulyatsiya bo‘lishi mumkin.
- **Kim foyda ko‘radi?** Xabar kimgadir pul, ovoz yoki obuna keltiradimi?
- **Klikbeyt** — o‘quvchini havolani bosishga undash uchun bo‘rttirilgan, aldamchi sarlavha.
""",
            """
## Ishni bajarish tartibi
O‘quvchilar juftliklarda quyidagi turdagi 6 ta xabar namunasini tekshiradi:
| № | Xabar turi |
| 1 | «Ertadan barcha maktablarda dars bekor qilinadi» — noma’lum kanal skrinshoti |
| 2 | Toshqin haqidagi rasm — aslida boshqa davlatda 5 yil oldin olingan |
| 3 | Rasmiy saytdagi yangi qonun haqidagi xabar |
| 4 | «Bu ilovani o‘rnating, 500 000 so‘m bonus olasiz» |
| 5 | Mashhur shaxs nomidan sun’iy intellekt yaratgan video |
| 6 | Ob-havo markazining ogohlantirishi |
- **Tekshirish.** Har bir xabarni algoritm bo‘yicha tekshiring, ishlatgan usulingizni yozing.
- **Rasmni tekshirish.** Google Lens orqali 2-xabardagi rasmning asl manbasini toping.
- **Rasmiy manbani topish.** 1- va 3-xabarlar uchun tegishli vazirlik rasmiy saytini yoki kanalini toping.
- **Deepfake belgilarini izlash.** 5-videoda lab harakati, ko‘z qisish, yuz chegarasidagi xiralik va ovozning g‘alatiligiga e’tibor bering.
""",
            """
## Qaror jadvali
| Xabar | Haqqoniyligi | Dalil | Qaror |
| 1 | Soxta | Rasmiy saytda bunday xabar yo‘q | Tarqatmaslik, guruhga to‘g‘ri ma’lumot yozish |
| 2 | Buzib ko‘rsatilgan | Rasm 5 yil oldingi, boshqa joydan | Tarqatmaslik |
| 3 | To‘g‘ri | Rasmiy sayt, lex.uz | Manba bilan tarqatish mumkin |
| 4 | Firibgarlik | Noma’lum ilova, «bonus» va’dasi | Tarqatmaslik, ogohlantirish |
## Mas’uliyatli tarqatish qoidalari
- Shubha bo‘lsa — tarqatmang.
- Tarqatsangiz, manbani ko‘rsating.
- Xato tarqatgan bo‘lsangiz, tuzatish yozing.
- Soxta xabarni ko‘rsangiz, platformaning «Пожаловаться» funksiyasi orqali xabar bering.
Mashg‘ulot oxirida o‘quvchilar o‘z oilaviy chatlarida tarqalgan biror xabarni eslab, uni algoritm bo‘yicha qayta baholaydi.
""",
        ],
        'oldingi': ['Kiberetika nima?',
                    'Netiket qoidalarini sanang.',
                    'Raqamli obro‘ qanday shakllanadi?'],
        'savollar': ['Fakt-cheking nima?',
                     'Xabarni tekshirish algoritmi qanday bosqichlardan iborat?',
                     'Klikbeyt sarlavhaga misol keltiring.',
                     'Rasmning asl manbasini qanday topish mumkin?',
                     'Deepfake videoning qanday belgilari bo‘ladi?'],
        'testlar': [
            ('Xabar to‘g‘riligini ishonchli manbalar asosida tekshirish:',
             ['Fakt-cheking', 'Kopirayting', 'Striming', 'Blogging'], 'a'),
            ('Bosishga undovchi bo‘rttirilgan, aldamchi sarlavha:',
             ['Annotatsiya', 'Klikbeyt', 'Xeshteg', 'Rubrika'], 'b'),
            ('Rasmning asl manbasini topish vositasi:',
             ['Kalkulyator', 'Bloknot', 'Google Lens (teskari qidiruv)', 'Arxivator'], 'c'),
            ('Xabarning haqqoniyligiga shubha bo‘lsa:',
             ['Darhol hammaga yuborish', 'Ikki marta yuborish', 'Faqat do‘stlarga yuborish', 'Tarqatmaslik'], 'd'),
            ('Kuchli qo‘rquv yoki g‘azab uyg‘otuvchi xabar nimaning belgisi bo‘lishi mumkin?',
             ['Manipulyatsiya', 'Rasmiy e’lon', 'Ob-havo ma’lumoti', 'Ilmiy maqola'], 'a'),
        ],
        'mustaqil': ['Bir hafta davomida ko‘rgan 3 ta xabarni fakt-cheking algoritmi bo‘yicha tekshirib, qaror jadvalini to‘ldiring.',
                     'Oila a’zolaringiz uchun «Xabarni tarqatishdan oldin 5 ta savol» eslatmasini tayyorlang.'],
    },
    # ------------------------------------------------------------------ 44
    {
        'type': 'N',
        'title': 'Internet ma’lumotlaridan ehtiyotkorlik bilan va mas’uliyatli foydalanish, kiberetika',
        'reja': ['Internetdagi axloqiy muammolar',
                 'Sun’iy intellekt va axborotdan foydalanish etikasi',
                 'Kiberetika qoidalari buzilganda harakatlar'],
        'maqsad': 'O‘quvchilarga internetdagi axloqiy muammolar — kiberbulling, trolling, shaxsiy hayotga aralashish, '
                  'sun’iy intellektdan foydalanish etikasi va ularga qarshi harakat qilish yo‘llarini tushuntirish.',
        'natija': 'O‘quvchilar internetdagi axloqiy muammolarni aniqlaydi, sun’iy intellektdan halol foydalanish '
                  'qoidalarini biladi va kiberbullingga duch kelganda to‘g‘ri harakat qiladi.',
        'bolimlar': [
            """
## Axloqiy muammolar
| Muammo | Mazmuni |
| Kiberbulling | Internetda insonni muntazam kamsitish, qo‘rqitish |
| Trolling | Ataylab janjal chiqarish uchun provokatsion izohlar yozish |
| Shaxsiy hayotga aralashish | Birovning rasm va yozishmalarini ruxsatsiz tarqatish |
| Soxta akkaunt | Boshqa odam nomidan sahifa ochish |
| Nafrat tili | Millat, din, jins yoki tashqi ko‘rinish bo‘yicha kamsitish |
| Internetga qaramlik | Real hayotga zarar yetkazadigan darajada ekranga bog‘lanib qolish |
- **Trolling** — internetda boshqalarni g‘azablantirish va janjal chiqarish maqsadida ataylab provokatsion xabarlar yozish.
- **Soxta akkaunt** — boshqa shaxs nomidan yoki uydirma shaxs sifatida yaratilgan ijtimoiy tarmoq sahifasi.
Birovning nomidan sahifa ochish yoki uning rasmlarini kamsituvchi maqsadda tarqatish nafaqat axloqsizlik, balki qonunbuzarlik hamdir.
""",
            """
## Sun’iy intellekt va halollik
Sun’iy intellekt yordamchilari matn yozish, tarjima qilish, rasm va kod yaratishda katta yordam beradi. Lekin ulardan foydalanishda ham axloqiy qoidalar bor:
- **Halollik.** Sun’iy intellekt yozgan ishni to‘liq o‘zingizniki deb topshirmang; o‘qituvchi ruxsat bergan hollarda va foydalanganingizni ko‘rsatib ishlating.
- **Tekshirish.** Sun’iy intellekt ishonchli ko‘rinadigan, lekin noto‘g‘ri ma’lumot berishi mumkin — har bir faktni manbadan tekshiring.
- **Maxfiylik.** Shaxsiy ma’lumotlar, parollar va maxfiy hujjatlarni sun’iy intellekt xizmatlariga kiritmang.
- **Hurmat.** Real odamlar haqida soxta rasm, video yoki ovoz yaratmang.
- **Gallyutsinatsiya** — sun’iy intellekt modelining haqiqatga to‘g‘ri kelmaydigan, lekin ishonchli ko‘rinadigan ma’lumot to‘qib chiqarishi.
Sun’iy intellekt o‘ylash o‘rnini bosmaydi, u faqat yordamchi vosita. U bilan ishlaganda tanqidiy fikrlash yanada muhimroq bo‘ladi.
""",
            """
## Kiberbullingga duch kelganda
- **Javob bermang.** Bullerning maqsadi — sizni g‘azablantirish; javob bermaslik uni zaiflashtiradi.
- **Dalillarni saqlang.** Xabarlar skrinshoti, sana va vaqtni saqlab qo‘ying.
- **Bloklang.** Foydalanuvchini bloklang va maxfiylik sozlamalarini kuchaytiring.
- **Xabar bering.** Platformaning «Пожаловаться» funksiyasidan foydalaning.
- **Yordam so‘rang.** Ota-ona, kurator, psixolog yoki ishonchli kattalarga aytib bering. Tahdid bo‘lsa — ichki ishlar organlariga murojaat qiling.
## Guvoh bo‘lsangiz
Agar boshqa odam kiberbullingga uchrayotganini ko‘rsangiz, kamsituvchi postni «layk» qilmang va tarqatmang, jabrlanuvchini qo‘llab-quvvatlang va platformaga xabar bering. Jim turgan guvoh ham bilvosita bullerga yordam beradi.
""",
        ],
        'oldingi': ['Fakt-cheking algoritmi qanday bosqichlardan iborat?',
                    'Klikbeyt nima?',
                    'Deepfake belgilari qanday?'],
        'savollar': ['Internetdagi qanday axloqiy muammolarni bilasiz?',
                     'Trolling va kiberbulling farqi nimada?',
                     'Sun’iy intellektdan halol foydalanish qoidalari qanday?',
                     'Sun’iy intellekt gallyutsinatsiyasi nima?',
                     'Kiberbullingga duch kelganda qanday harakat qilish kerak?'],
        'testlar': [
            ('Janjal chiqarish maqsadida ataylab provokatsion izohlar yozish:',
             ['Trolling', 'Netiket', 'Bloging', 'Fakt-cheking'], 'a'),
            ('Sun’iy intellektning haqiqatga to‘g‘ri kelmaydigan ma’lumot to‘qib chiqarishi:',
             ['Kompilyatsiya', 'Shifrlash', 'Gallyutsinatsiya', 'Arxivlash'], 'c'),
            ('Kiberbullingga duch kelganda birinchi navbatda nima qilinmaydi?',
             ['Dalillarni saqlash', 'Bullerga qo‘pol javob yozish', 'Bloklash', 'Kattalarga aytish'], 'b'),
            ('Sun’iy intellekt xizmatlariga nimani kiritmaslik kerak?',
             ['Umumiy savollarni', 'Tarjima uchun matnni', 'Matematik misolni', 'Parol va shaxsiy ma’lumotlarni'], 'd'),
            ('Boshqa shaxs nomidan yaratilgan ijtimoiy tarmoq sahifasi:',
             ['Soxta akkaunt', 'Rasmiy kanal', 'Biznes profil', 'Arxiv sahifa'], 'a'),
        ],
        'mustaqil': ['«Sun’iy intellektdan o‘qishda halol foydalanish qoidalari» mavzusida 7 bandlik eslatma yozing.',
                     'Kiberbullingga qarshi tengdoshlar uchun plakat yoki qisqa video ssenariysi tayyorlang.'],
    },
    # ------------------------------------------------------------------ 45
    {
        'type': 'A',
        'title': 'Axborotdan mas’uliyatli foydalanish va kiberetika qoidalarini qo‘llash',
        'reja': ['Kiberetika bo‘yicha vaziyatli masalalar',
                 'Amaliy ish: platformalarda xabar berish va bloklash funksiyalari',
                 'Guruh uchun kiberetika kodeksini ishlab chiqish'],
        'maqsad': 'O‘quvchilarda kiberetika vaziyatlarida to‘g‘ri qaror qabul qilish, platformalarning xabar berish va '
                  'bloklash funksiyalaridan foydalanish hamda jamoaviy kiberetika qoidalarini ishlab chiqish ko‘nikmasini shakllantirish.',
        'natija': 'O‘quvchilar vaziyatlarni axloqiy jihatdan tahlil qiladi, Telegram va Instagram’da shikoyat va bloklash '
                  'funksiyalarini topadi va guruh uchun kiberetika kodeksini yozadi.',
        'metod': 'Rol o‘yini, «Keys-stadi», guruhda ishlash, «Aqliy hujum», taqdimot',
        'vosita': 'Vaziyatli masalalar kartochkalari, smartfon yoki kompyuterlardagi o‘quv hisoblari, A3 qog‘oz, markerlar',
        'bolimlar': [
            """
## Vaziyatli masalalar
| № | Vaziyat | Savol |
| 1 | Guruhdoshingizning kulgili rasmini u bilmagan holda guruh chatiga yuborishdi | Siz nima qilasiz? |
| 2 | Do‘stingiz uy vazifasini sun’iy intellektga to‘liq yozdirib, o‘ziniki deb topshirmoqchi | Unga qanday maslahat berasiz? |
| 3 | Sizga «Bu sirni hech kimga aytma» deb yuborilgan shaxsiy xabar keldi, boshqalar skrinshot so‘ramoqda | Qanday yo‘l tutasiz? |
| 4 | Ijtimoiy tarmoqda o‘qituvchingiz nomidan soxta sahifa ochilgan | Kimga va qanday xabar berasiz? |
| 5 | Guruh chatida bir o‘quvchini doimiy masxara qilishmoqda | Guvoh sifatida nima qilasiz? |
- **Axloqiy dilemma** — har bir variant qandaydir qiymatni buzadigan, to‘g‘ri yo‘lni tanlash qiyin bo‘lgan vaziyat.
Har bir guruh 2 ta vaziyatni oladi, mumkin bo‘lgan harakatlarni va ularning oqibatlarini yozadi, so‘ng eng to‘g‘ri yo‘lni asoslaydi.
""",
            """
## Xabar berish va bloklash funksiyalari
- **Telegram — bloklash.** Foydalanuvchi profili → «⋮» → «Заблокировать».
- **Telegram — shikoyat.** Xabar ustida bosib turing → «Пожаловаться» → sababni tanlang (spam, zo‘ravonlik, soxta akkaunt va boshqalar).
- **Instagram — shikoyat.** Post yoki profilda «⋯» → «Пожаловаться» → sababni tanlang.
- **Instagram — cheklash.** «Ограничить» funksiyasi: odam bloklanganini bilmaydi, lekin uning izohlari faqat o‘ziga ko‘rinadi.
- **Izohlarni filtrlash.** Instagram «Настройки» → «Скрытые слова» — haqoratli so‘zlar avtomatik yashiriladi.
- **Dalil saqlash.** Skrinshotda xabar matni, yuboruvchi nomi va sana ko‘rinishi kerak.
Funksiyalar o‘quv hisoblarida yoki o‘qituvchi namoyishida ko‘rib chiqiladi — haqiqiy foydalanuvchilarga asossiz shikoyat yuborilmaydi.
""",
            """
## Kiberetika kodeksi
Guruh birgalikda o‘z chatlari va onlayn muloqoti uchun kodeks yozadi. Kodeks qisqa, aniq va ijobiy shaklda bo‘lishi kerak.
| № | Qoida namunasi |
| 1 | Biz bir-birimizga hurmat bilan yozamiz |
| 2 | Birovning rasmini uning roziligisiz joylamaymiz |
| 3 | Tekshirilmagan xabarlarni tarqatmaymiz |
| 4 | Kimdir kamsitilsa, jim turmaymiz — qo‘llab-quvvatlaymiz va xabar beramiz |
| 5 | Sun’iy intellektdan halol foydalanamiz |
| 6 | Kechqurun soat 22:00 dan keyin guruhga ishga oid xabar yozmaymiz |
- **Kiberetika kodeksi** — jamoa a’zolari raqamli muhitda amal qilishga kelishib olgan axloqiy qoidalar to‘plami.
Kodeks A3 qog‘ozga yoziladi, guruh a’zolari imzo chekadi va u guruh chatiga mahkamlangan xabar sifatida joylanadi.
""",
        ],
        'oldingi': ['Internetdagi qanday axloqiy muammolarni bilasiz?',
                    'Sun’iy intellektdan halol foydalanish qoidalari qanday?',
                    'Kiberbullingga duch kelganda nima qilish kerak?'],
        'savollar': ['Axloqiy dilemma nima?',
                     'Telegram’da foydalanuvchi qanday bloklanadi?',
                     'Instagram’dagi «Ограничить» funksiyasi bloklashdan nimasi bilan farq qiladi?',
                     'Kiberbulling dalili sifatidagi skrinshotda nimalar ko‘rinishi kerak?',
                     'Kiberetika kodeksi qanday tuziladi?'],
        'testlar': [
            ('Telegram’da xabar ustida bosib turib tanlanadigan shikoyat buyrug‘i:',
             ['«Пожаловаться»', '«Переслать»', '«Копировать»', '«Закрепить»'], 'a'),
            ('Odam bloklanganini bilmaydigan, izohlari faqat o‘ziga ko‘rinadigan Instagram funksiyasi:',
             ['Архив', 'Ограничить', 'Близкие друзья', 'Прямой эфир'], 'b'),
            ('Jamoa a’zolari raqamli muhitda amal qilishga kelishgan qoidalar:',
             ['Antivirus bazasi', 'Litsenziya kaliti', 'Kiberetika kodeksi', 'Tarmoq sxemasi'], 'c'),
            ('Haqoratli so‘zlarni avtomatik yashiruvchi Instagram sozlamasi:',
             ['Сохранённое', 'Архив историй', 'Избранное', 'Скрытые слова'], 'd'),
            ('Guruhdoshingizning rasmini roziligisiz joylash:',
             ['Kiberetika qoidasi buzilishi', 'Netiket talabi', 'Xavfsiz amaliyot', 'Fakt-cheking'], 'a'),
        ],
        'mustaqil': ['Vaziyatli masalalardan biri bo‘yicha qaror daraxtini (variant → oqibat) chizing.',
                     'Oila chatingiz uchun 5 bandlik kiberetika qoidalarini taklif qiling.'],
    },
    # ------------------------------------------------------------------ 46
    {
        'type': 'N',
        'title': 'Axborot xavfsizligini ta’minlash bo‘yicha himoya choralarini tanlash',
        'reja': ['Himoya choralarini tanlash tamoyillari',
                 'Tahdidlarga mos himoya choralari',
                 'Himoya choralarining narxi va samaradorligi'],
        'maqsad': 'O‘quvchilarga xavflar tahlili asosida himoya choralarini tanlash tamoyillari, tahdid va chora '
                  'muvofiqligi hamda xarajat va samaradorlik nisbatini tushuntirish.',
        'natija': 'O‘quvchilar tahdidga mos himoya chorasini tanlaydi, profilaktik, aniqlovchi va tiklovchi choralarni '
                  'farqlaydi va choralarni narx-samaradorlik bo‘yicha asoslaydi.',
        'bolimlar': [
            """
## Tanlash tamoyillari
Himoya choralari tasodifan emas, xavflar tahlili natijasida tanlanadi. Asosiy tamoyillar:
- **Muvofiqlik.** Chora aniq bir tahdidga qarshi qaratilgan bo‘lishi kerak.
- **Ustuvorlik.** Avval eng yuqori darajali xavflar bartaraf etiladi.
- **Iqtisodiy asoslanganlik.** Chora narxi kutilayotgan zarardan oshmasligi kerak.
- **Ko‘p qatlamlilik.** Bitta xavfga qarshi bir nechta turli chora qo‘llaniladi.
- **Qulaylik.** Juda noqulay chorani foydalanuvchilar chetlab o‘tishga harakat qiladi.
## Choralar turlari vazifasiga ko‘ra
| Turi | Vazifasi | Misollar |
| Profilaktik | Hodisaning oldini oladi | Kuchli parol, 2FA, yangilanishlar, o‘qitish |
| Aniqlovchi | Hodisani o‘z vaqtida payqaydi | Antivirus, IDS, jurnallarni kuzatish |
| Tiklovchi | Hodisa oqibatlarini bartaraf etadi | Zaxira nusxa, tiklash rejasi, UPS |
- **Profilaktik chora** — xavfsizlik hodisasining yuz berishiga yo‘l qo‘ymaslikka qaratilgan himoya chorasi.
""",
            """
## Tahdid — chora jadvali
| Tahdid | Profilaktik | Aniqlovchi | Tiklovchi |
| Zararli dastur | Yangilanishlar, standart hisob, ehtiyotkorlik | Antivirus, xulq-atvor tahlili | Zaxiradan tiklash |
| Phishing | Xodimlarni o‘qitish, spam filtri, 2FA | Shubhali kirish haqida bildirishnoma | Parolni almashtirish, hisobni tiklash |
| Parol buzilishi | Kuchli parol, parol menejeri | Muvaffaqiyatsiz kirishlar jurnali | Hisobni bloklash va tiklash |
| Wi-Fi’ga ruxsatsiz ulanish | WPA2/WPA3, WPS o‘chirish | Ulangan qurilmalar ro‘yxati | Parolni almashtirish |
| Disk buzilishi | Sifatli disk, RAID | S.M.A.R.T. monitoringi | Zaxira nusxa |
| Elektr uzilishi | UPS, kuchlanish stabilizatori | UPS ogohlantirishi | Tizimni to‘g‘ri qayta ishga tushirish |
| Ma’lumot o‘g‘irlanishi | Shifrlash, kirish huquqlari | Jurnallar, DLP tizimi | Huquqiy choralar |
- **DLP tizimi** — maxfiy ma’lumotlarning tashkilotdan tashqariga ruxsatsiz chiqib ketishini nazorat qiluvchi va bloklovchi tizim.
""",
            """
## Narx va samaradorlik
Kichik tashkilotda cheklangan mablag‘ bilan ham yuqori himoyaga erishish mumkin. Ko‘pgina samarali choralar bepul:
| Chora | Narxi | Samaradorligi |
| Yangilanishlarni o‘rnatish | Bepul | Juda yuqori |
| Microsoft Defender | Bepul | Yuqori |
| 2FA ni yoqish | Bepul | Juda yuqori |
| Xodimlarni o‘qitish | Kam xarajat | Juda yuqori |
| Tashqi diskka zaxiralash | Kam xarajat | Juda yuqori |
| UPS | O‘rtacha | Yuqori |
| Apparat firewall, IDS | Yuqori | Yuqori (katta tarmoqlar uchun) |
- **Qoldiq xavf** — barcha himoya choralari qo‘llanganidan keyin ham saqlanib qoladigan xavf.
Hech bir tizim mutlaq xavfsiz emas: maqsad — xavfni nolga tushirish emas, balki uni tashkilot qabul qila oladigan darajagacha kamaytirish.
""",
        ],
        'oldingi': ['Kiberetika kodeksi nima?',
                    'Platformalarda qanday xabar berish funksiyalari bor?',
                    'Axloqiy dilemma nima?'],
        'savollar': ['Himoya choralarini tanlashning qanday tamoyillari bor?',
                     'Profilaktik, aniqlovchi va tiklovchi choralarga misol keltiring.',
                     'Phishingga qarshi qanday choralar qo‘llaniladi?',
                     'DLP tizimi nima?',
                     'Qoldiq xavf nima va u nima uchun saqlanib qoladi?'],
        'testlar': [
            ('Hodisaning oldini olishga qaratilgan chora:',
             ['Profilaktik', 'Tiklovchi', 'Aniqlovchi', 'Huquqiy'], 'a'),
            ('Zaxira nusxadan tiklash qanday chora?',
             ['Profilaktik', 'Aniqlovchi', 'Tiklovchi', 'Fizik'], 'c'),
            ('Maxfiy ma’lumot tashqariga chiqishini nazorat qiluvchi tizim:',
             ['DNS', 'DLP', 'DHCP', 'VPN'], 'b'),
            ('Barcha choralar qo‘llanganidan keyin saqlanib qoladigan xavf:',
             ['Asosiy xavf', 'Ichki xavf', 'Tashqi xavf', 'Qoldiq xavf'], 'd'),
            ('Bepul va juda samarali himoya chorasi:',
             ['Yangilanishlarni o‘rnatish va 2FA', 'Yangi server sotib olish', 'Qimmat IDS', 'Qo‘riqchi yollash'], 'a'),
        ],
        'mustaqil': ['O‘z uy tarmog‘ingiz uchun tahdid — chora jadvalini tuzing (kamida 5 ta tahdid).',
                     'Kichik ofis uchun 1 mln so‘mlik byudjetda eng samarali himoya choralari to‘plamini tanlang va asoslang.'],
    },
    # ------------------------------------------------------------------ 47
    {
        'type': 'A',
        'title': 'Axborot xavfsizligi uchun himoya choralarini tanlash',
        'reja': ['Tashkilot uchun himoya choralarini tanlash topshirig‘i',
                 'Amaliy ish: himoya rejasini tuzish',
                 'Rejani himoya qilish va baholash'],
        'maqsad': 'O‘quvchilarda real tashkilot misolida xavflar tahlili asosida himoya choralarini tanlash, ularni '
                  'ustuvorlik va byudjet bo‘yicha rejalashtirish va rejani himoya qilish ko‘nikmasini shakllantirish.',
        'natija': 'O‘quvchilar tashkilot uchun himoya rejasini tuzadi: har bir xavfga chora, mas’ul, muddat va narxni '
                  'belgilaydi, rejani taqdim etadi va asoslaydi.',
        'metod': 'Loyiha usuli, «Keys-stadi», guruhda ishlash, taqdimot va o‘zaro baholash',
        'vosita': 'Keys tavsifi, kompyuterlar, Excel/Word, proyektor',
        'bolimlar': [
            """
## Keys: «Ilm-ziyo» o‘quv markazi
O‘quv markazida 12 ta xodim, 2 ta o‘quv kompyuter xonasi (har birida 15 ta kompyuter), ma’muriyat uchun 4 ta kompyuter, 1 ta server (o‘quvchilar bazasi va to‘lovlar), Wi-Fi tarmog‘i va veb-sayt bor. Himoya uchun yillik byudjet — 5 mln so‘m.
Oldingi tekshiruvda aniqlangan muammolar:
- O‘quv kompyuterlarida o‘quvchilar administrator huquqi bilan ishlaydi.
- Server va ma’muriyat kompyuterlari o‘quvchilar bilan bitta tarmoqda.
- Zaxira nusxa olinmaydi, server UPS’siz ishlaydi.
- Xodimlar elektron pochtasida 2FA yo‘q, o‘tgan oy bir xodim phishing xatga aldangan.
- Ma’muriyat kompyuterlarida antivirus litsenziyasi tugagan.
- Veb-sayt boshqaruv paneli paroli «admin123».
""",
            """
## Ishni bajarish tartibi
- **Xavflarni baholash.** Har bir muammo uchun xavf darajasini (ehtimollik × zarar) aniqlang.
- **Choralarni tanlash.** Har bir xavfga kamida bitta profilaktik va bitta aniqlovchi yoki tiklovchi chora tanlang.
- **Byudjetni taqsimlash.** Choralar narxini taxminiy hisoblang, umumiy summa 5 mln so‘mdan oshmasin; bepul choralardan maksimal foydalaning.
- **Reja jadvalini tuzish.** Excel’da jadval tuzing.
| Xavf | Daraja | Chora | Turi | Mas’ul | Muddat | Narxi |
| O‘quvchilarda admin huquqi | 9 | Standart hisoblar, UAC | Profilaktik | Tizim administratori | 1 hafta | Bepul |
| Bitta tarmoq | 6 | VLAN yoki alohida router bilan segmentlash | Profilaktik | Tizim administratori | 1 oy | 1 mln |
| Zaxira yo‘q | 9 | Tashqi disk + bulut, haftalik jadval | Tiklovchi | Tizim administratori | 1 hafta | 1,2 mln |
| Phishing | 6 | 2FA, xodimlar treningi | Profilaktik | Rahbar | 2 hafta | Bepul |
""",
            """
## Rejani himoya qilish
Har bir guruh rejasini 5 daqiqada taqdim etadi va quyidagi savollarga javob beradi:
- Nima uchun aynan shu xavfni birinchi o‘ringa qo‘ydingiz?
- Byudjet yetmasa, qaysi chorani keyinga qoldirasiz?
- Qaysi xavflar qoldiq xavf sifatida qoladi?
| Baholash mezoni | Ball |
| Barcha muammolar uchun chora tanlangan | 2 |
| Choralar tahdidga mos va asoslangan | 3 |
| Byudjet to‘g‘ri hisoblangan | 2 |
| Mas’ul va muddatlar aniq | 1 |
| Taqdimot va javoblar sifati | 2 |
- **Himoya rejasi** — tashkilotda qaysi himoya choralari, kim tomonidan, qachon va qancha mablag‘ evaziga amalga oshirilishini belgilovchi hujjat.
Eng yaxshi reja keyingi mashg‘ulotda amalda qo‘llash uchun tanlanadi.
""",
        ],
        'oldingi': ['Himoya choralarini tanlash tamoyillarini sanang.',
                    'Profilaktik va tiklovchi choralar farqi nimada?',
                    'Qoldiq xavf nima?'],
        'savollar': ['Keysdagi eng xavfli muammolar qaysilar va nima uchun?',
                     'Server va o‘quvchilar kompyuterlarini nima uchun alohida tarmoqqa ajratish kerak?',
                     'Byudjet cheklangan bo‘lsa, qanday choralar birinchi qo‘llaniladi?',
                     'Himoya rejasida qanday ma’lumotlar bo‘ladi?',
                     'Veb-sayt boshqaruv paneli uchun qanday choralar kerak?'],
        'testlar': [
            ('O‘quvchilar administrator huquqi bilan ishlashi qaysi tamoyilni buzadi?',
             ['Eng kam imtiyoz', 'Foydalanuvchanlik', 'Rad etib bo‘lmaslik', 'Haqqoniylik'], 'a'),
            ('Server va o‘quvchilar kompyuterlarini ajratish chorasi:',
             ['Formatlash', 'Arxivlash', 'Tarmoqni segmentlash (VLAN)', 'Defragmentatsiya'], 'c'),
            ('Phishingdan keyin xodimlar pochtasini himoyalovchi bepul chora:',
             ['Yangi kompyuter', '2FA ni yoqish', 'Monitor almashtirish', 'Kabelni uzaytirish'], 'b'),
            ('Server UPS’siz ishlashi qaysi tahdidga zaif qiladi?',
             ['Phishing', 'Plagiat', 'Kiberbulling', 'Elektr uzilishi'], 'd'),
            ('Himoya rejasida har bir chora uchun ko‘rsatiladi:',
             ['Mas’ul, muddat va narx', 'Faqat rang', 'Faqat nom', 'Hech narsa'], 'a'),
        ],
        'mustaqil': ['Guruh rejasidagi bitta chora uchun batafsil amalga oshirish yo‘riqnomasini yozing.',
                     'Texnikum kompyuter xonasi uchun himoya rejasini xuddi shu shaklda tuzing.'],
    },
    # ------------------------------------------------------------------ 48
    {
        'type': 'A',
        'title': 'Tanlangan himoya choralarini amalda qo‘llash',
        'reja': ['Himoya choralarini joriy etish tartibi',
                 'Amaliy ish: kompyuterda himoya choralar to‘plamini qo‘llash',
                 'Tarmoq darajasidagi choralarni qo‘llash va hujjatlashtirish'],
        'maqsad': 'O‘quvchilarda tanlangan himoya choralarini kompyuter va tarmoq darajasida ketma-ket joriy etish, '
                  'har bir qadamni tekshirish va o‘zgarishlarni hujjatlashtirish ko‘nikmasini shakllantirish.',
        'natija': 'O‘quvchilar kompyuterda hisoblar, yangilanishlar, antivirus, firewall, shifrlash va zaxiralashni '
                  'sozlaydi, routerda xavfsizlik sozlamalarini qo‘llaydi va o‘zgarishlar jurnalini yuritadi.',
        'vosita': 'Windows 10/11 kompyuterlar (administrator huquqi), o‘quv routerlari, tashqi disk, o‘zgarishlar jurnali shakli',
        'bolimlar': [
            """
## Joriy etish tartibi
Himoya choralari tartibsiz emas, rejali ravishda joriy etiladi:
- **Holatni yozib olish.** O‘zgartirishdan oldin joriy sozlamalar qayd etiladi — muammo chiqsa, ortga qaytish mumkin bo‘ladi.
- **Tiklash nuqtasi.** Windows’da «Создать точку восстановления» orqali tiklash nuqtasi yaratiladi.
- **Bosqichma-bosqich qo‘llash.** Har safar bitta chora qo‘llanadi va darhol tekshiriladi.
- **Foydalanuvchilarni ogohlantirish.** O‘zgarish ularning ishiga qanday ta’sir qilishi tushuntiriladi.
- **Hujjatlashtirish.** Har bir o‘zgarish jurnalga yoziladi.
- **O‘zgarishlar jurnali** — tizimda qachon, kim tomonidan, qanday o‘zgartirish kiritilgani va natijasi yozib boriladigan hujjat.
- **Tiklash nuqtasi** — Windows tizim fayllari va sozlamalarining ma’lum vaqtdagi holati saqlangan nusxasi; muammo bo‘lsa, tizim shu holatga qaytariladi.
""",
            """
## Kompyuter darajasidagi choralar
- **Tiklash nuqtasi.** `Win + R` → `sysdm.cpl` → «Защита системы» → «Создать».
- **Hisoblar.** O‘quvchi uchun standart hisob yarating, «Гость» ni o‘chiring, administrator parolini kuchli qiling (19-mavzu).
- **Yangilanishlar.** Windows Update orqali barcha yangilanishlarni o‘rnating va avtomatik yangilanishni yoqing.
- **Antivirus.** Defender’da real vaqt, bulutli himoya, o‘zgartirishdan himoya va boshqariladigan papkalarga kirishni yoqing (34-mavzu).
- **Firewall.** Barcha profillarda yoqilganligini tekshiring, tarmoq profilini to‘g‘ri tanlang (29-mavzu).
- **Parol siyosati.** `secpol.msc` da minimal uzunlik 12 va bloklash chegarasi 5 ni o‘rnating (16-mavzu).
- **Ekran qulfi.** 5 daqiqa harakatsizlikdan keyin avtomatik qulflanishni sozlang.
- **Zaxiralash.** Fayl tarixini tashqi diskka yoqing (37-mavzu).
""",
            """
## Tarmoq darajasidagi choralar
- **Router paroli.** Administrator parolini almashtiring.
- **Wi-Fi.** WPA2-AES yoki WPA3, kuchli parol, WPS o‘chirilgan.
- **Mehmon tarmog‘i.** Alohida SSID, lokal tarmoqqa kirishsiz.
- **Proshivka.** Router dasturini yangilang.
## O‘zgarishlar jurnali namunasi
| Sana, vaqt | Obyekt | O‘zgarish | Bajaruvchi | Tekshiruv natijasi |
| 28.10, 10:05 | PC-07 | Tiklash nuqtasi yaratildi | Familiya I. | Muvaffaqiyatli |
| 28.10, 10:12 | PC-07 | «talaba» standart hisobi yaratildi | Familiya I. | Kirish tekshirildi |
| 28.10, 10:30 | PC-07 | Defender: boshqariladigan papkalar yoqildi | Familiya I. | Holat «Вкл.» |
| 28.10, 10:50 | Router | WPS o‘chirildi, WPA2-AES | Familiya I. | Noutbuk yangi parol bilan ulandi |
Mashg‘ulot oxirida juftliklar kompyuterlarni almashib, bir-birining ishini 39-mavzudagi nazorat varag‘i bo‘yicha tekshiradi.
""",
        ],
        'oldingi': ['Himoya rejasida qanday ma’lumotlar bo‘ladi?',
                    'Byudjet cheklangan bo‘lsa, qaysi choralar birinchi qo‘llaniladi?',
                    'Tarmoqni segmentlash nima?'],
        'savollar': ['Himoya choralarini joriy etishdan oldin nima qilinadi?',
                     'Tiklash nuqtasi qanday yaratiladi?',
                     'O‘zgarishlar jurnaliga qanday ma’lumotlar yoziladi?',
                     'Kompyuter darajasida qanday choralar qo‘llandi?',
                     'Router darajasida qanday choralar qo‘llandi?'],
        'testlar': [
            ('Windows tizim sozlamalarining saqlangan holati:',
             ['Tiklash nuqtasi', 'Ish stoli', 'Savat', 'Yorliq'], 'a'),
            ('«Защита системы» oynasini ochuvchi buyruq:',
             ['calc', 'sysdm.cpl', 'mspaint', 'write'], 'b'),
            ('Tizimga kiritilgan o‘zgarishlar yozib boriladigan hujjat:',
             ['Taqdimot', 'Referat', 'O‘zgarishlar jurnali', 'Kundalik'], 'c'),
            ('Himoya choralarini qo‘llashning to‘g‘ri usuli:',
             ['Hammasini bir vaqtda, tekshirmasdan', 'Faqat bittasini', 'Hech birini', 'Bosqichma-bosqich, har birini tekshirib'], 'd'),
            ('Kompyuter qarovsiz qolganda himoyalovchi chora:',
             ['Avtomatik ekran qulfi', 'Yorqinlikni oshirish', 'Ovozni o‘chirish', 'Fon rasmini almashtirish'], 'a'),
        ],
        'mustaqil': ['Uy kompyuteringizda kamida 4 ta himoya chorasini qo‘llang va o‘zgarishlar jurnalini yuriting.',
                     'Tiklash nuqtasidan tizimni qaytarish tartibini o‘rganib, qadamlarini yozing.'],
    },
    # ------------------------------------------------------------------ 49
    {
        'type': 'N',
        'title': 'Himoya choralarining samaradorligini oshirish va baholash',
        'reja': ['Himoya samaradorligi va uning ko‘rsatkichlari',
                 'Samaradorlikni baholash usullari',
                 'Himoyani uzluksiz takomillashtirish'],
        'maqsad': 'O‘quvchilarga himoya choralarining samaradorlik ko‘rsatkichlari, ularni baholash usullari va '
                  'xavfsizlikni uzluksiz takomillashtirish siklini tushuntirish.',
        'natija': 'O‘quvchilar samaradorlik ko‘rsatkichlarini sanaydi, audit, penetratsion test va o‘quv phishingning '
                  'vazifasini izohlaydi hamda PDCA siklini xavfsizlikka qo‘llaydi.',
        'bolimlar': [
            """
## Samaradorlik nima?
- **Himoya samaradorligi** — qo‘llangan choralar xavflarni qanchalik kamaytirgani va xavfsizlik maqsadlariga qanchalik erishilganini ko‘rsatuvchi daraja.
Chorani o‘rnatishning o‘zi yetarli emas — uning haqiqatan ishlayotganini o‘lchash kerak. Masalan, antivirus o‘rnatilgan, lekin bazasi yarim yildan beri yangilanmagan bo‘lsa, chora bor, samara yo‘q.
## Ko‘rsatkichlar
| Ko‘rsatkich | Nimani o‘lchaydi | Maqsadli qiymat |
| Yangilangan kompyuterlar ulushi | Yangilanishlar intizomi | 95 % dan yuqori |
| Antivirus faol kompyuterlar ulushi | Himoya qamrovi | 100 % |
| 2FA yoqilgan hisoblar ulushi | Hisoblar himoyasi | 100 % |
| Phishing sinovida aldangan xodimlar ulushi | Xodimlar tayyorgarligi | 5 % dan kam |
| Hodisani aniqlash vaqti | Aniqlovchi choralar tezligi | Imkon qadar qisqa |
| Zaxiradan tiklash vaqti | Tiklovchi choralar tayyorligi | Rejadagi vaqt ichida |
- **Samaradorlik ko‘rsatkichi** — xavfsizlik holatini son bilan ifodalab, vaqt o‘tishi bilan solishtirish imkonini beruvchi o‘lchov.
""",
            """
## Baholash usullari
- **Ichki audit.** Tashkilot xodimlari nazorat varag‘i bo‘yicha himoya choralarini tekshiradi.
- **Tashqi audit.** Mustaqil mutaxassislar tashkilotni xalqaro standartlar asosida baholaydi.
- **Zaifliklarni skanerlash.** Maxsus dasturlar tarmoq va kompyuterlardagi ma’lum zaifliklarni avtomatik izlaydi.
- **Penetratsion test.** Etik xakerlar tashkilot ruxsati bilan haqiqiy hujumni taqlid qilib, himoyani yorib o‘tishga urinadi.
- **O‘quv phishing.** Xodimlarga zararsiz «phishing» xat yuborilib, qanchasi havolani bosgani o‘lchanadi.
- **Tiklash mashqi.** Zaxira nusxadan tizimni tiklash amalda sinab ko‘riladi.
- **Penetratsion test** — tizim egasining ruxsati bilan himoyadagi zaifliklarni topish maqsadida hujumchi harakatlarini taqlid qilish orqali o‘tkaziladigan nazorat sinovi.
- **ISO/IEC 27001** — axborot xavfsizligini boshqarish tizimiga qo‘yiladigan talablarni belgilovchi xalqaro standart.
Ruxsatsiz «penetratsion test» — bu oddiy hujum va jinoyat hisoblanadi.
""",
            """
## PDCA sikli
Xavfsizlik bir marta bajariladigan ish emas, balki uzluksiz jarayon. Uni takomillashtirish uchun PDCA sikli qo‘llaniladi:
| Bosqich | Mazmuni | Xavfsizlikdagi misol |
| Rejalashtirish (Plan) | Maqsad va choralarni belgilash | Xavflar tahlili, himoya rejasi |
| Bajarish (Do) | Choralarni joriy etish | Sozlamalarni qo‘llash, o‘qitish |
| Tekshirish (Check) | Natijani o‘lchash | Audit, ko‘rsatkichlar, sinovlar |
| Takomillashtirish (Act) | Kamchiliklarni tuzatish | Rejani yangilash, yangi choralar |
- **PDCA sikli** — rejalashtirish, bajarish, tekshirish va takomillashtirish bosqichlaridan iborat uzluksiz yaxshilash usuli.
## Samaradorlikni oshirish yo‘llari
- Choralarni avtomatlashtirish: avtomatik yangilanish, avtomatik zaxiralash.
- Xodimlarni muntazam o‘qitish va rag‘batlantirish.
- Yangi tahdidlar haqida UZCERT va csec.uz ogohlantirishlarini kuzatish.
- Har bir hodisadan keyin saboq chiqarib, rejaga kiritish.
""",
        ],
        'oldingi': ['Himoya choralarini joriy etish tartibi qanday?',
                    'O‘zgarishlar jurnali nima?',
                    'Tiklash nuqtasi nima uchun kerak?'],
        'savollar': ['Himoya samaradorligi deganda nimani tushunasiz?',
                     'Samaradorlikning qanday ko‘rsatkichlarini bilasiz?',
                     'Penetratsion test nima va u qanday shartda qonuniy?',
                     'O‘quv phishing nima uchun o‘tkaziladi?',
                     'PDCA siklining bosqichlarini tushuntiring.'],
        'testlar': [
            ('Ruxsat bilan hujumni taqlid qilib, zaifliklarni topish sinovi:',
             ['Penetratsion test', 'Defragmentatsiya', 'Formatlash', 'Arxivlash'], 'a'),
            ('Axborot xavfsizligini boshqarish tizimi xalqaro standarti:',
             ['ISO 9001', 'ISO/IEC 27001', 'USB 3.0', 'IEEE 802.3'], 'b'),
            ('PDCA siklidagi «Check» bosqichi:',
             ['Rejalashtirish', 'Bajarish', 'Tekshirish', 'Takomillashtirish'], 'c'),
            ('Xodimlar tayyorgarligini o‘lchash usuli:',
             ['Disk tozalash', 'Monitorni sozlash', 'Printer sinovi', 'O‘quv phishing sinovi'], 'd'),
            ('2FA yoqilgan hisoblar ulushining maqsadli qiymati:',
             ['100 %', '10 %', '30 %', '50 %'], 'a'),
        ],
        'mustaqil': ['Texnikum kompyuter xonasi uchun 5 ta samaradorlik ko‘rsatkichini tanlang va o‘lchash usulini yozing.',
                     'PDCA siklini uy kompyuteringiz xavfsizligiga qo‘llab, har bir bosqich uchun aniq harakatlarni yozing.'],
    },
    # ------------------------------------------------------------------ 50
    {
        'type': 'A',
        'title': 'Amalga oshirilgan himoya choralarining natijasini tekshirish va baholash',
        'reja': ['Yakuniy tekshiruvga tayyorgarlik',
                 'Amaliy ish: himoya choralarini sinab ko‘rish',
                 'Yakuniy hisobot va xulosa'],
        'maqsad': 'O‘quvchilarda qo‘llangan himoya choralari natijasini «oldin/keyin» taqqoslash, amaliy sinovlar orqali '
                  'tekshirish, ko‘rsatkichlarni hisoblash va yakuniy hisobot tuzish ko‘nikmasini shakllantirish.',
        'natija': 'O‘quvchilar himoya choralarini sinovdan o‘tkazadi, samaradorlik ko‘rsatkichlarini hisoblaydi, '
                  'qoldiq xavflarni aniqlaydi va fan bo‘yicha yakuniy hisobotni himoya qiladi.',
        'metod': 'Amaliy topshiriq, loyiha himoyasi, o‘zaro baholash, refleksiya',
        'vosita': 'Windows 10/11 kompyuterlar, o‘quv routerlari, EICAR test fayli, 2- va 39-mavzulardagi nazorat varaqlari, proyektor',
        'bolimlar': [
            """
## Tayyorgarlik
Yakuniy tekshiruvda o‘quvchilar 48-mavzuda himoya choralari qo‘llangan kompyuter va tarmoqni baholaydi. Buning uchun quyidagilar tayyorlanadi:
- 2-mavzudagi boshlang‘ich nazorat varag‘i natijalari («oldin» holati);
- 48-mavzudagi o‘zgarishlar jurnali;
- 39-mavzudagi kompleks tekshiruv shakli;
- sinov uchun EICAR test fayli va o‘quv hisoblari.
- **Oldin/keyin tahlili** — chora qo‘llanishidan oldingi va keyingi holatni bir xil mezonlar bo‘yicha solishtirib, natijani baholash usuli.
Tekshiruvni chorani qo‘llagan o‘quvchi emas, boshqa juftlik o‘tkazadi — bu xolislikni ta’minlaydi.
""",
            """
## Sinovlar
| № | Sinov | Kutilgan natija |
| 1 | Standart hisobdan dastur o‘rnatishga urinish | UAC administrator parolini so‘raydi |
| 2 | 6 marta noto‘g‘ri parol kiritish (o‘quv hisobida) | Hisob vaqtincha bloklanadi |
| 3 | EICAR faylini «Документы» ga saqlash | Defender bloklaydi va karantinga oladi |
| 4 | Qo‘shni kompyuterdan ping (ping blok qoidasi bilan) | Javob kelmaydi |
| 5 | Wi-Fi’ga eski parol bilan ulanish | Ulanmaydi |
| 6 | Mehmon tarmog‘idan ichki kompyuterga kirish | Kirish imkoni yo‘q |
| 7 | O‘chirilgan faylni fayl tarixidan tiklash | Fayl tiklanadi |
| 8 | 5 daqiqa harakatsiz qoldirish | Ekran qulflanadi |
- **Sinov.** Har bir sinovni bajaring va haqiqiy natijani yozing.
- **Taqqoslash.** Haqiqiy natija kutilgan natija bilan solishtiriladi; mos kelmasa — chora ishlamayapti, sababi aniqlanadi.
- **Ko‘rsatkich.** Muvaffaqiyatli sinovlar ulushi hisoblanadi: masalan, 8 tadan 7 tasi — 87,5 %.
""",
            """
## Yakuniy hisobot tuzilmasi
| Bo‘lim | Mazmuni |
| 1. Kirish | Obyekt tavsifi va tekshiruv maqsadi |
| 2. Boshlang‘ich holat | 2-mavzudagi nazorat varag‘i natijalari |
| 3. Qo‘llangan choralar | O‘zgarishlar jurnalidan qisqacha |
| 4. Sinov natijalari | Sinovlar jadvali va muvaffaqiyat ulushi |
| 5. Oldin/keyin taqqoslash | Ballar va ko‘rsatkichlar o‘zgarishi |
| 6. Qoldiq xavflar | Bartaraf etilmagan yoki qisman bartaraf etilgan xavflar |
| 7. Tavsiyalar | Keyingi PDCA sikli uchun takliflar |
## Refleksiya
Fan yakunida har bir o‘quvchi uchta savolga javob yozadi: «Fan davomida o‘zimda qanday xavfsiz odatlar shakllandi?», «Qaysi mavzu eng foydali bo‘ldi?», «Kelajakda IT-servis mutaxassisi sifatida mijozlarimga qanday xavfsizlik maslahatlarini beraman?».
Axborot xavfsizligi — bilimlar emas, kundalik odatlar majmui. Kuchli parol, 2FA, yangilanishlar, zaxira nusxa va ehtiyotkorlik — bularning har biri oddiy, lekin birgalikda ular ishonchli himoya qalqonini tashkil etadi.
""",
        ],
        'oldingi': ['Himoya samaradorligining qanday ko‘rsatkichlari bor?',
                    'PDCA sikli nima?',
                    'Penetratsion test qanday shartda qonuniy?'],
        'savollar': ['Oldin/keyin tahlili qanday o‘tkaziladi?',
                     'Nima uchun tekshiruvni boshqa juftlik o‘tkazadi?',
                     'EICAR sinovi qaysi himoya chorasini tekshiradi?',
                     'Sinov natijasi kutilgandan farq qilsa nima qilinadi?',
                     'Yakuniy hisobot qanday bo‘limlardan iborat?'],
        'testlar': [
            ('Chora qo‘llanishidan oldingi va keyingi holatni solishtirish usuli:',
             ['Oldin/keyin tahlili', 'Brute force', 'Fakt-cheking', 'Defragmentatsiya'], 'a'),
            ('Standart hisobdan dastur o‘rnatishga uringanda nima bo‘lishi kerak?',
             ['Dastur o‘zi o‘rnatiladi', 'Kompyuter o‘chadi', 'UAC administrator parolini so‘raydi', 'Hech narsa bo‘lmaydi'], 'c'),
            ('8 ta sinovdan 6 tasi muvaffaqiyatli bo‘lsa, ko‘rsatkich:',
             ['60 %', '75 %', '80 %', '86 %'], 'b'),
            ('Tekshiruvni boshqa juftlik o‘tkazishi nimani ta’minlaydi?',
             ['Tezlikni', 'Arzonlikni', 'Qulaylikni', 'Xolislikni'], 'd'),
            ('Yakuniy hisobotda bartaraf etilmagan xavflar qaysi bo‘limda ko‘rsatiladi?',
             ['Qoldiq xavflar', 'Kirish', 'Boshlang‘ich holat', 'Sinov natijalari'], 'a'),
        ],
        'mustaqil': ['Uy kompyuteringiz uchun «oldin/keyin» tahlili asosida qisqa yakuniy hisobot yozing.',
                     'Fan davomida o‘rgangan eng muhim 10 ta xavfsizlik odatini eslatma ko‘rinishida tayyorlang.'],
    },
]
