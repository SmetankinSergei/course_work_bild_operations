import pytest

import app_state
import main


@pytest.fixture(autouse=True)
def change_app_state():
    main.state_now = app_state.State.TEST
    yield
    main.state_now = app_state.State.WORK
