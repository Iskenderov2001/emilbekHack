"""
ТЗ для проекта на хакатон “CRUD”

Цель проекта: реализовать CRUD действия для продукта в интернет
магазине ноутбуков
Задание:
1. Создайте базу данных (файл JSON), полями продукта со
следующими:
- марка (строка)
- модель (строка)
- год выпуска (целое число)
- описание (строка)
- цена (decimal, точность 2 знака)
2. Создайте функции, в которых будут реализованы коды для
манипуляции записями в БД(файл JSON):
- create для создания записей
- listing для получения списка записей
- retrieve для получения одной записи
- update для обновления записей
- delete для удаления записей
3. Реализуйте запрос данных и команд от пользователя,
все действия будут запрашиваться от пользователя
в терминале, там же он должен вводить данные для
продукта (input).
Требования к проекту:
- код должен соответствовать PEP8
- при использовании каких-либо библиотек, укажите их в файле
requirements.txt
- При запуски кода не должно возникать ошибок
- За реализацию хорошего интерфейся для пользователя
в терминале, доп баллы(чтобы пользователь решал что делать
и когда заканчивать работу).
"""

# 1. Создайте базу данных (файл JSON), полями продукта со следующими:

import json

import webbrowser 

FILE_PATH = 'data.json'


def listing():
    with open(FILE_PATH) as file:
       return json.load(file)
    

def retrieve():
    data = listing()
    id = int(input("Enter id product "))
    element = list(filter(lambda x: x['id'] == id, data))
    a = input('Vy hotite chitat instrukciyu mashin? \nDa ili Net? ')
    if a == "Da":
        webbrowser.open("https://marafon.kg")
    elif a.lower() == 'da':
        webbrowser.open("https://marafon.kg")
    elif a.upper() == 'DA':
        webbrowser.open("https://marafon.kg")
    elif a == 'Net' or 'net':
        print('Vam nado proiti po ssylky, Ya je vremiya ne zria trachu? ')
        c = input('Tak vy hotite zaiti ili net? ')
        if c == 'da':
            webbrowser.open("https://marafon.kg")
        else:
            webbrowser.open("https://marafon.kg")
    return element[0]
        

def create():
    data = listing()
    data.append({
        'id': int(input('Enter id product (1-100) ')),
        'name': input('Enter name product: '),
        'model': input('Enter model machine '),
        'price': float(input('Enter pricein product ')),
        'description': input('Google vam pomosh))) ')
    })
    with open(FILE_PATH, 'w') as file:
        json.dump(data, file)
    return 'CREATED'

def update():
    data = listing()
    id = int(input('Enter id product '))
    update = list(filter(lambda x: x['id'] == id, data))

    if not update:
        return 'Not product'
    
    index_ = data.index(update[0])
    
    data[index_]['name'] = input('Enter new name product ')
    data[index_]['price'] = float(input('Enter new price '))
    data[index_]['model'] = float(input('Enter new model '))
    data[index_]['description'] = float(input('Enter new description '))

    update = list(filter(lambda x: x['id'] == id, data))
    with open(FILE_PATH, 'w') as file:
        json.dump(data, file)


def delete_data():
    data = listing()
    id = int(input('Enter id: '))
    delete = list(filter(lambda x: x['id'] == id, data))
    if not delete:
        return 'Not have product!'
    index_ = data.index(delete[0])
    data.pop(index_)
    json.dump(data, open(FILE_PATH, 'w'))
    return 'DELETED'