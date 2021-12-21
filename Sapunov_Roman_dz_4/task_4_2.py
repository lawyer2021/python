import datetime
from requests import get, utils

response = get("http://www.cbr.ru/scripts/XML_daily.asp")
print("Cегодня: ", datetime.date.today())
encodings = utils.get_encoding_from_headers(response.headers)
content = response.content.decode(encoding=encodings)


def currency_rates(CharCode):
    lstcont = content.split("ID")
    for i in lstcont:
        if i.count(CharCode.upper()):
            _course = i[(int(str(i.find("<Value>"))) + 7):(int(str(i.find("</Value>"))))]
            course = float(_course.replace(",", "."))
            return course


print("Курс ЕВРО к рублю: ", currency_rates("eur"))
print("Курс доллара США к рублю: ", currency_rates("USD"))
