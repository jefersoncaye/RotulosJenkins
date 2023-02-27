import pytest

@pytest.fixture
def set_up(page):

    yield page