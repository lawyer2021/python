# 7. Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число».
# Реализуйте перегрузку методов сложения и умножения комплексных чисел. Проверьте работу проекта.
# Для этого создаёте экземпляры класса (комплексные числа), выполните сложение и умножение созданных экземпляров.
# Проверьте корректность полученного результата.

class Complex:
    def __init__(self, num):
        self.num = num

    def __add__(self, other):
        return Complex(self.num + other.num)

    def __mul__(self, other):
        return Complex(self.num * other.num)

    def __str__(self):
        return f"Результат: {self.num}"


a = Complex(1 + 2j)
b = Complex(2 + 4j)
print(a + b)
print(a * b)
