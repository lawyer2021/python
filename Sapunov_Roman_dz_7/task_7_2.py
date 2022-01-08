# 2. * (вместо 1) Написать скрипт, создающий из config.yaml стартер для проекта со следующей структурой:
# |--my_project
#    |--settings
#    |  |--__init__.py
#    |  |--dev.py
#    |  |--prod.py
#    |--mainapp
#    |  |--__init__.py
#    |  |--models.py
#    |  |--views.py
#    |  |--templates
#    |     |--mainapp
#    |        |--base.html
#    |        |--index.html
#    |--authapp
#    |  |--__init__.py
#    |  |--models.py
#    |  |--views.py
#    |  |--templates
#    |     |--authapp
#    |        |--base.html
#    |        |--index.html
# Примечание: структуру файла config.yaml
# придумайте сами, его можно создать в любом текстовом редакторе «руками» (не программно);
# предусмотреть возможные исключительные ситуации, библиотеки использовать нельзя.

import os

with open("config.yaml", "r") as file:
    for line in file:
        if "." not in line:
            my_dir = line.splitlines()
            os.makedirs(os.path.join(my_dir[0]))
        else:
            my_dir = os.path.join(os.getcwd(), " ".join(line.splitlines()))
            with open(my_dir, 'w') as f:
                f.write("этот файл создан автоматически")