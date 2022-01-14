# Написать функцию email_parse(<email_address>), которая при помощи регулярного выражения
# извлекает имя пользователя и почтовый домен из email адреса и возвращает их в виде словаря.
# Если адрес не валиден, выбросить исключение ValueError. Пример:
# >>> email_parse('someone@geekbrains.ru')
# {'username': 'someone', 'domain': 'geekbrains.ru'}
# >>> email_parse('someone@geekbrainsru')
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
#   ...
#     raise ValueError(msg)
# ValueError: wrong email: someone@geekbrainsru
#
#
# Примечание: подумайте о возможных ошибках в адресе и постарайтесь
# учесть их в регулярном выражении; имеет ли смысл в данном случае использовать функцию re.compile()?
import re

my_dict = {}
check = re.compile(r"([a-zA-Z0-9-]+[.-_])*[A-Za-z0-9]+@[a-zA-Z0-9-]+\.([a-zA-Z0-9-]{2,})+")


def email_parse(email_address):
    if check.fullmatch(email_address):
        username, my_domain = email_address.split("@")
        my_dict["username"] = username
        my_dict["domain"] = my_domain
    else:
        raise ValueError(f'wrong email: {email_address}')


email_parse("ingo_sfo@mail.5ru")
print(my_dict)
