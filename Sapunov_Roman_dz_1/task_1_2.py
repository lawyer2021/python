numbers = range(1, 1001)
my_numbers = []

for number in numbers:
    if number % 2 != 0:
        cube = number ** 3
        my_numbers.append(cube)
print("Список, состоящий из кубов нечётных чисел от 1 до 1000: ", my_numbers)

for index in range(len(my_numbers)):
    my_numbers[index] += 17
print("Список, состоящий из кубов нечётных чисел от 1 до 1000, увеличенных на 17: ", my_numbers)

sum_numbers = 0
for cube in my_numbers:
    _sum_numbers = 0
    while cube != 0:
        _sum_numbers += cube % 10
        cube = cube // 10
    if _sum_numbers % 7 == 0:
        sum_numbers += _sum_numbers
print("Сумма чисел из списка, сумма цифр которых делится нацело на 7: ", sum_numbers)
