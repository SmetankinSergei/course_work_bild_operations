import json
import os


def get_bills_list(bills_amount):
    all_data = get_all_data()
    bills_list = sort_bills(all_data)
    result_list = []
    for bill in bills_list:
        if bill['state'] == 'EXECUTED':
            result_list.append(bill)
            bills_amount -= 1
            if bills_amount == 0:
                return result_list
    return result_list


def get_all_data():
    path = os.path.join('data', 'operations.json')
    with open(path, encoding='UTF-8') as file:
        all_data = json.load(file)
        return all_data


def sort_bills(all_data):
    bills_list = []
    for item in all_data:
        if item != {}:
            bills_list.append(item)
    return list(sorted(bills_list, key=lambda x: x['date'], reverse=True))