# 3. Есть два списка:
# tutors = [
#     'Иван', 'Анастасия', 'Петр', 'Сергей',
#     'Дмитрий', 'Борис', 'Елена'
# ]
# klasses = [
#     '9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А'
# ]
# Необходимо реализовать генератор, возвращающий кортежи вида (<tutor>, <klass>), например:
# ('Иван', '9А')
# ('Анастасия', '7В')
# ...
# Количество генерируемых кортежей не должно быть больше длины списка tutors. Если в списке klasses меньше элементов, чем в списке tutors, необходимо вывести последние
# кортежи в виде: (<tutor>, None), например:
# ('Станислав', None)
#
# ### Доказать, что вы создали именно генератор. Проверить его работу вплоть до истощения. Подумать, в каких ситуациях генератор даст эффект.
#
from itertools import zip_longest
from time import perf_counter

start = perf_counter()


def gen_class(tutors, klasses):
    for i in zip_longest(tutors, klasses, fillvalue=None):
        print(i)


gen_class(['Иван', 'Анастасия', 'Петр', 'Сергей', 'Дмитрий', 'Борис', 'Елена', 'Станислав', 'Максим', 'Аким'],
          ['9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А'])
print("Скорость через цикл: ", perf_counter() - start, "\n")

start = perf_counter()
tutors = [
    'Иван', 'Анастасия', 'Петр', 'Сергей', 'Дмитрий', 'Борис', 'Елена', 'Станислав', 'Максим', 'Аким'
]
klasses = [
    '9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А'
]
t = (tutors[n] for n in range(0, len(tutors)))
k = (klasses[n] for n in range(0, len(klasses)))
for i in zip_longest((tutors[n] for n in range(0, len(tutors))), (klasses[n] for n in range(0, len(klasses))),
                     fillvalue=None):
    print(i)
print(type(t), type(k))
print("Скорость через генератор: ", perf_counter() - start)
