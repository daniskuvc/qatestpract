from selenium.webdriver.common.by import By
from core.base_page import BasePage


class LoginPage(BasePage):
    
    USERNAME = (By.ID, "username")
    PASSWORD = (By.ID, "password")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")
    SUCCESS_MESSAGE = (By.ID, "flash")
    
    def login(self, username, password):
        self.wait_for_element_visible(self.USERNAME).clear()
        self.wait_for_element_visible(self.USERNAME).send_keys(username)
        self.wait_for_element_visible(self.PASSWORD).clear()
        self.wait_for_element_visible(self.PASSWORD).send_keys(password)
        self.wait_for_clickable(self.LOGIN_BUTTON).click()
        
    def is_message_displayed(self):
        return self.wait_for_element_visible(self.SUCCESS_MESSAGE).is_displayed()
    
    def get_flash_message(self):
        return self.wait_for_element_visible(self.SUCCESS_MESSAGE).text
