from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from locators import Locators as L
from tests.data import VALID_EMAIL, VALID_PASSWORD
from urls import Url


def test_login_from_home_page_button(driver):
    # Открываем главную страницу.
    driver.get(Url.HOME_PAGE)

    # Нажимаем «Войти в аккаунт».
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(L.HOME_LOGIN_BUTTON)
    ).click()

    # Ждём открытия страницы входа.
    WebDriverWait(driver, 10).until(
        lambda browser: browser.current_url.rstrip("/")
        == Url.LOGIN_PAGE.rstrip("/")
    )

    # Вводим email заранее зарегистрированного аккаунта.
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(L.EMAIL_INPUT)
    ).send_keys(VALID_EMAIL)

    # Вводим пароль заранее зарегистрированного аккаунта.
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(L.PASSWORD_INPUT)
    ).send_keys(VALID_PASSWORD)

    # Нажимаем «Войти».
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(L.LOGIN_BUTTON)
    ).click()

    # Ждём перехода на главную страницу после входа.
    WebDriverWait(driver, 10).until(
        lambda browser: browser.current_url.rstrip("/")
        == Url.HOME_PAGE.rstrip("/")
    )

    # Проверяем успешный вход.
    assert driver.current_url.rstrip("/") == Url.HOME_PAGE.rstrip("/")


def test_login_via_personal_account_button(driver):
    # Открываем главную страницу.
    driver.get(Url.HOME_PAGE)

    # Нажимаем «Личный кабинет».
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(L.PERSONAL_ACCOUNT_LINK)
    ).click()

    # Для неавторизованного пользователя должна открыться страница входа.
    WebDriverWait(driver, 10).until(
        lambda browser: browser.current_url.rstrip("/")
        == Url.LOGIN_PAGE.rstrip("/")
    )

    # Вводим email аккаунта.
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(L.EMAIL_INPUT)
    ).send_keys(VALID_EMAIL)

    # Вводим пароль аккаунта.
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(L.PASSWORD_INPUT)
    ).send_keys(VALID_PASSWORD)

    # Отправляем форму входа.
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(L.LOGIN_BUTTON)
    ).click()

    # Ждём перехода на главную страницу.
    WebDriverWait(driver, 10).until(
        lambda browser: browser.current_url.rstrip("/")
        == Url.HOME_PAGE.rstrip("/")
    )

    # Проверяем успешный вход.
    assert driver.current_url.rstrip("/") == Url.HOME_PAGE.rstrip("/")


def test_login_from_registration_page(driver):
    # Открываем страницу регистрации.
    driver.get(Url.REGISTER_PAGE)

    # Нажимаем ссылку перехода ко входу.
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(L.LOGIN_LINK)
    ).click()

    # Ждём открытия страницы входа.
    WebDriverWait(driver, 10).until(
        lambda browser: browser.current_url.rstrip("/")
        == Url.LOGIN_PAGE.rstrip("/")
    )

    # Вводим email аккаунта.
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(L.EMAIL_INPUT)
    ).send_keys(VALID_EMAIL)

    # Вводим пароль аккаунта.
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(L.PASSWORD_INPUT)
    ).send_keys(VALID_PASSWORD)

    # Нажимаем кнопку входа.
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(L.LOGIN_BUTTON)
    ).click()

    # Ждём перехода на главную страницу.
    WebDriverWait(driver, 10).until(
        lambda browser: browser.current_url.rstrip("/")
        == Url.HOME_PAGE.rstrip("/")
    )

    # Проверяем успешный вход.
    assert driver.current_url.rstrip("/") == Url.HOME_PAGE.rstrip("/")


def test_login_from_forgot_password_page(driver):
    # Открываем страницу восстановления пароля.
    driver.get(Url.FORGOT_PASSWORD_PAGE)

    # Нажимаем ссылку перехода ко входу.
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(L.LOGIN_LINK)
    ).click()

    # Ждём открытия страницы входа.
    WebDriverWait(driver, 10).until(
        lambda browser: browser.current_url.rstrip("/")
        == Url.LOGIN_PAGE.rstrip("/")
    )

    # Вводим email аккаунта.
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(L.EMAIL_INPUT)
    ).send_keys(VALID_EMAIL)

    # Вводим пароль аккаунта.
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(L.PASSWORD_INPUT)
    ).send_keys(VALID_PASSWORD)

    # Отправляем форму входа.
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(L.LOGIN_BUTTON)
    ).click()

    # Ждём перехода на главную страницу.
    WebDriverWait(driver, 10).until(
        lambda browser: browser.current_url.rstrip("/")
        == Url.HOME_PAGE.rstrip("/")
    )

    # Проверяем успешный вход.
    assert driver.current_url.rstrip("/") == Url.HOME_PAGE.rstrip("/")