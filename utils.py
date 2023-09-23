def create_list_for_output(bills_list):
    result_list = []
    for bill in bills_list:
        bill_date_list = bill['date'][:10].split('-')
        bill_date = bill_date_list[2] + '.' + bill_date_list[1] + '.' + bill_date_list[0]
        from_description = get_accounts_description(bill)[0]
        to_description = get_accounts_description(bill)[1]
        amount = bill['operationAmount']['amount'] + ' ' + bill['operationAmount']['currency']['name']
        result_list.append(f'{bill_date} {bill["description"]}\n{from_description} -> {to_description}\n{amount}\n')
    return result_list


def get_number_mask(number):
    if len(number) == 16:
        return number[:4] + ' ' + number[4:6] + '** **** ' + number[12:]
    elif len(number) == 20:
        return '**' + number[-4:]


def get_accounts_description(bill):
    if bill['description'] == 'Открытие вклада':
        to_description = ' '.join(bill['to'].split()[:-1]) + ' ' + get_number_mask(bill['to'].split()[-1])
        return 'open', to_description
    else:
        from_description = ' '.join(bill['from'].split()[:-1]) + ' ' + get_number_mask(bill['from'].split()[-1])
        to_description = ' '.join(bill['to'].split()[:-1]) + ' ' + get_number_mask(bill['to'].split()[-1])
        return from_description, to_description
