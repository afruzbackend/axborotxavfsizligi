"""11–20-mavzular: xavflarni tahlil qilish, parollar, autentifikatsiya va 2FA."""

MAVZULAR = [
    # ------------------------------------------------------------------ 11
    {
        'type': 'A',
        'title': 'Kompyuter tizimidagi xavflarni aniqlash',
        'reja': ['Kompyuter tizimidagi zaifliklarni izlash joylari',
                 'Amaliy ish: Windows vositalari yordamida zaifliklarni aniqlash',
                 'Aniqlangan xavflar ro‘yxatini tuzish'],
        'maqsad': 'O‘quvchilarda Windows’ning o‘rnatilgan vositalari yordamida kompyuterdagi zaifliklar va xavflarni '
                  'aniqlash hamda ularni ro‘yxatga olish ko‘nikmasini shakllantirish.',
        'natija': 'O‘quvchilar foydalanuvchi hisoblari, ochiq portlar, avtoyuklanish dasturlari va o‘rnatilgan '
                  'dasturlarni tekshiradi, aniqlangan xavflar ro‘yxatini tuzadi.',
        'vosita': 'Windows 10/11 o‘rnatilgan kompyuterlar, buyruqlar satri, Task Manager, xavflar ro‘yxati shakli',
        'bolimlar': [
            """
## Zaifliklar qayerda bo‘ladi?
Kompyuterdagi xavflarni aniqlash uchun tizimning eng ko‘p zaiflik uchraydigan joylari tekshiriladi.
| Joy | Ehtimoliy zaiflik |
| Foydalanuvchi hisoblari | Parolsiz hisob, keraksiz administrator, faol «Гость» hisobi |
| Dasturlar | Eskirgan, yangilanmagan yoki noma’lum manbadan o‘rnatilgan dasturlar |
| Avtoyuklanish | Kompyuter yoqilganda o‘zi ishga tushadigan shubhali dasturlar |
| Tarmoq | Ochiq portlar, umumiy (shared) papkalar |
| Himoya | O‘chirilgan antivirus yoki firewall |
- **Port** — kompyuterdagi dastur tarmoq orqali ma’lumot qabul qiladigan raqamlangan «eshik».
- **Avtoyuklanish** — operatsion tizim ishga tushganda dasturlarning avtomatik ishga tushishi.
""",
            """
## Ishni bajarish tartibi
- **Hisoblarni ko‘rish.** Buyruqlar satrida `net user` buyrug‘ini bering — kompyuterdagi barcha hisoblar ro‘yxati chiqadi. Administratorlar guruhini `net localgroup Администраторы` (ingliz tilli tizimda `Administrators`) buyrug‘i bilan ko‘ring.
- **Avtoyuklanishni tekshirish.** `Ctrl + Shift + Esc` bilan Task Manager (Диспетчер задач) ni oching, «Автозагрузка» bo‘limida noma’lum dasturlarni yozib oling.
- **Ochiq portlarni ko‘rish.** `netstat -an` buyrug‘i ochiq ulanishlar va tinglayotgan (LISTENING) portlarni ko‘rsatadi.
- **Umumiy papkalarni ko‘rish.** `net share` buyrug‘i tarmoqda ochiq qilingan papkalarni chiqaradi.
- **O‘rnatilgan dasturlarni ko‘rish.** Sozlamalar → «Приложения» bo‘limida uzoq vaqt yangilanmagan yoki noma’lum dasturlarni aniqlang.
Hech qanday dasturni o‘qituvchi ruxsatisiz o‘chirmang — ba’zi tizim xizmatlari kompyuter ishlashi uchun zarur.
""",
            """
## Xavflar ro‘yxati
Aniqlangan har bir kamchilik ro‘yxatga yoziladi va baholanadi.
| № | Aniqlangan holat | Xavf | Daraja | Tavsiya |
| 1 | «Гость» hisobi faol | Begona shaxs kirishi mumkin | O‘rta | Hisobni o‘chirish |
| 2 | Avtoyuklanishda noma’lum dastur | Troyan bo‘lishi mumkin | Yuqori | Antivirus bilan tekshirish |
| 3 | Disk C umumiy qilingan | Ma’lumotlar sizib chiqishi | Yuqori | Ulashishni bekor qilish |
## Xulosa
- **Xavflar reyestri** — aniqlangan xavflar, ularning darajasi va mas’ul shaxslar yozilgan jadval.
Amaliy ish oxirida har bir o‘quvchi kamida 3 ta holatni reyestrga yozadi. Bu reyestr keyingi mashg‘ulotlarda xavflilik darajasini baholash uchun ishlatiladi.
""",
        ],
        'oldingi': ['Xavflarni boshqarish jarayoni bosqichlarini sanang.',
                    'Xavflar matritsasi qanday tuziladi?',
                    'Xavfga munosabatning qanday strategiyalari bor?'],
        'savollar': ['Kompyuterdagi qaysi joylarda zaiflik ko‘p uchraydi?',
                     'net user buyrug‘i nima uchun ishlatiladi?',
                     'Avtoyuklanishdagi dasturlarni qayerdan ko‘rish mumkin?',
                     'netstat -an buyrug‘i qanday ma’lumot beradi?',
                     'Xavflar reyestriga qanday ma’lumotlar yoziladi?'],
        'testlar': [
            ('Kompyuterdagi barcha foydalanuvchi hisoblarini chiqaruvchi buyruq:',
             ['net user', 'ipconfig', 'ping', 'cls'], 'a'),
            ('Task Manager’ni tezda ochish tugmalari:',
             ['Ctrl + Alt + T', 'Win + E', 'Ctrl + Shift + Esc', 'Alt + Tab'], 'c'),
            ('Tarmoqda ochiq qilingan papkalarni ko‘rsatuvchi buyruq:',
             ['net time', 'net share', 'dir', 'tree'], 'b'),
            ('Dastur tarmoq orqali ma’lumot qabul qiladigan raqamlangan «eshik»:',
             ['Fayl', 'Papka', 'Drayver', 'Port'], 'd'),
            ('Avtoyuklanishda noma’lum dastur topilsa, birinchi navbatda nima qilinadi?',
             ['Antivirus bilan tekshiriladi', 'Kompyuter formatlanadi', 'E’tiborsiz qoldiriladi', 'Monitor o‘chiriladi'], 'a'),
        ],
        'mustaqil': ['Uy kompyuteringizda net user, net share va Task Manager orqali tekshiruv o‘tkazib, xavflar reyestrini tuzing.',
                     'netstat buyrug‘ining boshqa kalitlari (-b, -o) vazifasini o‘rganib, qisqa izoh yozing.'],
    },
    # ------------------------------------------------------------------ 12
    {
        'type': 'N',
        'title': 'Real holatlar asosida axborot xavflarini tahlil qilish',
        'reja': ['Xavfsizlik hodisasi va uni tahlil qilish',
                 'Mashhur kiberhodisalardan saboqlar',
                 'Hodisalarga javob berish rejasi'],
        'maqsad': 'O‘quvchilarga xavfsizlik hodisalarini tahlil qilish usulini, real hodisalardan olingan saboqlarni va '
                  'hodisaga javob berish bosqichlarini tushuntirish.',
        'natija': 'O‘quvchilar xavfsizlik hodisasining sababi va oqibatini tahlil qiladi, hodisaga javob berish '
                  'bosqichlarini sanaydi va tashkilot uchun xulosa chiqaradi.',
        'bolimlar': [
            """
## Xavfsizlik hodisasi
- **Xavfsizlik hodisasi** — axborotning maxfiyligi, yaxlitligi yoki foydalanuvchanligi buzilishiga olib kelgan yoki olib kelishi mumkin bo‘lgan voqea.
Hodisani tahlil qilishdan maqsad — aybdorni topishgina emas, balki hodisa nima uchun yuz berganini tushunib, uning takrorlanishiga yo‘l qo‘ymaslik.
## «Besh marta nima uchun» usuli
Hodisaning asl sababini topish uchun ketma-ket «Nima uchun?» savoli beriladi:
- Server ishlamay qoldi. — Nima uchun? Fayllar shifrlangan.
- Nima uchun shifrlandi? Xodim xatdagi ilovani ochgan.
- Nima uchun ochdi? Xat rahbar nomidan kelgan edi.
- Nima uchun ajrata olmadi? Xodimlar phishing bo‘yicha o‘qitilmagan.
- Nima uchun zarar katta bo‘ldi? Zaxira nusxa serverning o‘zida saqlangan.
Natijada ikkita asl sabab aniqlanadi: o‘qitish yo‘qligi va zaxira nusxaning noto‘g‘ri saqlanishi.
""",
            """
## Saboq beruvchi hodisalar
| Hodisa | Nima bo‘ldi | Asosiy saboq |
| WannaCry (2017) | Shifrlovchi chuvalchang 150 dan ortiq davlatda yuz minglab kompyuterni zararladi | Windows yangilanishlarini o‘z vaqtida o‘rnatish |
| Ma’lumotlar bazalari sizib chiqishi | Saytlardan millionlab login va parollar o‘g‘irlanib, internetga joylandi | Har bir saytga alohida parol, 2FA |
| Bank nomidan SMS firibgarlik | Fuqarolar soxta havola orqali karta ma’lumotlarini kiritib, pulidan ayrildi | SMS-kodni hech kimga aytmaslik |
| Standart parolli kameralar | Internetga ulangan minglab kameralar botnetga aylantirildi | Qurilma parolini almashtirish |
WannaCry hujumida Microsoft zaiflikni tuzatuvchi yangilanishni hujumdan ikki oy oldin chiqargan edi. Yangilanishni o‘rnatgan tashkilotlar zarar ko‘rmadi.
""",
            """
## Hodisaga javob berish bosqichlari
- **Tayyorgarlik.** Javob berish rejasi tuziladi, mas’ullar belgilanadi, zaxira nusxalar tayyorlanadi.
- **Aniqlash.** Hodisa belgilarini payqash va uning haqiqatan ham xavfsizlik hodisasi ekanini tasdiqlash.
- **Cheklash.** Zararlangan kompyuterni tarmoqdan uzish, tarqalishni to‘xtatish.
- **Bartaraf etish.** Zararli dasturni o‘chirish, zaiflikni yopish, parollarni almashtirish.
- **Tiklash.** Ma’lumotlarni zaxira nusxadan tiklash va tizimni ishga tushirish.
- **Xulosa chiqarish.** Hodisa tahlil qilinib, xavfsizlik siyosatiga o‘zgartirishlar kiritiladi.
## Birinchi harakatlar
Oddiy foydalanuvchi kompyuterida g‘alati holat sezsa (fayllar ochilmaydi, ekranda to‘lov talabi chiqdi), u kompyuterni tarmoqdan uzishi, hech narsani o‘chirmasligi va darhol IT-mutaxassisga xabar berishi kerak.
""",
        ],
        'oldingi': ['Kompyuterdagi zaifliklarni qanday aniqladik?',
                    'Xavflar reyestriga nimalar yoziladi?',
                    'net share buyrug‘i nimani ko‘rsatadi?'],
        'savollar': ['Xavfsizlik hodisasi deganda nimani tushunasiz?',
                     '«Besh marta nima uchun» usulining maqsadi nima?',
                     'WannaCry hujumidan qanday saboq olish mumkin?',
                     'Hodisaga javob berish bosqichlarini sanang.',
                     'Kompyuterda shifrlovchi virus belgisi sezilsa, foydalanuvchi nima qilishi kerak?'],
        'testlar': [
            ('2017-yilda yuz minglab kompyuterlarni zararlagan shifrlovchi chuvalchang:',
             ['WannaCry', 'Notepad', 'Chrome', 'Telegram'], 'a'),
            ('Zararlangan kompyuterni tarmoqdan uzish qaysi bosqichga kiradi?',
             ['Tayyorgarlik', 'Tiklash', 'Cheklash', 'Xulosa chiqarish'], 'c'),
            ('Hodisaning asl sababini ketma-ket savollar orqali topish usuli:',
             ['Brute force', '«Besh marta nima uchun»', 'Defragmentatsiya', 'Formatlash'], 'b'),
            ('Ma’lumotlarni zaxira nusxadan qaytarish bosqichi:',
             ['Aniqlash', 'Cheklash', 'Bartaraf etish', 'Tiklash'], 'd'),
            ('WannaCry hujumidan qaysi tashkilotlar zarar ko‘rmadi?',
             ['Yangilanishni o‘rnatganlar', 'Kompyuteri ko‘plar', 'Internet tezligi yuqorilar', 'Printeri borlar'], 'a'),
        ],
        'mustaqil': ['O‘zingiz bilgan biror xavfsizlik hodisasini «Besh marta nima uchun» usulida tahlil qiling.',
                     'Kompyuter xonasi uchun bir sahifali hodisaga javob berish rejasini yozing.'],
    },
    # ------------------------------------------------------------------ 13
    {
        'type': 'A',
        'title': 'Tahdidlarni xavflilik darajasi bo‘yicha baholash',
        'reja': ['Xavflilik darajasini baholash mezonlari',
                 'Amaliy ish: xavflar matritsasini elektron jadvalda tuzish',
                 'Xavflarni ustuvorlik bo‘yicha saralash'],
        'maqsad': 'O‘quvchilarda tahdidlarni ehtimollik va zarar bo‘yicha baholab, elektron jadvalda xavflar matritsasini '
                  'tuzish va ustuvor xavflarni aniqlash ko‘nikmasini shakllantirish.',
        'natija': 'O‘quvchilar Excel’da xavflar jadvalini tuzadi, formula yordamida xavf darajasini hisoblaydi, '
                  'shartli formatlash bilan ranglaydi va xavflarni saralaydi.',
        'vosita': 'MS Excel yoki LibreOffice Calc o‘rnatilgan kompyuterlar, 11-mavzuda tuzilgan xavflar reyestri',
        'bolimlar': [
            """
## Baholash shkalasi
Xavflilik darajasini baholashda yagona shkala qo‘llaniladi, aks holda turli odamlar bir xil xavfni turlicha baholaydi.
| Ball | Ehtimollik | Zarar |
| 1 | Kam: yiliga bir martadan kam | Kichik: ish bir necha daqiqaga to‘xtaydi |
| 2 | O‘rta: yiliga bir necha marta | O‘rta: ish bir kunga to‘xtaydi, ayrim fayllar yo‘qoladi |
| 3 | Yuqori: har oy yoki tez-tez | Katta: muhim ma’lumotlar yo‘qoladi yoki sizib chiqadi |
- **Ustuvorlik** — qaysi xavf birinchi navbatda bartaraf etilishi kerakligini ko‘rsatuvchi tartib.
Xavf darajasi 6 va undan yuqori bo‘lsa — darhol, 3–4 bo‘lsa — rejali ravishda, 1–2 bo‘lsa — kuzatuv ostida choralar ko‘riladi.
""",
            """
## Ishni bajarish tartibi
- **Jadval tuzish.** Excel’da ustunlar yarating: A — №, B — Tahdid, C — Ehtimollik, D — Zarar, E — Xavf darajasi, F — Chora.
- **Ma’lumot kiritish.** Xavflar reyestridagi kamida 8 ta tahdidni kiriting va har biriga 1–3 ball qo‘ying.
- **Formula yozish.** E2 katakka `=C2*D2` formulasini yozib, pastga cho‘zing.
- **Daraja nomini chiqarish.** G2 katakka `=ЕСЛИ(E2>=6;"Yuqori";ЕСЛИ(E2>=3;"O‘rta";"Past"))` formulasini yozing (ingliz tilidagi Excel’da `ЕСЛИ` o‘rniga `IF`).
- **Shartli formatlash.** E ustunini belgilab «Условное форматирование» → «Цветовые шкалы» ni tanlang: yuqori xavflar qizil, past xavflar yashil bo‘ladi.
Formuladagi ajratuvchi belgi (`;` yoki `,`) kompyuterning til sozlamalariga bog‘liq.
""",
            """
## Saralash va xulosa
- **Saralash.** Jadvalni belgilab, «Данные» → «Сортировка» orqali E ustuni bo‘yicha kamayish tartibida saralang.
- **Ustuvor ro‘yxat.** Eng yuqori 3 ta xavf uchun aniq chora, mas’ul va muddat yozing.
| Tahdid | Ehtimollik | Zarar | Daraja | Chora |
| Shifrlovchi virus | 2 | 3 | 6 — Yuqori | Zaxira nusxa, antivirus, xodimlarni o‘qitish |
| Disk buzilishi | 2 | 2 | 4 — O‘rta | Disk holatini tekshirish, zaxiralash |
| Elektr uzilishi | 3 | 1 | 3 — O‘rta | UPS o‘rnatish |
| Parolsiz Wi-Fi | 1 | 2 | 2 — Past | Parol va WPA2 o‘rnatish |
Ishni tugatgach, fayl «Xavflar_matritsasi_Familiya.xlsx» nomi bilan saqlanadi va o‘qituvchiga topshiriladi.
""",
        ],
        'oldingi': ['Xavflar matritsasida xavf darajasi qanday hisoblanadi?',
                    'Xavfsizlik hodisasiga javob berish bosqichlarini sanang.',
                    'Xavflar reyestri nima?'],
        'savollar': ['Nima uchun yagona baholash shkalasi kerak?',
                     'Xavf darajasini Excel’da qaysi formula bilan hisoblaysiz?',
                     'Shartli formatlash nima uchun qo‘llaniladi?',
                     'Ustuvorlik qanday aniqlanadi?',
                     'Darajasi 6 bo‘lgan xavfga qanday munosabatda bo‘linadi?'],
        'testlar': [
            ('Ehtimollik C2, zarar D2 katakda bo‘lsa, xavf darajasi formulasi:',
             ['=C2+D2', '=C2*D2', '=C2/D2', '=C2-D2'], 'b'),
            ('Xavflarni rang bilan ajratish uchun Excel’ning qaysi vositasidan foydalaniladi?',
             ['Shartli formatlash', 'Sahifa parametrlari', 'Imlo tekshiruvi', 'Chop etish'], 'a'),
            ('Xavf darajasi 6 va undan yuqori bo‘lsa:',
             ['E’tibor berilmaydi', 'Bir yildan keyin ko‘riladi', 'Kuzatiladi', 'Darhol chora ko‘riladi'], 'd'),
            ('Elektr uzilishi xavfini kamaytiruvchi qurilma:',
             ['Skaner', 'Router', 'UPS', 'Proyektor'], 'c'),
            ('Qaysi xavf birinchi navbatda bartaraf etilishini ko‘rsatuvchi tartib:',
             ['Ustuvorlik', 'Formatlash', 'Arxivlash', 'Kompilyatsiya'], 'a'),
        ],
        'mustaqil': ['Uy tarmog‘ingiz uchun 6 ta tahdiddan iborat xavflar matritsasini Excel’da tuzing.',
                     'ЕСЛИ (IF) funksiyasi o‘rniga УСЛОВИЯ (IFS) funksiyasidan foydalanib daraja nomini chiqaruvchi formula yozing.'],
    },
    # ------------------------------------------------------------------ 14
    {
        'type': 'A',
        'title': 'Real vaziyatlar asosida xavflarni tahlil qilish',
        'reja': ['Kichik tashkilot uchun xavflarni tahlil qilish topshirig‘i',
                 'Amaliy ish: guruhlarda xavflar tahlili hisobotini tayyorlash',
                 'Hisobotni himoya qilish va baholash'],
        'maqsad': 'O‘quvchilarda real tashkilot misolida aktivlar, tahdidlar va xavflarni kompleks tahlil qilib, '
                  'hisobot tayyorlash va uni himoya qilish ko‘nikmasini shakllantirish.',
        'natija': 'O‘quvchilar tashkilot aktivlarini aniqlaydi, xavflarni baholaydi, himoya rejasini tuzadi va '
                  'guruh hisobotini taqdim etadi.',
        'metod': '«Keys-stadi», loyiha usuli, guruhda ishlash, taqdimot va o‘zaro baholash',
        'vosita': 'Tashkilot tavsifi yozilgan keys, kompyuterlar, Excel/Word, proyektor',
        'bolimlar': [
            """
## Keys: «Tezkor servis» kompyuter ta’mirlash markazi
Markazda 6 ta xodim ishlaydi. Ofisda 5 ta kompyuter, 1 ta fayl server, Wi-Fi router, kassa apparati va videokuzatuv kamerasi bor. Mijozlar ta’mirga noutbuk va telefonlarini topshiradi. Mijozlar bazasi (ism, telefon, manzil) Excel faylida serverda saqlanadi.
Ma’lum kamchiliklar:
- Barcha xodimlar bitta umumiy hisob va «12345» paroli bilan ishlaydi.
- Wi-Fi paroli kassada qog‘ozga yozib qo‘yilgan, mijozlarga ham beriladi.
- Zaxira nusxa olinmaydi.
- Xodimlar ta’mirdagi qurilmalardagi mijoz fayllarini o‘z fleshkasiga ko‘chirib oladi.
- Kamera standart parol bilan internetga ulangan.
""",
            """
## Ishni bajarish tartibi
- **Aktivlar ro‘yxati.** Markazning himoya qilinishi kerak bo‘lgan aktivlarini sanang: mijozlar bazasi, server, mijoz qurilmalari, obro‘ va boshqalar.
- **Xavflar jadvali.** Har bir kamchilik uchun tahdid, buzilgan tamoyil, ehtimollik, zarar va xavf darajasini yozing.
- **Himoya rejasi.** Har bir xavf uchun texnik va tashkiliy chorani taklif qiling.
- **Hisobot.** Word’da 2–3 sahifali hisobot tayyorlang: kirish, aktivlar, xavflar jadvali, himoya rejasi, xulosa.
| Kamchilik | Tahdid | Tamoyil | Daraja | Chora |
| Umumiy hisob va «12345» | Ruxsatsiz kirish, hisobdorlik yo‘q | Konfidensiallik | 9 | Har bir xodimga alohida hisob, kuchli parol |
| Zaxira yo‘q | Server buzilsa baza yo‘qoladi | Foydalanuvchanlik | 6 | Haftalik zaxira, tashqi disk |
""",
            """
## Hisobotni himoya qilish
Har bir guruh 5 daqiqa davomida o‘z hisobotini taqdim etadi va boshqa guruhlarning savollariga javob beradi.
| Baholash mezoni | Ball |
| Aktivlar to‘liq aniqlangan | 2 |
| Xavflar to‘g‘ri baholangan | 3 |
| Himoya choralari aniq va amalga oshirish mumkin | 3 |
| Hisobot va taqdimot sifati | 2 |
## Muhim xulosa
Mijozning shaxsiy fayllarini ruxsatsiz nusxalash — nafaqat xavfsizlik, balki qonun buzilishi hamdir. «Shaxsga doir ma’lumotlar to‘g‘risida»gi Qonunga ko‘ra, shaxsiy ma’lumotlarni egasining roziligisiz yig‘ish va tarqatish taqiqlanadi. IT-servis mutaxassisining obro‘si mijoz ma’lumotlarini ishonchli saqlashga bog‘liq.
""",
        ],
        'oldingi': ['Xavf darajasini Excel’da qanday hisobladik?',
                    'Ustuvorlik qanday aniqlanadi?',
                    'Hodisaga javob berish bosqichlarini sanang.'],
        'savollar': ['Keysdagi markazning asosiy aktivlari nimalar?',
                     'Umumiy hisobdan foydalanish qaysi tamoyillarni buzadi?',
                     'Kameraning standart paroli qanday xavf tug‘diradi?',
                     'Mijoz fayllarini nusxalash qaysi qonunni buzadi?',
                     'Hisobot qanday qismlardan iborat bo‘ladi?'],
        'testlar': [
            ('Barcha xodimlar bitta umumiy hisobdan foydalanganda qaysi tamoyil ta’minlanmaydi?',
             ['Hisobdorlik', 'Foydalanuvchanlik', 'Tezkorlik', 'Mavjudlik'], 'a'),
            ('Mijozning shaxsiy fayllarini ruxsatsiz nusxalash qaysi qonunni buzadi?',
             ['Yo‘l harakati qoidalarini', '«Shaxsga doir ma’lumotlar to‘g‘risida»gi Qonunni', 'Soliq kodeksini', 'Hech qaysi'], 'b'),
            ('Internetga ulangan kamerani himoyalashning birinchi qadami:',
             ['Kamerani bo‘yash', 'Kabelni uzaytirish', 'Standart parolni almashtirish', 'Yorug‘likni oshirish'], 'c'),
            ('Wi-Fi parolini kassada qog‘ozga yozib qo‘yish:',
             ['Xavfsiz amaliyot', 'Tavsiya etiladi', 'Qonun talabi', 'Konfidensiallikka tahdid'], 'd'),
            ('Server buzilganda bazani yo‘qotmaslik uchun chora:',
             ['Muntazam zaxira nusxa olish', 'Serverni o‘chirib qo‘yish', 'Monitorni almashtirish', 'Ekran fonini o‘zgartirish'], 'a'),
        ],
        'mustaqil': ['Yashash joyingizdagi biror kichik tashkilot (do‘kon, apteka) uchun xuddi shunday xavflar tahlilini qiling.',
                     'Guruh hisobotidagi himoya rejasi bo‘yicha xarajatlar smetasini taxminiy hisoblang.'],
    },
    # ------------------------------------------------------------------ 15
    {
        'type': 'N',
        'title': 'Kuchli parol yaratish tamoyillari',
        'reja': ['Parol va uning himoyadagi o‘rni',
                 'Kuchsiz parollar va ularni buzish usullari',
                 'Kuchli parol yaratish qoidalari va parol menejerlari'],
        'maqsad': 'O‘quvchilarga parolning himoyadagi o‘rni, kuchsiz parollar xavfi, parollarni buzish usullari va '
                  'kuchli parol yaratish tamoyillarini tushuntirish.',
        'natija': 'O‘quvchilar kuchsiz va kuchli parollarni farqlaydi, parol buzish usullarini izohlaydi va kuchli parol '
                  'yaratish qoidalarini qo‘llaydi.',
        'bolimlar': [
            """
## Parol nima?
- **Parol** — foydalanuvchi shaxsini tasdiqlash uchun ishlatiladigan, faqat unga ma’lum bo‘lgan belgilar ketma-ketligi.
- **Login** — tizimda foydalanuvchini aniqlovchi nom yoki identifikator.
Login — bu eshik qayerda ekanini ko‘rsatadi, parol esa — eshik kaliti. Agar kalit oddiy bo‘lsa yoki boshqalarga ma’lum bo‘lsa, eshik qanchalik mustahkam bo‘lmasin, uni ochish oson.
Bugungi kunda bir odam o‘rtacha bir necha o‘nlab hisoblarga ega: elektron pochta, ijtimoiy tarmoqlar, bank ilovasi, davlat xizmatlari portali. Ularning har biri parol bilan himoyalangan va bitta parol oshkor bo‘lishi qolgan hisoblarga ham xavf tug‘dirishi mumkin.
""",
            """
## Kuchsiz parollar
Har yili e’lon qilinadigan eng ko‘p ishlatiladigan parollar ro‘yxatining boshida doim bir xil parollar turadi: «123456», «password», «qwerty», «111111». Bunday parollar bir soniyada topiladi.
| Kuchsiz parol turi | Misol | Nima uchun xavfli |
| Oddiy raqamlar | 123456, 000000 | Lug‘atda birinchi turadi |
| Klaviatura ketma-ketligi | qwerty, 1q2w3e | Hamma biladi |
| Shaxsiy ma’lumot | Ism + tug‘ilgan yil: Ali2007 | Ijtimoiy tarmoqdan topiladi |
| Qisqa parol | 6 belgidan kam | Barcha variantlar tez sinaladi |
| Bir xil parol | Hamma saytda bitta parol | Bir sayt buzilsa, hammasi ochiladi |
## Parolni buzish usullari
- **Lug‘at bo‘yicha tanlash** — mashhur so‘zlar va parollar ro‘yxatini sinash.
- **To‘liq tanlash (brute force)** — barcha belgilar birikmasini sinash; parol qancha uzun bo‘lsa, shuncha ko‘p vaqt ketadi.
- **Kredensial to‘ldirish** — boshqa saytdan o‘g‘irlangan login va parolni yangi saytda sinab ko‘rish.
""",
            """
## Kuchli parol qoidalari
- Uzunligi kamida 12 belgi; qancha uzun bo‘lsa, shuncha yaxshi.
- Katta va kichik harflar, raqamlar va maxsus belgilar (! @ # $ %) aralash ishlatiladi.
- Lug‘atdagi so‘z, ism, tug‘ilgan sana va telefon raqami ishlatilmaydi.
- Har bir muhim hisob uchun alohida parol.
- Parol hech kimga aytilmaydi, qog‘ozga yozib monitorga yopishtirilmaydi.
## Parol iborasi usuli
- **Parol iborasi** — bir nechta tasodifiy so‘zdan iborat uzun, lekin eslab qolish oson parol.
Masalan, «Olma7Daraxt!Qor_Kitob» — 21 belgili parol, uni eslab qolish oson, buzish esa juda qiyin. Yana bir usul — gapning bosh harflari: «Men 2026-yilda texnikumni a’lo baholarga tugataman!» → «M2026yta’bt!».
- **Parol menejeri** — barcha parollarni shifrlangan holda saqlaydigan va yangi kuchli parollar yaratadigan dastur (masalan, Bitwarden, KeePass).
""",
        ],
        'oldingi': ['Xavflar tahlili hisobotida qanday qismlar bor edi?',
                    'Umumiy hisobdan foydalanish qanday xavf tug‘diradi?',
                    'Brute force hujumi nima?'],
        'savollar': ['Login va parolning farqi nimada?',
                     'Qanday parollar kuchsiz hisoblanadi?',
                     'Kredensial to‘ldirish hujumi qanday amalga oshiriladi?',
                     'Kuchli parolga qanday talablar qo‘yiladi?',
                     'Parol menejeri nima uchun kerak?'],
        'testlar': [
            ('Quyidagilardan qaysi biri kuchli parol?',
             ['123456', 'qwerty', 'Ali2007', 'T7#mavZu!qor_29'], 'd'),
            ('Kuchli parolning tavsiya etiladigan eng kam uzunligi:',
             ['4 belgi', '12 belgi', '6 belgi', '8 belgi'], 'b'),
            ('Boshqa saytdan o‘g‘irlangan parolni yangi saytda sinash:',
             ['Kredensial to‘ldirish', 'Shifrlash', 'Zaxiralash', 'Autentifikatsiya'], 'a'),
            ('Parollarni shifrlangan holda saqlaydigan dastur:',
             ['Antivirus', 'Brauzer kengaytmasi «reklama»', 'Parol menejeri', 'Media pleyer'], 'c'),
            ('Bir nechta tasodifiy so‘zdan tuzilgan uzun parol:',
             ['Lug‘at hujumi', 'PIN-kod', 'Login', 'Parol iborasi'], 'd'),
        ],
        'mustaqil': ['Parol iborasi usulida 3 ta misol tuzing (haqiqiy parollaringizni yozmang!) va ularning uzunligini hisoblang.',
                     'Bitwarden yoki KeePass parol menejerining imkoniyatlarini o‘rganib, qisqa taqdimot tayyorlang.'],
    },
    # ------------------------------------------------------------------ 16
    {
        'type': 'A',
        'title': 'Kuchli parol yaratish va parol xavfsizligini tekshirish',
        'reja': ['Parol mustahkamligini baholash usullari',
                 'Amaliy ish: kuchli parol yaratish va mustahkamligini tekshirish',
                 'Windows’da parol siyosatini sozlash'],
        'maqsad': 'O‘quvchilarda kuchli parol yaratish, uning mustahkamligini hisoblash va tekshirish hamda Windows’da '
                  'parol siyosatini sozlash ko‘nikmasini shakllantirish.',
        'natija': 'O‘quvchilar parol entropiyasini taxminiy hisoblaydi, parol generatoridan foydalanadi, parol '
                  'sizib chiqqanini tekshiradi va mahalliy parol siyosatini sozlaydi.',
        'vosita': 'Internetga ulangan kompyuterlar, brauzer, parol menejeri (KeePass/Bitwarden), Windows Pro',
        'bolimlar': [
            """
## Parol qanchalik kuchli?
Parol mustahkamligi uning uzunligi va ishlatilgan belgilar to‘plamiga bog‘liq. Variantlar soni = belgilar soni ^ uzunlik.
| Belgilar to‘plami | Belgilar soni | 8 belgili parol variantlari |
| Faqat raqamlar | 10 | 100 mln |
| Kichik lotin harflari | 26 | ~209 mlrd |
| Katta + kichik harflar + raqamlar | 62 | ~218 trln |
| + maxsus belgilar | ~94 | ~6 kvadrillion |
- **Parol entropiyasi** — parolni taxmin qilish qiyinligini bitlarda ifodalovchi o‘lchov; qancha katta bo‘lsa, parol shuncha kuchli.
Har bir qo‘shimcha belgi variantlar sonini o‘nlab marta oshiradi. Shuning uchun murakkab qisqa paroldan ko‘ra uzun parol iborasi kuchliroq.
""",
            """
## Ishni bajarish tartibi
- **Parol yaratish.** Parol iborasi usulida 3 ta o‘quv parol tuzing (haqiqiy hisoblaringizda ishlatmang).
- **Generator bilan yaratish.** KeePass yoki Bitwarden parol generatorida 16 belgili, barcha belgi turlari qatnashgan parol yarating.
- **Mustahkamlikni tekshirish.** Parol menejeridagi sifat ko‘rsatkichi (entropiya, bit) ni yozib oling va o‘z parollaringiz bilan solishtiring.
- **Sizib chiqqanini tekshirish.** O‘qituvchi namoyishida haveibeenpwned.com saytida o‘quv elektron pochta manzili ma’lumotlar sizib chiqishida qatnashganini tekshirish ko‘rsatiladi.
Parollarni hech qachon noma’lum «parolingizni tekshiring» saytlariga kiritmang — ular parolni o‘g‘irlash uchun yaratilgan bo‘lishi mumkin.
""",
            """
## Windows parol siyosati
Windows Pro versiyasida `secpol.msc` (Локальная политика безопасности) orqali kompyuterdagi barcha hisoblar uchun parol talablari o‘rnatiladi.
- **Minimal uzunlik.** «Политики учётных записей» → «Политика паролей» → «Минимальная длина пароля» — 12 belgi.
- **Murakkablik.** «Пароль должен отвечать требованиям сложности» — «Включен».
- **Bloklash.** «Политика блокировки учётной записи» → 5 marta noto‘g‘ri kiritilganda hisob 15 daqiqaga bloklanadi.
| Sozlama | Tavsiya etiladigan qiymat |
| Minimal parol uzunligi | 12 |
| Murakkablik talabi | Yoqilgan |
| Noto‘g‘ri urinishlar chegarasi | 5 |
| Bloklash davomiyligi | 15 daqiqa |
- **Hisobni bloklash** — belgilangan sonda noto‘g‘ri parol kiritilganda hisobga kirishni vaqtincha to‘xtatish; brute force hujumiga qarshi samarali chora.
""",
        ],
        'oldingi': ['Kuchli parolga qanday talablar qo‘yiladi?',
                    'Parol iborasi nima?',
                    'Qanday parollar kuchsiz hisoblanadi?'],
        'savollar': ['Parol variantlari soni qanday hisoblanadi?',
                     'Parol entropiyasi nimani ko‘rsatadi?',
                     'Nima uchun uzun parol qisqa murakkab paroldan kuchliroq?',
                     'secpol.msc orqali qanday sozlamalar o‘rnatiladi?',
                     'Hisobni bloklash qaysi hujumga qarshi chora?'],
        'testlar': [
            ('Faqat raqamlardan iborat 8 belgili parolning variantlari soni:',
             ['100 million', '1000', '10 ming', '1 milliard'], 'a'),
            ('Windows’da mahalliy xavfsizlik siyosatini ochuvchi buyruq:',
             ['notepad', 'secpol.msc', 'calc', 'mspaint'], 'b'),
            ('5 marta noto‘g‘ri parol kiritilganda hisobni vaqtincha to‘xtatish:',
             ['Formatlash', 'Arxivlash', 'Hisobni bloklash', 'Zaxiralash'], 'c'),
            ('Parolni taxmin qilish qiyinligini bitlarda ifodalovchi o‘lchov:',
             ['Tezlik', 'Hajm', 'Chastota', 'Entropiya'], 'd'),
            ('Qaysi parol eng kuchli?',
             ['Qwerty12', 'kitob', 'Bahor-Daryo-Tog‘-2026!', '11111111'], 'c'),
        ],
        'mustaqil': ['Har xil belgilar to‘plami va uzunlikdagi 5 ta parolning variantlar sonini kalkulyatorda hisoblab, jadval tuzing.',
                     'Telefoningizdagi ekran qulfi turini (PIN, chizma, parol, barmoq izi) xavfsizlik nuqtai nazaridan taqqoslang.'],
    },
    # ------------------------------------------------------------------ 17
    {
        'type': 'N',
        'title': 'Autentifikatsiya va avtorizatsiya tushunchalari',
        'reja': ['Identifikatsiya, autentifikatsiya va avtorizatsiya',
                 'Autentifikatsiya omillari va usullari',
                 'Avtorizatsiya modellari va kirish huquqlari'],
        'maqsad': 'O‘quvchilarga identifikatsiya, autentifikatsiya va avtorizatsiya tushunchalari, autentifikatsiya '
                  'omillari va kirish huquqlarini boshqarish modellarini tushuntirish.',
        'natija': 'O‘quvchilar uchta tushunchani farqlaydi, autentifikatsiya omillariga misol keltiradi va '
                  'avtorizatsiya modellarini izohlaydi.',
        'bolimlar': [
            """
## Uch bosqich
Tizimga kirish jarayoni uch bosqichdan iborat:
- **Identifikatsiya** — foydalanuvchining o‘zini tanishtirishi, ya’ni login, telefon raqami yoki ID kartani ko‘rsatishi.
- **Autentifikatsiya** — foydalanuvchi haqiqatan ham o‘zi aytgan shaxs ekanini tekshirish.
- **Avtorizatsiya** — autentifikatsiyadan o‘tgan foydalanuvchiga tizimda qanday amallarni bajarish huquqi berilishini aniqlash.
Hayotiy misol: texnikumga kirishda o‘quvchi familiyasini aytadi (identifikatsiya), qorovul uning guvohnomasidagi rasmni yuziga solishtiradi (autentifikatsiya), so‘ng o‘quvchi faqat o‘z guruhi xonasi va kutubxonaga kira oladi, o‘qituvchilar xonasiga esa kira olmaydi (avtorizatsiya).
""",
            """
## Autentifikatsiya omillari
| Omil | Mazmuni | Misollar |
| Bilish omili | Foydalanuvchi biladigan narsa | Parol, PIN-kod, maxfiy savol javobi |
| Egalik omili | Foydalanuvchida bor narsa | Telefon (SMS-kod), bank kartasi, USB-kalit, smart-karta |
| Biometrik omil | Foydalanuvchining o‘ziga xos belgisi | Barmoq izi, yuz tasviri, ko‘z qorachig‘i, ovoz |
- **Biometrik autentifikatsiya** — insonning takrorlanmas jismoniy yoki xulq-atvor belgilari asosida shaxsni tasdiqlash.
- **Ko‘p omilli autentifikatsiya** — ikki yoki undan ortiq turli omillardan birgalikda foydalanish.
Bir xil omildan ikki marta foydalanish (masalan, parol va maxfiy savol) ko‘p omilli hisoblanmaydi, chunki ikkalasi ham «bilish» omili.
""",
            """
## Kirish huquqlari
Avtorizatsiyada har bir foydalanuvchi yoki guruhga resurslarga nisbatan huquqlar beriladi: o‘qish, yozish, o‘zgartirish, o‘chirish, ishga tushirish.
- **Rolga asoslangan kirish nazorati** — huquqlar alohida odamlarga emas, rollarga (o‘qituvchi, o‘quvchi, administrator) beriladi; foydalanuvchi rolga qo‘shilganda uning huquqlarini oladi.
- **Kirish nazorati ro‘yxati** — resurs (fayl, papka) uchun qaysi foydalanuvchi qanday huquqqa egaligini ko‘rsatuvchi ro‘yxat.
| Rol | Elektron jurnal | Baholar | Sozlamalar |
| O‘quvchi | Ko‘rish | Faqat o‘ziniki | Yo‘q |
| O‘qituvchi | Ko‘rish, yozish | O‘z fanidan qo‘yish | Yo‘q |
| Administrator | To‘liq | To‘liq | To‘liq |
## Seans
Autentifikatsiyadan so‘ng tizim seans ochadi. Seansni tugatish uchun «Chiqish» tugmasi bosiladi — ayniqsa umumiy kompyuterlarda bu juda muhim.
""",
        ],
        'oldingi': ['Kuchli parolni qanday yaratdingiz?',
                    'Hisobni bloklash sozlamasi nima uchun kerak?',
                    'Parol entropiyasi nima?'],
        'savollar': ['Identifikatsiya va autentifikatsiyaning farqi nimada?',
                     'Autentifikatsiyaning qanday omillari bor?',
                     'Biometrik autentifikatsiyaga misollar keltiring.',
                     'Rolga asoslangan kirish nazorati qanday ishlaydi?',
                     'Umumiy kompyuterda nima uchun seansdan chiqish kerak?'],
        'testlar': [
            ('Foydalanuvchi o‘zi aytgan shaxs ekanini tekshirish:',
             ['Identifikatsiya', 'Avtorizatsiya', 'Autentifikatsiya', 'Arxivlash'], 'c'),
            ('Foydalanuvchiga tizimda qanday huquqlar berilishini aniqlash:',
             ['Avtorizatsiya', 'Identifikatsiya', 'Shifrlash', 'Indekslash'], 'a'),
            ('Barmoq izi qaysi autentifikatsiya omiliga kiradi?',
             ['Bilish omili', 'Biometrik omil', 'Egalik omili', 'Vaqt omili'], 'b'),
            ('Qaysi juftlik ko‘p omilli autentifikatsiya hisoblanadi?',
             ['Parol va maxfiy savol', 'Ikki xil parol', 'PIN va parol', 'Parol va telefonga kelgan SMS-kod'], 'd'),
            ('Huquqlar odamlarga emas, rollarga beriladigan model:',
             ['Rolga asoslangan kirish nazorati', 'Brute force', 'Phishing', 'DDoS'], 'a'),
        ],
        'mustaqil': ['Kundalik hayotdan identifikatsiya, autentifikatsiya va avtorizatsiyaga 3 tadan misol yozing.',
                     'Texnikum elektron tizimi uchun rollar va huquqlar jadvalini tuzing (kamida 4 rol).'],
    },
    # ------------------------------------------------------------------ 18
    {
        'type': 'A',
        'title': 'Autentifikatsiya va avtorizatsiya jarayonlarini amalda ko‘rib chiqish',
        'reja': ['Windows’da kirish usullari',
                 'Amaliy ish: papkaga kirish huquqlarini (NTFS) sozlash',
                 'Kirish hodisalarini jurnaldan kuzatish'],
        'maqsad': 'O‘quvchilarda Windows’da autentifikatsiya usullarini sozlash, NTFS ruxsatlari orqali avtorizatsiyani '
                  'boshqarish va kirish hodisalarini kuzatish ko‘nikmasini shakllantirish.',
        'natija': 'O‘quvchilar PIN-kod o‘rnatadi, papkaga turli foydalanuvchilar uchun huquq beradi, huquqlarni sinab '
                  'ko‘radi va Event Viewer’da kirish hodisalarini topadi.',
        'vosita': 'Windows 10/11 Pro o‘rnatilgan kompyuterlar, o‘quv foydalanuvchi hisoblari, proyektor',
        'bolimlar': [
            """
## Windows Hello va kirish usullari
Windows’da tizimga kirishning bir necha usuli mavjud: parol, PIN-kod, rasmli parol, barmoq izi va yuz orqali tanish (Windows Hello). Ularni «Параметры» → «Учётные записи» → «Варианты входа» bo‘limida sozlash mumkin.
- **Windows Hello** — Windows’da PIN-kod, barmoq izi yoki yuz tasviri orqali tezkor va xavfsiz kirish texnologiyasi.
PIN-kod faqat shu kompyuterga bog‘lanadi: u o‘g‘irlansa ham, boshqa qurilmadan Microsoft hisobiga kirib bo‘lmaydi. Shuning uchun PIN oddiy paroldan xavfsizroq hisoblanadi.
## Mashg‘ulot uchun tayyorgarlik
O‘qituvchi oldindan ikkita o‘quv hisobini yaratadi: «talaba1» (oddiy foydalanuvchi) va «talaba2» (oddiy foydalanuvchi). Amaliy ish administrator hisobi ostida bajariladi.
""",
            """
## Ishni bajarish tartibi
- **Papka yaratish.** D diskida «Hisobotlar» papkasini yarating va ichiga matnli fayl joylang.
- **Xususiyatlarni ochish.** Papka ustida o‘ng tugma → «Свойства» → «Безопасность» bo‘limiga o‘ting.
- **Huquq berish.** «Изменить» → «Добавить» orqali «talaba1» ni qo‘shing va unga faqat «Чтение» (o‘qish) huquqini bering.
- **Ikkinchi foydalanuvchi.** «talaba2» ga «Изменение» (o‘zgartirish) huquqini bering.
- **Sinab ko‘rish.** `Win + L` orqali «talaba1» bilan kiring va fayl ichiga yozib saqlashga urinib ko‘ring — tizim ruxsat bermasligi kerak. So‘ng «talaba2» bilan tekshiring.
| Ruxsat | Imkoniyat |
| Чтение | Fayllarni ko‘rish va ochish |
| Запись | Yangi fayl yaratish va yozish |
| Изменение | O‘qish, yozish va o‘chirish |
| Полный доступ | Barcha amallar, huquqlarni o‘zgartirish ham |
""",
            """
## Kirish hodisalarini kuzatish
- **Jurnalni ochish.** `Win + R` → `eventvwr.msc` → «Журналы Windows» → «Безопасность».
- **Muvaffaqiyatli kirish.** 4624 kodli hodisalar — foydalanuvchi tizimga muvaffaqiyatli kirgan vaqtlar.
- **Muvaffaqiyatsiz kirish.** 4625 kodli hodisalar — noto‘g‘ri parol kiritilgan urinishlar.
- **Filtrlash.** O‘ng paneldagi «Фильтр текущего журнала» orqali faqat 4625 kodli hodisalarni ko‘rsating.
| Kod | Hodisa |
| 4624 | Hisobga muvaffaqiyatli kirish |
| 4625 | Kirishga muvaffaqiyatsiz urinish |
| 4634 | Seansdan chiqish |
| 4720 | Yangi foydalanuvchi hisobi yaratildi |
## Xulosa
Amaliy ishda autentifikatsiya (kim kirdi) va avtorizatsiya (nima qila oladi) qanday ishlashini o‘z ko‘zimiz bilan ko‘rdik, hisobdorlik esa jurnallar orqali ta’minlanadi.
""",
        ],
        'oldingi': ['Autentifikatsiya omillarini sanang.',
                    'Avtorizatsiya nima?',
                    'Rolga asoslangan kirish nazorati qanday ishlaydi?'],
        'savollar': ['Windows Hello qanday kirish usullarini taklif qiladi?',
                     'Nima uchun PIN-kod oddiy paroldan xavfsizroq?',
                     'Papkaga kirish huquqi qayerda sozlanadi?',
                     '«Чтение» va «Изменение» ruxsatlarining farqi nimada?',
                     'Event Viewer’dagi 4625 kodli hodisa nimani bildiradi?'],
        'testlar': [
            ('Windows’da hodisalar jurnalini ochuvchi buyruq:',
             ['eventvwr.msc', 'calc', 'winver', 'write'], 'a'),
            ('Muvaffaqiyatli kirish hodisasining kodi:',
             ['4625', '4720', '4624', '1000'], 'c'),
            ('Faqat fayllarni ko‘rish va ochishga imkon beruvchi NTFS ruxsati:',
             ['Полный доступ', 'Чтение', 'Изменение', 'Запись'], 'b'),
            ('PIN-kod, barmoq izi yoki yuz orqali kirish texnologiyasi:',
             ['BitLocker', 'Defender', 'OneDrive', 'Windows Hello'], 'd'),
            ('Papkaga kirish huquqlari qaysi bo‘limda sozlanadi?',
             ['«Свойства» → «Безопасность»', '«Вид» → «Значки»', '«Файл» → «Печать»', '«Пуск» → «Выключение»'], 'a'),
        ],
        'mustaqil': ['Uy kompyuteringizda Event Viewer orqali oxirgi bir hafta ichidagi kirish hodisalarini ko‘rib chiqing va natijani yozing.',
                     'NTFS ruxsatlari va «Общий доступ» (tarmoq ulashish) ruxsatlarining farqini o‘rganib, jadval tuzing.'],
    },
    # ------------------------------------------------------------------ 19
    {
        'type': 'A',
        'title': 'Foydalanuvchi hisoblarini xavfsiz sozlash',
        'reja': ['Hisob turlari va administrator huquqlari',
                 'Amaliy ish: standart foydalanuvchi hisobini yaratish va sozlash',
                 'UAC va hisob xavfsizligini mustahkamlash'],
        'maqsad': 'O‘quvchilarda Windows’da foydalanuvchi hisoblarini yaratish, turini belgilash, keraksiz hisoblarni '
                  'o‘chirish va UAC sozlamalari orqali hisob xavfsizligini oshirish ko‘nikmasini shakllantirish.',
        'natija': 'O‘quvchilar standart hisob yaratadi, administrator huquqlarini cheklaydi, «Гость» hisobini o‘chiradi, '
                  'UAC darajasini tekshiradi va hisob xavfsizligi bo‘yicha tavsiyalar beradi.',
        'vosita': 'Windows 10/11 o‘rnatilgan kompyuterlar (administrator huquqi bilan), buyruqlar satri, proyektor',
        'bolimlar': [
            """
## Hisob turlari
| Hisob turi | Imkoniyatlari | Qachon ishlatiladi |
| Administrator | Dastur o‘rnatish, tizim sozlamalarini o‘zgartirish, boshqa hisoblarni boshqarish | Faqat sozlash va ta’mirlash ishlarida |
| Standart foydalanuvchi | Dasturlardan foydalanish, o‘z sozlamalarini o‘zgartirish | Kundalik ish uchun |
| Mehmon (Гость) | Juda cheklangan vaqtinchalik kirish | Odatda o‘chirib qo‘yiladi |
- **Administrator hisobi** — kompyuterni to‘liq boshqarish huquqiga ega bo‘lgan hisob.
- **Standart hisob** — kundalik ish uchun mo‘ljallangan, tizim sozlamalarini o‘zgartira olmaydigan cheklangan hisob.
Xavfsizlik qoidasi: kundalik ish standart hisobda bajariladi. Agar foydalanuvchi administrator bo‘lib ishlasa, u tasodifan ochgan virus ham administrator huquqini oladi.
""",
            """
## Ishni bajarish tartibi
- **Hisob yaratish (grafik usul).** «Параметры» → «Учётные записи» → «Другие пользователи» → «Добавить пользователя» → «У меня нет данных для входа...» → «Добавить пользователя без учётной записи Майкрософт». Nom: «xodim1», kuchli parol kiriting.
- **Hisob turini tekshirish.** Yaratilgan hisob ustiga bosib, «Изменить тип учётной записи» bo‘limida «Стандартный пользователь» tanlanganiga ishonch hosil qiling.
- **Buyruq orqali yaratish.** Administrator sifatida ochilgan buyruqlar satrida: `net user xodim2 * /add` — parol so‘raladi.
- **Mehmon hisobini o‘chirish.** `net user Гость /active:no` (ingliz tilli tizimda `Guest`).
- **Ro‘yxatni tekshirish.** `net localgroup Администраторы` buyrug‘i bilan administratorlar guruhida ortiqcha hisob yo‘qligini tekshiring.
""",
            """
## UAC — foydalanuvchi hisoblarini nazorat qilish
- **UAC** — dastur tizimga o‘zgartirish kiritmoqchi bo‘lganda foydalanuvchidan ruxsat so‘raydigan Windows himoya mexanizmi.
UAC sozlamasini `Win + R` → `UserAccountControlSettings` buyrug‘i bilan ochish mumkin. Slayder kamida ikkinchi pog‘onada («Уведомлять только при попытках приложений внести изменения») bo‘lishi kerak. UAC’ni butunlay o‘chirish tavsiya etilmaydi.
## Hisob xavfsizligi bo‘yicha qo‘shimcha choralar
- Ishlatilmayotgan hisoblarni o‘chirish yoki bloklash.
- Har bir xodimga alohida hisob — hisobdorlik uchun.
- Ekran qulfining avtomatik yoqilishini sozlash: «Параметры» → «Персонализация» → «Экран блокировки» → «Заставка» → «Начинать с экрана входа».
- Ishdan bo‘shagan xodim hisobini darhol bloklash.
""",
        ],
        'oldingi': ['NTFS ruxsatlarini qanday sozladik?',
                    'Event Viewer’da qaysi kodlar kirish hodisalarini ko‘rsatadi?',
                    'Windows Hello nima?'],
        'savollar': ['Administrator va standart hisob o‘rtasidagi farq nimada?',
                     'Nima uchun kundalik ishni standart hisobda bajarish kerak?',
                     'Buyruqlar satri orqali hisob qanday yaratiladi?',
                     'UAC qanday vazifani bajaradi?',
                     'Ishdan bo‘shagan xodim hisobi bilan nima qilish kerak?'],
        'testlar': [
            ('Kundalik ish uchun tavsiya etiladigan hisob turi:',
             ['Administrator', 'Standart foydalanuvchi', 'Mehmon', 'Tizim hisobi'], 'b'),
            ('Dastur tizimga o‘zgartirish kiritmoqchi bo‘lganda ruxsat so‘raydigan mexanizm:',
             ['UAC', 'BIOS', 'DNS', 'FTP'], 'a'),
            ('Buyruqlar satrida yangi hisob yaratish buyrug‘i:',
             ['net share xodim2', 'ipconfig /add', 'net user xodim2 * /add', 'dir xodim2'], 'c'),
            ('Mehmon hisobini o‘chirish buyrug‘ining kaliti:',
             ['/delete:all', '/add', '/time', '/active:no'], 'd'),
            ('Ishdan bo‘shagan xodim hisobi bilan nima qilinadi?',
             ['Darhol bloklanadi', 'Yangi xodimga beriladi', 'Administrator qilinadi', 'O‘zgarishsiz qoldiriladi'], 'a'),
        ],
        'mustaqil': ['Oila a’zolaringiz foydalanadigan kompyuter uchun hisoblar tuzilmasini rejalashtiring: kimga qanday hisob turi kerak?',
                     'Microsoft hisobi va mahalliy hisobning afzallik va kamchiliklarini taqqoslang.'],
    },
    # ------------------------------------------------------------------ 20
    {
        'type': 'N',
        'title': 'Ikki bosqichli autentifikatsiya va 2FA usullari',
        'reja': ['Ikki bosqichli autentifikatsiya tushunchasi va zarurati',
                 '2FA usullari: SMS, autentifikator ilovasi, apparat kalit',
                 '2FA zaxira kodlari va xavfsiz foydalanish qoidalari'],
        'maqsad': 'O‘quvchilarga ikki bosqichli autentifikatsiya tushunchasi, uning turli usullari, ularning afzallik va '
                  'kamchiliklari hamda zaxira kodlardan foydalanishni tushuntirish.',
        'natija': 'O‘quvchilar 2FA ning ahamiyatini asoslaydi, SMS, TOTP va apparat kalit usullarini taqqoslaydi va '
                  '2FA dan xavfsiz foydalanish qoidalarini biladi.',
        'bolimlar': [
            """
## 2FA nima?
- **Ikki bosqichli autentifikatsiya (2FA)** — tizimga kirishda paroldan tashqari ikkinchi, boshqa turdagi tasdiq — odatda telefondagi kod yoki maxsus qurilma talab qilinadigan himoya usuli.
2FA bilan himoyalangan hisobga kirish uchun hujumchi parolni bilishining o‘zi yetarli emas: unga sizning telefoningiz yoki kalitingiz ham kerak bo‘ladi. Shuning uchun parol sizib chiqsa ham, hisob himoyalanganicha qoladi.
Statistik tadqiqotlar ko‘rsatishicha, 2FA yoqilgan hisoblarga avtomatlashtirilgan hujumlarning deyarli barchasi muvaffaqiyatsiz tugaydi. Shuning uchun elektron pochta, ijtimoiy tarmoq va bank ilovalarida 2FA albatta yoqilishi kerak.
""",
            """
## 2FA usullari
| Usul | Qanday ishlaydi | Afzalligi | Kamchiligi |
| SMS-kod | Telefonga bir martalik kod keladi | Oddiy, har qanday telefonda ishlaydi | SIM-karta almashtirish va SMS ushlab qolish xavfi |
| Autentifikator ilovasi | Ilova har 30 soniyada yangi kod yaratadi | Internet va aloqasiz ishlaydi, xavfsizroq | Telefon yo‘qolsa, zaxira kod kerak |
| Push-bildirishnoma | Telefonda «Kirishni tasdiqlaysizmi?» so‘rovi chiqadi | Juda qulay | Bexosdan «Ha» bosib yuborish mumkin |
| Apparat kalit | USB yoki NFC kalit kompyuterga ulanadi | Eng ishonchli, phishingdan himoyalaydi | Pullik, yo‘qotish mumkin |
- **TOTP** — vaqtga asoslangan bir martalik parol; maxfiy kalit va joriy vaqt asosida har 30 soniyada yangi 6 xonali kod yaratiladi.
- **Autentifikator ilovasi** — TOTP kodlarini yaratuvchi mobil ilova, masalan, Google Authenticator yoki Microsoft Authenticator.
""",
            """
## Zaxira kodlar
- **Zaxira kodlar** — telefon yo‘qolganda yoki ishlamaganda hisobga kirish uchun oldindan beriladigan bir martalik kodlar to‘plami.
Zaxira kodlar chop etilib yoki yozib olinib, xavfsiz joyda (masalan, hujjatlar papkasida) saqlanadi. Ularni telefonning o‘zida saqlash ma’nosiz — telefon yo‘qolsa, kodlar ham yo‘qoladi.
## Xavfsiz foydalanish qoidalari
- SMS-kodni hech kimga, hatto «bank xodimi» yoki «texnik yordam» deb tanishtirgan shaxsga ham aytmang.
- Siz kirmayotgan paytda tasdiqlash so‘rovi kelsa — rad eting va parolni darhol almashtiring.
- Telefonga ekran qulfi qo‘ying, aks holda uni olgan odam kodlarni ham oladi.
- Imkon bo‘lsa, SMS o‘rniga autentifikator ilovasidan foydalaning.
- Telefon raqamini almashtirsangiz, avval hisoblardagi 2FA sozlamasini yangilang.
""",
        ],
        'oldingi': ['Hisob turlari qanday farqlanadi?',
                    'UAC nima?',
                    'Autentifikatsiyaning qanday omillari bor?'],
        'savollar': ['2FA nima va u nima uchun kerak?',
                     'SMS-kod usulining kamchiliklari qanday?',
                     'TOTP kodi qanday yaratiladi?',
                     'Zaxira kodlar nima uchun kerak va qayerda saqlanadi?',
                     'Kirmayotgan paytingizda tasdiqlash so‘rovi kelsa nima qilasiz?'],
        'testlar': [
            ('Har 30 soniyada yangi kod yaratuvchi usul:',
             ['SMS-kod', 'TOTP (autentifikator ilovasi)', 'Maxfiy savol', 'Parol'], 'b'),
            ('Phishingdan eng yaxshi himoyalovchi 2FA usuli:',
             ['Apparat kalit', 'SMS-kod', 'Maxfiy savol', 'Elektron xat'], 'a'),
            ('Telefon yo‘qolganda hisobga kirish uchun oldindan beriladigan kodlar:',
             ['Pin-kodlar', 'Shtrix-kodlar', 'Zaxira kodlar', 'QR-kodlar'], 'c'),
            ('Quyidagilardan qaysi biri autentifikator ilovasi?',
             ['Paint', 'Excel', 'Telegram', 'Google Authenticator'], 'd'),
            ('«Bank xodimi» SMS-kodni so‘rasa:',
             ['Hech qachon aytmaslik kerak', 'Aytish kerak', 'Faqat yarmini aytish', 'Ertaga aytish'], 'a'),
        ],
        'mustaqil': ['O‘zingiz foydalanadigan 3 ta xizmatda (pochta, ijtimoiy tarmoq, messenjer) 2FA mavjudligini va usulini aniqlang.',
                     '2FA usullarini xavfsizlik va qulaylik bo‘yicha 5 ballik shkalada baholab, diagramma chizing.'],
    },
]
