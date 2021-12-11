prices = [57.8, 46.51, 97, 254, 19.20, 450, 59.12, 88, 41, 90.22, 133]
new_price = ''
for i in prices:
    if type(i) == float:
        a = str(i)
        rr = a.split(".")[0]
        if int(a.split(".")[1]) < 10:
            kk = int(a.split(".")[1]) * 10
            new_price += (f'{rr} руб {kk:d} коп, ')
        else:
            kk = int(a.split(".")[1])
            new_price += (f'{rr} руб {kk:2d} коп, ')
    else:
        new_price += (f"{i:d} руб 00 коп, ")
print("Цены с разбивкой на рубли и копейки через запятую в одну строку: \n", new_price)

print("ID изначального списка цен: ", id(prices))
prices.sort()
print("ID отсортированного списка по возрастанию: ", id(prices))
print("Цены, отсортированные по возрастанию: ", prices)

sort_price = sorted(prices, reverse=True)
print("Цены, отсортированные по убыванию (новый список): ", sort_price)
print("ID отсротированного списка по убыванию (новый список): ", id(sort_price))

print("Цены пяти самых дорогих товаров по возрастанию: ", prices[-5:])
