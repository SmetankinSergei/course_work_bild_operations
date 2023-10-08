ITEM = {
    "id": 441945886,
    "state": "EXECUTED",
    "date": "2019-08-26T10:50:58.294041",
    "operationAmount": {
        "amount": "31957.58",
        "currency": {
            "name": "руб.",
            "code": "RUB"
        }
    },
    "description": "Перевод организации",
    "from": "Maestro 1596837868705199",
    "to": "Счет 64686473678894779589"
}
ITEM_1 = {
    "id": 41428829,
    "state": "EXECUTED",
    "date": "2019-07-03T18:35:29.512364",
    "operationAmount": {
        "amount": "8221.37",
        "currency": {
            "name": "USD",
            "code": "USD"
        }
    },
    "description": "Перевод организации",
    "from": "MasterCard 7158300734726758",
    "to": "Счет 35383033474447895560"
}
ITEM_2 = {
    "id": 939719570,
    "state": "EXECUTED",
    "date": "2018-06-30T02:08:58.425572",
    "operationAmount": {
        "amount": "9824.07",
        "currency": {
            "name": "USD",
            "code": "USD"
        }
    },
    "description": "Перевод организации",
    "from": "Счет 75106830613657916952",
    "to": "Счет 11776614605963066702"
}
ITEM_3 = {
    "id": 587085106,
    "state": "EXECUTED",
    "date": "2018-03-23T10:45:06.972075",
    "operationAmount": {
        "amount": "48223.05",
        "currency": {
            "name": "руб.",
            "code": "RUB"
        }
    },
    "description": "Открытие вклада",
    "to": "Счет 41421565395219882431"
}
ITEM_4 = {
    "id": 214024827,
    "state": "EXECUTED",
    "date": "2018-12-20T16:43:26.929246",
    "operationAmount": {
        "amount": "70946.18",
        "currency": {
            "name": "USD",
            "code": "USD"
        }
    },
    "description": "Перевод организации",
    "to": "Счет 21969751544412966366"
}
DATA_LIST = [ITEM_2, ITEM_1, ITEM]
DATA_LIST_FOR_PRINT = [['30.06.2018 Перевод организации',
                        'Счет **6952 -> Счет **6702',
                        '9824.07 USD\n'],
                       ['03.07.2019 Перевод организации',
                        'MasterCard 7158 30** **** 6758 -> Счет **5560',
                        '8221.37 USD\n'],
                       ['26.08.2019 Перевод организации',
                        'Maestro 1596 83** **** 5199 -> Счет **9589',
                        '31957.58 руб.\n']]
