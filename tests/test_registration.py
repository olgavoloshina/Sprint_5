import pytest
from locators import Locators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_successful_registration(driver):
    driver.get("https://stellarburgers.nomoreparties.site/")
    WebDriverWait(driver, 10).until(EC.presence_of_element_located(Locators.REGISTRATION_NAME_INPUT)).send_keys("Test User")
    driver.find_element(*Locators.REGISTRATION_EMAIL_INPUT).send_keys("test_user_001@yandex.ru")
    driver.find_element(*Locators.REGISTRATION_PASSWORD_INPUT).send_keys("password123")
    driver.find_element(*Locators.REGISTRATION_SUBMIT_BUTTON).click()
    assert "Успешная регистрация" in driver.page_source

def test_invalid_password_registration(driver):
    driver.get("https://stellarburgers.nomoreparties.site/")
    WebDriverWait(driver, 10).until(EC.presence_of_element_located(Locators.REGISTRATION_NAME_INPUT)).send_keys("Test User")
    driver.find_element(*Locators.REGISTRATION_EMAIL_INPUT).send_keys("test_user_002@yandex.ru")
    driver.find_element(*Locators.REGISTRATION_PASSWORD_INPUT).send_keys("123")
    driver.find_element(*Locators.REGISTRATION_SUBMIT_BUTTON).click()
    assert WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(Locators.REGISTRATION_ERROR_MESSAGE)
    ).is_displayed()
