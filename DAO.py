import json
import os


def get_all_data():
    path = os.path.join('data', 'operations.json')
    with open(path, encoding='UTF-8') as file:
        all_data = json.load(file)
        return all_data
