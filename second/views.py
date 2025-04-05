from django.shortcuts import render
from django.http import HttpResponse

def first(request):
    html="""
<h1>First View page</h1>
<h2>Welcome to the first view page of the second app.</h2>
<a href='/second/'>Second View >></a> <br>

<a href='pages/Kampyuterlar'>Computers >></a> <br>
<a href='pages/Telefonlar'>Phones >></a>
"""
    return HttpResponse(html)


def second(request):
    return HttpResponse("<h1>First View page</h1>"
                        "<h2>Second view page of the second app.</h2>"
                        "<a href='/../'><< First View</a>")


def pages(request, page):
    if page == 'Kampyuterlar':
        return HttpResponse(f"<h1>Page {page}</h1>"
                            f"<h2>Bo'lim - {page}</h2>"
                            """<p>
Kompyuter (inglizcha: computer – ,,kodlar bilan ishlamayman'') – oldindan berilgan dastur boʻyicha ishlaydigan avtomatik qurilma. Elektron hisoblash mashinasi (EHM) bilan bir xildagi atama. Biroq, kompyuter hisoblash ishlarini bajarishdan tashqari uning funksiyasi ancha keng. EHMlarning rivojlanishida kompyuterning bir necha avlodlarini koʻrsatish mumkin. Bu avlodlar element turlari, konstruktiv-texnologik xususiyatlari, mantiqiy tuzilishi, dastur taʼminoti, texnik tafsilotlari, texnikadan foydalanishning qulaylik darajasi bilan bir-biridan farq qiladi. Kompyuterning dastlabki avlodida (Ural-1, Minsk-2, BSEM-2) asosiy element elektron lampa boʻlgani uchun u juda katta joyni egallagan edi. Soʻngra bu lampa oʻrnida tranzistorlar ishlatilgan kompyuter (Razdan-2, M-220, Minsk-22 va boshqalar), integral mikrosxemalar ishlatilgan kompyuter (IBM-360, 1BM-370, (AQSh), YESEVM (Rossiya) va boshqalar, integratsiya darajasi katta boʻlgan integral sxemalar oʻrnatilgan shaxsiy kompyuterlar paydo boʻldi. Shaxsiy kompyuter (mikro va mikro EHM) tushunchasi XX asr 70-yillar oxiridan boshlab keng tarqala boshladi. Shaxsiy kompyuterning keyingi avlodlarida mikroelektron va biosxemalardan foydalanildi; ularning hajmi kitob kattaligidek hajmga kichraydi, massasi esa 3,5 kg gacha kamaydi. 1981-yil IBM shirkati shaxsiy kompyuterning yanada takomillashgan modellarini ishlab chiqara boshladi. Keyinchalik boshqa firmalar IBM bilan PC biriktirilgan kompyuterni, Apple shirkati esa Macintosh (talaffuzi: „Makintosh“) yoki oddiygina „maki“ deb ataladigan kompyuterni yaratishdi. XXI asr boshlarida dunyoda oʻnlab million shaxsiy kompyuterlar, 1 millionga yaqin EHM (shu jumladan, bir necha oʻn superEVM) boʻlgan. Kompyuterlar masalalarni yechishda foydalaniladigan komponentlar (tarkibiy qismlar) tarkibi va tavsifi jihatdan bir-biridan farq qiladi. Murakkab masalalarni yechishda kuchli qurilmalar oʻrnatilgan kompyuterdan, hujjatlarni bosishda harf bosish qurilmasi boʻlgan kompyuterdan foydalaniladi. Istalgan kompyuter tizimlar bloki, monitor va klaviaturadan iborat boʻladi. Kerak boʻlganda boʻlardan tashqari boshqa qurilmalar ham ulanadi. Tizimlar blokida kompyuterning ishlashi uchun zarur muhim qismlar (diskni yuritkich, vinchester – qattiq disk, mantiqiy amallarni bajaruvchi mikrosxemalar) boʻlib, unga qolgan qurilmalar ulanadi. Monitor (displey) matn va turli tasvir koʻrinishidagi axborotlarni ekranda aks ettiradi. Klaviatura kompyuterga buyruq va turli axborotlarni kiritadi. Koʻpincha, kompyuter tarkibiga „sichqoncha“ manipulyatori va printer kiritiladi. „Sichqoncha“ ikki yoki uchta knopkasi (tugmasi) boʻlgan qurilma boʻlib, uning yordamida kompyuter ishi osonlashtiriladi. Printer esa axborotlarni qogʻozga tushirish uchun xizmat qiladi. Zamonaviy kompyuterlar, asosan, toʻrt qurilma: boshqarish, protsessor, xotira va kiritish-chiqarish qurilmalaridan iborat. Boshqarish qurilmasi kompyuterning barcha qurilmalari ishini muvofiqlashtiradi va boshqaradi. Protsessor kompyuterning asosiy qurilmasi boʻlib, axborotlarga ishlov beradi, yaʼni hisoblash amallari, solishtirish va uzatish kabi arifmetik-mantiqiy amallarni bajaradi. Bu qurilma bajaradigan amallar dasturlar orqali belgilanadi. Xotira qurilmasi axborotlarga ishlov berish vaqtida uni saqlash uchun xizmat qiladi. Foydalanayotgan dasturlar ichki xotirada, uzoq, muddat saqlanadigan axborotlar tashqi xotira (disketalar)da saqlanadi. Ichki va tashqi xotiralarda axborot almashinuvi kiritish-chiqarish qurilmalari yordamida amalga oshiriladi.
</p>"""
                            "<a href='/../'><< main page</a>")
    elif page == 'Telefonlar':
        return HttpResponse(f"<h1>Page {page}</h1>"
                            f"<h2>Bo'lim - {page}</h2>"
                            """<p>Telefon — tovush uzatish va qabul qilish uchun moʻljallangan telekommunikatsiyalar qurilmasidir. Odatda, tovushning mexanik energiyasini elektrik signallar energiyasiga aylantirish, masofadan uzatish va uni qaytadan tovushga aylantirish prinsipi bilan ishlaydi.

Telefon (tele... olis va fon un = olisun) — 1) elektr signallarini tovush signallariga aylantirib beradigan elektrakustik asbob. Elektromagnitli, elektrodinamik va pyezoelektr turlariga bo'linadi. Elektromagnitli T. eng keng tarqalgan bo`lib, uning asosiy elementlari doimiy magnit, chulgʻamli qutblar va membranadan iborat. Abonent "telefon qilganida" T. signalining oʻzgaruvchan elektr toki taʼsirida membrana tebranib, tovush hosil qiladi. T. telefon apparati, turli radiotexnika asboblari va boshqa qurilmalarda ishlatiladi; 2) telefon apparatining qisqa nomi; 3) telefon aloqasining qisqa nomi.
</p>"""
                            "<a href='/../'><< main page</a>")
    else:
        return HttpResponse(f"<h1>Page {page}</h1>"
                            f"<h2>Bo'lim - {page}</h2>"
                            "<a href='/../'><< First View</a>")
