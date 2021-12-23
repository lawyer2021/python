# 1. Написать генератор нечётных чисел от 1 до n (включительно), используя ключевое слово yield, например:
# >>> odd_to_15 = odd_nums(15)
# >>> next(odd_to_15)
# 1
# >>> next(odd_to_15)
# 3
# ...
# >>> next(odd_to_15)
# 15
# >>> next(odd_to_15)
# ...StopIteration...

def gen_nums(nums):
    for n in range(1, nums + 1, 2):
        yield (n)


gen = gen_nums(15)
print(next(gen), next(gen), next(gen))
