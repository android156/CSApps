# 3. Задание на закрепление знаний по модулю yaml. Написать скрипт, автоматизирующий сохранение данных в файле
# YAML-формата. Для этого:
# Подготовить данные для записи в виде словаря, в котором первому ключу соответствует список, второму — целое число,
# третьему — вложенный словарь, где значение каждого ключа — это целое число с юникод-символом, отсутствующим в
# кодировке ASCII (например, €);
# Реализовать сохранение данных в файл формата YAML — например, в файл file.yaml. При этом обеспечить стилизацию файла
# с помощью параметра default_flow_style, а также установить возможность работы с юникодом: allow_unicode = True;
# Реализовать считывание данных из созданного файла и проверить, совпадают ли они с исходными.

import yaml


def reset_yaml():
    with open('file.yaml', 'w') as new_yaml_file:
        print('Пустой yaml-файл создан')


def write_to_yaml(yaml_data):
    with open('file.yaml', 'w') as yaml_file:
        yaml.dump(yaml_data, yaml_file, allow_unicode=True, default_flow_style=True)
    print(f'{yaml_data} записано в файл')


def read_from_yaml(file):
    with open(file, 'r') as yaml_file:
        yaml.data = yaml.load(yaml_file, Loader=yaml.Loader)
    print(f'{yaml_data} прочитано из файла')

yaml_data = {
    'list': ['val1', 'val2', 'val3', 'val4'],
    'int': 156,
    'dict': {1: '25€', 2: '75$'}
}

reset_yaml()
write_to_yaml(yaml_data)
read_from_yaml('file.yaml')


