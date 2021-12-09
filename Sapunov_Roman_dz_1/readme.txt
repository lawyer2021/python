1. Вот это очень долго пришлось изобретать:

sum_numbers = 0
for cube in my_numbers:
    _sum_numbers = 0
    while cube != 0:
        _sum_numbers += cube % 10
        cube = cube // 10
    if _sum_numbers % 7 == 0:
        sum_numbers += _sum_numbers

А так всё хорошо. Было интересно.

2. Не совсем понял, почему вот так не работает перебор:
my_numbers = [1, 27, 125, 343]
for index in my_numbers:
    my_numbers[index] += 17
При переборе for получается в этом случае не видит предел списка...

В общем, пришлось перечитывать методичку, а там оказывается всё было дано изначально, но не раскрыт принцип работы:
for index in range(len(my_numbers)):
    my_numbers[index] += 17

3. Пинцип работы enumerate тоже не ясен.