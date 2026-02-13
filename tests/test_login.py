from config.settings import TEST_USERNAME, TEST_PASSWORD, DEBUG, TEST_URL
from core.driver_factory import get_driver
from pages.login_page import LoginPage


def test_valid_login(driver):
    login_page = LoginPage(driver)
    login_page.open(url=TEST_URL)
    login_page.login(username=TEST_USERNAME, password=TEST_PASSWORD)
    
    # assert login_page.is_login_successful(), "Login should be successful with valid credentials"
    assert login_page.is_message_displayed(), "Success message should be displayed after login"
    
    if not DEBUG:
        driver.quit()
    