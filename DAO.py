import json
import os


def get_all_data():
    """Возвращает данные из файла"""
    path = os.path.join('data', 'operations.json')
    with open(path, encoding='UTF-8') as file:
        return json.load(file)
