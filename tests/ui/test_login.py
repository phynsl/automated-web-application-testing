import pytest
from framework.pages.login_page import LoginPage

@pytest.mark.ui
def test_successful_login(driver):
    page = LoginPage(driver)
    page.login("testuser@example.com", "password123")
    assert "selfconcept" in driver.current_url

@pytest.mark.ui
def test_login_wrong_password(driver):
    page = LoginPage(driver)
    page.login("testuser@example.com", "wrongpass")
    assert "Invalid password" in page.get_password_error()

@pytest.mark.ui
def test_login_unknown_email(driver):
    page = LoginPage(driver)
    page.login("nouser@example.com", "password123")
    assert "Email not found" in page.get_email_error()

