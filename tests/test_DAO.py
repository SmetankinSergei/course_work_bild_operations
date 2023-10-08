import pytest

import app_state
import main
from DAO import get_all_data


@pytest.fixture(autouse=True)
def change_app_state():
    main.state_now = app_state.State.TEST
    yield
    main.state_now = app_state.State.WORK


def test_get_all_data(change_app_state):
    assert isinstance(get_all_data(), list)
