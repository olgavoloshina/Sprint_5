import pytest
from locators import Locators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_login_from_main_page(driver):
    driver.get("https://stellarburgers.nomoreparties.site/")
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable(Locators.LOGIN_FROM_MAIN_BUTTON)).click()
    WebDriverWait(driver, 10).until(EC.presence_of_element_located(Locators.LOGIN_EMAIL_INPUT)).send_keys("test_user_001@yandex.ru")
    driver.find_element(*Locators.LOGIN_PASSWORD_INPUT).send_keys("password123")
    driver.find_element(*Locators.LOGIN_SUBMIT_BUTTON).click()
    assert "Личный кабинет" in driver.page_source

def test_login_from_personal_account_button(driver):
    driver.get("https://stellarburgers.nomoreparties.site/")
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable(Locators.LOGIN_FROM_PERSONAL_BUTTON)).click()
    WebDriverWait(driver, 10).until(EC.presence_of_element_located(Locators.LOGIN_EMAIL_INPUT)).send_keys("test_user_001@yandex.ru")
    driver.find_element(*Locators.LOGIN_PASSWORD_INPUT).send_keys("password123")
    driver.find_element(*Locators.LOGIN_SUBMIT_BUTTON).click()
    assert "Личный кабинет" in driver.page_source
