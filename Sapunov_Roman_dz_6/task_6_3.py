# 3. Есть два файла: в одном хранятся ФИО пользователей сайта, а в другом — данные об их хобби. Известно, что при хранении данных
# используется принцип: одна строка — один пользователь, разделитель между значениями — запятая.
# Написать код, загружающий данные из обоих файлов и формирующий из них словарь:
# ключи — ФИО, значения — данные о хобби. Сохранить словарь в файл.
# Проверить сохранённые данные. Если в файле, хранящем данные о хобби, меньше записей,
# чем в файле с ФИО, задаём в словаре значение None. Если наоборот — выходим из скрипта с кодом «1».
# При решении задачи считать, что объём данных в файлах во много раз меньше объема ОЗУ.
# Фрагмент файла с данными о пользователях (users.csv):
# Иванов,Иван,Иванович
# Петров,Петр,Петрович
# Фрагмент файла с данными о хобби (hobby.csv):
# скалолазание,охота
# горные лыжи
from itertools import zip_longest

users_dict = {}
hobby_dict = {}
with open("users.csv", "r", encoding="utf-8") as users:
    for line in users:
        users_dict[line.replace(",", " ").replace("\n", "")] = 0
with open("hobby.csv", "r", encoding="utf-8") as hobby:
    for line in hobby:
        hobby_dict[line.replace(",", ", ").replace("\n", "")] = 0
union_dicts = {}
if len(hobby_dict) <= len(users_dict):
    for k1, k2 in zip_longest(users_dict.keys(), hobby_dict.keys(), fillvalue=None):
        union_dicts[k1] = k2
else:
    exit(1)
print(union_dicts)
with open("union_dicts.txt", "w", encoding="utf-8") as f:
    f.write(str(union_dicts))
