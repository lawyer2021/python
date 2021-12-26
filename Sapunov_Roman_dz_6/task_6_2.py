# 2. * (вместо 1) Найти IP адрес спамера и количество отправленных им запросов по данным файла логов из предыдущего задания.
# Примечания: спамер — это клиент, отправивший больше всех запросов; код должен работать даже с файлами, размер которых превышает объем ОЗУ компьютера.
"""Парсинг файла логов с сайта"""
import requests
from requests import get, utils
from collections import Counter

response = get("https://github.com/elastic/examples/raw/master/Common%20Data%20Formats/nginx_logs/nginx_logs")
encodings = requests.utils.get_encoding_from_headers(response.headers)
content = response.content.decode(encoding = encodings)

answer = []
remote_addr_lst = []
for i in (content.strip().split("\n")):
    remote_addr, _, _2, _date, _zone, _request_type, requested_resource, *other = i.split(" ")
    request_type = _request_type.replace('"', "")
    answer.append((remote_addr, request_type, requested_resource))
    _remote_addr = [i[0:(int(str(i.find("- -")))-1)]]
    remote_addr_lst += (remote_addr,)
max_ip_counter_tuple = Counter(remote_addr_lst).most_common(1)
print(f"\nIP адрес спамера и количество отправленных им запросов: {max_ip_counter_tuple} \n")
print(*answer[:7], sep='\n')
print("И так далее...")