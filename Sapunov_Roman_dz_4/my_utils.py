from requests import get, utils

response = get("http://www.cbr.ru/scripts/XML_daily.asp")
encodings = utils.get_encoding_from_headers(response.headers)
content = response.content.decode(encoding=encodings)


def currency_rates_adv(charcode):
    lst_cont = content.split("ID")
    for i in lst_cont:
        if i.count(charcode.upper()):
            _course = i[(int(str(i.find("<Value>"))) + 7):(int(str(i.find("</Value>"))))]
            course = float(_course.replace(",", "."))
            return course
