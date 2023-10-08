import pytest

import app_state
import main
from main import app


@pytest.fixture(autouse=True)
def change_app_state():
    main.state_now = app_state.State.TEST
    yield
    main.state_now = app_state.State.WORK


def test_home():
    response = app.test_client().get('/')
    assert response.status_code == 200
    assert b'Bills operations' in response.data
