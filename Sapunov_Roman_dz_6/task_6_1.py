# 1. Не используя библиотеки для парсинга, распарсить (получить определённые данные) файл логов web-сервера nginx_logs.txt
# (https://github.com/elastic/examples/raw/master/Common%20Data%20Formats/nginx_logs/nginx_logs) —
# получить список кортежей вида: (<remote_addr>, <request_type>, <requested_resource>). Например:
#
# [
# ...
# ('141.138.90.60', 'GET', '/downloads/product_2'),
# ('141.138.90.60', 'GET', '/downloads/product_2'),
# ('173.255.199.22', 'GET', '/downloads/product_2'),
# ...
# ]
#
# Примечание: код должен работать даже с файлами, размер которых превышает объем ОЗУ компьютера.


from collections import Counter
answer = []
remote_addr_lst = []
with open("nginx_logs.txt", "r", encoding="utf-8") as content:
    for line in content:
        remote_addr, _, _2, _date, _zone, _request_type, requested_resource, *other = line.split(" ")
        request_type = _request_type.replace('"', "")
        answer.append((remote_addr, request_type, requested_resource))
        remote_addr_lst += (remote_addr,)
max_ip_counter_tuple = Counter(remote_addr_lst).most_common(1)
print(f"IP адрес спамера и количество отправленных им запросов: {max_ip_counter_tuple}")
print(*answer[:50], sep='\n')




