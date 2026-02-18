import pytest
from config.settings import TEST_USERNAME, TEST_PASSWORD, DEBUG, TEST_URL
from pages.login_page import LoginPage

@pytest.mark.parametrize("username, password, expected_message", [
    (TEST_USERNAME, TEST_PASSWORD, "You logged into a secure area!"),
    ("invalid_user", "invalid_pass", "Your username is invalid!"),
])

def test_login(driver, username, password, expected_message):
    login_page = LoginPage(driver)
    login_page.open(url=TEST_URL)
    login_page.login(username=username, password=password)
    
    message = login_page.get_flash_message()
    assert expected_message in message, f"Expected message '{expected_message}' but got '{message}'"
        