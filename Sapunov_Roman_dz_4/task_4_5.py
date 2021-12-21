from requests import get, utils
import my_utils

response = get("http://www.cbr.ru/scripts/XML_daily.asp")


def currency_rates(charcode):
    lst_cont = content.split("ID")
    for i in lst_cont:
        if i.count(charcode.upper()):
            _course = i[(int(str(i.find("<Value>"))) + 7):(int(str(i.find("</Value>"))))]
            course = float(_course.replace(",", "."))
            return course


def main(argv):
    code = argv[1:]
    for i in code:
        global charcode
        charcode = str(i)
        print(
            f"Курс валюты равен: {my_utils.currency_rates_adv(charcode)} рублей, дата: {response.headers.get('Date')}")


"""Uncomment this to use without terminal"""
# print(f"Курс валюты равен: {my_utils.currency_rates_adv(input('ВВЕДИТЕ КОД ВАЛЮТЫ: '))} рублей")

if __name__ == "__main__":
    import sys

    main(sys.argv)
