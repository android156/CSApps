# Задание на закрепление знаний по модулю CSV. Написать скрипт, осуществляющий выборку определенных данных из файлов
# info_1.txt, info_2.txt, info_3.txt и формирующий новый «отчетный» файл в формате CSV. Для этого:
#
# Создать функц. get_data(), в которой в цикле осуществляется перебор файлов с данными, их открытие и считывание данных.
# В этой функции из считанных данных необходимо с помощью регулярных выражений извлечь значения параметров «Изготовитель
# системы», «Название ОС», «Код продукта», «Тип системы». Значения каждого параметра поместить в соответствующий список.
# Должно получиться четыре списка — например, os_prod_list, os_name_list, os_code_list, os_type_list. В этой же функции
# создать главный список для хранения данных отчета — например, main_data — и поместить в него названия столбцов отчета
# в виде списка: «Изготовитель системы», «Название ОС», «Код продукта», «Тип системы». Значения для этих столбцов также
# оформить в виде списка и поместить в файл main_data (также для каждого файла);
# Создать функцию write_to_csv(), в которую передавать ссылку на CSV-файл. В этой функции реализовать получение данных
# через вызов функции get_data(), а также сохранение подготовленных данных в соответствующий CSV-файл;
# Проверить работу программы через вызов функции write_to_csv().

import csv
import os
import glob


def get_data(path, mask, column_list):
    main_data = []
    main_dict = {}
    for col_name in column_list:
        main_dict[col_name] = []

    main_data.append(column_list)
    for file in glob.glob(f'{path}/{mask}'):
        print(f'{file}')
        impotent_data_from_file = []
        with open(file) as csv_file:
            csv_reader = csv.reader(csv_file)
            for row in csv_reader:
                row_data = row[0].split(sep=':')
                row_name = row_data[0].strip()
                if len(row_data) > 1:
                    row_value = row_data[1].strip()
                else:
                    row_value = 'Пусто'
                if row_name in column_list:
                    main_dict[row_name].append(row_value)
                    print(f'{row_name}:{row_value}')
                    impotent_data_from_file.append(row_value)
        main_data.append(impotent_data_from_file)
    return main_data, main_dict


def write_to_csv(path_to_csv, data_for_csv):
    with open(path_to_csv, 'w') as csv_file:
        csv_writer = csv.writer(csv_file)
        for row in data_for_csv:
            csv_writer.writerow(row)
    print(f'{data_for_csv} - записано в файл {path_to_csv}')


col_name_dir = [
    'Изготовитель системы',
    'Название ОС',
    'Код продукта',
    'Тип системы'
]
mask = 'info*.txt'
csv_file_name = 'main_data.csv'
path = os.getcwd()
path_to_csv = f'{path}/{csv_file_name}'

main_data, main_dict = get_data(path, mask, col_name_dir)
write_to_csv(path_to_csv, main_data)

os_prod_list = main_dict[col_name_dir[0]]
os_name_list = main_dict[col_name_dir[1]]
os_code_list = main_dict[col_name_dir[2]]
os_type_list = main_dict[col_name_dir[3]]

write_to_csv('os_prod_list.csv', os_prod_list)
write_to_csv('os_name_list.csv', os_name_list)
write_to_csv('os_code_list.csv', os_code_list)
write_to_csv('os_type_list.csv', os_type_list)




