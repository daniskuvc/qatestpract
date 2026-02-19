import pytest
from config.settings import DEBUG
from core.driver_factory import get_driver


@pytest.fixture(scope="function")
def driver():
    driver = get_driver()
    yield driver
    if DEBUG:
        driver.quit()
