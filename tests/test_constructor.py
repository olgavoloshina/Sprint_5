import pytest
from locators import Locators
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_constructor_buns_section(driver):
    driver.get("https://stellarburgers.nomoreparties.site/")
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable(Locators.CONSTRUCTOR_BUTTON)).click()
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable(Locators.CONSTRUCTOR_BUNS_TAB)).click()
    assert "Булки" in driver.page_source

def test_constructor_sauces_section(driver):
    driver.get("https://stellarburgers.nomoreparties.site/")
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable(Locators.CONSTRUCTOR_BUTTON)).click()
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable(Locators.CONSTRUCTOR_SAUCES_TAB)).click()
    assert "Соусы" in driver.page_source

def test_constructor_fillings_section(driver):
    driver.get("https://stellarburgers.nomoreparties.site/")
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable(Locators.CONSTRUCTOR_BUTTON)).click()
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable(Locators.CONSTRUCTOR_FILLINGS_TAB)).click()
    assert "Начинки" in driver.page_source
