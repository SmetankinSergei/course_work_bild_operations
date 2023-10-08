import pytest

import app_state
import constants
import main
from utils import check_valid_data, sort_bills, get_bills_list


@pytest.fixture(autouse=True)
def change_app_state():
    main.state_now = app_state.State.TEST
    yield
    main.state_now = app_state.State.WORK


@pytest.mark.parametrize('bills_amount', [4, 10, 15, 55])
def test_get_bills_list(bills_amount):
    assert isinstance(get_bills_list(bills_amount), list)


@pytest.mark.parametrize('item, expected', [({}, False), (constants.ITEM, True)])
def test_check_valid_data(item, expected):
    assert check_valid_data(item) == expected


@pytest.mark.parametrize('data_list, expected', [([constants.ITEM_2, constants.ITEM_1],
                                                  [constants.ITEM_1, constants.ITEM_2]),
                                                 ([{}, constants.ITEM], [constants.ITEM])])
def test_sort_bills(data_list, expected):
    assert sort_bills(data_list) == expected


@pytest.mark.parametrize('number, expected', [('1234123412341234', '1234 12** **** 1234'),
                                              ('12341234123412341234', '**1234')])
def test_get_number_mask(number, expected):
    assert get_number_mask(number) == expected


@pytest.mark.parametrize('bill, expected', [(constants.ITEM, ('Maestro 1596 83** **** 5199', 'Счет **9589')),
                                            (constants.ITEM_3, ('open', 'Счет **2431')),
                                            (constants.ITEM_4, ('unknown sender', 'Счет **6366'))])
def test_get_accounts_description(bill, expected):
    assert get_accounts_description(bill) == expected


@pytest.mark.parametrize('bills_list, expected', [(constants.DATA_LIST, constants.DATA_LIST_FOR_PRINT)])
def test_create_list_for_output(bills_list, expected):
    assert create_list_for_output(bills_list) == expected

