"""21–30-mavzular: 2FA ni sozlash, internetda xavfsiz ishlash, phishing, tarmoq va Wi-Fi xavfsizligi."""

MAVZULAR = [
    # ------------------------------------------------------------------ 21
    {
        'type': 'A',
        'title': 'Elektron pochta va xizmatlarda 2FA ni sozlash',
        'reja': ['2FA ni sozlashga tayyorgarlik',
                 'Amaliy ish: Gmail va Telegram’da ikki bosqichli himoyani yoqish',
                 'Zaxira kodlarni saqlash va 2FA ishlashini tekshirish'],
        'maqsad': 'O‘quvchilarda elektron pochta va messenjerlarda ikki bosqichli autentifikatsiyani yoqish, '
                  'autentifikator ilovasini ulash va zaxira kodlarni to‘g‘ri saqlash ko‘nikmasini shakllantirish.',
        'natija': 'O‘quvchilar Google hisobida 2FA ni yoqadi, autentifikator ilovasini ulaydi, Telegram’da bulutli parol '
                  'o‘rnatadi va zaxira kodlarni xavfsiz saqlaydi.',
        'vosita': 'Internetga ulangan kompyuterlar, o‘quvchilarning smartfonlari, o‘quv Google hisoblari, proyektor',
        'bolimlar': [
            """
## Tayyorgarlik
2FA ni yoqishdan oldin quyidagilarga ishonch hosil qilinadi:
- Hisob paroli kuchli va boshqa saytlarda takrorlanmaydi.
- Hisobga ulangan telefon raqami hozir ishlatilayotgan raqam.
- Smartfonda ekran qulfi o‘rnatilgan.
- Zaxira kodlarni yozib olish uchun qog‘oz yoki xavfsiz joy tayyor.
Amaliy ish o‘quv maqsadida ochilgan hisoblarda bajariladi. Shaxsiy hisobingizda sozlashni uyda, o‘zingiz bajarasiz — parolingizni hech kimga, jumladan o‘qituvchiga ham aytmang.
- **Bulutli parol** — Telegram’da SMS-koddan keyin qo‘shimcha so‘raladigan parol; u Telegram’ning ikki bosqichli himoyasi hisoblanadi.
""",
            """
## Google hisobida 2FA ni yoqish
- **Sozlamalarni ochish.** myaccount.google.com → «Безопасность» (Xavfsizlik) bo‘limiga o‘ting.
- **Ikki bosqichli tekshiruv.** «Двухэтапная аутентификация» bandini tanlang va telefon raqamini tasdiqlang.
- **Autentifikator ulash.** «Приложение Authenticator» bandida «Настроить» ni bosing; ekranda QR-kod chiqadi. Telefondagi Google Authenticator ilovasida «+» → «QR-kodni skanerlash» orqali kodni skanerlang.
- **Tasdiqlash.** Ilovada paydo bo‘lgan 6 xonali kodni saytga kiriting.
## Telegram’da himoya
- **Bulutli parolni o‘rnatish.** Telegram → «Настройки» → «Конфиденциальность» → «Облачный пароль» → kuchli parol va maslahat (podskazka) kiriting.
- **Tiklash pochtasini ulash.** Parol unutilganda tiklash uchun elektron pochta kiritiladi va tasdiqlanadi.
- **Faol seanslarni tekshirish.** «Устройства» bo‘limida begona qurilmalar bo‘lsa, «Завершить все другие сеансы» ni bosing.
""",
            """
## Zaxira kodlar
Google hisobida «Резервные коды» bandi orqali 10 ta bir martalik kod olinadi. Ular chop etiladi yoki qog‘ozga yozib, xavfsiz joyda saqlanadi. Har bir kod faqat bir marta ishlaydi.
## 2FA ni tekshirish
- **Chiqib qayta kirish.** Brauzerning yashirin oynasida (`Ctrl + Shift + N`) hisobga kiring — parol kiritilgandan so‘ng tizim ikkinchi bosqich kodini so‘rashi kerak.
- **Natijani qayd etish.** Har bir xizmat uchun natija jadvalga yoziladi.
| Xizmat | 2FA usuli | Holat | Zaxira usuli |
| Google (Gmail) | Authenticator ilovasi | Yoqilgan | 10 ta zaxira kod |
| Telegram | Bulutli parol | Yoqilgan | Tiklash pochtasi |
| Instagram | Autentifikator yoki SMS | Uyda sozlanadi | Zaxira kodlar |
Mashg‘ulot oxirida o‘quvchilar 2FA yoqilgan hisobga kirish qanchalik oddiyligini va himoya qanchalik oshganini muhokama qiladi.
""",
        ],
        'oldingi': ['2FA nima?',
                    'TOTP kodi qanday ishlaydi?',
                    'Zaxira kodlar qayerda saqlanadi?'],
        'savollar': ['2FA ni yoqishdan oldin nimalarga ishonch hosil qilish kerak?',
                     'Google hisobida autentifikator ilovasi qanday ulanadi?',
                     'Telegram’dagi bulutli parol nima?',
                     'Telegram’da begona qurilmani qanday chiqarib yuborish mumkin?',
                     '2FA ishlayotganini qanday tekshirish mumkin?'],
        'testlar': [
            ('Telegram’dagi ikki bosqichli himoya qanday ataladi?',
             ['Bulutli parol', 'PIN-kod', 'Stiker', 'Kanal'], 'a'),
            ('Autentifikator ilovasini hisobga ulash uchun nima skanerlanadi?',
             ['Shtrix-kod', 'Barmoq izi', 'QR-kod', 'Pasport'], 'c'),
            ('Brauzerning yashirin oynasini ochish tugmalari (Chrome):',
             ['Ctrl + P', 'Ctrl + Shift + N', 'Ctrl + S', 'Alt + F4'], 'b'),
            ('Google zaxira kodlarining har biri necha marta ishlatiladi?',
             ['Cheksiz', '10 marta', '3 marta', '1 marta'], 'd'),
            ('Telegram’da faol seanslar qaysi bo‘limda ko‘rinadi?',
             ['«Устройства»', '«Стикеры»', '«Звонки»', '«Папки»'], 'a'),
        ],
        'mustaqil': ['Uyda o‘z elektron pochtangizda 2FA ni yoqing va bajarilgan qadamlarni (shaxsiy ma’lumotlarsiz) yozing.',
                     'Oila a’zolaringizdan biriga Telegram bulutli parolini o‘rnatishda yordam bering va qisqa hisobot yozing.'],
    },
    # ------------------------------------------------------------------ 22
    {
        'type': 'N',
        'title': 'Internetda xavfsiz ishlash qoidalari',
        'reja': ['Internetdagi asosiy xavflar',
                 'Xavfsiz ulanish: HTTPS, sertifikat va domen nomi',
                 'Internetda xavfsiz ishlashning asosiy qoidalari'],
        'maqsad': 'O‘quvchilarga internetdagi asosiy xavflar, xavfsiz ulanish belgilari va internetda xavfsiz ishlash '
                  'qoidalarini tushuntirish.',
        'natija': 'O‘quvchilar xavfsiz va xavfli saytni farqlaydi, HTTPS va sertifikat vazifasini izohlaydi, internetda '
                  'xavfsiz ishlash qoidalariga amal qiladi.',
        'bolimlar': [
            """
## Internetdagi xavflar
Internet bilim, aloqa va xizmatlar manbai bo‘lishi bilan birga, unda xavflar ham ko‘p.
| Xavf | Qanday namoyon bo‘ladi |
| Firibgarlik | Soxta do‘konlar, «yutuq» xabarlari, soxta ish e’lonlari |
| Zararli dasturlar | «Bepul» dastur yoki o‘yin bilan birga yuklanadigan viruslar |
| Phishing | Bank, pochta yoki davlat xizmati nomidan soxta saytlar |
| Shaxsiy ma’lumot sizishi | Anketalar, testlar orqali ma’lumot yig‘ish |
| Kiberbulling | Internetda haqorat, tahdid, kamsitish |
| Ishonchsiz axborot | Soxta yangiliklar va vahimali xabarlar |
- **Kiberbulling** — internet va messenjerlar orqali insonni muntazam haqoratlash, qo‘rqitish yoki kamsitish.
- **Soxta yangilik** — ataylab tarqatiladigan, haqiqatga to‘g‘ri kelmaydigan yoki buzib ko‘rsatilgan xabar.
""",
            """
## HTTPS va sertifikat
- **HTTPS** — brauzer va sayt o‘rtasidagi ma’lumotlarni shifrlab uzatuvchi xavfsiz protokol.
- **SSL/TLS sertifikati** — saytning haqiqiyligini tasdiqlovchi va shifrlangan ulanishni ta’minlovchi raqamli hujjat.
Brauzer manzil satrida qulf belgisi yoki «Xavfsiz ulanish» yozuvi HTTPS ishlayotganini bildiradi. Lekin bu belgi faqat ulanish shifrlanganini ko‘rsatadi — sayt egasi firibgar bo‘lishi ham mumkin. Firibgarlar ham bepul sertifikat olishadi.
## Domen nomini tekshirish
Soxta saytlar haqiqiy sayt nomiga juda o‘xshash domen oladi:
| Haqiqiy | Soxta (misol) | Farqi |
| my.gov.uz | my-gov-uz.com | Boshqa domen zonasi |
| paypal.com | paypa1.com | «l» o‘rniga «1» |
| google.com | goog1e-login.net | Qo‘shimcha so‘z va raqam |
Domenning asosiy qismini aniqlash uchun oxirgi nuqtadan oldingi so‘z va zonaga (`.uz`, `.com`) qarang. «secure-bank.uz.login-verify.com» manzilining haqiqiy domeni — login-verify.com.
""",
            """
## Asosiy qoidalar
- Parol va karta ma’lumotlarini faqat manzilini o‘zingiz yozgan yoki xatcho‘pdan ochgan saytga kiriting.
- Dasturlarni faqat rasmiy saytlardan va do‘konlardan (Microsoft Store, Google Play) yuklang.
- Brauzer va operatsion tizimni yangilab boring.
- Ommaviy Wi-Fi’da bank operatsiyalarini bajarmang yoki VPN’dan foydalaning.
- Begona kompyuterda «Parolni saqlash» ni bosmang va ishni tugatgach hisobdan chiqing.
- Shaxsiy ma’lumotlarni (manzil, pasport, telefon) ochiq e’lon qilmang.
- Notanish odamlar bilan internetdagi tanishuvda ehtiyot bo‘ling, ular bilan yolg‘iz uchrashmang.
- Shubhali xabar haqida kattalarga yoki IT-mutaxassisga xabar bering.
- **Raqamli iz** — inson internetda qoldiradigan barcha ma’lumotlar: postlar, izohlar, rasmlar, qidiruvlar; ular uzoq yillar saqlanib qolishi mumkin.
""",
        ],
        'oldingi': ['Google hisobida 2FA qanday yoqiladi?',
                    'Telegram’dagi bulutli parol nima uchun kerak?',
                    'Zaxira kodlar nima?'],
        'savollar': ['Internetdagi asosiy xavflarni sanang.',
                     'HTTPS protokoli nimani ta’minlaydi?',
                     'Qulf belgisi saytning xavfsizligini to‘liq kafolatlaydimi?',
                     'Soxta domenni qanday aniqlash mumkin?',
                     'Raqamli iz nima?'],
        'testlar': [
            ('Brauzer va sayt o‘rtasidagi ma’lumotlarni shifrlovchi protokol:',
             ['HTTP', 'FTP', 'HTTPS', 'SMTP'], 'c'),
            ('«secure-bank.uz.login-verify.com» manzilining haqiqiy domeni:',
             ['secure-bank.uz', 'login-verify.com', 'bank.uz', 'uz.login'], 'b'),
            ('Internet orqali insonni muntazam haqoratlash va qo‘rqitish:',
             ['Kiberbulling', 'Brauzing', 'Striming', 'Bloging'], 'a'),
            ('Dasturlarni qayerdan yuklash xavfsiz?',
             ['Noma’lum forumdan', 'Reklama bannerdan', 'Begona fleshkadan', 'Rasmiy sayt yoki do‘kondan'], 'd'),
            ('Inson internetda qoldiradigan barcha ma’lumotlar:',
             ['Raqamli iz', 'Kesh', 'Cookie', 'Spam'], 'a'),
        ],
        'mustaqil': ['«Internetda xavfsiz ishlashning 10 qoidasi» mavzusida infografika tayyorlang.',
                     'O‘zingizning raqamli izingizni tahlil qiling: qidiruv tizimida ismingiz bo‘yicha nima topiladi?'],
    },
    # ------------------------------------------------------------------ 23
    {
        'type': 'A',
        'title': 'Internet brauzerlarida xavfsizlik sozlamalarini o‘rnatish',
        'reja': ['Brauzerning xavfsizlik va maxfiylik sozlamalari',
                 'Amaliy ish: Google Chrome xavfsizlik sozlamalarini o‘rnatish',
                 'Kengaytmalar, saqlangan parollar va tarixni boshqarish'],
        'maqsad': 'O‘quvchilarda brauzerda xavfsiz ko‘rish rejimini yoqish, sayt ruxsatlarini boshqarish, kengaytmalarni '
                  'tekshirish va maxfiylik sozlamalarini o‘rnatish ko‘nikmasini shakllantirish.',
        'natija': 'O‘quvchilar Chrome’da kengaytirilgan himoyani yoqadi, faqat HTTPS rejimini o‘rnatadi, sayt ruxsatlarini '
                  'cheklaydi, shubhali kengaytmalarni o‘chiradi va xavfsizlik tekshiruvini o‘tkazadi.',
        'vosita': 'Google Chrome va Microsoft Edge o‘rnatilgan kompyuterlar, internet, proyektor',
        'bolimlar': [
            """
## Brauzer — himoyaning birinchi chizig‘i
Internetdagi deyarli barcha ishlar brauzer orqali bajariladi, shuning uchun uning sozlamalari xavfsizlikka bevosita ta’sir qiladi.
| Sozlama | Vazifasi |
| Xavfsiz ko‘rish (Safe Browsing) | Xavfli va phishing saytlar haqida ogohlantiradi |
| Faqat HTTPS rejimi | Shifrlanmagan saytlarga kirishdan oldin ogohlantiradi |
| Sayt ruxsatlari | Kamera, mikrofon, joylashuv, bildirishnomalarga ruxsatni boshqaradi |
| Cookie fayllar | Uchinchi tomon kuzatuv cookie’larini bloklaydi |
| Kengaytmalar | Qo‘shimcha dasturlar; ular sahifadagi ma’lumotni o‘qiy oladi |
- **Cookie** — sayt brauzerga saqlaydigan kichik ma’lumot fayli; u kirish holatini eslab qoladi, lekin kuzatish uchun ham ishlatiladi.
- **Brauzer kengaytmasi** — brauzerga yangi imkoniyat qo‘shuvchi kichik dastur; zararli kengaytma parollar va yozishmalarni o‘g‘irlashi mumkin.
""",
            """
## Ishni bajarish tartibi (Google Chrome)
- **Sozlamalarni ochish.** Manzil satriga `chrome://settings/security` yozing.
- **Himoya darajasi.** «Расширенная защита» (Kengaytirilgan himoya) yoki kamida «Стандартная защита» ni tanlang.
- **Faqat HTTPS.** Shu sahifada «Всегда использовать безопасные подключения» ni yoqing.
- **Sayt ruxsatlari.** `chrome://settings/content` sahifasida joylashuv, kamera, mikrofon va bildirishnomalar uchun «Спрашивать» (so‘rash) rejimini qo‘ying; ruxsat berilgan noma’lum saytlarni o‘chiring.
- **Cookie sozlamasi.** «Сторонние файлы cookie» bo‘limida uchinchi tomon cookie’larini bloklang.
- **Xavfsizlik tekshiruvi.** `chrome://settings/safetyCheck` sahifasida «Проверить» tugmasini bosing — brauzer yangilanish, parollar va kengaytmalar holatini tekshiradi.
""",
            """
## Kengaytmalarni tekshirish
`chrome://extensions` sahifasida o‘rnatilgan kengaytmalar ro‘yxati ko‘rinadi. Har bir kengaytma uchun savol beriladi: men uni o‘rnatganmanmi? Hozir kerakmi? Ishonchli ishlab chiquvchimi? Keraksiz va noma’lum kengaytmalar o‘chiriladi.
## Parollar va tarix
- **Saqlangan parollar.** `chrome://password-manager` sahifasida «Проверка паролей» bo‘limi sizib chiqqan va takrorlangan parollarni ko‘rsatadi.
- **Tarixni tozalash.** `Ctrl + Shift + Delete` → vaqt oralig‘ini tanlab, tarix, cookie va keshni o‘chiring (umumiy kompyuterda ishdan keyin).
- **Yashirin rejim.** `Ctrl + Shift + N` — tarix va cookie saqlanmaydi, lekin bu internet provayder yoki tarmoq administratoridan yashirmaydi.
| Tekshiruv | Natija |
| Himoya darajasi | Kengaytirilgan / standart |
| Faqat HTTPS | Yoqilgan |
| Noma’lum kengaytmalar | O‘chirildi: __ ta |
| Sizib chiqqan parollar | __ ta (o‘quv hisobida) |
""",
        ],
        'oldingi': ['HTTPS protokoli nimani ta’minlaydi?',
                    'Soxta domenni qanday aniqlash mumkin?',
                    'Internetda xavfsiz ishlashning qanday qoidalarini bilasiz?'],
        'savollar': ['Xavfsiz ko‘rish (Safe Browsing) qanday vazifani bajaradi?',
                     'Cookie nima va u qanday xavf tug‘diradi?',
                     'Sayt ruxsatlari qayerda boshqariladi?',
                     'Kengaytmalarni nima uchun tekshirish kerak?',
                     'Yashirin rejim nimadan himoya qiladi va nimadan himoya qilmaydi?'],
        'testlar': [
            ('Chrome xavfsizlik sozlamalari sahifasi manzili:',
             ['chrome://settings/security', 'chrome://games', 'chrome://music', 'chrome://video'], 'a'),
            ('Brauzer tarixi va cookie’larni tozalash oynasini ochuvchi tugmalar:',
             ['Ctrl + P', 'Ctrl + Z', 'Ctrl + Shift + Delete', 'Ctrl + F'], 'c'),
            ('Sayt brauzerga saqlaydigan kichik ma’lumot fayli:',
             ['Drayver', 'Cookie', 'Arxiv', 'Shrift'], 'b'),
            ('Yashirin rejim nimani saqlamaydi?',
             ['Yuklab olingan fayllarni', 'Xatcho‘plarni', 'Internet provayder yozuvlarini', 'Tarix va cookie’larni'], 'd'),
            ('Noma’lum va keraksiz kengaytma bilan nima qilinadi?',
             ['O‘chiriladi', 'Barcha ruxsatlar beriladi', 'Do‘stlarga yuboriladi', 'Yangilanadi'], 'a'),
        ],
        'mustaqil': ['Uydagi brauzeringizda xavfsizlik tekshiruvini o‘tkazing va natijalarni jadvalga yozing.',
                     'Chrome, Edge va Firefox brauzerlarining xavfsizlik imkoniyatlarini taqqoslang.'],
    },
    # ------------------------------------------------------------------ 24
    {
        'type': 'A',
        'title': 'Xavfsiz internetdan foydalanish va xavfli saytlarni aniqlash',
        'reja': ['Xavfli sayt belgilari',
                 'Amaliy ish: saytlarni onlayn xizmatlar yordamida tekshirish',
                 'Sayt xavfsizligini baholash varag‘ini to‘ldirish'],
        'maqsad': 'O‘quvchilarda xavfli saytlarni tashqi belgilari bo‘yicha aniqlash va onlayn tekshiruv xizmatlari '
                  'yordamida havola hamda sayt xavfsizligini baholash ko‘nikmasini shakllantirish.',
        'natija': 'O‘quvchilar saytning domeni, sertifikati, yoshi va obro‘sini tekshiradi, VirusTotal va Google Safe '
                  'Browsing orqali havolalarni tahlil qiladi va baholash varag‘ini to‘ldiradi.',
        'vosita': 'Internetga ulangan kompyuterlar, brauzer, o‘qituvchi tayyorlagan havolalar ro‘yxati, baholash varag‘i',
        'bolimlar': [
            """
## Xavfli sayt belgilari
| Belgi | Izoh |
| Manzil haqiqiy saytga juda o‘xshash | Harf almashtirilgan, qo‘shimcha so‘z qo‘shilgan |
| Juda arzon narxlar, «faqat bugun!» | Firibgar do‘kon belgisi |
| Darhol karta ma’lumoti so‘raladi | Oldindan to‘lov, aloqa ma’lumotlari yo‘q |
| Ko‘p qalqib chiquvchi oynalar | «Kompyuteringizda virus!» degan soxta ogohlantirishlar |
| Avtomatik fayl yuklanadi | Siz bosmagan holda .exe fayl yuklanadi |
| Imlo va tarjima xatolari | Shoshilib yasalgan soxta sayt |
| Kontaktlar va manzil yo‘q | Kompaniya haqida ma’lumot topilmaydi |
- **Qalqib chiquvchi oyna** — sayt ochilganda o‘z-o‘zidan paydo bo‘ladigan qo‘shimcha oyna; ko‘pincha reklama yoki soxta ogohlantirish uchun ishlatiladi.
- **Tipo-skvotting** — mashhur sayt nomining xato yozilishiga o‘xshash domenni ro‘yxatdan o‘tkazib, adashgan foydalanuvchilarni aldash.
""",
            """
## Ishni bajarish tartibi
- **Havolani ochmasdan tekshirish.** Havola ustiga sichqonchani olib boring (bosmang!) — brauzerning pastki chap burchagida haqiqiy manzil ko‘rinadi.
- **VirusTotal.** virustotal.com → «URL» bo‘limiga havolani joylab «Поиск» bosing; o‘nlab antivirus dasturlari natijasi chiqadi.
- **Google Safe Browsing.** transparencyreport.google.com/safe-browsing/search sahifasida sayt nomini tekshiring.
- **Sertifikatni ko‘rish.** Sayt ochilgan bo‘lsa, manzil satridagi qulf belgisi → «Подключение защищено» → «Сертификат» orqali kimga berilganini ko‘ring.
- **Sayt yoshini aniqlash.** whois xizmatida domen qachon ro‘yxatdan o‘tganini tekshiring — bir necha kun oldin yaratilgan «bank» sayti shubhali.
Tekshirish uchun o‘qituvchi bergan o‘quv havolalaridan foydalaning, shubhali saytlarga ma’lumot kiritmang.
""",
            """
## Baholash varag‘i
| Mezon | Ha | Yo‘q |
| Domen haqiqiy tashkilot nomiga to‘liq mos | | |
| HTTPS va sertifikat tashkilotga berilgan | | |
| Domen 1 yildan ortiq vaqt oldin yaratilgan | | |
| VirusTotal’da xavf aniqlanmagan | | |
| Kontaktlar, manzil, telefon ko‘rsatilgan | | |
| Qalqib chiquvchi soxta ogohlantirishlar yo‘q | | |
## Xulosa
5–6 ta «ha» — sayt ishonchli, 3–4 ta — ehtiyotkorlik bilan foydalanish, 2 va kam — sayt xavfli, undan foydalanmaslik kerak. Xavfli sayt topilganda Safe Browsing’ga xabar berish (Report phishing) mumkin — bu boshqa foydalanuvchilarni ham himoya qiladi.
""",
        ],
        'oldingi': ['Chrome’da qanday xavfsizlik sozlamalarini o‘rnatdik?',
                    'Cookie nima?',
                    'Kengaytmalarni qanday tekshirdik?'],
        'savollar': ['Xavfli saytning qanday belgilarini bilasiz?',
                     'Tipo-skvotting nima?',
                     'Havolani ochmasdan haqiqiy manzilini qanday ko‘rish mumkin?',
                     'VirusTotal xizmati qanday ishlaydi?',
                     'Nima uchun yangi yaratilgan domen shubha uyg‘otadi?'],
        'testlar': [
            ('Havolani bir necha antivirus bilan tekshiradigan onlayn xizmat:',
             ['VirusTotal', 'YouTube', 'Wikipedia', 'Canva'], 'a'),
            ('Mashhur sayt nomining xato yozilishiga o‘xshash domen olish:',
             ['Brute force', 'Spam', 'Tipo-skvotting', 'Striming'], 'c'),
            ('Havolaning haqiqiy manzilini xavfsiz ko‘rish usuli:',
             ['Havolani bosish', 'Sichqonchani havola ustiga olib borish', 'Havolani do‘stga yuborish', 'Kompyuterni o‘chirish'], 'b'),
            ('Domen qachon ro‘yxatdan o‘tganini aniqlash xizmati:',
             ['Paint', 'Excel', 'Telegram', 'Whois'], 'd'),
            ('«Kompyuteringizda virus! Darhol yuklab oling» degan qalqib chiquvchi oyna:',
             ['Soxta ogohlantirish', 'Operatsion tizim xabari', 'Antivirus hisoboti', 'Rasmiy xabar'], 'a'),
        ],
        'mustaqil': ['Internetdagi 3 ta onlayn do‘konni baholash varag‘i asosida tekshiring va natijalarni taqqoslang.',
                     'Firibgar saytlar haqida tengdoshlaringiz uchun qisqa video yoki ovozli xabar ssenariysini yozing.'],
    },
    # ------------------------------------------------------------------ 25
    {
        'type': 'N',
        'title': 'Shubhali havola, fayl va xabarlarni aniqlash',
        'reja': ['Phishing va ijtimoiy muhandislik xabarlarining tuzilishi',
                 'Shubhali havola va fayllar belgilari',
                 'Shubhali xabar olinganda harakatlar tartibi'],
        'maqsad': 'O‘quvchilarga phishing xabarlarning tuzilishi, shubhali havola va fayllar belgilari hamda bunday '
                  'xabar olinganda to‘g‘ri harakat qilish tartibini tushuntirish.',
        'natija': 'O‘quvchilar phishing xabardagi psixologik usullarni aniqlaydi, xavfli fayl kengaytmalarini biladi va '
                  'shubhali xabarga to‘g‘ri munosabatda bo‘ladi.',
        'bolimlar': [
            """
## Phishing xabar qanday tuziladi?
Firibgarlar insonning his-tuyg‘ularidan foydalanadi. Phishing xabarlarda odatda quyidagi psixologik usullar uchraydi:
| Usul | Misol |
| Shoshiltirish | «24 soat ichida tasdiqlamasangiz, hisobingiz o‘chiriladi!» |
| Qo‘rqitish | «Kartangizdan shubhali to‘lov amalga oshirildi» |
| Ochko‘zlik | «Siz iPhone yutib oldingiz! Yetkazish uchun 20 000 so‘m to‘lang» |
| Obro‘ | «Bank xavfsizlik xizmati», «Soliq qo‘mitasi», «direktor» nomidan |
| Qiziqish | «Sizning rasmlaringiz shu yerda tarqalmoqda, ko‘ring» |
- **Smishing** — SMS orqali amalga oshiriladigan phishing.
- **Vishing** — telefon qo‘ng‘irog‘i orqali amalga oshiriladigan phishing.
- **Spear-phishing** — aniq bir shaxs yoki tashkilotga qaratilgan, oldindan to‘plangan ma’lumotlar asosida tuzilgan maqsadli phishing.
""",
            """
## Shubhali havola belgilari
- Qisqartirilgan havolalar (bit.ly va shu kabilar) — oxirida qayerga olib borishi ko‘rinmaydi.
- Domen tashkilot nomiga mos emas yoki harflar almashtirilgan.
- Havolada IP manzil bor: `http://185.23.xx.xx/login`.
- Havola matni va haqiqiy manzili farq qiladi.
## Xavfli fayllar
| Kengaytma | Xavf |
| .exe, .msi, .scr, .bat, .cmd | Dastur — ochilsa darhol ishga tushadi |
| .js, .vbs, .ps1 | Skript — zararli buyruqlarni bajaradi |
| .docm, .xlsm | Makrosli hujjat — makros yoqilsa, virus ishga tushadi |
| .zip, .rar parolli arxiv | Antivirus ichini tekshira olmaydi |
| «hujjat.pdf.exe» | Ikki kengaytma — aslida dastur |
- **Makros** — Word yoki Excel hujjati ichiga yozilgan kichik dastur; zararli makros kompyuterga virus o‘rnatishi mumkin.
Windows’da fayl kengaytmalari ko‘rinib turishi uchun Explorer’da «Вид» → «Расширения имён файлов» belgilanadi.
""",
            """
## Harakatlar tartibi
- **To‘xtang.** Shoshilmang — firibgar aynan shoshilishingizni kutadi.
- **Tekshiring.** Yuboruvchi manzilini, havolani va matnni diqqat bilan ko‘ring.
- **Boshqa kanal orqali aniqlang.** Bank yoki tanishingizga o‘zingiz bilgan rasmiy raqam orqali qo‘ng‘iroq qiling.
- **Ochmang.** Havola va ilovani ochmang, javob yozmang, kodlarni aytmang.
- **Xabar bering.** Ish joyida — IT-bo‘limga, shaxsiy holatda — bankka; xabarni «spam» deb belgilang.
- **Xato qilgan bo‘lsangiz.** Darhol parolni almashtiring, bankka qo‘ng‘iroq qilib kartani bloklang, kompyuterni antivirus bilan tekshiring.
Bank va davlat tashkilotlari hech qachon SMS-kod, karta PIN-kodi yoki CVV kodini telefon orqali so‘ramaydi.
""",
        ],
        'oldingi': ['Xavfli saytning qanday belgilari bor?',
                    'VirusTotal xizmati nima uchun kerak?',
                    'Tipo-skvotting nima?'],
        'savollar': ['Phishing xabarlarda qanday psixologik usullar qo‘llaniladi?',
                     'Smishing va vishingning farqi nimada?',
                     'Qanday fayl kengaytmalari xavfli?',
                     '«hujjat.pdf.exe» fayli nima uchun xavfli?',
                     'Shubhali xabar olganda qanday harakat qilish kerak?'],
        'testlar': [
            ('SMS orqali amalga oshiriladigan phishing:',
             ['Vishing', 'Smishing', 'Spam', 'Striming'], 'b'),
            ('Aniq bir shaxsga qaratilgan maqsadli phishing:',
             ['Spear-phishing', 'DDoS', 'Brute force', 'Vishing'], 'a'),
            ('Quyidagi fayllardan qaysi biri aslida dastur?',
             ['rasm.jpg', 'hisobot.pdf', 'hujjat.pdf.exe', 'qo‘shiq.mp3'], 'c'),
            ('Bank telefon orqali hech qachon nimani so‘ramaydi?',
             ['Ismingizni', 'Qaysi filialga kelishingizni', 'Qulay vaqtingizni', 'SMS-kod va PIN-kodni'], 'd'),
            ('Word hujjati ichidagi kichik dastur:',
             ['Makros', 'Shrift', 'Kolontitul', 'Jadval'], 'a'),
        ],
        'mustaqil': ['Shubhali xabarlarning 5 ta namunasini (o‘zingiz o‘ylab toping) tuzib, har biridagi psixologik usulni aniqlang.',
                     '«Shubhali xabar olsangiz» mavzusida bir sahifali yo‘riqnoma tayyorlang.'],
    },
    # ------------------------------------------------------------------ 26
    {
        'type': 'A',
        'title': 'Shubhali havola va phishing xabarlarini aniqlash',
        'reja': ['Elektron xatning texnik belgilarini o‘rganish',
                 'Amaliy ish: phishing xatlarni tahlil qilish',
                 'Phishing haqida xabar berish va himoya choralarini qo‘llash'],
        'maqsad': 'O‘quvchilarda elektron xatning yuboruvchi manzili, sarlavhalari va havolalarini tekshirib, phishing '
                  'xatlarni haqiqiysidan ajratish ko‘nikmasini shakllantirish.',
        'natija': 'O‘quvchilar xat yuboruvchisini va havolalarni tekshiradi, xat sarlavhasidan ma’lumot oladi, phishing '
                  'xatni belgilaydi va xabar beradi.',
        'vosita': 'O‘qituvchi tayyorlagan phishing va haqiqiy xatlar namunalari (skrinshot), o‘quv pochta hisoblari, kompyuterlar',
        'bolimlar': [
            """
## Xatning texnik belgilari
- **Yuboruvchi manzili.** Ko‘rinadigan ism («Bank xavfsizlik xizmati») har qanday bo‘lishi mumkin; haqiqiy manzilni ko‘rish uchun ism ustiga bosing.
- **Javob manzili.** «Reply-To» maydoni boshqa manzilga yo‘naltirilgan bo‘lsa — shubhali.
- **Murojaat.** «Hurmatli mijoz» kabi umumiy murojaat; haqiqiy tashkilotlar odatda ismingiz bilan murojaat qiladi.
- **Havolalar.** Matndagi havola va haqiqiy manzil mos kelmaydi.
- **Ilovalar.** Kutilmagan arxiv yoki makrosli hujjat.
- **Xat sarlavhasi** — xatning qaysi serverlardan o‘tgani, yuboruvchi va tekshiruv natijalari yozilgan texnik ma’lumotlar qismi.
- **SPF va DKIM** — xat haqiqatan ham ko‘rsatilgan domen serveridan yuborilganini tekshiruvchi texnologiyalar.
""",
            """
## Ishni bajarish tartibi
- **Namunalarni ko‘rish.** Har bir juftlik 8 ta xat namunasini oladi: ulardan bir qismi haqiqiy, bir qismi phishing.
- **Belgilarni aniqlash.** Har bir xatda yuboruvchi, murojaat, shoshiltirish, havola va ilovani tekshiring.
- **Sarlavhani ochish.** O‘quv Gmail hisobida xatni oching → «⋮» → «Показать оригинал» — SPF va DKIM natijalari «PASS» yoki «FAIL» ekanini ko‘ring.
- **Havolani tekshirish.** Havolani nusxalab (ochmasdan!) VirusTotal’da tekshiring.
- **Xulosa.** Har bir xat uchun «Haqiqiy» yoki «Phishing» deb yozing va kamida 2 ta dalil keltiring.
| Xat | Yuboruvchi | Belgilar | SPF/DKIM | Xulosa |
| 1 | support@paypa1-secure.com | Shoshiltirish, harf almashgan | FAIL | Phishing |
| 2 | no-reply@accounts.google.com | Ismingiz bilan, havola google.com | PASS | Haqiqiy |
""",
            """
## Xabar berish
- **Gmail’da.** Xatni oching → «⋮» → «Сообщить о фишинге». Xat o‘chiriladi va Google boshqa foydalanuvchilarni ogohlantiradi.
- **Outlook’da.** «Сообщить» → «Фишинг».
- **Tashkilotda.** Xatni ochmasdan IT-bo‘limga yo‘naltiring.
## Himoya choralari
- Pochtada 2FA yoqilgan bo‘lishi.
- Spam filtrini o‘chirmaslik.
- Xatdagi havola orqali emas, saytga manzilni o‘zingiz yozib kirish.
- Makroslarni avtomatik ishga tushirishni taqiqlash (Office’da standart holatda o‘chirilgan).
- **Spam filtri** — kiruvchi xatlarni tahlil qilib, reklama va shubhali xatlarni alohida papkaga ajratuvchi tizim.
Mashg‘ulot oxirida eng ko‘p phishing xatni to‘g‘ri aniqlagan juftlik rag‘batlantiriladi.
""",
        ],
        'oldingi': ['Phishing xabarlarda qanday psixologik usullar ishlatiladi?',
                    'Qanday fayl kengaytmalari xavfli?',
                    'Shubhali xabar olganda nima qilish kerak?'],
        'savollar': ['Xat yuboruvchisining haqiqiy manzilini qanday ko‘rish mumkin?',
                     'SPF va DKIM nimani tekshiradi?',
                     'Gmail’da xat sarlavhasi qanday ochiladi?',
                     'Phishing xat haqida qanday xabar beriladi?',
                     'Spam filtri qanday vazifani bajaradi?'],
        'testlar': [
            ('Xat ko‘rsatilgan domen serveridan yuborilganini tekshiruvchi texnologiyalar:',
             ['SPF va DKIM', 'HTML va CSS', 'USB va HDMI', 'RAM va ROM'], 'a'),
            ('Gmail’da xatning texnik sarlavhasini ko‘rish buyrug‘i:',
             ['«Печать»', '«Переслать»', '«Показать оригинал»', '«Удалить»'], 'c'),
            ('«support@paypa1-secure.com» manzili:',
             ['Haqiqiy PayPal manzili', 'Shubhali (harf almashtirilgan)', 'Davlat manzili', 'Bank manzili'], 'b'),
            ('Reklama va shubhali xatlarni alohida papkaga ajratuvchi tizim:',
             ['Arxivator', 'Brauzer', 'Drayver', 'Spam filtri'], 'd'),
            ('Xatdagi havolani xavfsiz tekshirish usuli:',
             ['Nusxalab VirusTotal’da tekshirish', 'Darhol bosish', 'Do‘stlarga yuborish', 'Javob yozish'], 'a'),
        ],
        'mustaqil': ['O‘z pochtangizning «Spam» papkasidagi 3 ta xatni tahlil qilib, phishing belgilarini yozing (havolalarni ochmang).',
                     'Phishing xatni aniqlash bo‘yicha 10 ta savoldan iborat test tuzing.'],
    },
    # ------------------------------------------------------------------ 27
    {
        'type': 'A',
        'title': 'Shubhali fayllarni tekshirish va xavfsizligini baholash',
        'reja': ['Fayl xavfsizligini tekshirish usullari',
                 'Amaliy ish: faylni antivirus, VirusTotal va xesh-summa orqali tekshirish',
                 'Fayl xavfsizligi bo‘yicha xulosa chiqarish'],
        'maqsad': 'O‘quvchilarda shubhali fayllarni ochmasdan tekshirish: kengaytma, raqamli imzo, xesh-summa, antivirus '
                  'va onlayn xizmatlar yordamida xavfsizligini baholash ko‘nikmasini shakllantirish.',
        'natija': 'O‘quvchilar fayl kengaytmasi va raqamli imzosini tekshiradi, certutil orqali xesh-summani hisoblaydi, '
                  'faylni Defender va VirusTotal’da tekshirib, xulosa yozadi.',
        'vosita': 'Windows 10/11 kompyuterlar, o‘qituvchi tayyorlagan zararsiz test fayllari (EICAR test fayli), internet',
        'bolimlar': [
            """
## Tekshirish usullari
| Usul | Nimani ko‘rsatadi |
| Kengaytmani ko‘rish | Fayl turi — hujjat, rasm yoki dastur |
| Raqamli imzo | Dastur kim tomonidan chiqarilgani va o‘zgartirilmagani |
| Xesh-summa | Fayl rasmiy saytdagi asl nusxa bilan bir xilligi |
| Antivirus bilan skanerlash | Ma’lum zararli dasturlar bor-yo‘qligi |
| VirusTotal | 70 ga yaqin antivirus dasturining xulosasi |
- **Xesh-summa** — fayl tarkibidan maxsus algoritm bilan hisoblanadigan qisqa qiymat; faylda bitta belgi o‘zgarsa ham, xesh butunlay boshqacha bo‘ladi.
- **Raqamli imzo** — dastur ishlab chiqaruvchisi tomonidan qo‘yiladigan, faylning muallifi va yaxlitligini tasdiqlovchi kriptografik belgi.
- **EICAR test fayli** — antivirus ishlashini tekshirish uchun yaratilgan, mutlaqo zararsiz, lekin barcha antiviruslar «virus» deb aniqlaydigan maxsus fayl.
""",
            """
## Ishni bajarish tartibi
- **Kengaytmani ko‘rsatish.** Explorer’da «Вид» → «Показать» → «Расширения имён файлов» ni yoqing va papkadagi fayllar turini aniqlang.
- **Raqamli imzoni tekshirish.** Dastur fayli ustida o‘ng tugma → «Свойства» → «Цифровые подписи» bo‘limida imzo egasini ko‘ring. Imzo yo‘q bo‘lsa — ehtiyot bo‘ling.
- **Xeshni hisoblash.** Buyruqlar satrida: `certutil -hashfile D:\\test\\setup.exe SHA256` — chiqqan qiymatni rasmiy saytdagi qiymat bilan solishtiring.
- **Defender bilan skanerlash.** Fayl ustida o‘ng tugma → «Проверить с помощью Microsoft Defender».
- **VirusTotal.** virustotal.com saytiga faylni yuklang (maxfiy hujjatlarni yuklamang — ular boshqalarga ko‘rinishi mumkin).
- **EICAR sinovi.** O‘qituvchi namoyishida EICAR test fayli yaratiladi va antivirus uni qanday bloklashi kuzatiladi.
""",
            """
## Natijalar jadvali
| Fayl | Haqiqiy turi | Raqamli imzo | Xesh mosligi | Antivirus | Xulosa |
| setup.exe | Dastur | Ishonchli ishlab chiquvchi | Mos | Toza | Xavfsiz |
| hisobot.pdf.exe | Dastur | Yo‘q | — | Aniqlandi | Xavfli — o‘chirish |
| eicar.com | Test fayli | Yo‘q | — | Aniqlandi | Test natijasi to‘g‘ri |
## Xulosa chiqarish
Bitta usulning o‘zi yetarli emas. Masalan, yangi chiqqan zararli dasturni antiviruslar hali bilmasligi mumkin, shuning uchun imzo va manba ham tekshiriladi. Shubha qolsa, fayl ochilmaydi.
- **Karantin** — antivirus aniqlagan shubhali faylni yopiq joyga ko‘chirib, ishga tushishiga yo‘l qo‘ymaydigan himoya holati.
""",
        ],
        'oldingi': ['Phishing xatni qanday belgilar orqali aniqladik?',
                    'SPF va DKIM nima?',
                    'Qanday fayl kengaytmalari xavfli?'],
        'savollar': ['Xesh-summa nima va u nima uchun kerak?',
                     'Dasturning raqamli imzosini qanday tekshirish mumkin?',
                     'certutil buyrug‘i qanday ishlatiladi?',
                     'EICAR test fayli nima uchun yaratilgan?',
                     'Nima uchun maxfiy hujjatni VirusTotal’ga yuklash tavsiya etilmaydi?'],
        'testlar': [
            ('Fayl xesh-summasini hisoblovchi Windows buyrug‘i:',
             ['certutil -hashfile', 'ipconfig /all', 'ping', 'tasklist'], 'a'),
            ('Faylda bitta belgi o‘zgarsa, xesh-summa:',
             ['O‘zgarmaydi', 'Ikki baravar oshadi', 'Butunlay boshqacha bo‘ladi', 'Nolga teng bo‘ladi'], 'c'),
            ('Antivirus ishlashini tekshirish uchun yaratilgan zararsiz fayl:',
             ['WannaCry', 'EICAR test fayli', 'Troyan', 'Keylogger'], 'b'),
            ('Antivirus shubhali faylni yopiq joyga ko‘chirishi:',
             ['Arxivlash', 'Defragmentatsiya', 'Formatlash', 'Karantin'], 'd'),
            ('Dastur muallifi va yaxlitligini tasdiqlovchi belgi:',
             ['Raqamli imzo', 'Fayl hajmi', 'Yaratilgan sana', 'Ikonka'], 'a'),
        ],
        'mustaqil': ['Biror rasmiy dastur (masalan, 7-Zip) saytidan o‘rnatish faylini yuklab, xesh-summasi va raqamli imzosini tekshiring.',
                     'MD5, SHA-1 va SHA-256 algoritmlari farqini o‘rganib, qisqa izoh yozing.'],
    },
    # ------------------------------------------------------------------ 28
    {
        'type': 'N',
        'title': 'Tarmoqda ma’lumotlarni himoya qilish usullari',
        'reja': ['Tarmoqdagi tahdidlar va himoya darajalari',
                 'Tarmoqlararo ekran, VPN va tarmoqni segmentlash',
                 'Ma’lumot uzatishni shifrlash protokollari'],
        'maqsad': 'O‘quvchilarga tarmoqdagi asosiy tahdidlar, tarmoqlararo ekran, VPN, segmentlash va shifrlash '
                  'protokollari orqali ma’lumotlarni himoya qilish usullarini tushuntirish.',
        'natija': 'O‘quvchilar tarmoq tahdidlarini sanaydi, firewall va VPN vazifasini izohlaydi, xavfsiz va xavfsiz '
                  'bo‘lmagan protokollarni farqlaydi.',
        'bolimlar': [
            """
## Tarmoqdagi tahdidlar
Kompyuter tarmoqlari va IT-servis mutaxassisi uchun tarmoq xavfsizligi asosiy vazifalardan biri. Lokal tarmoqda bir kompyuter zararlansa, virus qolgan kompyuterlarga ham tarqalishi mumkin.
| Tahdid | Mazmuni |
| Trafikni tinglash | Shifrlanmagan ma’lumotlarni tarmoqdan ushlab o‘qish |
| Ruxsatsiz ulanish | Begona qurilmaning tarmoqqa ulanishi |
| Portlarni skanerlash | Hujumchi ochiq xizmatlarni izlaydi |
| Soxta kirish nuqtasi | Haqiqiy Wi-Fi nomiga o‘xshash tuzoq tarmoq |
| Chuvalchanglar | Tarmoq orqali kompyuterdan kompyuterga tarqalish |
- **Trafik** — tarmoq orqali uzatilayotgan ma’lumotlar oqimi.
- **Sniffer** — tarmoq trafikini ushlab, tahlil qiluvchi dastur; administrator uchun diagnostika vositasi, hujumchi uchun josuslik quroli.
""",
            """
## Himoya vositalari
- **Tarmoqlararo ekran** — oldindan belgilangan qoidalar asosida tarmoq trafikini filtrlaydigan, ruxsat etilmagan ulanishlarni bloklaydigan dasturiy yoki apparat vosita (firewall).
- **VPN** — ochiq tarmoq ustida shifrlangan «tunnel» yaratib, ma’lumotlarni begona ko‘zdan himoyalovchi virtual xususiy tarmoq.
- **Tarmoqni segmentlash** — tarmoqni alohida qismlarga (masalan, VLAN) bo‘lish; bir qismdagi muammo boshqasiga tarqalmaydi.
- **VLAN** — bitta fizik kommutator ichida mantiqiy ajratilgan alohida virtual tarmoqlar.
Masalan, texnikumda buxgalteriya, o‘quv xonalari va mehmon Wi-Fi alohida VLAN’larga ajratiladi: mehmon tarmog‘idagi qurilma buxgalteriya serveriga kira olmaydi.
## Tarmoq qurilmalari xavfsizligi
- Router va kommutatorlarning standart parollari almashtiriladi.
- Qurilma dasturi (proshivka) yangilanadi.
- Ishlatilmaydigan portlar o‘chiriladi.
- Boshqaruv paneliga faqat ichki tarmoqdan kirishga ruxsat beriladi.
""",
            """
## Xavfsiz va xavfsiz bo‘lmagan protokollar
| Vazifa | Xavfsiz bo‘lmagan | Xavfsiz o‘rinbosar |
| Veb-saytlar | HTTP (80-port) | HTTPS (443-port) |
| Masofadan boshqarish | Telnet (23-port) | SSH (22-port) |
| Fayl uzatish | FTP (21-port) | SFTP, FTPS |
| Pochta | POP3/IMAP shifrsiz | IMAPS, SMTP + TLS |
| Wi-Fi | WEP, ochiq tarmoq | WPA2, WPA3 |
- **SSH** — tarmoq qurilmalari va serverlarni masofadan shifrlangan ulanish orqali boshqarish protokoli.
- **TLS** — internetda ma’lumotlarni shifrlab uzatuvchi protokol; HTTPS, xavfsiz pochta va boshqa xizmatlar asosida ishlaydi.
Telnet va FTP’da parollar ochiq matn ko‘rinishida uzatiladi — trafikni tinglagan har kim ularni o‘qiy oladi. Shuning uchun zamonaviy tarmoqlarda ularning o‘rniga shifrlangan protokollar ishlatiladi.
""",
        ],
        'oldingi': ['Fayl xesh-summasi qanday hisoblanadi?',
                    'Karantin nima?',
                    'Raqamli imzo nimani tasdiqlaydi?'],
        'savollar': ['Tarmoqdagi asosiy tahdidlarni sanang.',
                     'Tarmoqlararo ekran qanday ishlaydi?',
                     'VPN qanday hollarda ishlatiladi?',
                     'Tarmoqni segmentlash nima uchun kerak?',
                     'Nima uchun Telnet o‘rniga SSH ishlatiladi?'],
        'testlar': [
            ('Ochiq tarmoq ustida shifrlangan tunnel yaratuvchi texnologiya:',
             ['DNS', 'VPN', 'DHCP', 'HTML'], 'b'),
            ('Telnet protokolining xavfsiz o‘rinbosari:',
             ['FTP', 'HTTP', 'SSH', 'WEP'], 'c'),
            ('HTTPS protokoli odatda qaysi portda ishlaydi?',
             ['443', '21', '23', '80'], 'a'),
            ('Trafikni qoidalar asosida filtrlaydigan vosita:',
             ['Kommutator', 'Proyektor', 'Printer', 'Tarmoqlararo ekran (firewall)'], 'd'),
            ('Bitta kommutator ichida mantiqiy ajratilgan virtual tarmoqlar:',
             ['VLAN', 'WAN', 'URL', 'USB'], 'a'),
        ],
        'mustaqil': ['Texnikum uchun segmentlangan tarmoq sxemasini chizing: o‘quv xonalari, ma’muriyat, mehmon Wi-Fi.',
                     'Xavfsiz va xavfsiz bo‘lmagan protokollar va ularning portlari bo‘yicha eslatma kartochka tayyorlang.'],
    },
    # ------------------------------------------------------------------ 29
    {
        'type': 'A',
        'title': 'Tarmoqdagi ma’lumotlarni himoyalash usullarini qo‘llash',
        'reja': ['Windows Defender tarmoqlararo ekranini sozlash',
                 'Amaliy ish: firewall qoidalarini yaratish va tekshirish',
                 'Tarmoq ulashish va tarmoq profilini xavfsiz sozlash'],
        'maqsad': 'O‘quvchilarda Windows tarmoqlararo ekranini sozlash, kiruvchi va chiquvchi qoidalar yaratish, tarmoq '
                  'profilini to‘g‘ri tanlash va umumiy ulashishni xavfsiz sozlash ko‘nikmasini shakllantirish.',
        'natija': 'O‘quvchilar firewall holatini tekshiradi, ping’ni bloklovchi va ruxsat beruvchi qoida yaratadi, '
                  'natijani ping orqali sinaydi, tarmoq profilini «Общедоступная» qiladi va keraksiz ulashishni o‘chiradi.',
        'vosita': 'Lokal tarmoqqa ulangan Windows 10/11 kompyuterlar (administrator huquqi), kommutator, proyektor',
        'bolimlar': [
            """
## Tarmoq profillari
Windows har bir tarmoqqa profil beradi va firewall qoidalari profilga qarab ishlaydi.
| Profil | Qachon tanlanadi | Xususiyati |
| Частная (Xususiy) | Uy yoki ishonchli ofis tarmog‘i | Kompyuter tarmoqda ko‘rinadi, fayl ulashish mumkin |
| Общедоступная (Ommaviy) | Kafe, aeroport, mehmonxona Wi-Fi | Kompyuter boshqalarga ko‘rinmaydi, ulashish o‘chirilgan |
| Домен | Tashkilot domeniga ulangan kompyuter | Administrator siyosati bo‘yicha |
- **Tarmoq profili** — Windows’da tarmoqning ishonchlilik darajasini belgilovchi va shunga mos xavfsizlik sozlamalarini qo‘llovchi parametr.
Notanish tarmoqda har doim «Общедоступная» profil tanlanadi.
""",
            """
## Ishni bajarish tartibi
- **Firewall holati.** `Win + R` → `wf.msc` — «Монитор брандмауэра Защитника Windows» oynasi ochiladi. Barcha profillarda holat «Включен» ekanini tekshiring.
- **Ping sinovi.** Qo‘shni kompyuterning IP manzilini `ipconfig` bilan aniqlang va `ping 192.168.1.X` buyrug‘ini bering.
- **Bloklovchi qoida.** wf.msc → «Правила для входящих подключений» → «Создать правило» → «Настраиваемые» → protokol: ICMPv4 → harakat: «Блокировать подключение» → nom: «Ping blok».
- **Qayta sinash.** Qo‘shni kompyuterdan ping yuboring — javob kelmasligi («Превышен интервал ожидания») kerak.
- **Qoidani o‘chirish.** Sinovdan keyin «Ping blok» qoidasini o‘chiring yoki faolsizlantiring.
- **Buyruq orqali.** `netsh advfirewall show allprofiles` buyrug‘i barcha profillar holatini chiqaradi.
""",
            """
## Ulashishni xavfsiz sozlash
- **Profilni tekshirish.** «Параметры» → «Сеть и Интернет» → tarmoq xususiyatlari → profil turini tanlang.
- **Ulashilgan papkalar.** `net share` buyrug‘i bilan ulashilgan papkalarni ko‘ring; keraksizlarini `net share NOM /delete` bilan o‘chiring.
- **Huquqlarni cheklash.** Ulashilgan papka uchun «Все» (Everyone) guruhiga «Полный доступ» bermang — faqat kerakli foydalanuvchilarga «Чтение».
- **Parol bilan himoyalangan ulashish.** «Центр управления сетями» → «Изменить дополнительные параметры общего доступа» → «Включить общий доступ с парольной защитой».
| Tekshiruv | Natija |
| Firewall barcha profillarda yoqilgan | ha / yo‘q |
| Ping blok qoidasi ishladi | ha / yo‘q |
| Tarmoq profili to‘g‘ri tanlangan | ha / yo‘q |
| Keraksiz ulashish o‘chirildi | ha / yo‘q |
""",
        ],
        'oldingi': ['Tarmoqlararo ekran nima?',
                    'VPN qanday ishlaydi?',
                    'Qanday protokollar xavfsiz hisoblanadi?'],
        'savollar': ['Windows’da qanday tarmoq profillari bor?',
                     'Kafe Wi-Fi’ida qaysi profilni tanlash kerak?',
                     'wf.msc orqali qanday ishlar bajariladi?',
                     'Ping’ni bloklovchi qoida qanday yaratiladi?',
                     'Ulashilgan papkaga huquq berishda qanday xato qilinmasligi kerak?'],
        'testlar': [
            ('Windows firewall’ning kengaytirilgan sozlamalarini ochuvchi buyruq:',
             ['wf.msc', 'mspaint', 'notepad', 'winver'], 'a'),
            ('Kafe va aeroport Wi-Fi’ida tanlanadigan profil:',
             ['Частная', 'Домен', 'Общедоступная', 'Профиль не нужен'], 'c'),
            ('Ping qaysi protokoldan foydalanadi?',
             ['ICMP', 'FTP', 'SMTP', 'HTTP'], 'a'),
            ('Barcha firewall profillari holatini chiqaruvchi buyruq:',
             ['ping /all', 'netsh advfirewall show allprofiles', 'dir /s', 'ipconfig /release'], 'b'),
            ('Ulashilgan papkada «Все» guruhiga nima berilmasligi kerak?',
             ['O‘qish huquqi', 'Ko‘rish', 'Hech narsa', '«Полный доступ»'], 'd'),
        ],
        'mustaqil': ['Uy kompyuteringizda tarmoq profili, firewall holati va ulashilgan papkalarni tekshiring, natijani yozing.',
                     'Ma’lum bir dasturning internetga chiqishini taqiqlovchi chiquvchi qoida yaratish tartibini yozing.'],
    },
    # ------------------------------------------------------------------ 30
    {
        'type': 'A',
        'title': 'Wi-Fi tarmog‘i xavfsizligini tekshirish va sozlash',
        'reja': ['Wi-Fi xavfsizlik standartlari',
                 'Amaliy ish: Wi-Fi routerni xavfsiz sozlash',
                 'Ulangan qurilmalarni tekshirish va mehmon tarmog‘i'],
        'maqsad': 'O‘quvchilarda Wi-Fi routerning boshqaruv paneliga kirish, standart parolni almashtirish, WPA2/WPA3 '
                  'shifrlashni yoqish, WPS’ni o‘chirish va ulangan qurilmalarni tekshirish ko‘nikmasini shakllantirish.',
        'natija': 'O‘quvchilar routerni xavfsiz sozlaydi, kuchli Wi-Fi paroli o‘rnatadi, ulangan qurilmalar ro‘yxatini '
                  'tahlil qiladi va mehmon tarmog‘ini yaratadi.',
        'vosita': 'O‘quv Wi-Fi routerlari (TP-Link, D-Link va boshqalar), patch-kord, noutbuklar, proyektor',
        'bolimlar': [
            """
## Wi-Fi shifrlash standartlari
| Standart | Holati | Izoh |
| Ochiq tarmoq | Xavfli | Ma’lumotlar shifrlanmaydi |
| WEP | Eskirgan, xavfli | Bir necha daqiqada buziladi |
| WPA (TKIP) | Eskirgan | Ishlatilmasligi kerak |
| WPA2-PSK (AES) | Xavfsiz | Eng keng tarqalgan |
| WPA3 | Eng xavfsiz | Yangi qurilmalarda mavjud |
- **SSID** — Wi-Fi tarmog‘ining ko‘rinadigan nomi.
- **WPA2** — Wi-Fi tarmog‘ida AES algoritmi bilan ma’lumotlarni shifrlovchi xavfsizlik standarti.
- **WPS** — tugma yoki 8 xonali PIN orqali qurilmani Wi-Fi’ga tez ulash funksiyasi; PIN usuli zaif bo‘lgani uchun o‘chirib qo‘yish tavsiya etiladi.
""",
            """
## Ishni bajarish tartibi
- **Panelga kirish.** Noutbukni routerga kabel yoki Wi-Fi orqali ulang. Brauzerda `192.168.0.1` yoki `192.168.1.1` manzilini oching (aniq manzil router tagidagi yorliqda yoki `ipconfig` dagi «Основной шлюз» qatorida).
- **Administrator parolini almashtirish.** «Система» → «Пароль» bo‘limida standart «admin/admin» parolini kuchli parolga almashtiring.
- **SSID nomi.** Tarmoq nomida familiya, manzil yoki router modelini ko‘rsatmang.
- **Shifrlash.** «Беспроводной режим» → «Защита» → WPA2-PSK (AES) yoki WPA3 ni tanlang, kamida 12 belgili parol kiriting.
- **WPS’ni o‘chirish.** «WPS» bo‘limida funksiyani «Отключить».
- **Masofaviy boshqaruv.** «Удалённое управление» o‘chirilganligini tekshiring.
- **Proshivka.** «Обновление встроенного ПО» bo‘limida yangi versiya bor-yo‘qligini tekshiring.
""",
            """
## Ulangan qurilmalar
Routerning «DHCP» → «Список клиентов» yoki «Статистика» bo‘limida tarmoqqa ulangan barcha qurilmalar ko‘rinadi: nomi, IP va MAC manzili.
- **MAC manzil** — tarmoq qurilmasiga ishlab chiqaruvchi tomonidan berilgan noyob jismoniy manzil.
Noma’lum qurilma topilsa, Wi-Fi paroli almashtiriladi — barcha qurilmalar uziladi va faqat yangi parolni bilganlar qayta ulanadi.
## Mehmon tarmog‘i
- **Mehmon tarmog‘i** — mehmonlar uchun alohida SSID bilan yaratiladigan, asosiy tarmoqdagi kompyuterlarga kirish imkoni yo‘q Wi-Fi tarmog‘i.
Routerning «Гостевая сеть» bo‘limida mehmon tarmog‘i yoqiladi, alohida parol qo‘yiladi va «Доступ к локальной сети» o‘chiriladi.
| Sozlama | Oldin | Keyin |
| Administrator paroli | admin | Kuchli parol |
| Shifrlash | — | WPA2-AES |
| WPS | Yoqilgan | O‘chirilgan |
| Mehmon tarmog‘i | Yo‘q | Alohida, izolyatsiyalangan |
""",
        ],
        'oldingi': ['Windows’da qanday tarmoq profillari bor?',
                    'Firewall qoidasini qanday yaratdik?',
                    'Ulashilgan papkalarni qaysi buyruq bilan ko‘rish mumkin?'],
        'savollar': ['Qaysi Wi-Fi shifrlash standartlari xavfsiz hisoblanadi?',
                     'Router boshqaruv paneliga qanday kiriladi?',
                     'Nima uchun WPS’ni o‘chirish tavsiya etiladi?',
                     'Ulangan qurilmalar ro‘yxatida noma’lum qurilma topilsa nima qilish kerak?',
                     'Mehmon tarmog‘i nima uchun kerak?'],
        'testlar': [
            ('Bir necha daqiqada buziladigan eskirgan Wi-Fi shifrlash standarti:',
             ['WPA3', 'WEP', 'WPA2-AES', 'TLS'], 'b'),
            ('Wi-Fi tarmog‘ining ko‘rinadigan nomi:',
             ['SSID', 'MAC', 'DNS', 'URL'], 'a'),
            ('Ko‘pchilik routerlarning boshqaruv paneli manzili:',
             ['8.8.8.8', 'google.com', '192.168.0.1 yoki 192.168.1.1', '127.0.0.1:80'], 'c'),
            ('Zaif PIN usuli sababli o‘chirib qo‘yish tavsiya etiladigan funksiya:',
             ['DHCP', 'NAT', 'QoS', 'WPS'], 'd'),
            ('Qurilmaning ishlab chiqaruvchi bergan noyob jismoniy manzili:',
             ['MAC manzil', 'IP manzil', 'Domen', 'Port'], 'a'),
        ],
        'mustaqil': ['Uy routeringizda (kattalar ruxsati bilan) shifrlash turi, WPS holati va ulangan qurilmalarni tekshiring.',
                     'Wi-Fi routerni xavfsiz sozlash bo‘yicha 10 bandlik yo‘riqnoma yozing.'],
    },
]
