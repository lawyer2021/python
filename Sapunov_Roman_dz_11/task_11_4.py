# 4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад.
# А также класс «Оргтехника», который будет базовым для классов-наследников.
# Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
# В базовом классе определите параметры, общие для приведённых типов.
# В классах-наследниках реализуйте параметры, уникальные для каждого типа оргтехники.


### Склад оргтехники ###

class Warehouse:
    def __init__(self):
        self.dict = {}

    def add_item(self, equipment):
        self.dict.setdefault(equipment.name, []).append(
            f'Тип: {equipment.group}, Серийный номер: {equipment.serial}, Год выпуска: {equipment.year} ')

    def ext_item(self, name):
        if self.dict[name]:
            self.dict.setdefault(name).pop(0)


class Equipment:
    def __init__(self, name, serial, year):
        self.name = name
        self.serial = serial
        self.year = year
        self.group = self.__class__.__name__

    def group_name(self):
        return f'{self.group}'

    def __str__(self):
        return f"Наименование: {self.name}, Серийный номер: {self.serial}, Год выпуска: {self.year}"


class Printers(Equipment):
    def __init__(self, name, serial, year):
        super().__init__(name, serial, year)

    def __str__(self):
        return f"Наименование: {self.name}, Серийный номер: {self.serial}, Год выпуска: {self.year}"

    def action(self):
        return "Печатает"


class Scanner(Equipment):
    def __init__(self, name, serial, year):
        super().__init__(name, serial, year)

    def __str__(self):
        return f"Наименование: {self.name}, Серийный номер: {self.serial}, Год выпуска: {self.year}"

    def action(self):
        return "Сканирует"


class Xerox(Equipment):
    def __init__(self, name, serial, year):
        super().__init__(name, serial, year)

    def __str__(self):
        return f"Наименование: {self.name}, Серийный номер: {self.serial}, Год выпуска: {self.year}"

    def action(self):
        return "Копирует"


warehouse = Warehouse()
scaner = Scanner("HP", 2354, 2020)
warehouse.add_item(scaner)
print(scaner)
scaner = Scanner("Samsung", 15156, 2022)
warehouse.add_item(scaner)
printer = Printers("Brothers", 4516, 2000)
warehouse.add_item(printer)
print(warehouse.dict)
print(scaner)
print(scaner.action())
print(printer.action())
