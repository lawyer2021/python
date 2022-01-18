# 4. Реализуйте базовый класс Car.
# у класса должны быть следующие атрибуты: speed, color, name, is_police(булево).
# А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась,
# повернула (куда); опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
# добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля;
# для классов TownCar и WorkCar переопределите метод show_speed.
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar)
# должно выводиться сообщение о превышении скорости.
#
# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
# Вызовите методы и покажите результат.

class Car:
    speed = 68
    color = "Белый"
    name = "Lincoln"
    is_police = False

    def go(self):
        print("Машина поехала")

    def stop(self):
        print("Машина остановилась")

    def turn(self, direction):
        print(f"Машина повернула {direction}")

    def show_speed(self, speed=None):
        if speed is not None:
            print(f"Скорость машины: {speed}")
        else:
            print(f"Скорость машины: {Car.speed}")


class TownCar(Car):
    name = "MAN"
    color = "Желтый"

    def show_speed(self, speed):
        if speed > 60:
            print(f"Превышение скорости на {speed - 60} км/ч")
        else:
            print(f"Скорость машины: {self.speed} км/ч")


class SportCar(Car):
    name = "Ferrari"
    color = "Синий"


class WorkCar(Car):
    name = "Lada"
    color = "Баклажан"

    def show_speed(self, speed):
        if speed > 40:
            print(f"Превышение скорости на {speed - 40} км/ч")
        else:
            print(f"Скорость машины: {self.speed} км/ч")


class PoliceCar(Car):
    is_police = True

    def show_speed(self, speed):
        print(f"Скорость машины: {speed} км/ч")


a = TownCar()
print(a.name)
print(a.color)
a.go()
a.stop()
a.turn("влево")
a.show_speed(90)
print(a.is_police)
print("\n")

b = PoliceCar()
print(b.name)
print(b.color)
b.go()
b.stop()
b.turn("вправо")
b.show_speed(250)
print(b.is_police)
print("\n")

с = WorkCar()
print(с.name)
print(с.color)
с.go()
с.stop()
с.turn("назад")
с.show_speed(42)
print(с.is_police)
print("\n")

d = SportCar()
d.go()
d.show_speed()
