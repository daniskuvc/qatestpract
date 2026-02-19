import pytest
from config.settings import TEST_USERNAME, TEST_PASSWORD, DEBUG, TEST_URL
from pages.login_page import LoginPage


test_data = [
    (TEST_USERNAME, TEST_PASSWORD, "You logged into a secure area!"),
    (TEST_USERNAME, "invalid_pass", "Your password is invalid!"),
    ("invalid_user", TEST_PASSWORD, "Your username is invalid!"),
    ("invalid_user", "invalid_pass", "Your username is invalid!"),
]

@pytest.mark.parametrize("username, password, expected_message", test_data)

def test_login(driver, username, password, expected_message):
    login_page = LoginPage(driver)
    login_page.wait_until_page_loaded()
    login_page.open(url=TEST_URL)
    login_page.login(username=username, password=password)
    
    message = login_page.get_flash_message()
    assert expected_message in message, f"Expected message '{expected_message}' but got '{message}'"
