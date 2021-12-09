percent_1 = "процент"
percent_2 = "процента"
percent_3 = "процентов"

for n in range(1, 101):
    if n % 10 == 1 and n != 11:
        print(n, percent_1)
    elif n % 10 == 2 and n != 12 or n % 10 == 3 and n != 13 or n % 10 == 4 and n != 14:
        print(n, percent_2)
    elif 11 <= n <= 20 or n % 10 == 5 or n % 10 == 6 or n % 10 == 7 or n % 10 == 8 or n % 10 == 9 or n % 10 == 0:
        print(n, percent_3)
