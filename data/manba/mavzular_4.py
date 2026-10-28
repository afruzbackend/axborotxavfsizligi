"""31–40-mavzular: shaxsiy ma'lumotlar, antivirus, shifrlash va zaxiralash, himoya vositalari, qonunchilik."""

MAVZULAR = [
    # ------------------------------------------------------------------ 31
    {
        'type': 'N',
        'title': 'Shaxsiy ma’lumotlarni himoya qilish',
        'reja': ['Shaxsga doir ma’lumotlar tushunchasi va turlari',
                 'Shaxsiy ma’lumotlarga tahdidlar',
                 'Shaxsiy ma’lumotlarni himoya qilish qoidalari'],
        'maqsad': 'O‘quvchilarga shaxsga doir ma’lumotlar tushunchasi, ularning turlari, sizib chiqish yo‘llari va himoya '
                  'qilish qoidalarini tushuntirish.',
        'natija': 'O‘quvchilar shaxsiy ma’lumotlarni oddiy va maxsus toifalarga ajratadi, ularning sizib chiqish '
                  'yo‘llarini biladi va himoya qoidalariga amal qiladi.',
        'bolimlar': [
            """
## Shaxsiy ma’lumot nima?
- **Shaxsga doir ma’lumotlar** — muayyan jismoniy shaxsga taalluqli bo‘lgan yoki uni identifikatsiya qilish imkonini beradigan har qanday axborot.
- **Ma’lumotlar subyekti** — shaxsga doir ma’lumotlar o‘ziga taalluqli bo‘lgan jismoniy shaxs.
| Toifa | Misollar |
| Identifikatsiya ma’lumotlari | Familiya, ism, tug‘ilgan sana, pasport seriyasi, JSHSHIR |
| Aloqa ma’lumotlari | Telefon raqami, manzil, elektron pochta |
| Moliyaviy ma’lumotlar | Bank kartasi raqami, hisob raqami |
| Maxsus ma’lumotlar | Sog‘liq holati, diniy e’tiqod, biometrik ma’lumotlar |
| Raqamli ma’lumotlar | IP manzil, joylashuv, login, qurilma identifikatori |
O‘zbekistonda bu soha 2019-yilda qabul qilingan «Shaxsga doir ma’lumotlar to‘g‘risida»gi Qonun bilan tartibga solinadi. Qonunga ko‘ra, shaxsiy ma’lumotlar faqat subyektning roziligi bilan yig‘iladi va qayta ishlanadi.
""",
            """
## Ma’lumotlar qanday sizib chiqadi?
- **Ochiq e’lon qilish.** Ijtimoiy tarmoqda pasport, chipta yoki karta rasmini joylash.
- **Anketalar va testlar.** «Qaysi multfilm qahramonisiz?» testida onangizning qizlik familiyasi va birinchi uy hayvoningiz nomini so‘rashadi — bu ko‘p saytlarda maxfiy savol javoblari.
- **Phishing.** Soxta saytga ma’lumot kiritish.
- **Ilovalar ruxsati.** Kontaktlar, joylashuv va kameraga keraksiz ruxsat bergan ilovalar.
- **Yo‘qotilgan qurilma.** Qulflanmagan telefon yoki shifrlanmagan noutbuk.
- **Saytlarning buzilishi.** Tashkilot bazasidan ma’lumotlar o‘g‘irlanishi.
- **Doksing** — insonning shaxsiy ma’lumotlarini (manzil, telefon, ish joyi) uning roziligisiz to‘plab, internetda ommaga e’lon qilish.
- **Shaxsni o‘g‘irlash** — birovning shaxsiy ma’lumotlaridan foydalanib, uning nomidan kredit olish, hisob ochish yoki firibgarlik qilish.
""",
            """
## Himoya qoidalari
- Pasport, ID karta, bank kartasi rasmlarini messenjer va ijtimoiy tarmoqda yubormang.
- Ma’lumot so‘ralganda o‘zingizga savol bering: bu xizmatga shu ma’lumot rostdan kerakmi?
- Ilovalarga faqat zarur ruxsatlarni bering.
- Telefon va noutbukda ekran qulfi va shifrlashni yoqing.
- Joylashuvni faqat kerak paytda yoqing, rasmlardagi joylashuv belgisini o‘chiring.
- Eski qurilmani sotishdan oldin ma’lumotlarni to‘liq o‘chiring va zavod sozlamalariga qaytaring.
- Qog‘ozdagi hujjat nusxalarini «faqat ... uchun» yozuvi bilan bering.
## IT-servis mutaxassisi majburiyatlari
Ta’mirga kelgan qurilmadagi mijoz ma’lumotlari — begona mulk. Mutaxassis ularni ko‘rmaydi, nusxalamaydi va tarqatmaydi. Diskni almashtirishda eski diskdagi ma’lumotlar mijoz roziligi bilan o‘chiriladi yoki diskning o‘zi mijozga qaytariladi.
""",
        ],
        'oldingi': ['Wi-Fi routerni qanday xavfsiz sozladik?',
                    'Mehmon tarmog‘i nima?',
                    'WPA2 va WEP farqi nimada?'],
        'savollar': ['Shaxsga doir ma’lumotlarga qanday ma’lumotlar kiradi?',
                     'Maxsus toifadagi ma’lumotlarga misol keltiring.',
                     'Internetdagi «qiziqarli testlar» qanday xavf tug‘diradi?',
                     'Doksing nima?',
                     'Eski telefonni sotishdan oldin nima qilish kerak?'],
        'testlar': [
            ('O‘zbekistonda «Shaxsga doir ma’lumotlar to‘g‘risida»gi Qonun qachon qabul qilingan?',
             ['2003-yilda', '2019-yilda', '2022-yilda', '2010-yilda'], 'b'),
            ('Sog‘liq holati haqidagi ma’lumot qaysi toifaga kiradi?',
             ['Maxsus ma’lumotlar', 'Aloqa ma’lumotlari', 'Moliyaviy ma’lumotlar', 'Ochiq ma’lumotlar'], 'a'),
            ('Shaxsiy ma’lumotlarni roziligisiz to‘plab, internetda e’lon qilish:',
             ['Bloging', 'Striming', 'Doksing', 'Zaxiralash'], 'c'),
            ('Birovning ma’lumotlari bilan uning nomidan kredit olish:',
             ['Kiberetika', 'Avtorizatsiya', 'Shifrlash', 'Shaxsni o‘g‘irlash'], 'd'),
            ('Shaxsiy ma’lumotlar qonunga ko‘ra qanday asosda yig‘iladi?',
             ['Subyektning roziligi bilan', 'Istalgan vaqtda', 'Faqat internet orqali', 'Hech qanday shartsiz'], 'a'),
        ],
        'mustaqil': ['Telefoningizdagi 5 ta ilovaning ruxsatlarini tekshirib, qaysi ruxsatlar keraksiz ekanini yozing.',
                     '«Shaxsga doir ma’lumotlar to‘g‘risida»gi Qonundan subyekt huquqlari haqidagi moddalarni topib, qisqacha yozing.'],
    },
    # ------------------------------------------------------------------ 32
    {
        'type': 'A',
        'title': 'Ijtimoiy tarmoqlarda maxfiylik sozlamalarini boshqarish',
        'reja': ['Ijtimoiy tarmoqlardagi maxfiylik xavflari',
                 'Amaliy ish: Telegram va Instagram maxfiylik sozlamalarini o‘rnatish',
                 'Raqamli izni tekshirish va tozalash'],
        'maqsad': 'O‘quvchilarda Telegram va Instagram’da telefon raqami, profil, joylashuv va faollik ko‘rinishini '
                  'cheklash hamda raqamli izni tekshirish ko‘nikmasini shakllantirish.',
        'natija': 'O‘quvchilar messenjer va ijtimoiy tarmoqlarda maxfiylik sozlamalarini o‘rnatadi, faol seanslarni '
                  'tekshiradi va profilidagi ortiqcha shaxsiy ma’lumotlarni olib tashlaydi.',
        'vosita': 'O‘quvchilarning smartfonlari yoki kompyuterlardagi o‘quv hisoblari, Telegram Desktop, proyektor',
        'bolimlar': [
            """
## Nimalar xavf tug‘diradi?
- Hamma ko‘ra oladigan telefon raqami — spam va firibgar qo‘ng‘iroqlar manbai.
- Ochiq profil — notanish odamlar rasmlar, do‘stlar va qiziqishlarni ko‘radi.
- Rasmlardagi joylashuv — uy va o‘qish joyini aniqlash mumkin.
- «Onlayn» holati — kundalik tartibingizni kuzatish imkonini beradi.
- Notanishlarning guruhlarga qo‘shishi — spam va firibgarlik guruhlari.
- **Maxfiylik sozlamalari** — foydalanuvchi o‘z ma’lumotlarini kim ko‘ra olishini belgilaydigan parametrlar to‘plami.
Asosiy tamoyil: «Hamma» (Все) o‘rniga «Kontaktlarim» (Мои контакты) yoki «Hech kim» (Никто).
""",
            """
## Telegram sozlamalari
«Настройки» → «Конфиденциальность» bo‘limida:
| Sozlama | Tavsiya |
| Номер телефона — кто видит | Никто |
| Кто может найти меня по номеру | Мои контакты |
| Время захода (onlayn holati) | Мои контакты yoki Никто |
| Фотографии профиля | Мои контакты |
| Пересылка сообщений | Мои контакты |
| Звонки | Мои контакты |
| Приглашения в группы | Мои контакты |
## Instagram sozlamalari
- **Yopiq akkaunt.** «Настройки» → «Конфиденциальность аккаунта» → «Закрытый аккаунт» ni yoqing.
- **Hikoyalar.** «Скрыть историю от» orqali kerakli odamlardan yashiring.
- **Teglar va eslatmalar.** Sizni faqat obunachilar belgilashi mumkin bo‘lsin.
- **Faollik holati.** «Сетевой статус» ni o‘chiring.
- **Faol seanslar.** «Центр аккаунтов» → «Пароль и безопасность» → «Где вы вошли» bo‘limida begona qurilmalarni chiqaring.
""",
            """
## Raqamli izni tekshirish
- **Qidiruv.** Qidiruv tizimida ism-familiyangizni qo‘shtirnoq ichida qidiring: «"Ism Familiya"». Topilgan ma’lumotlar ro‘yxatini yozing.
- **Profilni ko‘rib chiqish.** Profilda manzil, maktab raqami, telefon, tug‘ilgan to‘liq sana ko‘rsatilgan bo‘lsa — olib tashlang.
- **Eski postlar.** Shaxsiy hujjat, chipta, uy manzili tushgan eski rasmlarni o‘chiring yoki arxivlang.
- **Ilovalar ulanishi.** Ijtimoiy tarmoq hisobi orqali kirilgan keraksiz saytlar ruxsatini bekor qiling.
- **Rasm metama’lumotlari** — rasm fayliga yozilgan qo‘shimcha ma’lumotlar: suratga olingan vaqt, kamera modeli va ko‘pincha GPS joylashuvi.
Rasmni joylashdan oldin telefon kamerasida joylashuv yozishni o‘chiring. Kompyuterda rasm «Свойства» → «Подробно» → «Удаление свойств и личной информации» orqali metama’lumotlardan tozalanadi.
""",
        ],
        'oldingi': ['Shaxsga doir ma’lumotlarga nimalar kiradi?',
                    'Doksing nima?',
                    'Shaxsiy ma’lumotlar qanday sizib chiqadi?'],
        'savollar': ['Ijtimoiy tarmoqlarda qanday maxfiylik xavflari bor?',
                     'Telegram’da telefon raqamini qanday yashirish mumkin?',
                     'Instagram’da yopiq akkaunt nima beradi?',
                     'Rasm metama’lumotlarida qanday ma’lumotlar bo‘ladi?',
                     'Raqamli izni qanday tekshirish mumkin?'],
        'testlar': [
            ('Telegram’da telefon raqamini yashirish uchun «Номер телефона» bandida nima tanlanadi?',
             ['Все', 'Никто', 'Каналы', 'Боты'], 'b'),
            ('Instagram’da profilni faqat obunachilarga ko‘rsatish:',
             ['Закрытый аккаунт', 'Бизнес-аккаунт', 'Архив', 'Прямой эфир'], 'a'),
            ('Rasm fayliga yozilgan vaqt, kamera va GPS ma’lumotlari:',
             ['Kesh', 'Kodek', 'Metama’lumotlar', 'Drayver'], 'c'),
            ('Telegram’da begona qurilmani hisobdan chiqarish bo‘limi:',
             ['«Стикеры»', '«Чаты»', '«Папки»', '«Устройства»'], 'd'),
            ('Ijtimoiy tarmoq profilida ko‘rsatish tavsiya etilmaydi:',
             ['Uy manzili va telefon raqami', 'Qiziqishlar', 'Sevimli kitob', 'Taxallus'], 'a'),
        ],
        'mustaqil': ['O‘zingiz foydalanadigan ijtimoiy tarmoqda maxfiylik sozlamalarini tekshirib, «oldin/keyin» jadvalini tuzing.',
                     'Oila a’zolaringizdan biriga Telegram maxfiylik sozlamalarini o‘rnatishda yordam bering.'],
    },
    # ------------------------------------------------------------------ 33
    {
        'type': 'N',
        'title': 'Antivirus va xavfsizlik dasturlarining vazifalari',
        'reja': ['Antivirus dasturi va uning ishlash usullari',
                 'Antivirus dasturlari turlari va ularni taqqoslash',
                 'Boshqa xavfsizlik dasturlari'],
        'maqsad': 'O‘quvchilarga antivirus dasturlarining vazifalari, aniqlash usullari, mashhur antiviruslar va boshqa '
                  'xavfsizlik dasturlarini tushuntirish.',
        'natija': 'O‘quvchilar signatura va evristik usullarni farqlaydi, antiviruslarni imkoniyatlari bo‘yicha taqqoslaydi '
                  'va qo‘shimcha xavfsizlik dasturlari vazifasini izohlaydi.',
        'bolimlar': [
            """
## Antivirus qanday ishlaydi?
- **Antivirus dasturi** — kompyuterdagi zararli dasturlarni aniqlash, zararsizlantirish va ularning kirishiga yo‘l qo‘ymaslik uchun mo‘ljallangan dastur.
| Usul | Ishlash tamoyili | Afzalligi / kamchiligi |
| Signatura usuli | Fayl ma’lum viruslar «barmoq izlari» bazasi bilan solishtiriladi | Aniq, lekin yangi viruslarni bilmaydi |
| Evristik usul | Fayl kodi shubhali buyruqlar bo‘yicha tahlil qilinadi | Yangi viruslarni ham topadi, ba’zan xato signal beradi |
| Xulq-atvor tahlili | Dastur ishlash jarayonida kuzatiladi: fayllarni ommaviy shifrlay boshlasa — to‘xtatiladi | Shifrlovchilarga qarshi samarali |
| Bulutli tahlil | Shubhali fayl ma’lumoti ishlab chiqaruvchi serverida tekshiriladi | Tez yangilanadi, internet kerak |
- **Virus signaturasi** — zararli dasturni aniqlash uchun ishlatiladigan uning o‘ziga xos kod bo‘lagi yoki xesh qiymati.
- **Real vaqt himoyasi** — antivirus fayl ochilishi, yuklanishi va ishga tushishini doimiy kuzatib boradigan rejim.
- **Yolg‘on signal** — zararsiz faylni antivirus xato ravishda zararli deb aniqlashi.
""",
            """
## Mashhur antiviruslar
| Antivirus | Turi | Xususiyati |
| Microsoft Defender | Bepul, Windows’ga o‘rnatilgan | Qo‘shimcha o‘rnatish shart emas, yetarlicha kuchli |
| Kaspersky | Pullik / bepul versiya | Kuchli aniqlash, ko‘p qo‘shimcha funksiyalar |
| ESET NOD32 | Pullik | Kompyuterni kam yuklaydi |
| Avast / AVG | Bepul va pullik | Keng tarqalgan, reklama takliflari bor |
| Dr.Web CureIt! | Bepul skaner | O‘rnatmasdan bir martalik tekshirish uchun |
## Tanlash mezonlari
- Mustaqil laboratoriyalar (AV-TEST, AV-Comparatives) sinovlari natijalari.
- Kompyuterni sekinlashtirish darajasi.
- Bazaning yangilanish tezligi.
- Qo‘shimcha imkoniyatlar: firewall, veb-himoya, ota-ona nazorati.
- Narxi va litsenziya shartlari.
Bitta kompyuterga ikkita real vaqt antivirusi o‘rnatilmaydi — ular bir-biriga xalaqit berib, tizimni sekinlashtiradi.
""",
            """
## Boshqa xavfsizlik dasturlari
- **Shaxsiy firewall** — kompyuterga kiruvchi va chiquvchi ulanishlarni boshqaradi.
- **Antispam** — elektron pochtadagi spam va phishing xatlarni filtrlaydi.
- **Ota-ona nazorati dasturi** — bolalar uchun xavfli saytlarni bloklaydi va vaqtni cheklaydi.
- **Parol menejeri** — parollarni shifrlangan holda saqlaydi.
- **VPN mijoz** — ochiq tarmoqda trafikni shifrlaydi.
- **Zaxiralash dasturi** — fayllar nusxasini avtomatik yaratadi.
- **Kompleks himoya** — antivirus, firewall, antispam, ota-ona nazorati va boshqa vositalarni bitta paketda birlashtirgan dastur (Internet Security).
Shuni unutmang: antivirus muhim, lekin yagona himoya emas. U foydalanuvchi o‘zi kiritgan parolni phishing saytdan himoya qila olmasligi mumkin, shuning uchun ehtiyotkorlik har doim birinchi o‘rinda.
""",
        ],
        'oldingi': ['Telegram’da qanday maxfiylik sozlamalarini o‘rnatdik?',
                    'Rasm metama’lumotlari nima?',
                    'Raqamli iz qanday tekshiriladi?'],
        'savollar': ['Antivirus dasturi qanday vazifalarni bajaradi?',
                     'Signatura va evristik usullar farqi nimada?',
                     'Real vaqt himoyasi nima?',
                     'Antivirus tanlashda qanday mezonlarga e’tibor beriladi?',
                     'Nima uchun bitta kompyuterga ikkita antivirus o‘rnatilmaydi?'],
        'testlar': [
            ('Faylni ma’lum viruslar bazasi bilan solishtirish usuli:',
             ['Evristik usul', 'Signatura usuli', 'Bulutli tahlil', 'Xulq-atvor tahlili'], 'b'),
            ('Windows’ga o‘rnatilgan bepul antivirus:',
             ['Microsoft Defender', 'WinRAR', 'Paint', 'Skype'], 'a'),
            ('Zararsiz faylni antivirus xato ravishda zararli deb aniqlashi:',
             ['Karantin', 'Signatura', 'Yolg‘on signal', 'Real vaqt himoyasi'], 'c'),
            ('O‘rnatmasdan bir martalik tekshirish uchun bepul skaner:',
             ['Kaspersky Total', 'ESET Smart Security', 'Avast Premium', 'Dr.Web CureIt!'], 'd'),
            ('Shifrlovchi viruslarga qarshi eng samarali aniqlash usuli:',
             ['Xulq-atvor tahlili', 'Fayl nomini ko‘rish', 'Ikonka rangini ko‘rish', 'Fayl hajmini ko‘rish'], 'a'),
        ],
        'mustaqil': ['3 ta antivirusni (Defender, Kaspersky, ESET) imkoniyatlari, narxi va AV-TEST natijalari bo‘yicha taqqoslang.',
                     'Kompleks himoya paketi tarkibidagi vositalarni klaster ko‘rinishida tasvirlang.'],
    },
    # ------------------------------------------------------------------ 34
    {
        'type': 'A',
        'title': 'Antivirus dasturini o‘rnatish va dastlabki sozlash',
        'reja': ['Antivirus o‘rnatishga tayyorgarlik',
                 'Amaliy ish: Microsoft Defender’ni sozlash',
                 'Boshqa antivirusni o‘rnatish va bazani yangilash'],
        'maqsad': 'O‘quvchilarda antivirusni rasmiy manbadan o‘rnatish, Microsoft Defender’da real vaqt himoyasi, '
                  'bulutli himoya, shifrlovchilardan himoya va bazani yangilash sozlamalarini o‘rnatish ko‘nikmasini shakllantirish.',
        'natija': 'O‘quvchilar Defender sozlamalarini tekshiradi va yoqadi, boshqariladigan papkalarga kirishni sozlaydi, '
                  'antivirus bazasini yangilaydi va o‘rnatish ketma-ketligini tushuntiradi.',
        'vosita': 'Windows 10/11 o‘rnatilgan kompyuterlar (administrator huquqi), internet, proyektor',
        'bolimlar': [
            """
## Tayyorgarlik
- **Mavjud antivirusni aniqlash.** Windows Security → «Защита от вирусов и угроз» bo‘limida qaysi antivirus ishlayotgani ko‘rsatiladi.
- **Eski antivirusni o‘chirish.** Boshqa antivirus o‘rnatishdan oldin eskisi «Параметры» → «Приложения» orqali yoki ishlab chiqaruvchining maxsus o‘chirish utilitasi bilan to‘liq o‘chiriladi.
- **Rasmiy manba.** O‘rnatish fayli faqat ishlab chiqaruvchining rasmiy saytidan yuklanadi.
- **Tizim talablari.** Operatsion tizim versiyasi va bo‘sh disk hajmi tekshiriladi.
- **Litsenziya kaliti** — pullik dasturdan qonuniy foydalanish huquqini tasdiqlovchi noyob kod.
«Kryak» qilingan (buzilgan) antivirus — o‘zi zararli dastur bo‘lishi mumkin. Pullik antivirusga mablag‘ bo‘lmasa, bepul Microsoft Defender’dan foydalanish ancha xavfsiz.
""",
            """
## Microsoft Defender sozlamalari
- **Ilovani ochish.** «Пуск» → «Безопасность Windows» → «Защита от вирусов и угроз» → «Параметры защиты от вирусов и других угроз» → «Управление настройками».
- **Real vaqt himoyasi.** «Защита в режиме реального времени» — «Вкл.»
- **Bulutli himoya.** «Облачная защита» va «Автоматическая отправка образцов» — «Вкл.»
- **O‘zgartirishdan himoya.** «Защита от подделки» — «Вкл.»: zararli dastur antivirusni o‘chira olmaydi.
- **Shifrlovchilardan himoya.** «Защита от программ-шантажистов» → «Контролируемый доступ к папкам» — «Вкл.». Shundan so‘ng «Документы», «Изображения» papkalaridagi fayllarni faqat ishonchli dasturlar o‘zgartira oladi.
- **Keraksiz dasturlarni bloklash.** «Управление приложениями и браузером» → «Защита на основе репутации» → «Блокировка потенциально нежелательных приложений» — «Вкл.»
- **Boshqariladigan papkalarga kirish** — shifrlovchi viruslar himoyalangan papkalardagi fayllarni o‘zgartira olmasligi uchun faqat ishonchli dasturlarga ruxsat beruvchi Defender funksiyasi.
""",
            """
## Bazani yangilash
- **Defender’da.** «Обновления защиты» → «Проверить наличие обновлений». Oxirgi yangilanish sanasi va versiyasi yozib olinadi.
- **Buyruq orqali.** Administrator sifatida PowerShell’da `Update-MpSignature` buyrug‘i bazani yangilaydi, `Get-MpComputerStatus` esa himoya holatini ko‘rsatadi.
## Boshqa antivirusni o‘rnatish ketma-ketligi
| Qadam | Harakat |
| 1 | Eski antivirusni to‘liq o‘chirish va kompyuterni qayta yuklash |
| 2 | Rasmiy saytdan o‘rnatish faylini yuklash va raqamli imzosini tekshirish |
| 3 | O‘rnatishda qo‘shimcha (reklama) dasturlar belgisini olib tashlash |
| 4 | Litsenziyani faollashtirish |
| 5 | Bazani yangilash |
| 6 | To‘liq tekshiruv o‘tkazish |
Boshqa antivirus o‘rnatilganda Defender avtomatik passiv rejimga o‘tadi — bu to‘g‘ri holat.
""",
        ],
        'oldingi': ['Antivirusning qanday aniqlash usullari bor?',
                    'Real vaqt himoyasi nima?',
                    'Kompleks himoya paketi tarkibiga nimalar kiradi?'],
        'savollar': ['Antivirus o‘rnatishdan oldin nimalarni tekshirish kerak?',
                     'Nima uchun buzilgan (kryak) antivirus xavfli?',
                     '«Защита от подделки» funksiyasi nima uchun kerak?',
                     'Boshqariladigan papkalarga kirish qanday himoya beradi?',
                     'Defender bazasini PowerShell’da qaysi buyruq yangilaydi?'],
        'testlar': [
            ('Zararli dastur antivirusni o‘chirib qo‘ymasligi uchun Defender funksiyasi:',
             ['Защита от подделки', 'Режим самолёта', 'Ночной свет', 'Фокусировка'], 'a'),
            ('Defender bazasini yangilovchi PowerShell buyrug‘i:',
             ['Get-Date', 'Update-MpSignature', 'Clear-Host', 'Get-Process'], 'b'),
            ('Shifrlovchilardan himoya qiluvchi Defender funksiyasi:',
             ['Облачная защита', 'Брандмауэр', 'Контролируемый доступ к папкам', 'Родительский контроль'], 'c'),
            ('Yangi antivirus o‘rnatishdan oldin nima qilinadi?',
             ['Monitor almashtiriladi', 'Internet uziladi', 'Disk formatlanadi', 'Eski antivirus to‘liq o‘chiriladi'], 'd'),
            ('Boshqa antivirus o‘rnatilganda Defender:',
             ['Passiv rejimga o‘tadi', 'Kompyuterni o‘chiradi', 'Ikkala antivirus to‘liq ishlaydi', 'O‘chirib tashlanadi'], 'a'),
        ],
        'mustaqil': ['Uy kompyuteringizdagi antivirus sozlamalarini tekshiring va yoqilmagan himoya funksiyalarini yozing.',
                     'Get-MpComputerStatus buyrug‘i natijasidagi asosiy maydonlar ma’nosini izohlang.'],
    },
    # ------------------------------------------------------------------ 35
    {
        'type': 'A',
        'title': 'Antivirus yordamida kompyuterni tekshirish',
        'reja': ['Tekshiruv turlari',
                 'Amaliy ish: tezkor, to‘liq va maxsus tekshiruv o‘tkazish',
                 'Tekshiruv natijalarini tahlil qilish va karantin bilan ishlash'],
        'maqsad': 'O‘quvchilarda antivirus yordamida tezkor, to‘liq, tanlangan va oflayn tekshiruv o‘tkazish, natijalarni '
                  'tahlil qilish va karantindagi fayllar bilan ishlash ko‘nikmasini shakllantirish.',
        'natija': 'O‘quvchilar tekshiruv turini vaziyatga qarab tanlaydi, tekshiruvni bajaradi, himoya jurnalini o‘qiydi, '
                  'karantindagi fayl bo‘yicha qaror qabul qiladi va hisobot yozadi.',
        'vosita': 'Windows 10/11 kompyuterlar, fleshka, EICAR test fayli, Dr.Web CureIt! skaneri, proyektor',
        'bolimlar': [
            """
## Tekshiruv turlari
| Turi | Nima tekshiriladi | Qachon |
| Tezkor tekshiruv | Tizim papkalari, xotira, avtoyuklanish | Har kuni avtomatik, shubha tug‘ilganda |
| To‘liq tekshiruv | Barcha disklar va fayllar | Antivirus yangi o‘rnatilganda, oyiga bir marta |
| Tanlangan tekshiruv | Ko‘rsatilgan papka, fayl yoki fleshka | Yangi fleshka yoki yuklangan fayl uchun |
| Oflayn tekshiruv | Windows yuklanmasdan oldin | Virus o‘zini yashirayotgan bo‘lsa |
- **Rootkit** — o‘zini va boshqa zararli dasturlarni operatsion tizim va antivirusdan yashiradigan zararli dastur.
- **Oflayn tekshiruv** — kompyuter qayta yuklanib, Windows ishga tushmasdan oldin maxsus muhitda o‘tkaziladigan chuqur tekshiruv; rootkitlarni aniqlash uchun ishlatiladi.
""",
            """
## Ishni bajarish tartibi
- **Tezkor tekshiruv.** Windows Security → «Защита от вирусов и угроз» → «Быстрая проверка». Davomiyligini yozib oling.
- **Fleshkani tekshirish.** Fleshkani ulang, Explorer’da uning ustida o‘ng tugma → «Проверить с помощью Microsoft Defender».
- **Tanlangan papka.** «Параметры сканирования» → «Настраиваемое сканирование» → «Загрузки» papkasini tanlang.
- **To‘liq tekshiruv.** «Параметры сканирования» → «Полное сканирование» ni boshlang (u uzoq davom etadi, uni mashg‘ulot oxirigacha qoldiring).
- **Buyruq orqali.** PowerShell’da `Start-MpScan -ScanType QuickScan` tezkor tekshiruvni boshlaydi.
- **Ikkinchi fikr.** Dr.Web CureIt! skanerini ishga tushirib, natijani Defender natijasi bilan solishtiring.
- **Oflayn tekshiruv (namoyish).** O‘qituvchi «Проверка Microsoft Defender в автономном режиме» ni namoyish etadi — kompyuter qayta yuklanadi.
""",
            """
## Natijalarni tahlil qilish
- **Himoya jurnali.** Windows Security → «Журнал защиты» bo‘limida aniqlangan tahdidlar, ularning nomi, xavf darajasi va bajarilgan harakat ko‘rsatiladi.
- **Karantin.** Karantindagi faylni darhol o‘chirmaslik ham mumkin: agar u kerakli fayl bo‘lsa va yolg‘on signal ekaniga ishonch bo‘lsa, «Восстановить» bosiladi. Shubha bo‘lsa — «Удалить».
| Tekshiruv turi | Davomiyligi | Tekshirilgan fayllar | Aniqlangan tahdidlar | Harakat |
| Tezkor | 3 daqiqa | 25 000 | 0 | — |
| Fleshka | 1 daqiqa | 340 | 1 (EICAR) | Karantinga olindi |
| To‘liq | 45 daqiqa | 480 000 | 0 | — |
## Profilaktika
Tekshiruvlar jadvalini «Планировщик заданий» orqali belgilash mumkin. Lekin eng yaxshi himoya — virusni kompyuterga kiritmaslik: fleshkalarni ochishdan oldin tekshirish va noma’lum fayllarni ishga tushirmaslik.
""",
        ],
        'oldingi': ['Defender’da qanday himoya funksiyalarini yoqdik?',
                    'Boshqariladigan papkalarga kirish nima?',
                    'Antivirus bazasi qanday yangilanadi?'],
        'savollar': ['Qanday tekshiruv turlari bor?',
                     'Qachon to‘liq tekshiruv o‘tkaziladi?',
                     'Rootkit nima va uni qanday aniqlash mumkin?',
                     'Karantindagi fayl bilan qanday qaror qabul qilinadi?',
                     'Fleshkani qanday tekshirish kerak?'],
        'testlar': [
            ('Windows yuklanmasdan oldin o‘tkaziladigan chuqur tekshiruv:',
             ['Tezkor tekshiruv', 'Oflayn tekshiruv', 'Tanlangan tekshiruv', 'Fon tekshiruvi'], 'b'),
            ('O‘zini antivirusdan yashiradigan zararli dastur:',
             ['Rootkit', 'Antispam', 'Firewall', 'Drayver'], 'a'),
            ('Antivirus yangi o‘rnatilganda o‘tkaziladigan tekshiruv:',
             ['Faqat fleshka tekshiruvi', 'Tekshiruv kerak emas', 'To‘liq tekshiruv', 'Faqat tezkor'], 'c'),
            ('PowerShell’da tezkor tekshiruvni boshlovchi buyruq:',
             ['Get-MpComputerStatus', 'Update-MpSignature', 'Stop-Computer', 'Start-MpScan -ScanType QuickScan'], 'd'),
            ('Defender aniqlagan tahdidlar qayerda ko‘rinadi?',
             ['«Журнал защиты»', '«Корзина»', '«Загрузки»', '«Рабочий стол»'], 'a'),
        ],
        'mustaqil': ['Uy kompyuteringizda tezkor va to‘liq tekshiruv o‘tkazib, natijalarni jadvalga yozing.',
                     '«Планировщик заданий» orqali haftalik tekshiruv jadvalini yaratish tartibini o‘rganib, yozing.'],
    },
    # ------------------------------------------------------------------ 36
    {
        'type': 'N',
        'title': 'Ma’lumotlarni shifrlash va zaxiralash asoslari',
        'reja': ['Kriptografiya va shifrlash tushunchalari',
                 'Simmetrik va asimmetrik shifrlash',
                 'Ma’lumotlarni zaxiralash va «3-2-1» qoidasi'],
        'maqsad': 'O‘quvchilarga shifrlash, kalit, simmetrik va asimmetrik shifrlash tushunchalarini hamda ma’lumotlarni '
                  'zaxiralash usullari va qoidalarini tushuntirish.',
        'natija': 'O‘quvchilar shifrlash turlarini farqlaydi, oddiy shifrlash misolini bajaradi, zaxiralash turlarini '
                  'taqqoslaydi va «3-2-1» qoidasini qo‘llaydi.',
        'bolimlar': [
            """
## Shifrlash nima?
- **Kriptografiya** — axborotni begona shaxslar o‘qiy olmaydigan ko‘rinishga keltirish usullari haqidagi fan.
- **Shifrlash** — ochiq matnni maxsus algoritm va kalit yordamida tushunarsiz shifrmatnga aylantirish jarayoni.
- **Deshifrlash** — shifrmatnni kalit yordamida qayta ochiq matnga aylantirish.
- **Kalit** — shifrlash va deshifrlash uchun ishlatiladigan maxfiy qiymat.
## Sezar shifri
Eng qadimgi shifrlardan biri — Sezar shifri: har bir harf alifboda belgilangan songa suriladi. Kalit 3 bo‘lsa: A → D, B → E, C → F.
| Ochiq matn | K | O | D |
| Kalit = 3 | N | R | G |
«KOD» so‘zi «NRG» bo‘ladi. Bunday shifr bugun bir zumda buziladi, chunki atigi 25 ta kalit varianti bor. Zamonaviy AES algoritmida esa kalit variantlari soni shunchalik ko‘pki, barcha kompyuterlar birgalikda ham uni amalda topa olmaydi.
""",
            """
## Shifrlash turlari
| Turi | Kalitlar | Misollar | Qo‘llanishi |
| Simmetrik | Shifrlash va ochish uchun bitta umumiy kalit | AES, DES | Disk va fayllarni shifrlash, Wi-Fi |
| Asimmetrik | Ochiq kalit (shifrlash) va yopiq kalit (ochish) juftligi | RSA, ECC | HTTPS, elektron raqamli imzo, xavfsiz pochta |
- **Simmetrik shifrlash** — ma’lumotni shifrlash va deshifrlash uchun bitta kalitdan foydalaniladigan usul.
- **Asimmetrik shifrlash** — ochiq va yopiq kalitlar juftligidan foydalaniladigan usul: ochiq kalit bilan shifrlangan ma’lumotni faqat yopiq kalit egasi ocha oladi.
- **Elektron raqamli imzo** — hujjat muallifini va o‘zgartirilmaganini tasdiqlovchi, yopiq kalit yordamida yaratiladigan elektron rekvizit.
Asimmetrik shifrlashni pochta qutisiga o‘xshatish mumkin: xat tashlash uchun teshik hammaga ochiq (ochiq kalit), qutini ochish kaliti esa faqat egasida (yopiq kalit).
""",
            """
## Zaxiralash
- **Zaxira nusxa** — asl ma’lumot yo‘qolgan yoki buzilgan holda tiklash uchun alohida joyda saqlanadigan nusxa.
| Zaxiralash turi | Nima nusxalanadi | Afzalligi |
| To‘liq | Barcha tanlangan ma’lumotlar | Tiklash oson, ko‘p joy egallaydi |
| Qo‘shimcha (inkremental) | Oxirgi zaxiradan keyin o‘zgargan fayllar | Tez va kam joy egallaydi |
| Differensial | Oxirgi to‘liq zaxiradan keyin o‘zgargan fayllar | Tiklash inkrementaldan tezroq |
## «3-2-1» qoidasi
- **3** — ma’lumotning kamida 3 ta nusxasi bo‘lsin (asl + 2 ta zaxira).
- **2** — nusxalar kamida 2 xil turdagi tashuvchida saqlansin (masalan, tashqi disk va bulut).
- **1** — bitta nusxa boshqa joyda (ofisdan tashqarida yoki bulutda) saqlansin.
Zaxira nusxadan tiklash vaqti-vaqti bilan sinab ko‘riladi — tiklab bo‘lmaydigan zaxira foydasiz. Zaxira disk doimiy ulanib turmasligi kerak, aks holda shifrlovchi virus uni ham shifrlaydi.
""",
        ],
        'oldingi': ['Qanday antivirus tekshiruv turlari bor?',
                    'Karantin nima?',
                    'Rootkit qanday aniqlanadi?'],
        'savollar': ['Shifrlash va deshifrlash nima?',
                     'Sezar shifri qanday ishlaydi va nima uchun ishonchsiz?',
                     'Simmetrik va asimmetrik shifrlashning farqi nimada?',
                     'Zaxiralashning qanday turlari bor?',
                     '«3-2-1» qoidasini tushuntiring.'],
        'testlar': [
            ('Shifrlash va ochish uchun bitta kalit ishlatiladigan usul:',
             ['Asimmetrik', 'Simmetrik', 'Xeshlash', 'Kodlash'], 'b'),
            ('Sezar shifrida kalit 3 bo‘lsa, «A» harfi qaysi harfga aylanadi?',
             ['D', 'C', 'B', 'E'], 'a'),
            ('HTTPS va elektron raqamli imzoda ishlatiladigan asimmetrik algoritm:',
             ['DES', 'Sezar', 'RSA', 'ZIP'], 'c'),
            ('Oxirgi zaxiradan keyin o‘zgargan fayllargina nusxalanadigan zaxiralash:',
             ['To‘liq', 'Differensial', 'Arxiv', 'Qo‘shimcha (inkremental)'], 'd'),
            ('«3-2-1» qoidasidagi «1» nimani bildiradi?',
             ['Bitta nusxa boshqa joyda saqlanadi', 'Bitta disk yetarli', 'Bir yilda bir marta zaxiralanadi', 'Bitta parol'], 'a'),
        ],
        'mustaqil': ['Sezar shifri bilan ismingizni (kalit 5) shifrlang va o‘rtog‘ingizga ochish uchun bering.',
                     'Uydagi muhim fayllaringiz uchun «3-2-1» qoidasiga mos zaxiralash rejasini tuzing.'],
    },
    # ------------------------------------------------------------------ 37
    {
        'type': 'A',
        'title': 'Fayllarni shifrlash usullaridan foydalanish',
        'reja': ['Fayl va diskni shifrlash vositalari',
                 'Amaliy ish: 7-Zip parolli arxiv va BitLocker To Go bilan shifrlash',
                 'Fayllarni zaxiralash va zaxiradan tiklash'],
        'maqsad': 'O‘quvchilarda 7-Zip yordamida AES-256 shifrlangan arxiv yaratish, BitLocker To Go bilan fleshkani '
                  'shifrlash va Windows vositalari bilan fayllarni zaxiralab tiklash ko‘nikmasini shakllantirish.',
        'natija': 'O‘quvchilar parolli shifrlangan arxiv yaratadi va ochadi, fleshkani BitLocker bilan shifrlaydi, tiklash '
                  'kalitini saqlaydi, fayl tarixi orqali zaxira nusxadan faylni tiklaydi.',
        'vosita': 'Windows 10/11 Pro kompyuterlar, 7-Zip dasturi, fleshkalar, tashqi disk, proyektor',
        'bolimlar': [
            """
## Shifrlash vositalari
| Vosita | Nimani shifrlaydi | Xususiyati |
| 7-Zip (AES-256) | Alohida fayl va papkalar arxivini | Bepul, har qanday kompyuterda ochiladi |
| BitLocker | Butun diskni (C: yoki D:) | Windows Pro’da o‘rnatilgan |
| BitLocker To Go | Fleshka va tashqi diskni | Fleshka yo‘qolsa ham ma’lumot o‘qilmaydi |
| EFS | NTFS diskdagi alohida fayllarni | Faqat shu foydalanuvchi hisobiga bog‘langan |
| VeraCrypt | Disk yoki shifrlangan konteynerni | Bepul, ochiq kodli |
- **BitLocker** — Windows’ning butun diskni shifrlovchi o‘rnatilgan vositasi.
- **Tiklash kaliti** — BitLocker paroli unutilganda diskni ochish uchun beriladigan 48 xonali maxsus kod.
Muhim: shifrlash paroli va tiklash kaliti yo‘qolsa, ma’lumotlarni hech kim, hatto ishlab chiquvchi ham tiklay olmaydi.
""",
            """
## Ishni bajarish tartibi
- **Parolli arxiv.** «Hisobotlar» papkasi ustida o‘ng tugma → «7-Zip» → «Добавить к архиву». Format: 7z, shifrlash usuli: AES-256, kuchli parol kiriting, «Шифровать имена файлов» ni belgilang (bu belgi faqat 7z formatida bor).
- **Arxivni tekshirish.** Arxivni ochishga urinib ko‘ring — parol so‘ralishi kerak. Noto‘g‘ri parol bilan ochilmasligini sinang.
- **Fleshkani shifrlash.** Explorer’da fleshka ustida o‘ng tugma → «Включить BitLocker» → «Использовать пароль» → kuchli parol.
- **Tiklash kalitini saqlash.** «Сохранить в файл» ni tanlab, kalitni kompyuterdagi xavfsiz papkaga (fleshkaning o‘ziga emas!) saqlang yoki chop eting.
- **Shifrlashni yakunlash.** «Шифровать только занятое место» va «Режим совместимости» ni tanlang, jarayon tugashini kuting.
- **Tekshirish.** Fleshkani chiqarib qayta ulang — parol so‘ralishi kerak.
""",
            """
## Zaxiralash va tiklash
- **Fayl tarixini yoqish.** «Панель управления» → «История файлов» → tashqi diskni tanlab «Включить». Windows «Документы», «Рабочий стол» va boshqa papkalarni har soatda nusxalaydi.
- **Faylni o‘chirish.** Sinov uchun o‘quv faylini o‘zgartiring yoki o‘chiring.
- **Tiklash.** «История файлов» → «Восстановление личных файлов» → kerakli sanani tanlab, faylni yashil tugma bilan tiklang.
- **Robocopy bilan nusxa.** Buyruqlar satrida: `robocopy D:\\Hisobotlar E:\\Zaxira /MIR` — papkaning aniq nusxasi tashqi diskka yoziladi.
| Vazifa | Natija |
| AES-256 arxiv yaratildi va parol tekshirildi | ha / yo‘q |
| Fleshka BitLocker bilan shifrlandi | ha / yo‘q |
| Tiklash kaliti xavfsiz joyda saqlandi | ha / yo‘q |
| Fayl zaxiradan tiklandi | ha / yo‘q |
Mashg‘ulot oxirida o‘quv fleshkalardagi BitLocker o‘chiriladi («Отключить BitLocker»).
""",
        ],
        'oldingi': ['Simmetrik va asimmetrik shifrlash farqi nimada?',
                    '«3-2-1» qoidasi nima?',
                    'Zaxiralashning qanday turlari bor?'],
        'savollar': ['7-Zip’da shifrlangan arxiv qanday yaratiladi?',
                     'Nima uchun «Шифровать имена файлов» belgilanadi?',
                     'BitLocker tiklash kaliti nima va u qayerda saqlanadi?',
                     'Fayl tarixi qanday ishlaydi?',
                     'robocopy /MIR buyrug‘i nima qiladi?'],
        'testlar': [
            ('Fleshkani shifrlovchi Windows vositasi:',
             ['BitLocker To Go', 'Paint', 'Defrag', 'Disk Cleanup'], 'a'),
            ('7-Zip’da tavsiya etiladigan shifrlash usuli:',
             ['ZipCrypto', 'Sezar', 'AES-256', 'Base64'], 'c'),
            ('BitLocker tiklash kaliti necha xonali?',
             ['4', '48', '8', '12'], 'b'),
            ('Tiklash kalitini qayerda saqlash mumkin emas?',
             ['Chop etilgan qog‘ozda', 'Xavfsiz papkada', 'Microsoft hisobida', 'Shifrlangan fleshkaning o‘zida'], 'd'),
            ('Windows’da fayllarni muntazam avtomatik nusxalovchi vosita:',
             ['История файлов', 'Блокнот', 'Калькулятор', 'Ножницы'], 'a'),
        ],
        'mustaqil': ['VeraCrypt dasturida shifrlangan konteyner yaratish tartibini o‘rganib, qadamlarini yozing.',
                     'Telefoningizdagi rasmlarni bulutga avtomatik zaxiralash sozlamasini tekshiring va tavsifini yozing.'],
    },
    # ------------------------------------------------------------------ 38
    {
        'type': 'N',
        'title': 'Axborot xavfsizligini himoya qilish vositalari',
        'reja': ['Himoya vositalarining tasnifi',
                 'Dasturiy va apparat himoya vositalari',
                 'Tashkiliy va huquqiy himoya choralari'],
        'maqsad': 'O‘quvchilarga axborotni himoya qilish vositalarining tasnifi, dasturiy, apparat, fizik, tashkiliy va '
                  'huquqiy himoya vositalarini tushuntirish.',
        'natija': 'O‘quvchilar himoya vositalarini guruhlarga ajratadi, IDS, UPS, RAID kabi vositalar vazifasini '
                  'izohlaydi va tashkilot uchun himoya vositalari majmuini tanlaydi.',
        'bolimlar': [
            """
## Himoya vositalarining guruhlari
| Guruh | Misollar |
| Dasturiy | Antivirus, firewall, parol menejeri, shifrlash dasturlari, zaxiralash dasturlari |
| Apparat | Apparat firewall, USB-kalitlar, smart-kartalar, UPS, RAID kontroller |
| Fizik | Eshik qulflari, videokuzatuv, kirish tizimlari, server shkaflari, qo‘riqlash |
| Tashkiliy | Xavfsizlik siyosati, yo‘riqnomalar, xodimlarni o‘qitish, kirish huquqlarini taqsimlash |
| Huquqiy | Qonunlar, shartnomalar, maxfiylik majburiyatlari |
Himoya samarali bo‘lishi uchun barcha guruhlar birgalikda qo‘llaniladi — bu ko‘p qatlamli himoya tamoyilining amaldagi ko‘rinishi.
""",
            """
## Dasturiy va apparat vositalar
- **IDS** — tarmoq yoki kompyuterdagi shubhali harakatlarni aniqlab, administratorga xabar beruvchi hujumlarni aniqlash tizimi.
- **IPS** — shubhali harakatni aniqlabgina qolmay, uni avtomatik bloklaydigan hujumlarning oldini olish tizimi.
- **UPS** — elektr uzilganda kompyuter va serverlarni akkumulyator orqali vaqtincha quvvat bilan ta’minlovchi uzluksiz quvvat manbai.
- **RAID** — bir nechta diskni birlashtirib, bittasi buzilganda ham ma’lumotlarni saqlab qoluvchi texnologiya.
- **Apparat firewall** — tarmoq chegarasiga o‘rnatiladigan, butun ofis tarmog‘ini himoyalovchi alohida qurilma.
| RAID turi | Ishlash tamoyili | Ishonchlilik |
| RAID 0 | Ma’lumot disklarga bo‘lib yoziladi | Past — bitta disk buzilsa hammasi yo‘qoladi |
| RAID 1 | Ikki diskka bir xil nusxa (oyna) | Yuqori — bitta disk buzilsa ham ishlaydi |
| RAID 5 | Kamida 3 disk, nazorat ma’lumoti taqsimlanadi | Yuqori — bitta disk buzilishiga chidaydi |
RAID zaxira nusxa o‘rnini bosmaydi: fayl tasodifan o‘chirilsa yoki virus shifrlasa, u barcha disklarda bir vaqtda o‘chadi.
""",
            """
## Tashkiliy choralar
- Xodimlar ishga qabul qilinganda maxfiylik to‘g‘risidagi majburiyatni imzolaydi.
- Har bir xodimga faqat kerakli huquqlar beriladi va ular muntazam qayta ko‘rib chiqiladi.
- Xavfsizlik bo‘yicha mas’ul shaxs tayinlanadi.
- Xodimlar yiliga kamida bir marta xavfsizlik bo‘yicha o‘qitiladi.
- Server xonasiga kirish jurnali yuritiladi.
## Huquqiy choralar
- **Maxfiylik to‘g‘risidagi kelishuv** — xodim yoki hamkor tashkilotning maxfiy ma’lumotlarini oshkor qilmaslik majburiyatini oladigan shartnoma.
Huquqiy choralar qonun buzilganda javobgarlikni belgilaydi va qo‘rqituvchi ta’sir ko‘rsatadi. Keyingi mavzularda O‘zbekistonning axborot xavfsizligiga oid qonunlari bilan batafsil tanishamiz.
""",
        ],
        'oldingi': ['7-Zip’da shifrlangan arxiv qanday yaratiladi?',
                    'BitLocker tiklash kaliti nima?',
                    'Fayl tarixi qanday ishlaydi?'],
        'savollar': ['Himoya vositalari qanday guruhlarga bo‘linadi?',
                     'IDS va IPS farqi nimada?',
                     'UPS qanday vazifani bajaradi?',
                     'Nima uchun RAID zaxira nusxa o‘rnini bosmaydi?',
                     'Qanday tashkiliy himoya choralarini bilasiz?'],
        'testlar': [
            ('Shubhali harakatni aniqlab, avtomatik bloklaydigan tizim:',
             ['IDS', 'IPS', 'DNS', 'DHCP'], 'b'),
            ('Elektr uzilganda vaqtincha quvvat beruvchi qurilma:',
             ['UPS', 'Router', 'Skaner', 'Kommutator'], 'a'),
            ('Ikki diskka bir xil nusxa yoziladigan RAID turi:',
             ['RAID 0', 'RAID 5', 'RAID 1', 'RAID 10'], 'c'),
            ('Videokuzatuv va eshik qulflari qaysi guruhga kiradi?',
             ['Dasturiy', 'Huquqiy', 'Tashkiliy', 'Fizik'], 'd'),
            ('Xodimlarni xavfsizlik bo‘yicha o‘qitish qanday chora?',
             ['Tashkiliy', 'Apparat', 'Fizik', 'Dasturiy'], 'a'),
        ],
        'mustaqil': ['Texnikum uchun himoya vositalari majmuini 5 ta guruh bo‘yicha jadval ko‘rinishida tanlang.',
                     'UPS tanlash mezonlari (quvvat, ishlash vaqti, turi) haqida qisqa ma’lumot tayyorlang.'],
    },
    # ------------------------------------------------------------------ 39
    {
        'type': 'A',
        'title': 'Kompyuterning himoya vositalarini tekshirish',
        'reja': ['Kompyuterning himoya vositalari ro‘yxati',
                 'Amaliy ish: himoya vositalarini kompleks tekshirish',
                 'Tekshiruv hisobotini tuzish'],
        'maqsad': 'O‘quvchilarda kompyuterdagi barcha himoya vositalari — antivirus, firewall, yangilanishlar, BitLocker, '
                  'Secure Boot, UAC va zaxiralash holatini kompleks tekshirish va hisobot tuzish ko‘nikmasini shakllantirish.',
        'natija': 'O‘quvchilar Windows vositalari va buyruqlar yordamida himoya holatini tekshiradi, kamchiliklarni aniqlaydi '
                  'va xulosa hamda tavsiyalar bilan hisobot tuzadi.',
        'vosita': 'Windows 10/11 kompyuterlar, PowerShell, nazorat varag‘i shakli, proyektor',
        'bolimlar': [
            """
## Tekshiriladigan vositalar
| Vosita | Vazifasi |
| Antivirus | Zararli dasturlardan himoya |
| Firewall | Tarmoq ulanishlarini nazorat qilish |
| Windows Update | Zaifliklarni yopuvchi yangilanishlar |
| UAC | Tizim o‘zgarishlariga ruxsat so‘rash |
| BitLocker | Disk shifrlash |
| Secure Boot | Yuklanishda zararli dasturlarni bloklash |
| TPM | Shifrlash kalitlarini xavfsiz saqlovchi chip |
| Zaxiralash | Ma’lumotlarni tiklash imkoniyati |
- **Secure Boot** — kompyuter yoqilganda faqat ishonchli, raqamli imzolangan yuklovchi dasturlarni ishga tushiruvchi UEFI funksiyasi.
- **TPM** — ona platadagi kriptografik chip bo‘lib, shifrlash kalitlarini xavfsiz saqlaydi va tizim butunligini tekshiradi.
""",
            """
## Ishni bajarish tartibi
- **Umumiy holat.** Windows Security bosh sahifasida barcha bo‘limlar yashil belgi bilan ko‘rsatilganini tekshiring.
- **Antivirus.** PowerShell’da `Get-MpComputerStatus` — «AntivirusEnabled» va «RealTimeProtectionEnabled» qiymati «True» bo‘lishi kerak.
- **Firewall.** `netsh advfirewall show allprofiles state` — barcha profillar «ON».
- **Yangilanishlar.** `Get-HotFix | Sort-Object InstalledOn -Descending | Select-Object -First 5` — oxirgi 5 ta yangilanish.
- **BitLocker.** Administrator sifatida `manage-bde -status` — disklarning shifrlash holati.
- **Secure Boot va TPM.** `Win + R` → `msinfo32` → «Состояние безопасной загрузки»; `tpm.msc` — TPM mavjudligi va holati.
- **UAC.** `UserAccountControlSettings` — slayder darajasini ko‘ring.
- **Zaxiralash.** «История файлов» yoqilganligini va oxirgi nusxa sanasini tekshiring.
""",
            """
## Hisobot shakli
| № | Vosita | Holat | Kamchilik | Tavsiya |
| 1 | Antivirus | Yoqilgan, baza 1 kun oldin yangilangan | — | — |
| 2 | Firewall | Ommaviy profilda o‘chirilgan | Bor | Yoqish |
| 3 | Yangilanishlar | Oxirgisi 3 oy oldin | Bor | Yangilanishlarni o‘rnatish |
| 4 | BitLocker | O‘chirilgan | Bor | Noutbukda yoqish |
| 5 | Secure Boot | Yoqilgan | — | — |
| 6 | Zaxiralash | Sozlanmagan | Bor | Fayl tarixini yoqish |
## Xulosa
Hisobot oxirida himoya darajasi baholanadi: 8 ta vositadan nechtasi to‘g‘ri ishlayotgani hisoblanadi. Kamchiliklar ustuvorlik bo‘yicha tartiblanadi: avval antivirus, firewall va yangilanishlar, keyin shifrlash va zaxiralash. Bu hisobot IT-servis mutaxassisining mijozga beradigan haqiqiy hujjatiga o‘xshaydi.
""",
        ],
        'oldingi': ['Himoya vositalarining qanday guruhlari bor?',
                    'IDS va IPS farqi nimada?',
                    'RAID 1 qanday ishlaydi?'],
        'savollar': ['Kompyuterda qanday himoya vositalari tekshiriladi?',
                     'Secure Boot qanday vazifani bajaradi?',
                     'TPM chipi nima uchun kerak?',
                     'BitLocker holatini qaysi buyruq ko‘rsatadi?',
                     'Kamchiliklar qanday tartibda bartaraf etiladi?'],
        'testlar': [
            ('Disklarning BitLocker shifrlash holatini ko‘rsatuvchi buyruq:',
             ['manage-bde -status', 'ping -t', 'ipconfig', 'tree'], 'a'),
            ('Faqat raqamli imzolangan yuklovchilarni ishga tushiruvchi UEFI funksiyasi:',
             ['Hibernation', 'Fast Startup', 'Secure Boot', 'Sleep mode'], 'c'),
            ('Shifrlash kalitlarini xavfsiz saqlovchi chip:',
             ['GPU', 'TPM', 'RAM', 'HDD'], 'b'),
            ('Oxirgi o‘rnatilgan yangilanishlar ro‘yxatini chiqaruvchi PowerShell buyrug‘i:',
             ['Get-Date', 'Get-Help', 'Get-Location', 'Get-HotFix'], 'd'),
            ('Tizim ma’lumotlari oynasini ochuvchi buyruq:',
             ['msinfo32', 'notepad', 'mspaint', 'charmap'], 'a'),
        ],
        'mustaqil': ['Uy kompyuteringizda kompleks tekshiruv o‘tkazib, hisobot shakli bo‘yicha natijani yozing.',
                     'Barcha tekshiruv buyruqlarini bitta PowerShell skript fayliga (.ps1) yozish rejasini tuzing.'],
    },
    # ------------------------------------------------------------------ 40
    {
        'type': 'N',
        'title': 'Axborot xavfsizligiga oid qonunchilik asoslari',
        'reja': ['O‘zbekistonning axborot sohasidagi asosiy qonunlari',
                 'Kiberxavfsizlik to‘g‘risidagi qonun va vakolatli organlar',
                 'Axborot texnologiyalari sohasidagi huquqbuzarliklar uchun javobgarlik'],
        'maqsad': 'O‘quvchilarga O‘zbekistonda axborot xavfsizligi sohasini tartibga soluvchi asosiy qonunlar, vakolatli '
                  'organlar va huquqbuzarliklar uchun javobgarlik turlarini tushuntirish.',
        'natija': 'O‘quvchilar asosiy qonunlarni va ularning maqsadini sanaydi, kiberxavfsizlik sohasidagi vakolatli '
                  'organlarni biladi va kiberjinoyatlar uchun javobgarlik turlarini izohlaydi.',
        'bolimlar': [
            """
## Asosiy qonunlar
| Qonun | Qabul qilingan | Tartibga soladigan soha |
| «Axborotlashtirish to‘g‘risida»gi Qonun | 2003-yil, 11-dekabr | Axborot resurslari va tizimlari, axborotni himoya qilish |
| «Mualliflik huquqi va turdosh huquqlar to‘g‘risida»gi Qonun | 2006-yil, 20-iyul | Asarlar, jumladan kompyuter dasturlari mualliflik huquqi |
| «Elektron raqamli imzo to‘g‘risida»gi Qonun | 2003-yil (yangi tahriri — 2022-yil) | Elektron hujjatlar va raqamli imzo |
| «Shaxsga doir ma’lumotlar to‘g‘risida»gi Qonun | 2019-yil, 2-iyul | Shaxsiy ma’lumotlarni yig‘ish va himoya qilish |
| «Kiberxavfsizlik to‘g‘risida»gi Qonun | 2022-yil, 15-aprel | Kibermakonda shaxs, jamiyat va davlat himoyasi |
Qonunlarning rasmiy matni qonunchilik ma’lumotlari milliy bazasi — lex.uz saytida joylashgan. Qonunlarga o‘zgartirishlar kiritilishi mumkin, shuning uchun doim amaldagi tahriri o‘qiladi.
""",
            """
## Kiberxavfsizlik to‘g‘risidagi qonun
Qonun kiberxavfsizlik sohasidagi asosiy tushunchalar, davlat organlarining vakolatlari, muhim axborot infratuzilmasi obyektlarini himoya qilish va kiberhodisalarga javob berish tartibini belgilaydi.
- **Kiberhodisa** — axborot tizimlari ishining buzilishiga yoki ulardagi axborotning maxfiyligi, yaxlitligi va foydalanuvchanligi buzilishiga olib kelgan voqea.
- **Muhim axborot infratuzilmasi** — ishdan chiqishi davlat boshqaruvi, mudofaa, iqtisodiyot yoki aholi hayotiga jiddiy zarar yetkazishi mumkin bo‘lgan axborot tizimlari (energetika, transport, bank tizimi va boshqalar).
- **Kiberxavfsizlik subyekti** — kibermakonda faoliyat yurituvchi davlat organlari, tashkilotlar va fuqarolar.
## Vakolatli tashkilotlar
- **Kiberxavfsizlik markazi** (csec.uz) — kiberhodisalarni monitoring qiladi, tavsiyalar beradi va hodisalarga javob berishda yordam ko‘rsatadi.
- **UZCERT** (uzcert.uz) — kompyuter hodisalariga javob berish xizmati: zaifliklar va tahdidlar haqida ogohlantirishlar e’lon qiladi.
Fuqaro yoki tashkilot kiberhodisaga duch kelsa, bu tashkilotlarga, firibgarlik holatida esa ichki ishlar organlariga murojaat qiladi.
""",
            """
## Javobgarlik turlari
| Javobgarlik turi | Qachon qo‘llaniladi | Misol |
| Intizomiy | Ish joyida ichki qoidalarni buzish | Xodim parolini hamkasbiga bergani uchun hayfsan |
| Ma’muriy | Kichik huquqbuzarliklar | Shaxsga doir ma’lumotlar to‘g‘risidagi qonunchilikni buzganlik uchun jarima |
| Fuqaroviy | Zarar yetkazilganda | Mualliflik huquqi buzilgani uchun zararni qoplash |
| Jinoiy | Og‘ir huquqbuzarliklar | Kompyuter tizimiga ruxsatsiz kirish, zararli dastur yaratish va tarqatish |
O‘zbekiston Respublikasi Jinoyat kodeksida axborot texnologiyalari sohasidagi jinoyatlar uchun alohida bob mavjud. Unda kompyuter axborotidan qonunga xilof foydalanish, unga ruxsatsiz kirish, axborotni o‘zgartirish va zararli dasturlar yaratish hamda tarqatish uchun jazo belgilangan.
- **Kiberjinoyat** — kompyuter, tarmoq yoki axborot texnologiyalari yordamida yoki ularga qarshi sodir etiladigan, qonunda jinoyat deb belgilangan qilmish.
«Qiziqish uchun» birovning hisobini buzish yoki «hazil» virus tarqatish ham jinoyat hisoblanadi.
""",
        ],
        'oldingi': ['Kompyuterning qanday himoya vositalarini tekshirdik?',
                    'Secure Boot nima?',
                    'Tashkiliy himoya choralariga misol keltiring.'],
        'savollar': ['O‘zbekistonning axborot sohasidagi qanday qonunlarini bilasiz?',
                     '«Kiberxavfsizlik to‘g‘risida»gi Qonun nimalarni belgilaydi?',
                     'Muhim axborot infratuzilmasiga misollar keltiring.',
                     'Kiberxavfsizlik markazi va UZCERT qanday vazifalarni bajaradi?',
                     'Axborot sohasidagi huquqbuzarliklar uchun qanday javobgarlik turlari bor?'],
        'testlar': [
            ('«Axborotlashtirish to‘g‘risida»gi Qonun qachon qabul qilingan?',
             ['2003-yilda', '2019-yilda', '2022-yilda', '1995-yilda'], 'a'),
            ('Qonunlarning rasmiy matni joylashgan sayt:',
             ['olx.uz', 'lex.uz', 'youtube.com', 'kun.uz'], 'b'),
            ('Ishdan chiqishi davlat va aholiga jiddiy zarar yetkazadigan tizimlar:',
             ['O‘yin serverlari', 'Shaxsiy bloglar', 'Muhim axborot infratuzilmasi', 'Ijtimoiy tarmoq profillari'], 'c'),
            ('Zararli dastur yaratish va tarqatish qanday javobgarlikka sabab bo‘ladi?',
             ['Intizomiy', 'Hech qanday', 'Faqat og‘zaki ogohlantirish', 'Jinoiy'], 'd'),
            ('Kompyuter hodisalariga javob berish xizmati:',
             ['UZCERT', 'UzAuto', 'Uzbektourism', 'UzReport'], 'a'),
        ],
        'mustaqil': ['lex.uz saytidan «Kiberxavfsizlik to‘g‘risida»gi Qonunni topib, 5 ta asosiy tushunchaning ta’rifini yozing.',
                     'Axborot sohasidagi qonunlar bo‘yicha xronologik lenta (timeline) chizing.'],
    },
]
