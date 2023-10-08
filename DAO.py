import json
import os

import app_state
import main


def get_all_data():
    """Возвращает данные из файла"""
    path = os.path.join('data', 'operations.json')
    if main.state_now == app_state.State.TEST:
        path = os.path.join('..', 'data', 'operations.json')
    with open(path, encoding='UTF-8') as file:
        return json.load(file)
