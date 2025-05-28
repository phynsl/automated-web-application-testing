from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from framework.config import settings

def wait_for_element(driver, locator, timeout=settings.SELENIUM_TIMEOUT):
    return WebDriverWait(driver, timeout).until(EC.presence_of_element_located(locator))

