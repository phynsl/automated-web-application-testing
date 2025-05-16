from framework.core.base_page import BasePage

def test_login_success(browser):
    page = BasePage(browser)
    page.open("https://example.com/login")
    page.find_element("input#username").send_keys("testuser")
    page.find_element("input#password").send_keys("password123")
    page.find_element("button#login").click()
    asser "Dashboard" in browser.title
