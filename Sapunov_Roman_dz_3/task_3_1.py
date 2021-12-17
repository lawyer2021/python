rus_translate = ["один", "два", "три", "четыре", "пять", "шесть", "семь", "восемь", "девять", "десять"]


def num_translate(word):
    if word == "one":
        print(rus_translate[0])
    elif word == "two":
        print(rus_translate[1])
    elif word == "three":
        print(rus_translate[2])
    elif word == "four":
        print(rus_translate[3])
    elif word == "five":
        print(rus_translate[4])
    elif word == "six":
        print(rus_translate[5])
    elif word == "seven":
        print(rus_translate[6])
    elif word == "eight":
        print(rus_translate[7])
    elif word == "nine":
        print(rus_translate[8])
    elif word == "ten":
        print(rus_translate[9])
    else:
        return None


num_translate("five")

"""Other method (dictionary)"""
# rus_translate = {
#     "one": "один",
#     "two": "два",
#     "three": "три",
#     "four": "четыре",
#     "five": "пять",
#     "six": "шесть",
#     "seven": "семь",
#     "eight": "восемь",
#     "nine": "девять",
#     "ten": "десять"
# }
# print(rus_translate[input("Введите число от 1 до 10 на аглийском языке: ")])
