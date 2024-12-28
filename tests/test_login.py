import pytest
from pages.login_page import LoginPage
from utils.browser_setup import setup_browser
from utils.config import BASE_URL, VALID_USER, VALID_PASSWORD

@pytest.fixture
def browser():
    driver = setup_browser()
    yield driver
    driver.quit()

def test_valid_login(browser):
    browser.get(BASE_URL)
    login_page = LoginPage(browser)
    login_page.enter_username(VALID_USER)
    login_page.enter_password(VALID_PASSWORD)
    login_page.click_login()
    assert login_page.is_logged_in(), "Login failed for valid credentials"

def test_invalid_login(browser):
    browser.get(BASE_URL)
    login_page = LoginPage(browser)
    login_page.enter_username("invalid_user")
    login_page.enter_password("invalid_password")
    login_page.click_login()
    assert login_page.is_error_displayed(), "Error not displayed for invalid credentials"