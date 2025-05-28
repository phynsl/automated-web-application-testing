from framework.core.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class LoginPage(BasePage):
    USERNAME_INPUT = (By.ID, "username")
    EMAIL_INPUT = (By.NAME, "email")
    PASSWORD_INPUT = (By.NAME, "password")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")
    ERROR_PASSWORD = (By.CLASS_NAME, "error-message")
    ERROR_MAIL = (By.CLASS_NAME, "error-mail")

    def __init__(self, driver):
        super().__init__(driver)
        self.open("http://localhost/selfconcept/login.html")

    def login(self, email, password):
        self.fill(self.EMAIL_INPUT, email)
        self.fill(self.PASSWORD_INPUT, password)
        self.click(self.LOGIN_BUTTON)

    def get_password_error(self):
        try:
            error_element = WebDriverWait(self.driver, 5).until(
                EC.visibility_of_element_located(self.ERROR_PASSWORD)
            )
            return error_element.text.strip()
        except:
            return ""

    def get_email_error(self):
        try:
            error_element = WebDriverWait(self.driver, 3).until(
                EC.visibility_of_element_located(self.ERROR_MAIL)
            )
            return error_element.text.strip()
        except:
            return ""
