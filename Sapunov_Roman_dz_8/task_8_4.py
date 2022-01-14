# Написать декоратор с аргументом-функцией (callback), позволяющий валидировать входные значения функции
# и выбрасывать исключение ValueError, если что-то не так, например:
# def val_checker...
#     ...
#
#
# @val_checker(lambda x: x > 0)
# def calc_cube(x):
#    return x ** 3
#
#
# >>> a = calc_cube(5)
# 125
# >>> a = calc_cube(-5)
# Traceback (most recent call last):
#   ...
#     raise ValueError(msg)
# ValueError: wrong val -5
#
#
# Примечание: сможете ли вы замаскировать работу декоратора?
# Задачи со * предназначены для продвинутых учеников, которым мало сделать обычное задание.
import functools


def val_checker(x):
    def out_func(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            if x(*args):
                val = func(*args, *kwargs)
                return val
            else:
                raise ValueError(f"wrong val {''.join(map(str, args))}")

        return wrapper

    return out_func


@val_checker(lambda x: x > 0)
def calc_cube(x):
    return x ** 3


print(f"Исходная функция: {calc_cube.__name__}")
a = calc_cube(-220)
print(a)
