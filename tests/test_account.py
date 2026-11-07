from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from locators import Locators as L
from tests.data import valid_email, valid_password
from urls import Url


def test_login_from_home_page_button(driver):           # Открываем главную страницу.
    
    driver.get(Url.home_page)

    
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(L.home_login_button) # Нажимаем «Войти в аккаунт».
    ).click()

    
    WebDriverWait(driver, 10).until(
        lambda browser: browser.current_url.rstrip("/") # Ждём открытия страницы входа.
        == Url.login_page.rstrip("/")
    )

    
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(L.email_input) # Вводим email заранее зарегистрированного аккаунта.
    ).send_keys(valid_email)

   
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(L.password_input)   # Вводим пароль заранее зарегистрированного аккаунта.
    ).send_keys(valid_password)

    
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(L.login_button)          # Нажимаем «Войти».
    ).click()

    
    WebDriverWait(driver, 10).until(
        lambda browser: browser.current_url.rstrip("/") # Ждём перехода на главную страницу после входа.
        == Url.home_page.rstrip("/")
    )

    
    assert driver.current_url.rstrip("/") == Url.home_page.rstrip("/")  # Проверяем успешный вход.


def test_login_via_personal_account_button(driver):
    # Открываем главную страницу.
    driver.get(Url.home_page)

    # Нажимаем «Личный кабинет».
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(L.personal_account_link)
    ).click()

    # Для неавторизованного пользователя должна открыться страница входа.
    WebDriverWait(driver, 10).until(
        lambda browser: browser.current_url.rstrip("/")
        == Url.login_page.rstrip("/")
    )

    # Вводим email аккаунта.
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(L.email_input)
    ).send_keys(valid_email)

    # Вводим пароль аккаунта.
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(L.password_input)
    ).send_keys(valid_password)

    # Отправляем форму входа.
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(L.login_button)
    ).click()

    # Ждём перехода на главную страницу.
    WebDriverWait(driver, 10).until(
        lambda browser: browser.current_url.rstrip("/")
        == Url.home_page.rstrip("/")
    )

    # Проверяем успешный вход.
    assert driver.current_url.rstrip("/") == Url.home_page.rstrip("/")


def test_login_from_registration_page(driver):
    # Открываем страницу регистрации.
    driver.get(Url.register_page)

    # Нажимаем ссылку перехода ко входу.
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(L.login_link)
    ).click()

    # Ждём открытия страницы входа.
    WebDriverWait(driver, 10).until(
        lambda browser: browser.current_url.rstrip("/")
        == Url.login_page.rstrip("/")
    )

    # Вводим email аккаунта.
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(L.email_input)
    ).send_keys(valid_email)

    # Вводим пароль аккаунта.
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(L.password_input)
    ).send_keys(valid_password)

    # Нажимаем кнопку входа.
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(L.login_button)
    ).click()

    # Ждём перехода на главную страницу.
    WebDriverWait(driver, 10).until(
        lambda browser: browser.current_url.rstrip("/")
        == Url.home_page.rstrip("/")
    )

    # Проверяем успешный вход.
    assert driver.current_url.rstrip("/") == Url.home_page.rstrip("/")


def test_login_from_forgot_password_page(driver):
    # Открываем страницу восстановления пароля.
    driver.get(Url.forgot_password_page)

    # Нажимаем ссылку перехода ко входу.
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(L.login_link)
    ).click()

    # Ждём открытия страницы входа.
    WebDriverWait(driver, 10).until(
        lambda browser: browser.current_url.rstrip("/")
        == Url.login_page.rstrip("/")
    )

    # Вводим email аккаунта.
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(L.email_input)
    ).send_keys(valid_email)

    # Вводим пароль аккаунта.
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(L.password_input)
    ).send_keys(valid_password)

    # Отправляем форму входа.
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(L.login_button)
    ).click()

    # Ждём перехода на главную страницу.
    WebDriverWait(driver, 10).until(
        lambda browser: browser.current_url.rstrip("/")
        == Url.home_page.rstrip("/")
    )

    # Проверяем успешный вход.
    assert driver.current_url.rstrip("/") == Url.home_page.rstrip("/")