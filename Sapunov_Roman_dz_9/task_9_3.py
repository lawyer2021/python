# 3. Реализовать базовый класс Worker (работник).
# определить атрибуты: name, surname, position (должность), income (доход);
# последний атрибут должен быть защищённым и ссылаться на словарь, содержащий элементы:
# оклад и премия, например, {"wage": wage, "bonus": bonus};
# создать класс Position (должность) на базе класса Worker;
# в классе Position реализовать методы получения полного имени сотрудника (get_full_name) и
# дохода с учётом премии (get_total_income);
# проверить работу примера на реальных данных: создать экземпляры класса Position, передать данные,
# проверить значения атрибутов, вызвать методы экземпляров.
class Worker:
    name = ""
    surname = ""
    position = ""
    _income = {}


class Position(Worker):
    def get_full_name(self, name, surname):
        Worker.name, Worker.surname = name, surname
        print(f"Работник: {Worker.name} {Worker.surname}")

    def get_total_income(self, wage, bonus):
        Worker._income["wage"], Worker._income["bonus"] = wage, bonus
        amount = Worker._income["bonus"] + Worker._income["wage"]
        print(f"Общий доход: {amount}")


a = Position()
a.get_full_name("Иван", "Иванов")
a.get_total_income(170, 10)

b = Position()
b.get_full_name("Сергей", "Петров")
a.get_total_income(200, 15)
