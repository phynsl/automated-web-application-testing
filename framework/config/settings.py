import os

BASE_URL = "http://localhost/selfconcept"

SELENIUM_BROWSER = "chrome"
SELENIUM_TIMEOUT = 10
HEADLESS = os.getenv("HEADLESS", "true").lower() == "true"
