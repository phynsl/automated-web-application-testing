import pytest
import random
from framework.pages.register_page import RegisterPage
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

@pytest.mark.ui
def test_successful_registration(driver):
    page = RegisterPage(driver)
    email = f"new{random.randint(1000,9999)}@example.com"
    result = page.register("newuser", email, "pass123", "pass123")
    assert result

    assert driver.find_element(By.ID, "email").is_displayed()


@pytest.mark.ui
def test_registration_password_mismatch(driver):
    page = RegisterPage(driver)
    alert_text = page.register_expect_alert("user", "user@example.com", "pass1", "pass2")
    assert alert_text == "Passwords do not match"

@pytest.mark.ui
def test_registration_existing_email(driver):
    page = RegisterPage(driver)
    existing_email = "testuser@example.com"
    alert_text = page.register_expect_alert("user", existing_email, "password123", "password123")
    assert alert_text == "Email already registered"
