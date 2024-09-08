from django.shortcuts import HttpResponse

def book_list(request):
    response = """
        <h1>Kitoblar ro'yhati</h1>
        <a href="/book/1">
            <ul>
                <li>Ikki eshik orasi</li>
            </ul>
        </a>
        <a href="/book/2">
            <ul>
                <li>Yulduzli tunlar</li>
            </ul>
        </a>
        <a href="/book/3">
            <ul>
                <li>Xamsa</li>
            </ul>
        </a>
    """
    return HttpResponse(response)

def book_list2(request):
    response = """
        <h1>Ikki eshik orasi</h1>
        <h4>Author:</h4>
        <p>O'tkir Hoshimov</p>
        <p>Asarda insonlar taqdiri va inson umrining murakkabligini mahorat bilan tasvirlangan. Adib, birinchi navbatda, tinchlikka rahna solgan urushni tilga oladi. Ayniqsa, urush voqeligining har bir ota-ona qalbini jarohatlagani, koʻngillariga ozor yetkazgani romanning umuminsoniy pafosini tashkil etadi. Adib qalamga olgan obrazlari oddiy odamlarning fazilatlari – mardligi, matonati, vatanparvarligi va sabr-bardoshi haqida soʻzlaydi. Tajribali yozuvchi roman hodisalarini teran oʻrgangani uchun har bir epizod oʻquvchini qalbiga jiddiy taʼsir qiladi. Asarda tasvirlangan hayot manzaralari, insonlararo munosabatlar shuningdek, yozuvchining oʻziga xos badiiy uslubi juda tabiiy hamda samimiyligi bilan ajralib turadi. Yetti qism, qirq yetti bobdan tarkib topgan roman kompozitsion qurilishi jihatidan ham oʻziga xosligi bilan ajralib turadi[2]. Undagi voqea-hodisalar bayonida qatnashgan toʻqqizta personaj hikoyalarini adib bir-biriga ustalik bilan bogʻlagan.</p>
        <a href="../">Back to list</a>
    """
    return HttpResponse(response)
def book_list3(request):
    response = """
        <h1>Yulduzli tunlar</h1>
        <h4>Author:</h4>
        <p>Pirimqul Qodirov</p>
        <p>„Yulduzli tunlar“ – oʻzbek yozuvchisi Pirimqul Qodirov qalamiga mansub tarixiy roman. Asarda Zahiriddin Muhammad Bobur hayoti haqida soʻz yuritiladi. Qodirov mazkur roman ustida oʻn yil (1969—1978) davomida ish olib borgan[1]. „Yulduzli tunlar“ga „Boburnoma“ hamda „Humoyunnoma“ asarlari asosiy manba boʻlib xizmat qilgan.
            „Yulduzli tunlar“ zamonaviy oʻzbek adabiyotining eng sara asarlaridan biri hisoblanadi[2].</p>
        <a href="../">Back to list</a>
    """
    return HttpResponse(response)

def book_list4(request):
    response = """
        <h1>Xamsa</h1>
        <h4>Author:</h4><p>Alisher Navoiy</p>
        <p>"Xamsa" yozishni ozarbayjonlik ulugʻ shoir Nizomiy Ganjaviy boshlab bergan. U 1170–1204-yillar oraligʻida birin-ketin 5 ta doston yaratdi. Bu dostonlar shoirning vafotidan keyin yaxlit bir toʻplam holiga keltirilib „Panj ganj“ („Besh xazina“) deb nomlandi va keyinchalik „Xamsa“ nomi bilan mashhur boʻldi.
            Nizomiy beshligidagi birinchi doton „Maxzan ul-asror“ („Sirlar xazinasi“) 1180-yil gʻaznaviylar hukmdori Bahromshohga bagʻishlab yozilgan. „Maxzan ul-asror“ falsafiy-axloqiy masalalarga bagʻishlangan boʻlib, 18 bob, muqaddima va xotimadan iborat.</p>
        <a href="../">Back to list</a>
    """
    return HttpResponse(response)