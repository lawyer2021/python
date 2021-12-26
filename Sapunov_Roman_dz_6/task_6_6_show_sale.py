# 6. Реализовать простую систему хранения данных о суммах продаж булочной. Должно быть два скрипта с интерфейсом командной строки:
# для записи данных и для вывода на экран записанных данных. При записи передавать из командной строки значение суммы продаж.
# Для чтения данных реализовать в командной строке следующую логику:
# просто запуск скрипта — выводить все записи;
# запуск скрипта с одним параметром-числом — выводить все записи с номера, равного этому числу, до конца;
# запуск скрипта с двумя числами — выводить записи, начиная с номера, равного первому числу, по номер,
# равный второму числу, включительно.
# Подумать, как избежать чтения всего файла при реализации второго и третьего случаев.
# Данные хранить в файле bakery.csv в кодировке utf-8. Нумерация записей начинается с 1. Примеры запуска скриптов:
#
# python add_sale.py 5978,5
# python add_sale.py 8914,3
# python add_sale.py 7879,1
# python add_sale.py 1573,7
# python show_sales.py
# 5978,5
# 8914,3
# 7879,1
# 1573,7
# python show_sales.py 3
# 7879,1
# 1573,7
# python show_sales.py 1 3
# 5978,5
# 8914,3
# 7879,1
from sys import argv

import task_6_6_add_sale

if __name__ == "__main__":
    from sys import argv
    from itertools import islice

    if len(argv) == 1:
        with open("bakery.csv", "r", encoding="utf-8") as sale:
            for line in sale:
                print(line.strip())
    elif len(argv) == 2:
        number_lines_start = int(argv[1])
        with open("bakery.csv", "r", encoding="utf-8") as sale:
            lines = islice(sale, number_lines_start - 1, None)
            for line in lines:
                print(line.strip())
    elif len(argv) == 3:
        number_lines_start = int(argv[1])
        number_lines_fin = int(argv[2])
        with open("bakery.csv", "r", encoding="utf-8") as sale:
            lines = islice(sale, number_lines_start - 1, number_lines_fin)
            for line in lines:
                print(line.strip())
    else:
        print("Неверное количество аргументов")
