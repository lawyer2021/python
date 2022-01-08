# 3. Создать структуру файлов и папок, как написано в задании 2 (при помощи скрипта или «руками» в проводнике).
# Написать скрипт, который собирает все шаблоны в одну папку templates, например:
# |--my_project
#    ...
#   |--templates
#    |   |--mainapp
#    |   |  |--base.html
#    |   |  |--index.html
#    |   |--authapp
#    |      |--base.html
#    |      |--index.html
# Примечание: исходные файлы необходимо оставить;
# обратите внимание, что html-файлы расположены в родительских папках (они играют роль пространств имён);
# предусмотреть возможные исключительные ситуации; это реальная задача, которая решена, например, во фреймворке django.
import os
import shutil

name_main_dir = "my_project"
name_dir = "templates"
root_dir = os.path.join(os.getcwd(), name_main_dir)
for root, dirs, files in os.walk(root_dir):
    _root = root.split("\\")[-1]
    if _root == name_dir:
        for root, dirs, files in os.walk(root):
            for file in files:
                src = os.path.join(os.getcwd(), root, file.rsplit("\\", maxsplit=1)[-1].lower())
                b = root.split("\\")[-1]
                dst = os.path.join(os.getcwd(), name_main_dir, name_dir, b)
                if not os.path.exists(os.path.join(name_main_dir, name_dir, b)):
                    os.makedirs(os.path.join(name_main_dir, name_dir, b))
                try:
                    shutil.copy(src, dst)
                except shutil.SameFileError:
                    pass