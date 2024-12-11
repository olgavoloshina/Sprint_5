from selenium.webdriver.common.by import By


class Locators:
    # Страница регистрации
    REGISTRATION_NAME_INPUT = (By.XPATH, "//input[@name='name']")
    REGISTRATION_EMAIL_INPUT = (By.XPATH, "//input[@name='email']")
    REGISTRATION_PASSWORD_INPUT = (By.XPATH, "//input[@name='password']")
    REGISTRATION_SUBMIT_BUTTON = (By.XPATH, "//button[text()='Зарегистрироваться']")
    REGISTRATION_ERROR_MESSAGE = (By.XPATH, "//p[contains(text(), 'Некорректный пароль')]")

    # Страница входа
    LOGIN_EMAIL_INPUT = (By.XPATH, "//input[@name='email']")
    LOGIN_PASSWORD_INPUT = (By.XPATH, "//input[@name='password']")
    LOGIN_SUBMIT_BUTTON = (By.XPATH, "//button[text()='Войти']")
    LOGIN_FROM_MAIN_BUTTON = (By.XPATH, "//button[text()='Войти в аккаунт']")
    LOGIN_FROM_PERSONAL_BUTTON = (By.XPATH, "//a[text()='Личный кабинет']")

    # Переходы
    PERSONAL_CABINET_BUTTON = (By.XPATH, "//a[text()='Личный кабинет']")
    CONSTRUCTOR_BUTTON = (By.XPATH, "//p[text()='Конструктор']")
    LOGO_BUTTON = (By.XPATH, "//div[@class='AppHeader_logo__3u8TI']")

    # Конструктор
    CONSTRUCTOR_BUNS_TAB = (By.XPATH, "//span[text()='Булки']")
    CONSTRUCTOR_SAUCES_TAB = (By.XPATH, "//span[text()='Соусы']")
    CONSTRUCTOR_FILLINGS_TAB = (By.XPATH, "//span[text()='Начинки']")
