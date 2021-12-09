duration = int(input("Please, input duration (sec): "))
if duration < 60:
    s = duration % 60
    print(s, "сек")
elif duration < 3600:
    m = duration // 60
    s = duration % 60
    print(m, "мин", s, "сек")
elif duration < 86400:
    h = duration // 3600
    m = (duration - h * 3600) // 60
    s = duration % 60
    print(h, "час", m, "мин", s, "сек")
else:
    d = duration // 86400
    h = (duration - d * 86400) // 3600
    m = (duration - d * 86400 - h * 3600) // 60
    s = duration % 60
    print(d, "дн", h, "час", m, "мин", s, "сек")
