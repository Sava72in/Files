"""TASK №1"""
import json
def create_cook_book():
    cook_book = {}
    with open('cook_book.txt', encoding='utf-8') as file:
        for l in file:
            if l != '\n':
                ingradients_name = l.strip()
                ingradients_count = file.readline()
                ingradients = []

                for i in range(int(ingradients_count)):
                    recept = file.readline()
                    product, quantity, word = recept.strip().split('|')
                    ingradients.append({'ingradients_name': product, 'quantity': quantity, 'measury': word})
                    x = {ingradients_name:ingradients} 
                    cook_book.update(x)
    return cook_book
print(create_cook_book())
with open('out.txt', 'w') as file:
    json.dump(create_cook_book(), file, indent=2, ensure_ascii=False) # для читаемости, занимет больше места

"""TASK №2"""
def get_shop_list_by_dishes(dishes, person_count):
    dict_ingredients = {}
    for elem in dishes: # перебираем названия блюд
        for ingredients in create_cook_book()[elem]: # заходим в словарь блюда
            name = ingredients['ingradients_name']
            measury = ingredients['measury']
            quantity = ingredients['quantity']
            dict_ingredients.setdefault(name, {}).setdefault('measury', measury)
            dict_ingredients[name]['quantity'] = dict_ingredients.setdefault(name, {}).setdefault('quantity', 0) + int(quantity) * person_count
    return dict_ingredients
print(get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2))

"""TASK №3"""
import os

path = os.listdir(path='./sorted/') 
def compile_files(path):
    data = {}
    for file_ in path:
        if file_.endswith('.txt'):
            with open(f'./sorted/{file_}', encoding="utf-8") as f:
                file_data = f.readlines()
                data[len(file_data)] = (file_, " ".join(file_data))
    data = dict(sorted(data.items()))
    with open(" result_data. txt", 'w', encoding="utf-8") as new_file:
        for key,value in data. items () :
            new_file.write(f'Имя файла: {value[0]}\n')
            new_file.write(f'Кол-ва строк: {key}\n')
            new_file.write(f'Данные:\n{value[1]}\n\n')
        
compile_files(path)
"""TASK №4"""


