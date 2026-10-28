"""1–10-mavzular: axborot xavfsizligi asoslari, tamoyillar, kiberhujumlar va tahdidlar.

Belgilash: '## ' — kichik sarlavha, '- ' — ro'yxat bandi, '|' — jadval qatori, **qalin**, `kod`.
«- **Atama** — ta'rif» ko'rinishidagi bandlar glossariyga avtomatik kiradi.
"""

MAVZULAR = [
    # ------------------------------------------------------------------ 1
    {
        'type': 'N',
        'title': 'Axborot xavfsizligi tushunchasi va uning asosiy yo‘nalishlari',
        'reja': ['Axborot va axborot xavfsizligi tushunchasi',
                 'Axborot xavfsizligining asosiy yo‘nalishlari',
                 'Kompyuter tarmoqlari va IT-servisda axborot xavfsizligining ahamiyati'],
        'maqsad': 'O‘quvchilarga axborot, axborot xavfsizligi, tahdid va himoya tushunchalarini hamda axborot '
                  'xavfsizligining asosiy yo‘nalishlarini tushuntirish.',
        'natija': 'O‘quvchilar axborot xavfsizligining asosiy tushunchalarini farqlaydi, uning yo‘nalishlarini sanaydi '
                  'va IT-servis mutaxassisi ishidagi ahamiyatini misollar bilan izohlaydi.',
        'bolimlar': [
            """
## Axborot nima?
Axborot — shaxslar, predmetlar, faktlar, voqealar va jarayonlar haqidagi ma’lumotlar, ular qanday shaklda taqdim etilishidan qat’i nazar. Kompyuterda axborot fayllar, ma’lumotlar bazalari, elektron xatlar, rasm va videolar ko‘rinishida saqlanadi hamda tarmoq orqali uzatiladi.
Bugungi kunda axborot eng qimmatli resurslardan biriga aylangan: bank hisob raqamlari, o‘quvchilarning baholari, korxonaning moliyaviy hisobotlari, shaxsiy yozishmalar — bularning barchasi himoya qilinishi zarur bo‘lgan axborotdir.
## Asosiy tushunchalar
- **Axborot xavfsizligi** — axborotning maxfiyligi, yaxlitligi va foydalanish imkoniyatini ruxsatsiz kirish, o‘zgartirish va yo‘q qilishdan himoyalangan holati.
- **Axborot resursi** — axborot tizimlarida saqlanadigan hujjatlar, ma’lumotlar bazalari va fayllar majmui.
- **Tahdid** — axborotga zarar yetkazishi mumkin bo‘lgan har qanday hodisa yoki harakat.
- **Zaiflik** — tizimdagi kamchilik bo‘lib, undan foydalanib tahdid amalga oshirilishi mumkin.
- **Himoya vositasi** — axborotni tahdidlardan himoyalash uchun qo‘llaniladigan dasturiy, texnik yoki tashkiliy chora.
Axborot xavfsizligi faqat texnik masala emas: u insonlar, qoidalar va texnologiyalarning birgalikdagi ishiga bog‘liq. Eng kuchli himoya dasturi ham parolini qog‘ozga yozib monitorga yopishtirgan xodim sababli foydasiz bo‘lib qolishi mumkin.
""",
            """
## Axborot xavfsizligining yo‘nalishlari
Axborot xavfsizligi bir necha o‘zaro bog‘liq yo‘nalishlarni o‘z ichiga oladi. Har bir yo‘nalish o‘z vositalari va mutaxassislariga ega.
| Yo‘nalish | Nimani himoya qiladi | Misol |
| Kompyuter xavfsizligi | Alohida kompyuter va undagi dasturlar | Antivirus, operatsion tizim yangilanishlari |
| Tarmoq xavfsizligi | Lokal va global tarmoq, ma’lumot uzatish kanallari | Tarmoqlararo ekran, VPN, Wi-Fi shifrlash |
| Ma’lumotlar xavfsizligi | Fayllar va ma’lumotlar bazalari | Shifrlash, zaxira nusxa |
| Ilovalar xavfsizligi | Veb-saytlar va dasturlar | Kirish huquqlarini cheklash, xatolarni tuzatish |
| Fizik xavfsizlik | Server xonasi, jihozlar | Eshik qulfi, videokuzatuv, kirish nazorati |
| Tashkiliy xavfsizlik | Xodimlar va ish tartibi | Xavfsizlik siyosati, yo‘riqnomalar, o‘qitish |
## Kiberxavfsizlik
- **Kiberxavfsizlik** — kibermakonda shaxs, jamiyat va davlat manfaatlarining tashqi va ichki tahdidlardan himoyalanganlik holati.
- **Kibermakon** — kompyuter tarmoqlari, internet va axborot tizimlari yordamida yaratiladigan virtual muhit.
O‘zbekistonda bu soha 2022-yilda qabul qilingan «Kiberxavfsizlik to‘g‘risida»gi Qonun bilan tartibga solinadi.
""",
            """
## IT-servis mutaxassisi va axborot xavfsizligi
Kompyuter tarmoqlari va IT-servis mutaxassisi kompyuterlarni sozlash, tarmoqni o‘rnatish, foydalanuvchilarga yordam berish bilan shug‘ullanadi. Bu ishlarning har birida u axborot xavfsizligi bilan bevosita to‘qnash keladi.
- Yangi kompyuterga operatsion tizim o‘rnatganda — yangilanishlarni va antivirusni yoqadi.
- Wi-Fi routerni sozlaganda — standart parolni almashtiradi va shifrlashni yoqadi.
- Foydalanuvchi hisobini yaratganda — kerakli huquqlarnigina beradi.
- Nosoz kompyuterni ta’mirlaganda — mijozning shaxsiy fayllarini ko‘rmaydi va tarqatmaydi.
## Xavfsizlik buzilishining oqibatlari
Axborot xavfsizligi buzilsa, tashkilot pul, vaqt va obro‘sini yo‘qotadi. Masalan, shifrlovchi virus server ma’lumotlarini qulflab qo‘ysa, korxona bir necha kun ishlay olmaydi; mijozlar ma’lumotlari sizib chiqsa, tashkilot qonun oldida javob beradi.
Shuning uchun xavfsizlik haqida kompyuter ishlay boshlagandan keyin emas, birinchi kundan boshlab o‘ylash kerak. Bu fan davomida biz tahdidlarni tanish, parol va hisoblarni himoyalash, tarmoq, antivirus, shifrlash va qonunchilik masalalarini bosqichma-bosqich o‘rganamiz.
""",
        ],
        'oldingi': ['Kompyuterda qanday turdagi ma’lumotlar saqlanadi?',
                    'Internetdan foydalanishda qanday xavflarni bilasiz?',
                    'Parol nima uchun kerak?'],
        'savollar': ['Axborot xavfsizligi deganda nimani tushunasiz?',
                     'Tahdid va zaiflik o‘rtasida qanday farq bor?',
                     'Axborot xavfsizligining qanday yo‘nalishlarini bilasiz?',
                     'Kiberxavfsizlik nima?',
                     'IT-servis mutaxassisi ishida axborot xavfsizligi qayerlarda uchraydi?'],
        'testlar': [
            ('Tizimdagi kamchilik bo‘lib, undan foydalanib hujum qilish mumkin bo‘lgan holat:',
             ['Tahdid', 'Zaiflik', 'Himoya vositasi', 'Axborot resursi'], 'b'),
            ('Tarmoqlararo ekran va VPN qaysi yo‘nalishga tegishli?',
             ['Fizik xavfsizlik', 'Tashkiliy xavfsizlik', 'Tarmoq xavfsizligi', 'Ilovalar xavfsizligi'], 'c'),
            ('Server xonasidagi eshik qulfi va videokuzatuv qaysi xavfsizlik turiga kiradi?',
             ['Fizik xavfsizlik', 'Ma’lumotlar xavfsizligi', 'Tarmoq xavfsizligi', 'Kiberetika'], 'a'),
            ('O‘zbekistonda «Kiberxavfsizlik to‘g‘risida»gi Qonun qachon qabul qilingan?',
             ['2003-yilda', '2010-yilda', '2019-yilda', '2022-yilda'], 'd'),
            ('Axborotga zarar yetkazishi mumkin bo‘lgan har qanday hodisa yoki harakat:',
             ['Zaiflik', 'Tahdid', 'Shifrlash', 'Autentifikatsiya'], 'b'),
        ],
        'mustaqil': ['O‘zingiz bilgan biror tashkilot (maktab, bank, do‘kon) misolida qanday axborotlar himoya '
                     'qilinishi kerakligini jadval ko‘rinishida yozing.',
                     'Axborot xavfsizligi yo‘nalishlari bo‘yicha «Klaster» chizmasini tuzing.'],
    },
    # ------------------------------------------------------------------ 2
    {
        'type': 'A',
        'title': 'Axborot xavfsizligi holatini aniqlash',
        'reja': ['Ish joyidagi axborot xavfsizligi holatini baholash mezonlari',
                 'Amaliy ish: kompyuterning xavfsizlik holatini tekshirish',
                 'Natijalarni nazorat varag‘iga yozish va xulosa chiqarish'],
        'maqsad': 'O‘quvchilarda ish joyi va kompyuterning axborot xavfsizligi holatini tekshirish, kamchiliklarni '
                  'aniqlash va nazorat varag‘ini to‘ldirish ko‘nikmasini shakllantirish.',
        'natija': 'O‘quvchilar Windows xavfsizlik markazini ochib holatni tekshiradi, kamchiliklarni aniqlaydi va '
                  'nazorat varag‘i asosida xulosa yozadi.',
        'vosita': 'Windows 10/11 o‘rnatilgan kompyuterlar, nazorat varag‘i shakli, proyektor, taqdimot',
        'bolimlar': [
            """
## Xavfsizlik holati qanday baholanadi?
Ish joyining xavfsizlik holati — kompyuter, undagi dasturlar va foydalanuvchining odatlari xavfsizlik talablariga qanchalik mos kelishini ko‘rsatadi. Uni baholash uchun oldindan tuzilgan savollar ro‘yxati — nazorat varag‘idan foydalaniladi.
- **Nazorat varag‘i** — tekshirilishi kerak bo‘lgan bandlar ro‘yxati bo‘lib, har bir band bo‘yicha «ha» yoki «yo‘q» deb belgilanadi.
- **Xavfsizlik auditi** — tizimning xavfsizlik talablariga muvofiqligini tizimli tekshirish jarayoni.
## Asosiy mezonlar
| Mezon | Nimani tekshiramiz |
| Hisob himoyasi | Kompyuterga kirishda parol yoki PIN-kod bormi |
| Yangilanishlar | Operatsion tizim oxirgi yangilanishlari o‘rnatilganmi |
| Antivirus | Antivirus yoqilganmi, bazasi yangimi |
| Tarmoq himoyasi | Tarmoqlararo ekran (firewall) yoqilganmi |
| Ekran qulfi | Kompyuter qarovsiz qolganda ekran qulflanadimi |
| Ish joyi | Stolda parol yozilgan qog‘oz, begona fleshka yo‘qmi |
""",
            """
## Ishni bajarish tartibi
- **Hisobni tekshirish.** «Пуск» → «Параметры» (Sozlamalar) → «Учётные записи» → «Варианты входа» bo‘limida kirish usuli (parol, PIN) borligini ko‘ring.
- **Yangilanishlarni tekshirish.** Sozlamalar → «Центр обновления Windows» bo‘limini oching va oxirgi yangilanish sanasini yozib oling.
- **Antivirusni tekshirish.** «Безопасность Windows» (Windows Security) ilovasini oching, «Защита от вирусов и угроз» bo‘limida himoya yoqilganini ko‘ring.
- **Tarmoqlararo ekranni tekshirish.** Windows Security → «Брандмауэр и защита сети» bo‘limida barcha tarmoq profillarida himoya yoqilganligini tekshiring.
- **Ekran qulfini sinash.** `Win + L` tugmalarini bosing — ekran qulflanishi va qaytishda parol so‘ralishi kerak.
## Tizim haqida ma’lumot olish
Buyruqlar satrida (`cmd`) `systeminfo` buyrug‘ini bering: operatsion tizim versiyasi va o‘rnatilgan yangilanishlar ro‘yxati chiqadi. Bu ma’lumotlar hisobotga yoziladi.
Muhim qoida: tekshiruv vaqtida hech qanday sozlamani o‘qituvchi ruxsatisiz o‘chirmang va boshqa foydalanuvchilarning fayllarini ochmang.
""",
            """
## Nazorat varag‘ini to‘ldirish
Har bir mezon bo‘yicha natija jadvalga yoziladi. Har bir «ha» javobi 1 ball hisoblanadi.
| № | Tekshiruv bandi | Natija | Izoh |
| 1 | Kirishda parol/PIN bor | ha / yo‘q | |
| 2 | Yangilanishlar o‘rnatilgan | ha / yo‘q | oxirgi sana |
| 3 | Antivirus yoqilgan | ha / yo‘q | |
| 4 | Firewall yoqilgan | ha / yo‘q | |
| 5 | Ekran qulfi ishlaydi | ha / yo‘q | |
| 6 | Ish joyida parol yozuvlari yo‘q | ha / yo‘q | |
## Xulosa chiqarish
- **6 ball** — xavfsizlik holati yaxshi.
- **4–5 ball** — qoniqarli, kamchiliklarni tuzatish kerak.
- **3 ball va kam** — xavfli holat, darhol choralar ko‘riladi.
Xulosada aniqlangan har bir kamchilik uchun tavsiya yoziladi: masalan, «Antivirus bazasi eskirgan — yangilash zarur». Juftlikdagi o‘quvchilar bir-birining nazorat varag‘ini tekshirib baholaydi.
""",
        ],
        'oldingi': ['Axborot xavfsizligi deganda nimani tushunasiz?',
                    'Tahdid va zaiflik o‘rtasidagi farq nimada?',
                    'Axborot xavfsizligining qanday yo‘nalishlarini bilasiz?'],
        'savollar': ['Nazorat varag‘i nima uchun kerak?',
                     'Windows xavfsizlik holatini qaysi ilova orqali tekshirish mumkin?',
                     'Ekran qulfini qaysi tugmalar bilan yoqish mumkin?',
                     'systeminfo buyrug‘i qanday ma’lumot beradi?',
                     'Ish joyida qanday holatlar xavfsizlikka tahdid soladi?'],
        'testlar': [
            ('Kompyuter ekranini tezda qulflash uchun qaysi tugmalar bosiladi?',
             ['Ctrl + C', 'Alt + F4', 'Win + L', 'Win + D'], 'c'),
            ('Tizimning xavfsizlik talablariga muvofiqligini tizimli tekshirish:',
             ['Xavfsizlik auditi', 'Shifrlash', 'Zaxiralash', 'Formatlash'], 'a'),
            ('Windows’da antivirus va firewall holatini ko‘rsatuvchi ilova:',
             ['Paint', 'Windows Security (Безопасность Windows)', 'Блокнот', 'Калькулятор'], 'b'),
            ('Operatsion tizim versiyasi va yangilanishlar ro‘yxatini chiqaruvchi buyruq:',
             ['ping', 'cls', 'systeminfo', 'dir'], 'c'),
            ('Nazorat varag‘ida 3 va undan kam ball to‘plansa, holat qanday baholanadi?',
             ['Yaxshi', 'Qoniqarli', 'A’lo', 'Xavfli'], 'd'),
        ],
        'mustaqil': ['Uydagi kompyuteringiz (yoki telefoningiz) xavfsizlik holatini nazorat varag‘i asosida tekshirib, '
                     'natijalarni jadvalga yozing.',
                     'Nazorat varag‘iga yana 3 ta yangi tekshiruv bandini taklif qiling va asoslang.'],
    },
    # ------------------------------------------------------------------ 3
    {
        'type': 'N',
        'title': 'Axborot xavfsizligining asosiy tamoyillari',
        'reja': ['Konfidensiallik, yaxlitlik va foydalanuvchanlik (CIA triadasi)',
                 'Qo‘shimcha tamoyillar: autentiklik, hisobdorlik, rad etib bo‘lmaslik',
                 'Eng kam imtiyoz va ko‘p qatlamli himoya tamoyillari'],
        'maqsad': 'O‘quvchilarga axborot xavfsizligining asosiy tamoyillari — konfidensiallik, yaxlitlik, '
                  'foydalanuvchanlik va qo‘shimcha tamoyillarni tushuntirish.',
        'natija': 'O‘quvchilar CIA triadasini izohlaydi, har bir tamoyil buzilishiga misol keltiradi va himoya '
                  'choralarini tamoyillar bilan bog‘laydi.',
        'bolimlar': [
            """
## CIA triadasi
Axborot xavfsizligining asosini uchta tamoyil tashkil etadi. Ular inglizcha bosh harflari bo‘yicha **CIA triadasi** deb ataladi: Confidentiality, Integrity, Availability.
- **Konfidensiallik** — axborotga faqat ruxsati bor shaxslar kira olishi va uni o‘qiy olishi.
- **Yaxlitlik** — axborotning ruxsatsiz o‘zgartirilmagan, to‘liq va to‘g‘ri holda saqlanishi.
- **Foydalanuvchanlik** — ruxsati bor foydalanuvchi axborotdan kerakli vaqtda to‘siqsiz foydalana olishi.
## Tamoyillar buzilishiga misollar
| Tamoyil | Buzilish holati | Himoya chorasi |
| Konfidensiallik | Begona shaxs o‘quvchilarning shaxsiy ma’lumotlarini ko‘rib qoldi | Parol, shifrlash, kirish huquqlari |
| Yaxlitlik | Elektron jurnaldagi baho ruxsatsiz o‘zgartirildi | Xesh-summa, o‘zgarishlar jurnali, zaxira nusxa |
| Foydalanuvchanlik | Sayt hujum sababli ochilmay qoldi | Zaxira server, DDoS himoyasi, UPS |
""",
            """
## Qo‘shimcha tamoyillar
CIA triadasidan tashqari zamonaviy tizimlarda yana bir nechta tamoyil qo‘llaniladi.
- **Autentiklik** — axborot yoki foydalanuvchi o‘zini kim deb ko‘rsatsa, haqiqatan ham o‘sha ekanligi.
- **Hisobdorlik** — tizimdagi har bir harakatni aniq foydalanuvchiga bog‘lash imkoniyati.
- **Rad etib bo‘lmaslik** — xabar yuborgan yoki amal bajargan shaxs keyinchalik buni inkor qila olmasligi.
Masalan, elektron raqamli imzo (ERI) bilan imzolangan hujjatni yuborgan shaxs «men yubormaganman» deya olmaydi — bu rad etib bo‘lmaslik tamoyilidir. Tizim jurnallari (loglar) kim, qachon va nima qilganini yozib boradi — bu hisobdorlikni ta’minlaydi.
""",
            """
## Eng kam imtiyoz tamoyili
- **Eng kam imtiyoz tamoyili** — har bir foydalanuvchi va dasturga faqat o‘z ishini bajarishi uchun zarur bo‘lgan minimal huquqlarni berish.
Masalan, kotiba kompyuterida administrator huquqi bo‘lishi shart emas: oddiy foydalanuvchi hisobi bilan ishlasa, virus ham tizimga chuqur o‘rnasha olmaydi.
## Ko‘p qatlamli himoya
- **Ko‘p qatlamli himoya** — bir nechta mustaqil himoya vositasini ketma-ket qo‘llash, shunda bitta qatlam yorib o‘tilsa ham keyingisi himoya qiladi.
Uni qal’aga o‘xshatish mumkin: devor, xandaq, darvoza va qorovul. Kompyuter tizimida bu qatlamlar quyidagicha bo‘ladi:
- Fizik qatlam: server xonasi eshigi va kirish nazorati.
- Tarmoq qatlami: router, tarmoqlararo ekran, Wi-Fi shifrlash.
- Qurilma qatlami: antivirus, yangilanishlar, disk shifrlash.
- Foydalanuvchi qatlami: kuchli parol, 2FA, xodimlarni o‘qitish.
Hech bir vosita 100 % himoya bermaydi, shuning uchun tamoyillar birgalikda qo‘llaniladi.
""",
        ],
        'oldingi': ['Axborot xavfsizligi qanday holat?',
                    'Kompyuterning xavfsizlik holatini qanday tekshirdingiz?',
                    'Nazorat varag‘ida qanday bandlar bor edi?'],
        'savollar': ['CIA triadasiga qaysi tamoyillar kiradi?',
                     'Konfidensiallik buzilishiga misol keltiring.',
                     'Yaxlitlik tamoyili nimani anglatadi?',
                     'Rad etib bo‘lmaslik tamoyili qayerda qo‘llaniladi?',
                     'Ko‘p qatlamli himoya nima uchun kerak?'],
        'testlar': [
            ('Axborotga faqat ruxsati bor shaxslar kira olishi qaysi tamoyil?',
             ['Yaxlitlik', 'Foydalanuvchanlik', 'Konfidensiallik', 'Hisobdorlik'], 'c'),
            ('Sayt hujum sababli ochilmay qolishi qaysi tamoyilning buzilishi?',
             ['Foydalanuvchanlik', 'Konfidensiallik', 'Autentiklik', 'Yaxlitlik'], 'a'),
            ('Elektron jurnaldagi bahoning ruxsatsiz o‘zgartirilishi qaysi tamoyilni buzadi?',
             ['Foydalanuvchanlik', 'Yaxlitlik', 'Eng kam imtiyoz', 'Rad etib bo‘lmaslik'], 'b'),
            ('Foydalanuvchiga faqat ishiga zarur huquqlarni berish tamoyili:',
             ['Ko‘p qatlamli himoya', 'Hisobdorlik', 'Autentiklik', 'Eng kam imtiyoz'], 'd'),
            ('ERI bilan imzolangan hujjatni yuborgan shaxs buni inkor qila olmasligi:',
             ['Rad etib bo‘lmaslik', 'Konfidensiallik', 'Foydalanuvchanlik', 'Yaxlitlik'], 'a'),
        ],
        'mustaqil': ['CIA triadasining har bir tamoyili uchun kundalik hayotdan 2 tadan buzilish misolini yozing.',
                     'Maktab yoki texnikum kompyuter xonasi uchun ko‘p qatlamli himoya sxemasini chizing.'],
    },
    # ------------------------------------------------------------------ 4
    {
        'type': 'A',
        'title': 'Axborot xavfsizligi tamoyillarini real vaziyatlarda aniqlash',
        'reja': ['Vaziyatli masalalarni tahlil qilish usuli',
                 'Amaliy ish: vaziyatlarda buzilgan tamoyilni aniqlash',
                 'Himoya choralarini taklif qilish va natijalarni taqdim etish'],
        'maqsad': 'O‘quvchilarda real vaziyatlarni tahlil qilib, qaysi xavfsizlik tamoyili buzilganini aniqlash va '
                  'himoya choralarini tanlash ko‘nikmasini shakllantirish.',
        'natija': 'O‘quvchilar vaziyatlarni CIA triadasi asosida tahlil qiladi, buzilgan tamoyilni asoslab aniqlaydi va '
                  'mos himoya chorasini taklif qiladi.',
        'metod': '«Keys-stadi», guruhda ishlash, «Aqliy hujum», taqdimot qilish, o‘zaro baholash',
        'vosita': 'Vaziyatli masalalar kartochkalari, tahlil jadvali shakli, kompyuter, proyektor',
        'bolimlar': [
            """
## Vaziyatni tahlil qilish bosqichlari
Real hayotdagi xavfsizlik hodisasini tahlil qilish uchun quyidagi savollarga javob beriladi:
- **Nima sodir bo‘ldi?** Hodisaning qisqa tavsifi yoziladi.
- **Qaysi axborot zarar ko‘rdi?** Fayl, hisob, ma’lumotlar bazasi yoki xizmat aniqlanadi.
- **Qaysi tamoyil buzildi?** Konfidensiallik, yaxlitlik yoki foydalanuvchanlik.
- **Sabab nima edi?** Zaiflik: kuchsiz parol, yangilanmagan dastur, ehtiyotsizlik va hokazo.
- **Qanday himoya chorasi yordam beradi?** Texnik va tashkiliy choralar taklif qilinadi.
- **Keys-stadi** — real yoki real hayotga yaqin vaziyatni tahlil qilib, yechim topishga asoslangan o‘qitish usuli.
""",
            """
## Vaziyatli masalalar
Guruhlar quyidagi vaziyatlarni tahlil jadvaliga yozib chiqadi.
| № | Vaziyat |
| 1 | Hisobchi kompyuterini qulflamay tushlikka chiqdi, bu vaqtda begona shaxs ish haqi jadvalini nusxalab oldi. |
| 2 | Do‘konning internet-sayti ko‘p sonli soxta so‘rovlar sababli bir kun ochilmadi. |
| 3 | O‘quvchi elektron jurnalga kirish parolini bilib olib, o‘z bahosini o‘zgartirdi. |
| 4 | Server qattiq diski buzildi, zaxira nusxa yo‘qligi sababli bir yillik hujjatlar yo‘qoldi. |
| 5 | Xodim «bank xodimi» deb tanishtirgan noma’lum shaxsga telefonda SMS-kodni aytib qo‘ydi. |
| 6 | Wi-Fi tarmog‘i parolsiz bo‘lgani sababli qo‘shnilar tarmoqdan foydalanib, internet tezligi pasaydi. |
## Ishni bajarish tartibi
- **Guruhlarga bo‘linish.** Sinf 4–5 kishilik guruhlarga bo‘linadi, har biri 2 ta vaziyat oladi.
- **Tahlil.** Har bir vaziyat oldingi bo‘limdagi savollar asosida tahlil qilinadi.
- **Jadvalni to‘ldirish.** Buzilgan tamoyil, sabab va himoya chorasi yoziladi.
""",
            """
## Tahlil jadvali namunasi
| Vaziyat | Buzilgan tamoyil | Sabab (zaiflik) | Himoya chorasi |
| 1 | Konfidensiallik | Ekran qulflanmagan | Win + L odati, avtomatik ekran qulfi |
| 4 | Foydalanuvchanlik | Zaxira nusxa yo‘q | Muntazam zaxiralash, RAID massiv |
## Natijalarni taqdim etish
Har bir guruh o‘z natijasini 2–3 daqiqada taqdim etadi. Boshqa guruhlar savol beradi va baholaydi. Bir vaziyatda bir nechta tamoyil buzilishi mumkinligiga e’tibor bering: 3-vaziyatda ham konfidensiallik (parol oshkor bo‘ldi), ham yaxlitlik (baho o‘zgartirildi) buzilgan.
## Xulosa
Amaliy ish natijasida o‘quvchilar xavfsizlik hodisalarining aksariyati murakkab texnik hujum emas, oddiy ehtiyotsizlik oqibati ekanini ko‘radilar. Demak, himoyaning muhim qismi — to‘g‘ri odatlarni shakllantirish.
""",
        ],
        'oldingi': ['CIA triadasiga qaysi tamoyillar kiradi?',
                    'Eng kam imtiyoz tamoyili nimani anglatadi?',
                    'Ko‘p qatlamli himoyaga misol keltiring.'],
        'savollar': ['Vaziyatni tahlil qilishda qanday savollarga javob beriladi?',
                     'Keys-stadi usuli nima?',
                     'Zaxira nusxa yo‘qligi qaysi tamoyilga xavf tug‘diradi?',
                     'Bir vaziyatda bir nechta tamoyil buzilishi mumkinmi? Misol keltiring.',
                     'SMS-kodni begona shaxsga aytish qanday oqibatlarga olib keladi?'],
        'testlar': [
            ('Kompyuterni qulflamay qoldirish natijasida fayl nusxalanishi qaysi tamoyilni buzadi?',
             ['Foydalanuvchanlik', 'Konfidensiallik', 'Rad etib bo‘lmaslik', 'Yaxlitlik'], 'b'),
            ('Soxta so‘rovlar sababli saytning ochilmay qolishi:',
             ['Konfidensiallik buzilishi', 'Yaxlitlik buzilishi', 'Foydalanuvchanlik buzilishi', 'Autentiklik buzilishi'], 'c'),
            ('Ma’lumotlar yo‘qolishining oldini oluvchi asosiy chora:',
             ['Muntazam zaxiralash', 'Ekran fonini almashtirish', 'Brauzerni yopish', 'Monitorni o‘chirish'], 'a'),
            ('Real vaziyatni tahlil qilishga asoslangan o‘qitish usuli:',
             ['Diktant', 'Insho', 'Ma’ruza', 'Keys-stadi'], 'd'),
            ('Parolsiz Wi-Fi tarmog‘i qanday zaiflik hisoblanadi?',
             ['Fizik xavfsizlik zaifligi', 'Tarmoq xavfsizligi zaifligi', 'Huquqiy zaiflik', 'Zaiflik hisoblanmaydi'], 'b'),
        ],
        'mustaqil': ['Ommaviy axborot vositalaridan bitta real xavfsizlik hodisasini topib, tahlil jadvali asosida '
                     'tahlil qiling.',
                     'O‘zingiz 2 ta vaziyatli masala tuzing va javob kalitini yozing.'],
    },
    # ------------------------------------------------------------------ 5
    {
        'type': 'N',
        'title': 'Axborot xavfsizligi tamoyillarining amaliy qo‘llanilishi',
        'reja': ['Tashkilotda xavfsizlik siyosati va qoidalar',
                 'Tamoyillarni texnik vositalar orqali amalga oshirish',
                 'Xodimlar va foydalanuvchilarning xavfsizlik madaniyati'],
        'maqsad': 'O‘quvchilarga axborot xavfsizligi tamoyillari tashkilotda qanday qoidalar va texnik vositalar orqali '
                  'amalga oshirilishini tushuntirish.',
        'natija': 'O‘quvchilar xavfsizlik siyosati tarkibini biladi, har bir tamoyilga mos texnik vositani tanlaydi va '
                  'xavfsizlik madaniyatining ahamiyatini izohlaydi.',
        'bolimlar': [
            """
## Xavfsizlik siyosati
- **Xavfsizlik siyosati** — tashkilotda axborotni himoya qilish bo‘yicha qabul qilingan qoidalar, talablar va mas’uliyatlar majmui.
Siyosat yozma hujjat bo‘lib, rahbar tomonidan tasdiqlanadi va barcha xodimlar bilan tanishtiriladi. Unda quyidagi masalalar belgilanadi:
- qaysi axborot maxfiy hisoblanadi va kim unga kira oladi;
- parollarga qo‘yiladigan talablar va ularni almashtirish muddati;
- shaxsiy fleshka va qurilmalardan foydalanish tartibi;
- zaxira nusxa olish jadvali;
- xavfsizlik hodisasi yuz berganda kimga murojaat qilish.
Siyosat qog‘ozda qolib ketmasligi uchun uning bajarilishi muntazam tekshiriladi.
""",
            """
## Tamoyil va vositalar bog‘liqligi
Har bir tamoyil aniq texnik vositalar orqali amalga oshiriladi.
| Tamoyil | Texnik vositalar | Tashkiliy choralar |
| Konfidensiallik | Parol, shifrlash (BitLocker), kirish huquqlari (NTFS) | Maxfiy hujjatlar ro‘yxati, tushuntirish xati |
| Yaxlitlik | Xesh-summa, raqamli imzo, o‘zgarishlar jurnali | Hujjatlarni tasdiqlash tartibi |
| Foydalanuvchanlik | Zaxira nusxa, UPS, RAID, zaxira internet kanali | Tiklash rejasi, navbatchilik |
| Hisobdorlik | Tizim jurnallari (Event Viewer), shaxsiy hisoblar | Har bir xodimga alohida hisob |
## Amaliy misol: texnikum kompyuter xonasi
Kompyuter xonasida o‘quvchilar uchun alohida cheklangan hisob yaratiladi (eng kam imtiyoz), o‘qituvchi kompyuterida administrator paroli faqat laborantda bo‘ladi (konfidensiallik), o‘quvchilar ishlari har hafta serverga nusxalanadi (foydalanuvchanlik), kirishlar jurnalda qayd etiladi (hisobdorlik).
""",
            """
## Inson omili
Statistik ma’lumotlarga ko‘ra, xavfsizlik hodisalarining katta qismi xodimlarning xatosi yoki ehtiyotsizligi tufayli yuz beradi. Shuning uchun texnik himoya bilan bir qatorda inson omiliga katta e’tibor beriladi.
- **Xavfsizlik madaniyati** — xodimlarning xavfsiz ishlashni odatga aylantirgan, xavflarni tushunadigan va qoidalarga ongli ravishda amal qiladigan holati.
- **Ijtimoiy muhandislik** — insonning ishonuvchanligi, qo‘rquvi yoki qiziqishidan foydalanib, uni maxfiy ma’lumotni oshkor qilishga yoki zararli harakatga undash usuli.
## Madaniyatni shakllantirish yo‘llari
- Yangi xodimlar uchun kirish yo‘riqnomasi o‘tkazish.
- Muntazam treninglar va o‘quv phishing-sinovlari.
- Plakat va eslatmalar: «Ketayotganda ekranni qulflang!».
- Xatoni yashirmay, darhol xabar bergan xodimni rag‘batlantirish.
""",
        ],
        'oldingi': ['Vaziyatli masalalarda qaysi tamoyillar ko‘proq buzilgan edi?',
                    'Foydalanuvchanlik tamoyilini qanday choralar ta’minlaydi?',
                    'Keys-stadi usulida qanday bosqichlar bor?'],
        'savollar': ['Xavfsizlik siyosatida qanday masalalar belgilanadi?',
                     'Konfidensiallikni qaysi texnik vositalar ta’minlaydi?',
                     'Hisobdorlik uchun qanday vosita qo‘llaniladi?',
                     'Ijtimoiy muhandislik nima?',
                     'Xavfsizlik madaniyatini qanday shakllantirish mumkin?'],
        'testlar': [
            ('Tashkilotda axborotni himoya qilish bo‘yicha qabul qilingan qoidalar majmui:',
             ['Xavfsizlik siyosati', 'Antivirus bazasi', 'Tarmoq sxemasi', 'Ish rejasi'], 'a'),
            ('Windows’da tizim jurnallarini ko‘rish dasturi:',
             ['Paint', 'Event Viewer (Просмотр событий)', 'WordPad', 'Media Player'], 'b'),
            ('UPS va zaxira nusxa qaysi tamoyilni ta’minlaydi?',
             ['Konfidensiallik', 'Rad etib bo‘lmaslik', 'Foydalanuvchanlik', 'Autentiklik'], 'c'),
            ('Insonning ishonuvchanligidan foydalanib maxfiy ma’lumot olish usuli:',
             ['Shifrlash', 'Zaxiralash', 'Defragmentatsiya', 'Ijtimoiy muhandislik'], 'd'),
            ('BitLocker vositasi asosan nimaga xizmat qiladi?',
             ['Diskni shifrlashga', 'Rasm chizishga', 'Internet tezligini oshirishga', 'Fayllarni o‘chirishga'], 'a'),
        ],
        'mustaqil': ['Kichik ofis (5 ta xodim) uchun 10 banddan iborat soddalashtirilgan xavfsizlik siyosatini yozing.',
                     '«Xavfsizlik madaniyati» mavzusida plakat yoki eslatma varaqasi tayyorlang.'],
    },
    # ------------------------------------------------------------------ 6
    {
        'type': 'A',
        'title': 'Internet manbalaridagi axborot xavfsizligi tamoyillarini real vaziyatlarda aniqlash',
        'reja': ['Ishonchli axborot manbalarini tanlash',
                 'Amaliy ish: internetdagi xavfsizlik hodisalari haqidagi maqolalarni tahlil qilish',
                 'Tahlil natijalarini taqdimot ko‘rinishida rasmiylashtirish'],
        'maqsad': 'O‘quvchilarda internetdagi rasmiy manbalardan xavfsizlik hodisalari haqida ma’lumot topish, ularni '
                  'tamoyillar asosida tahlil qilish va taqdim etish ko‘nikmasini shakllantirish.',
        'natija': 'O‘quvchilar ishonchli manbani soxtasidan farqlaydi, maqoladagi hodisada buzilgan tamoyilni aniqlaydi va '
                  'natijani qisqa taqdimotda bayon qiladi.',
        'vosita': 'Internetga ulangan kompyuterlar, brauzer, PowerPoint dasturi, tahlil jadvali shakli',
        'bolimlar': [
            """
## Qaysi manbalarga ishonish mumkin?
Internetda axborot xavfsizligi haqida juda ko‘p ma’lumot bor, lekin ularning hammasi ham to‘g‘ri emas. Rasmiy va ishonchli manbalardan foydalanish kerak.
| Manba | Manzil | Nima topiladi |
| O‘zbekiston kompyuter hodisalariga javob berish xizmati | uzcert.uz | Ogohlantirishlar, zaifliklar haqida xabarlar |
| Kiberxavfsizlik markazi | csec.uz | Tavsiyalar, statistik ma’lumotlar |
| Qonunchilik ma’lumotlari milliy bazasi | lex.uz | Qonunlar va me’yoriy hujjatlar |
| Ta’lim portali | ziyonet.uz | O‘quv materiallari |
## Manba ishonchliligi belgilari
- Sayt rasmiy domenda (gov.uz, uz) va xavfsiz `https://` protokolida ishlaydi.
- Maqola muallifi va e’lon qilingan sanasi ko‘rsatilgan.
- Ma’lumot boshqa rasmiy manbalar bilan tasdiqlanadi.
- Sarlavhada vahima uyg‘otuvchi so‘zlar («SHOSHILING!», «hamma ma’lumotingiz o‘g‘irlandi!») yo‘q.
""",
            """
## Ishni bajarish tartibi
- **Manbani ochish.** Brauzerda uzcert.uz yoki csec.uz saytining «Yangiliklar» yoki «Ogohlantirishlar» bo‘limini oching.
- **Maqola tanlash.** Oxirgi bir yil ichidagi bitta xavfsizlik hodisasi yoki ogohlantirish haqidagi maqolani tanlang.
- **Ishonchlilikni tekshirish.** Manba ishonchliligi belgilari asosida maqolani baholang.
- **Tahlil qilish.** Hodisada qaysi axborot zarar ko‘rgani, qaysi tamoyil buzilgani va sababini aniqlang.
- **Tavsiyalarni yozish.** Maqolada berilgan himoya tavsiyalarini o‘z so‘zlaringiz bilan qisqacha yozing.
## Qidiruv bo‘yicha maslahatlar
Qidiruv tizimida aniq so‘zlardan foydalaning: «firibgarlik SMS ogohlantirish», «zaiflik yangilanish Windows». Natijalar ichida reklama belgisi bor havolalarni tanlamang.
""",
            """
## Taqdimot tayyorlash
Tahlil natijasi 4–5 slayddan iborat qisqa taqdimotga joylanadi:
| Slayd | Mazmuni |
| 1 | Hodisa nomi, manba va sana |
| 2 | Nima sodir bo‘ldi — qisqa tavsif |
| 3 | Buzilgan tamoyil va zaiflik |
| 4 | Himoya choralari va tavsiyalar |
| 5 | Xulosa: bizning kompyuter xonamiz uchun saboq |
## Baholash
O‘quvchilar taqdimotni 3 daqiqada himoya qiladi. Baholashda manbaning ishonchliligi, tamoyilning to‘g‘ri aniqlangani va tavsiyalarning amaliyligi hisobga olinadi. Taqdimotda manba havolasi albatta ko‘rsatiladi — bu mualliflik huquqiga hurmat belgisidir.
""",
        ],
        'oldingi': ['Xavfsizlik siyosati nima?',
                    'Ijtimoiy muhandislikka misol keltiring.',
                    'Yaxlitlikni qaysi vositalar ta’minlaydi?'],
        'savollar': ['Axborot xavfsizligi bo‘yicha qanday rasmiy manbalarni bilasiz?',
                     'Manba ishonchliligini qanday belgilar orqali tekshirasiz?',
                     'uzcert.uz saytida qanday ma’lumotlar e’lon qilinadi?',
                     'Nima uchun vahimali sarlavhali maqolalarga ishonmaslik kerak?',
                     'Taqdimotda manba havolasini ko‘rsatish nima uchun muhim?'],
        'testlar': [
            ('O‘zbekistonda kompyuter hodisalariga javob berish xizmatining sayti:',
             ['uzcert.uz', 'kun.uz', 'olx.uz', 'mail.ru'], 'a'),
            ('Qonun hujjatlarini rasmiy manbadan qayerdan topish mumkin?',
             ['Ijtimoiy tarmoqdagi guruhdan', 'Forumdan', 'lex.uz saytidan', 'Reklama bannerdan'], 'c'),
            ('Manba ishonchliligi belgisi emas:',
             ['Muallif ko‘rsatilgan', 'Sana ko‘rsatilgan', 'https protokoli', 'Vahimali sarlavha'], 'd'),
            ('Xavfsiz ulanish protokoli:',
             ['ftp://', 'https://', 'http://', 'file://'], 'b'),
            ('Qidiruv natijalarida qaysi havolalardan ehtiyot bo‘lish kerak?',
             ['Rasmiy saytlardan', 'Ta’lim portallaridan', 'Reklama belgisi bor havolalardan', 'lex.uz dan'], 'c'),
        ],
        'mustaqil': ['csec.uz saytidagi bitta tavsiyani o‘rganib, uning asosida oila a’zolaringiz uchun eslatma tayyorlang.',
                     'Internetdan topilgan 3 ta xavfsizlik maqolasini ishonchlilik belgilari bo‘yicha taqqoslang.'],
    },
    # ------------------------------------------------------------------ 7
    {
        'type': 'N',
        'title': 'Kiberhujumlar va ularning ishlash mexanizmlari',
        'reja': ['Kiberhujum tushunchasi va hujumchilar turlari',
                 'Kiberhujumning bosqichlari',
                 'Zararli dasturlar va ularning ishlash mexanizmi'],
        'maqsad': 'O‘quvchilarga kiberhujum, hujumchilar turlari, hujum bosqichlari va zararli dasturlarning ishlash '
                  'mexanizmlarini tushuntirish.',
        'natija': 'O‘quvchilar kiberhujum bosqichlarini ketma-ket aytib beradi, zararli dastur turlarini farqlaydi va '
                  'ularning tarqalish yo‘llarini izohlaydi.',
        'bolimlar': [
            """
## Kiberhujum nima?
- **Kiberhujum** — kompyuter, tarmoq yoki axborot tizimiga ruxsatsiz kirish, uni ishdan chiqarish yoki undagi ma’lumotlarni o‘g‘irlash maqsadida amalga oshiriladigan qasddan qilingan harakat.
- **Xaker** — kompyuter tizimlarini chuqur biladigan, ularning zaifliklarini topa oladigan mutaxassis.
Xakerlar maqsadiga ko‘ra farqlanadi:
| Turi | Maqsadi |
| «Oq shlyapa» (etik xaker) | Tashkilot ruxsati bilan zaifliklarni topib, tuzatishga yordam beradi |
| «Qora shlyapa» | Ruxsatsiz kirib, pul, ma’lumot yoki shon-shuhrat uchun zarar yetkazadi |
| «Kulrang shlyapa» | Ruxsatsiz zaiflik topadi, lekin ko‘pincha zarar yetkazmaydi |
| Haktivist | Siyosiy yoki g‘oyaviy maqsadda hujum qiladi |
Kiberjinoyatchilik qonun bilan taqiqlanadi: O‘zbekiston Jinoyat kodeksida axborot texnologiyalari sohasidagi jinoyatlar uchun javobgarlik belgilangan.
""",
            """
## Hujum bosqichlari
Aksariyat kiberhujumlar ma’lum ketma-ketlikda amalga oshiriladi. Bu ketma-ketlikni bilish himoyachiga hujumni erta bosqichda to‘xtatish imkonini beradi.
- **Razvedka.** Hujumchi qurbon haqida ma’lumot to‘playdi: xodimlar ismlari, elektron pochtalar, ishlatiladigan dasturlar.
- **Qurollanish.** Zararli fayl yoki soxta sayt tayyorlanadi.
- **Yetkazish.** Zararli narsa qurbonga yuboriladi: elektron xat, fleshka, havola.
- **Ekspluatatsiya.** Dasturdagi zaiflikdan foydalanib, zararli kod ishga tushiriladi.
- **O‘rnashish.** Hujumchi tizimda doimiy qolish uchun yashirin dastur o‘rnatadi.
- **Maqsadga erishish.** Ma’lumot o‘g‘irlanadi, shifrlanadi yoki tizim ishdan chiqariladi.
- **Ekspluatatsiya** — dastur yoki tizimdagi zaiflikdan foydalanib, uni hujumchi xohlagan amalni bajarishga majburlash.
""",
            """
## Zararli dasturlar
- **Zararli dastur** — foydalanuvchi bilmagan holda kompyuterga zarar yetkazish, ma’lumot o‘g‘irlash yoki boshqarishni egallash uchun yaratilgan dastur.
| Turi | Ishlash mexanizmi |
| Virus | Boshqa fayllarga yozilib oladi, fayl ochilganda ko‘payadi |
| Chuvalchang (worm) | Tarmoq orqali o‘zi mustaqil tarqaladi |
| Troyan | Foydali dastur niqobida o‘rnatiladi, yashirin zararli ish qiladi |
| Shifrlovchi (ransomware) | Fayllarni shifrlab, ochish uchun to‘lov talab qiladi |
| Josus dastur (spyware) | Foydalanuvchi harakatlari va parollarini yashirincha yig‘adi |
| Klaviatura shpioni (keylogger) | Bosilgan har bir tugmani yozib, hujumchiga yuboradi |
| Botnet | Zararlangan kompyuterlar tarmog‘i, hujumchi ularni masofadan boshqaradi |
## Tarqalish yo‘llari
Zararli dasturlar ko‘pincha elektron xat ilovalari, noma’lum saytlardan yuklangan «bepul» dasturlar, fleshkalar va ijtimoiy tarmoqdagi havolalar orqali tarqaladi. Shuning uchun asosiy himoya — ehtiyotkorlik, yangilanishlar va antivirus.
""",
        ],
        'oldingi': ['Axborot xavfsizligi tamoyillarini sanang.',
                    'Internetdagi qaysi manbalar ishonchli?',
                    'Ijtimoiy muhandislik nima?'],
        'savollar': ['Kiberhujum nima?',
                     'Xakerlarning qanday turlari bor?',
                     'Kiberhujumning bosqichlarini sanang.',
                     'Troyan dasturi virusdan nimasi bilan farq qiladi?',
                     'Zararli dasturlar qanday yo‘llar bilan tarqaladi?'],
        'testlar': [
            ('Tashkilot ruxsati bilan zaifliklarni topib beradigan mutaxassis:',
             ['Haktivist', '«Qora shlyapa»', 'Etik xaker («oq shlyapa»)', 'Spamer'], 'c'),
            ('Fayllarni shifrlab, ochish uchun to‘lov talab qiladigan dastur:',
             ['Shifrlovchi (ransomware)', 'Chuvalchang', 'Keylogger', 'Antivirus'], 'a'),
            ('Tarmoq orqali o‘zi mustaqil tarqaladigan zararli dastur:',
             ['Troyan', 'Chuvalchang (worm)', 'Josus dastur', 'Brauzer'], 'b'),
            ('Hujumning birinchi bosqichi — qurbon haqida ma’lumot to‘plash:',
             ['Ekspluatatsiya', 'O‘rnashish', 'Yetkazish', 'Razvedka'], 'd'),
            ('Bosilgan tugmalarni yozib oladigan zararli dastur:',
             ['Botnet', 'Virus', 'Keylogger', 'Firewall'], 'c'),
        ],
        'mustaqil': ['Zararli dastur turlari bo‘yicha taqqoslash jadvalini tuzing: tarqalish yo‘li, belgisi, himoya usuli.',
                     'Kiberhujum bosqichlarini sxema ko‘rinishida chizing va har bir bosqichda qanday himoya qo‘llash '
                     'mumkinligini yozing.'],
    },
    # ------------------------------------------------------------------ 8
    {
        'type': 'A',
        'title': 'Kiberhujumlarning asosiy turlarini misollar orqali aniqlash',
        'reja': ['Kiberhujumlarning asosiy turlari',
                 'Amaliy ish: hujum belgilarini misollar asosida aniqlash',
                 'Hujum turini va himoya chorasini jadvalda rasmiylashtirish'],
        'maqsad': 'O‘quvchilarda kiberhujum turlarini tashqi belgilari bo‘yicha aniqlash va har bir turga qarshi himoya '
                  'chorasini tanlash ko‘nikmasini shakllantirish.',
        'natija': 'O‘quvchilar phishing, DDoS, parolni tanlash, MITM va zararli dastur hujumlarini belgilari bo‘yicha '
                  'aniqlaydi va mos himoya chorasini taklif qiladi.',
        'vosita': 'Hujum misollari tushirilgan kartochkalar va skrinshotlar, kompyuter, proyektor, jadval shakli',
        'bolimlar': [
            """
## Asosiy hujum turlari
- **Phishing** — soxta xat, SMS yoki sayt orqali foydalanuvchini aldab, uning login, parol yoki karta ma’lumotlarini olish.
- **DDoS hujum** — ko‘plab kompyuterlardan bir vaqtda juda ko‘p so‘rov yuborib, sayt yoki serverni ishlamay qoldirish.
- **Brute force** — barcha mumkin bo‘lgan parollarni ketma-ket sinab ko‘rish orqali hisobga kirish.
- **MITM hujum** — hujumchi ikki tomon o‘rtasiga yashirincha kirib, uzatilayotgan ma’lumotlarni tinglashi yoki o‘zgartirishi.
- **SQL in’ektsiya** — sayt formasiga maxsus buyruq yozib, ma’lumotlar bazasidan ruxsatsiz ma’lumot olish.
- **Lug‘at hujumi** — ko‘p ishlatiladigan parollar ro‘yxati («123456», «qwerty») asosida parolni topishga urinish.
Bu turlarning har biri o‘ziga xos belgilar qoldiradi. IT-servis mutaxassisi bu belgilarni erta payqashi kerak.
""",
            """
## Hujum belgilari
| Belgi | Ehtimoliy hujum turi |
| «Hisobingiz bloklandi, havolaga o‘tib tasdiqlang» degan xat | Phishing |
| Sayt juda sekin ishlaydi yoki umuman ochilmaydi, serverga minglab so‘rov kelmoqda | DDoS |
| Jurnalda bir hisobga qisqa vaqtda yuzlab muvaffaqiyatsiz kirish urinishi | Brute force / lug‘at hujumi |
| Ommaviy Wi-Fi’da brauzer «Ulanish xavfsiz emas» deb ogohlantiradi | MITM |
| Fayllar kengaytmasi o‘zgargan, ekranda to‘lov talabi | Shifrlovchi dastur |
## Ishni bajarish tartibi
- **Kartochkalarni o‘rganish.** Har bir juftlik 6 ta hujum misoli tushirilgan kartochka oladi.
- **Belgilarni ajratish.** Har bir misoldagi shubhali belgilarni tagiga chizib chiqing.
- **Turini aniqlash.** Belgilar jadvali asosida hujum turini aniqlang.
- **Windows jurnalini ko‘rish.** O‘qituvchi namoyishida «Просмотр событий» → «Журналы Windows» → «Безопасность» bo‘limida 4625 kodli (muvaffaqiyatsiz kirish) hodisalarni ko‘ring.
""",
            """
## Natijalar jadvali
| № | Misol | Hujum turi | Qaysi tamoyil buziladi | Himoya chorasi |
| 1 | Bank nomidan SMS | Phishing | Konfidensiallik | Havolaga o‘tmaslik, rasmiy ilova orqali tekshirish |
| 2 | Sayt ishlamay qoldi | DDoS | Foydalanuvchanlik | DDoS himoya xizmati, trafikni filtrlash |
| 3 | 500 ta noto‘g‘ri parol urinishi | Brute force | Konfidensiallik | Hisobni vaqtincha bloklash, 2FA |
## Himoya choralari umumlashmasi
- Noma’lum havola va ilovalarni ochmaslik.
- Kuchli, uzun parol va ikki bosqichli autentifikatsiya.
- Ommaviy Wi-Fi’da VPN ishlatish.
- Dasturlar va operatsion tizimni o‘z vaqtida yangilash.
- Muhim fayllarning zaxira nusxasini alohida saqlash.
Mashg‘ulot oxirida juftliklar jadvallarini almashtirib, bir-birining javoblarini tekshiradi.
""",
        ],
        'oldingi': ['Kiberhujum bosqichlarini sanang.',
                    'Zararli dasturlarning qanday turlari bor?',
                    'Troyan qanday ishlaydi?'],
        'savollar': ['Phishing hujumining asosiy belgilari qanday?',
                     'DDoS hujum qaysi tamoyilni buzadi?',
                     'Brute force hujumidan qanday himoyalanish mumkin?',
                     'MITM hujumi qayerda ko‘proq uchraydi?',
                     'Windows jurnalidagi 4625 kodli hodisa nimani bildiradi?'],
        'testlar': [
            ('Ko‘plab so‘rov yuborib serverni ishlamay qoldirish hujumi:',
             ['Phishing', 'Brute force', 'DDoS', 'SQL in’ektsiya'], 'c'),
            ('Barcha mumkin bo‘lgan parollarni ketma-ket sinash:',
             ['Brute force', 'MITM', 'DDoS', 'Spam'], 'a'),
            ('Ikki tomon o‘rtasiga yashirincha kirib ma’lumotlarni tinglash hujumi:',
             ['Lug‘at hujumi', 'Shifrlash', 'Phishing', 'MITM (o‘rtadagi odam)'], 'd'),
            ('«Hisobingiz bloklandi, havolaga o‘ting» degan xat qaysi hujumga xos?',
             ['DDoS', 'Phishing', 'Brute force', 'Botnet'], 'b'),
            ('Ommaviy Wi-Fi’da MITM hujumidan himoyalanish vositasi:',
             ['Ekran fonini almashtirish', 'VPN', 'Ovozni o‘chirish', 'Defragmentatsiya'], 'b'),
        ],
        'mustaqil': ['O‘zingiz yoki tanishlaringiz olgan shubhali xat yoki SMS namunasini (shaxsiy ma’lumotlarni yashirib) '
                     'tahlil qiling: qaysi belgilar hujumni ko‘rsatadi?',
                     'Kiberhujum turlari bo‘yicha 10 ta savoldan iborat krossvord tuzing.'],
    },
    # ------------------------------------------------------------------ 9
    {
        'type': 'N',
        'title': 'Axborot xavfsizligiga tahdidlar va ularning turlari',
        'reja': ['Tahdid tushunchasi va tahdid manbalari',
                 'Tahdidlarning tasnifi',
                 'Zamonaviy tahdidlar va ularning xususiyatlari'],
        'maqsad': 'O‘quvchilarga tahdid tushunchasi, tahdid manbalari va tahdidlarning turli belgilar bo‘yicha tasnifini '
                  'tushuntirish.',
        'natija': 'O‘quvchilar tahdidlarni manbasi, maqsadi va ta’sir obyekti bo‘yicha tasniflaydi, ichki va tashqi '
                  'tahdidlarga misollar keltiradi.',
        'bolimlar': [
            """
## Tahdid, zaiflik va xavf
Oldingi mavzularda tahdid tushunchasi bilan tanishdik. Endi uni chuqurroq ko‘rib chiqamiz.
- **Tahdid manbai** — tahdidni yuzaga keltiruvchi inson, tabiat hodisasi yoki texnik nosozlik.
- **Xavf** — tahdid zaiflikdan foydalanib amalga oshishi ehtimoli va bunda yetkaziladigan zarar miqdorining birikmasi.
Oddiy misol: ochiq qolgan deraza — zaiflik, o‘g‘ri — tahdid, uyda qimmatbaho buyumlar bo‘lgani uchun o‘g‘irlik ehtimoli va zarari — xavf. Kompyuter tizimida ham xuddi shunday: yangilanmagan dastur — zaiflik, virus — tahdid.
## Tahdid manbalari
| Manba | Misollar |
| Inson (qasddan) | Xaker, firibgar, norozi xodim |
| Inson (tasodifiy) | Noto‘g‘ri faylni o‘chirish, xatni boshqa odamga yuborish |
| Texnik | Qattiq disk buzilishi, elektr uzilishi, dasturiy xato |
| Tabiiy | Yong‘in, suv toshqini, zilzila, chaqmoq |
""",
            """
## Tasnif belgilari
Tahdidlar turli belgilarga ko‘ra tasniflanadi.
- **Ichki tahdid** — tashkilot xodimlari yoki tizimga qonuniy kirish huquqiga ega shaxslar tomonidan yuzaga keladigan tahdid.
- **Tashqi tahdid** — tashkilotdan tashqaridagi shaxslar yoki hodisalar tomonidan yuzaga keladigan tahdid.
| Belgi | Turlari |
| Manbaning joylashuvi | Ichki, tashqi |
| Niyat | Qasddan, tasodifiy |
| Ta’sir qiladigan tamoyil | Konfidensiallikka, yaxlitlikka, foydalanuvchanlikka |
| Obyekt | Apparat ta’minoti, dasturiy ta’minot, ma’lumotlar, foydalanuvchi |
| Tabiati | Tabiiy, sun’iy (inson tomonidan) |
Ichki tahdidlar ko‘pincha xavfliroq: xodim tizimni yaxshi biladi va uning harakatlari shubha uyg‘otmaydi. Shuning uchun eng kam imtiyoz tamoyili va harakatlarni jurnalga yozish muhim.
""",
            """
## Bugungi kunning dolzarb tahdidlari
- **Shifrlovchi viruslar** — tashkilotlar fayllarini shifrlab, katta to‘lov talab qiladi.
- **Telefon va SMS orqali firibgarlik** — «bank xodimi» nomidan qo‘ng‘iroq qilib, karta ma’lumotlari va SMS-kodni so‘rash.
- **Soxta ilovalar** — mashhur ilova nomi ostida tarqatiladigan, telefonni boshqarishni egallaydigan dasturlar.
- **Ma’lumotlar sizib chiqishi** — saytlardan o‘g‘irlangan login va parollar internetda tarqatiladi.
- **Deepfake** — sun’iy intellekt yordamida yaratilgan, haqiqiy insonning ovozi yoki tasviriga o‘xshatilgan soxta video yoki audio.
## IoT qurilmalari tahdidi
Aqlli kameralar, televizorlar, routerlar internetga ulanadi, lekin ko‘pincha standart parol bilan qoladi. Hujumchilar bunday qurilmalarni egallab, botnetga qo‘shadi. Shuning uchun har qanday tarmoq qurilmasi o‘rnatilganda standart parol albatta almashtiriladi.
""",
        ],
        'oldingi': ['Kiberhujumning asosiy turlarini sanang.',
                    'Phishing hujumi qanday belgilarga ega?',
                    'DDoS hujumidan qanday himoyalanish mumkin?'],
        'savollar': ['Tahdid, zaiflik va xavf o‘rtasidagi bog‘liqlikni misol bilan tushuntiring.',
                     'Tahdid manbalarining qanday turlari bor?',
                     'Ichki tahdid nima uchun xavfliroq?',
                     'Deepfake nima va u qanday xavf tug‘diradi?',
                     'IoT qurilmalarini himoyalash uchun nima qilish kerak?'],
        'testlar': [
            ('Qattiq disk buzilishi qanday tahdid manbaiga kiradi?',
             ['Texnik', 'Tabiiy', 'Inson (qasddan)', 'Tashqi qasddan'], 'a'),
            ('Tashkilot xodimi tomonidan yuzaga keladigan tahdid:',
             ['Tashqi tahdid', 'Tabiiy tahdid', 'Ichki tahdid', 'Texnik tahdid'], 'c'),
            ('Tahdidning zaiflikdan foydalanib amalga oshish ehtimoli va zarari birikmasi:',
             ['Zaiflik', 'Xavf', 'Himoya', 'Autentifikatsiya'], 'b'),
            ('Sun’iy intellekt yordamida yaratilgan soxta video yoki audio:',
             ['Deepfake', 'Spam', 'Botnet', 'Firewall'], 'a'),
            ('Xatni adashib boshqa odamga yuborish qanday tahdid?',
             ['Tabiiy', 'Qasddan tashqi', 'Texnik', 'Tasodifiy inson tahdidi'], 'd'),
        ],
        'mustaqil': ['Texnikum kompyuter xonasi uchun 10 ta tahdidni yozib, ularni tasnif belgilari bo‘yicha jadvalga joylang.',
                     'Telefon orqali firibgarlikdan himoyalanish bo‘yicha oila a’zolaringiz uchun 5 ta qoida yozing.'],
    },
    # ------------------------------------------------------------------ 10
    {
        'type': 'N',
        'title': 'Xavflarni aniqlash va baholash usullari',
        'reja': ['Xavflarni boshqarish jarayoni',
                 'Xavflarni baholashning sifat va miqdoriy usullari',
                 'Xavflar matritsasi va xavfga munosabat strategiyalari'],
        'maqsad': 'O‘quvchilarga xavflarni aniqlash, ehtimollik va zarar bo‘yicha baholash hamda xavflar matritsasidan '
                  'foydalanish usullarini tushuntirish.',
        'natija': 'O‘quvchilar xavflarni boshqarish bosqichlarini biladi, xavflar matritsasi yordamida xavf darajasini '
                  'aniqlaydi va mos strategiyani tanlaydi.',
        'bolimlar': [
            """
## Xavflarni boshqarish
- **Xavflarni boshqarish** — xavflarni aniqlash, baholash va ularni maqbul darajagacha kamaytirish choralarini ko‘rishning uzluksiz jarayoni.
Jarayon quyidagi bosqichlardan iborat:
- **Aktivlarni aniqlash.** Nimani himoya qilamiz: server, ma’lumotlar bazasi, xodimlar kompyuterlari, veb-sayt.
- **Tahdid va zaifliklarni aniqlash.** Har bir aktivga qanday tahdidlar bor va qayerda kamchilik mavjud.
- **Xavfni baholash.** Ehtimollik va zarar darajasi aniqlanadi.
- **Choralarni tanlash.** Xavfni kamaytiruvchi himoya vositalari belgilanadi.
- **Nazorat va qayta ko‘rib chiqish.** Vaqti-vaqti bilan baholash yangilanadi.
- **Aktiv** — tashkilot uchun qimmatga ega bo‘lgan va himoya qilinishi kerak bo‘lgan har qanday resurs.
""",
            """
## Baholash usullari
- **Sifat usuli** — xavf darajasi so‘zlar yoki ballar bilan ifodalanadi: past, o‘rta, yuqori.
- **Miqdoriy usul** — xavf pul yoki son ko‘rinishida hisoblanadi.
Sifat usuli soddaroq va maktab, kichik ofislar uchun qulay. Miqdoriy usulda yillik kutilayotgan zarar hisoblanadi:
| Ko‘rsatkich | Ma’nosi | Misol |
| Bir martalik zarar | Hodisa bir marta yuz berganda ko‘riladigan zarar | Server diskini tiklash — 2 mln so‘m |
| Yillik ehtimollik | Hodisaning bir yilda necha marta yuz berishi | 0,5 (ikki yilda bir marta) |
| Yillik kutilayotgan zarar | Zarar × ehtimollik | 2 mln × 0,5 = 1 mln so‘m |
Agar himoya vositasining yillik narxi kutilayotgan zarardan kam bo‘lsa, uni qo‘llash iqtisodiy jihatdan foydali.
""",
            """
## Xavflar matritsasi
Sifat usulida ehtimollik va zarar 1 dan 3 gacha ball bilan baholanadi. Xavf darajasi = ehtimollik × zarar.
| Ehtimollik \\ Zarar | Kichik (1) | O‘rta (2) | Katta (3) |
| Yuqori (3) | 3 — o‘rta | 6 — yuqori | 9 — juda yuqori |
| O‘rta (2) | 2 — past | 4 — o‘rta | 6 — yuqori |
| Past (1) | 1 — past | 2 — past | 3 — o‘rta |
## Xavfga munosabat strategiyalari
- **Kamaytirish.** Himoya vositasi o‘rnatiladi: antivirus, zaxira nusxa.
- **Uzatish.** Xavf boshqa tomonga o‘tkaziladi: sug‘urta, tashqi xizmat ko‘rsatuvchi.
- **Qochish.** Xavfli faoliyatdan voz kechiladi: eskirgan dasturdan foydalanish to‘xtatiladi.
- **Qabul qilish.** Xavf kichik bo‘lsa, uni ongli ravishda qabul qilib, kuzatib boriladi.
""",
        ],
        'oldingi': ['Tahdid manbalarining qanday turlari bor?',
                    'Ichki va tashqi tahdidga misol keltiring.',
                    'Xavf tushunchasi nimani anglatadi?'],
        'savollar': ['Xavflarni boshqarish jarayoni qanday bosqichlardan iborat?',
                     'Aktiv deganda nimani tushunasiz?',
                     'Sifat va miqdoriy baholash usullarining farqi nimada?',
                     'Xavflar matritsasida xavf darajasi qanday hisoblanadi?',
                     'Xavfga munosabatning qanday strategiyalari bor?'],
        'testlar': [
            ('Tashkilot uchun qimmatga ega va himoya qilinishi kerak bo‘lgan resurs:',
             ['Tahdid', 'Aktiv', 'Zaiflik', 'Hodisa'], 'b'),
            ('Ehtimollik 3, zarar 2 bo‘lsa, xavf darajasi necha ball?',
             ['5', '1', '6', '9'], 'c'),
            ('Xavfni sug‘urta orqali boshqa tomonga o‘tkazish strategiyasi:',
             ['Uzatish', 'Qochish', 'Qabul qilish', 'Kamaytirish'], 'a'),
            ('Xavf past, o‘rta, yuqori kabi so‘zlar bilan ifodalanadigan usul:',
             ['Miqdoriy usul', 'Statistik usul', 'Moliyaviy usul', 'Sifat usuli'], 'd'),
            ('Bir martalik zarar 4 mln so‘m, yillik ehtimollik 0,25. Yillik kutilayotgan zarar:',
             ['1 mln so‘m', '4 mln so‘m', '16 mln so‘m', '0,25 mln so‘m'], 'a'),
        ],
        'mustaqil': ['Uy kompyuteringiz uchun 5 ta xavfni aniqlab, ularni xavflar matritsasi asosida baholang.',
                     'Har bir xavf uchun munosabat strategiyasini tanlang va asoslang.'],
    },
]
