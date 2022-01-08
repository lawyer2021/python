# 4. Написать скрипт, который выводит статистику для заданной папки в виде словаря,
# в котором ключи — верхняя граница размера файла (пусть будет кратна 10),
# а значения — общее количество файлов (в том числе и в подпапках), размер которых не превышает этой границы,
# но больше предыдущей (начинаем с 0), например:
#     {
#       100: 15,
#       1000: 3,
#       10000: 7,
#       100000: 2
#     }
# Тут 15 файлов размером не более 100 байт; 3 файла больше 100 и не больше 1000 байт...
# Подсказка: размер файла можно получить из атрибута .st_size объекта os.stat.
import os
from os.path import relpath

name_main_dir = "venv"
root_dir = os.path.join(os.getcwd(), name_main_dir)
my_dict = {10: 0, 100: 0, 1000: 0, 10000: 0, 100000: 0}
for root, dirs, files in os.walk(root_dir):
    for file in files:
        rel_path = relpath(os.path.join(root, file))
        if os.stat(rel_path).st_size <= 10:
            my_dict[10] += 1
        elif 10 < os.stat(rel_path).st_size <= 100:
            my_dict[100] += 1
        elif 100 < os.stat(rel_path).st_size <= 1000:
            my_dict[1000] += 1
        elif 1000 < os.stat(rel_path).st_size <= 10000:
            my_dict[10000] += 1
        elif 10000 < os.stat(rel_path).st_size <= 100000:
            my_dict[100000] += 1
for key, value in my_dict.items():
    print(f' В указанной папке файлов размером от {key // 10} байт до {key} байт - {value} штук')