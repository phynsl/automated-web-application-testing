import os

BASE_URL = os.getenv("BASE_URL", "https://example.com")
API_URL = os.getenv("API_URL", "https://api.example.com")
TIMEOUT = int(os.getenv("TIMEOUT", 10))
BROWSER = os.getenv("BROWSER", "chrome")
HEADLESS = os.getenv("HEADLESS", "true").lower() == "true"
