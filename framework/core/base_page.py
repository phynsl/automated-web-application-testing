from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from framework.utils.logger import logger
from framework.utils.wait_utils import wait_for_element

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def open(self, url):
        logger.info(f"Opening URL: {url}")
        self.driver.get(url)

    def click(self, locator):
        logger.info(f"Clicking on: {locator}")
        wait_for_element(self.driver, locator).click()

    def fill(self, locator, text):
        logger.info(f"Filling {locator} with: {text}")
        element = wait_for_element(self.driver, locator)
        element.clear()
        element.send_keys(text)

    def get_text(self, locator):
        logger.info(f"Getting text from: {locator}")
        return wait_for_element(self.driver, locator).text
