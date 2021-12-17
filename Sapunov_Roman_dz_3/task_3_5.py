import random

nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]


def get_jokes(n):
    answer = []
    i = 0
    """using 'while' and function 'random'"""
    while i < n:
        answer += [f"{random.choice(nouns)} {random.choice(adverbs)} {random.choice(adjectives)}"]
        i += 1
    print(answer)


get_jokes(5)
