from selenium.webdriver.common.by import By
from core.base_page import BasePage


class LoginPage(BasePage):
    
    USERNAME = (By.ID, "username")
    PASSWORD = (By.ID, "password")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")
    SUCCESS_MESSAGE = (By.ID, "flash")
    
    def login(self, username, password):
        self.driver.find_element(*self.USERNAME).send_keys(username)
        self.driver.find_element(*self.PASSWORD).send_keys(password)
        self.driver.find_element(*self.LOGIN_BUTTON).click()
        
    # def is_login_successful(self):
    #     return "secure" in self.driver.current_url
    
    def is_message_displayed(self):
        return self.driver.find_element(*self.SUCCESS_MESSAGE).is_displayed()
    