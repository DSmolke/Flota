import pytest
from app.service.options_builder import ChromeOptionsBuilder

@pytest.fixture
def builder():
    """
    Returns an instance of ChromeOptionsBuilder.

    :return: An instance of ChromeOptionsBuilder.
    """
    return ChromeOptionsBuilder()
