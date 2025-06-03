from selenium.webdriver.common.by import By

class IndexPage:
    def __init__(self, driver):
        self.driver = driver

    SIGN_IN_LINK = (By.LINK_TEXT, "Login")
    REGISTER_LINK = (By.LINK_TEXT, "Register")

    def load(self, base_url):
        self.driver.get(f"{base_url}/index.html")

    def go_to_login(self):
        self.driver.find_element(*self.SIGN_IN_LINK).click()

    def go_to_register(self):
        self.driver.find_element(*self.REGISTER_LINK).click()

