# 2. Задание на закрепление знаний по модулю json. Есть файл orders в формате JSON с информацией о заказах.
# Написать скрипт, автоматизирующий его заполнение данными. Для этого: Создать функцию write_order_to_json(),
# в которую передается 5 параметров — товар (item), количество (quantity), цена (price), покупатель (buyer),
# дата (date). Функция должна предусматривать запись данных в виде словаря в файл orders.json. При записи данных
# указать величину отступа в 4 пробельных символа; Проверить работу программы через вызов функции write_order_to_json()
# с передачей в нее значений каждого параметра.

import json
import datetime


def read_json_orders():
    with open('orders.json', 'r') as json_file:
        json_data = json.load(json_file)
    return json_data


def write_order_to_json(item, quantity, price, buyer, date=str(datetime.datetime.now())):
    order = [item, quantity, price, buyer, date]
    json_data = read_json_orders()
    json_data['orders'].append(order)
    with open('orders.json', 'w') as json_file:
        json.dump(json_data, json_file, indent=4)


def reset_json():
    with open('orders.json', 'w') as new_json_file:
        base_data = '{"orders": []}'
        new_json_file.write(base_data)


reset_json()
print(read_json_orders())
write_order_to_json('Куртка', 20, 7600.3, 'Курточный барыга')
print(read_json_orders())
write_order_to_json('Носочки', 1, 100, 'Дедушка Василий')
print(read_json_orders())
