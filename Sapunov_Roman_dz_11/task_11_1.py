# 1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
# В рамках класса реализовать два метода. Первый, с декоратором @classmethod.
# Он должен извлекать число, месяц, год и преобразовывать их тип к типу «Число».
# Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
# Проверить работу полученной структуры на реальных данных.

class Date:
    def __init__(self, my_date):
        self.my_date = my_date

    @classmethod
    def date_split(cls, my_date):
        print(f'Дата: {(int(my_date.split("-")[0]))}')
        print(f'Месяц: {(int(my_date.split("-")[1]))}')
        print(f'Год: {(int(my_date.split("-")[2]))}')

    @staticmethod
    def is_wright_date(my_date):
        if int(my_date.split("-")[0]) <= 31 and int(my_date.split("-")[1]) <= 12:
            return True
        else:
            print("Неверный формат данных")
            return False


a = Date("12-12-2021")
print(a.is_wright_date("12-12-2021"))
print(a.date_split("12-12-2022"))
