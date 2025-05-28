from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class RegisterPage:
    URL = "http://localhost/selfconcept/reg.html"

    USERNAME_INPUT = (By.ID, "username")
    EMAIL_INPUT = (By.ID, "email")
    PASSWORD_INPUT = (By.ID, "password")
    CONFIRM_PASSWORD_INPUT = (By.ID, "confirm_password")
    SUBMIT_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")
    SUCCESS_MESSAGE = (By.ID, "success-message")

    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get(self.URL)

    def fill(self, locator, value):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(locator)
        ).send_keys(value)

    def click(self, locator):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(locator)
        ).click()

    def register(self, username, email, password, confirm_password):
        self.open()
        self.fill(self.USERNAME_INPUT, username)
        self.fill(self.EMAIL_INPUT, email)
        self.fill(self.PASSWORD_INPUT, password)
        self.fill(self.CONFIRM_PASSWORD_INPUT, confirm_password)
        self.click(self.SUBMIT_BUTTON)

        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.SUCCESS_MESSAGE)
        )

        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, "email"))
        )
        return True

    def register_expect_alert(self, username, email, password, confirm_password):
        self.open()
        self.fill(self.USERNAME_INPUT, username)
        self.fill(self.EMAIL_INPUT, email)
        self.fill(self.PASSWORD_INPUT, password)
        self.fill(self.CONFIRM_PASSWORD_INPUT, confirm_password)
        self.click(self.SUBMIT_BUTTON)
        return self.handle_alert()

    def handle_alert(self, timeout=10):
        try:
            WebDriverWait(self.driver, timeout).until(EC.alert_is_present())
            alert = self.driver.switch_to.alert
            alert_text = alert.text
            alert.accept()
            return alert_text
        except TimeoutException:
            return None

    def is_password_mismatch_alert(self):
        alert_text = self.handle_alert()
        return alert_text == "Passwords do not match"

    def is_email_already_registered_alert(self):
        alert_text = self.handle_alert()
        return alert_text == "Email already registered" 
