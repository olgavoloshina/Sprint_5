import pytest
from locators import Locators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_navigation_to_personal_account(driver):
    driver.get("https://stellarburgers.nomoreparties.site/")
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable(Locators.PERSONAL_CABINET_BUTTON)).click()
    assert "Профиль" in driver.page_source

def test_navigation_to_logo(driver):
    driver.get("https://stellarburgers.nomoreparties.site/")
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable(Locators.LOGO_BUTTON)).click()
    assert "Главная" in driver.page_source
