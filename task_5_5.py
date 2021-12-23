# 5. Подумайте, как можно сделать оптимизацию кода по памяти, по скорости.
# Представлен список чисел. Определить элементы списка, не имеющие повторений. Сформировать из этих элементов список с сохранением порядка их следования в исходном списке, например:
# src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
# result = [23, 1, 3, 10, 4, 11]
# Подсказка: напишите сначала решение «в лоб». Потом подумайте об оптимизации.

from time import perf_counter
import sys
import random

# генерируем случайный список для сравнения работы кодов по памяти и по скорости при разных параметрах списка
nums = []
for i in range(0, 1000):
    nums.append(random.randint(1, 10 * 10000))
if len(nums) < 15:
    print("ИЗНАЧАЛЬНЫЙ СПИСОК: ", nums)

# Данный вариант выигрывает по памяти в разы:
start = perf_counter()
result = [n for n in nums if nums.count(n) == 1]
if len(result) < 20:
    print("результат по порядку LIST: ", result)
print(perf_counter() - start, "размер: ", sys.getsizeof(result))

# Данный вариант выигрывает по скорости:
start = perf_counter()
uniq_nums = set()
tmp = set()
uniq_nums_ord = [el for el in uniq_nums if
                 el in uniq_nums]  # вывод элементов в той же последовательности, как они встречаются в исходном списке
for n in nums:
    if n not in tmp:
        uniq_nums.add(n)
        uniq_nums_ord.append(n)
    else:
        uniq_nums.discard(n)
    tmp.add(n)
if len(result) < 20:
    print("результат по порядку SET: ", uniq_nums_ord)
print(perf_counter() - start, "размер: ", sys.getsizeof(uniq_nums))
