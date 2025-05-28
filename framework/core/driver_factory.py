from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from framework.config import settings

def get_driver():
    browser = settings.SELENIUM_BROWSER.lower()

    if browser == "chrome":
        options = ChromeOptions()
        options.add_argument("--start-maximized")
        return webdriver.Chrome(service=ChromeService(), options=options)

    elif browser == "firefox":
        options = FirefoxOptions()
        options.add_argument("--width=1920")
        options.add_argument("--height=1080")
        return webdriver.Firefox(service=FirefoxService(), options=options)

    else:
        raise ValueError(f"Unsupported browser: {browser}")

