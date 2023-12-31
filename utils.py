import DAO


def get_bills_list(bills_amount):
    """Возвращает список операций по заданным параметрам (bills_amount, bill['state'] == 'EXECUTED')"""
    all_data = DAO.get_all_data()
    bills_list = sort_bills(all_data)
    result_list = []
    for bill in bills_list:
        if bill['state'] == 'EXECUTED':
            result_list.append(bill)
            bills_amount -= 1
            if bills_amount == 0:
                return result_list
    return result_list


def create_list_for_output(bills_list):
    """Собирает список строк из списка операций для отображения на странице"""
    result_list = []
    for bill in bills_list:
        bill_date_list = bill['date'][:10].split('-')[::-1]
        bill_date = '.'.join(bill_date_list)
        from_description, to_description = get_accounts_description(bill)
        amount = bill['operationAmount']['amount'] + ' ' + bill['operationAmount']['currency']['name']
        result_list.append([f'{bill_date} {bill["description"]}',
                            f'{from_description} -> {to_description}',
                            f'{amount}\n'])
    return result_list


def get_accounts_description(bill):
    """Собирает из информации об операции строки 'откуда' и 'куда'"""
    if bill['description'] == 'Открытие вклада':
        from_description = 'open'
    elif 'from' in bill.keys():
        from_description = ' '.join(bill['from'].split()[:-1]) + ' ' + get_number_mask(bill['from'].split()[-1])
    else:
        from_description = 'unknown sender'
    to_description = ' '.join(bill['to'].split()[:-1]) + ' ' + get_number_mask(bill['to'].split()[-1])
    return from_description, to_description


def get_number_mask(number):
    """Возвращает маску счёта или карты"""
    if len(number) == 16:
        return number[:4] + ' ' + number[4:6] + '** **** ' + number[12:]
    elif len(number) == 20:
        return '**' + number[-4:]


def sort_bills(all_data):
    """Сортирует операции"""
    bills_list = []
    for item in all_data:
        if check_valid_data(item):
            bills_list.append(item)
    return list(sorted(bills_list, key=lambda x: x['date'], reverse=True))


def check_valid_data(item):
    """Проверяет валидность данных в счёте. В настоящей программе я бы проверил и вложенные словари.."""
    required_list = ['state', 'description', 'to', 'date', 'operationAmount']
    keys = item.keys()
    for element in required_list:
        if element not in keys:
            return False
    return True
