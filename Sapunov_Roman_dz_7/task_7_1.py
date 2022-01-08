# 1. Написать скрипт, создающий стартер (заготовку) для проекта со следующей структурой папок:
# |--my_project
#    |--settings
#    |--mainapp
#    |--adminapp
#    |--authapp
# Примечание: подумайте о ситуации, когда некоторые папки уже есть на диске (как быть?);
# как лучше хранить конфигурацию этого стартера, чтобы в будущем можно было менять имена папок под конкретный проект;
# можно ли будет при этом расширять конфигурацию и хранить данные о вложенных папках и файлах (добавлять детали)?
import os

my_project = ["setting", "mainapp", "adminapp", "authapp"]
name_main_dir = "my_project"
for i in my_project:
    if not os.path.exists(os.path.join(name_main_dir, i)):
        os.makedirs(os.path.join(name_main_dir, i))