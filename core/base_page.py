from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open(self, url):
        self.driver.get(url)

    def get_title(self):
        return self.driver.title
    
    def wait_for_element_visible(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))
    
    def wait_for_clickable(self, locator):
        return self.wait.until(EC.element_to_be_clickable(locator))
