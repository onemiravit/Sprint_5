from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from locators import Locators as L
from data import valid_email, valid_password
from urls import Url


class TestLogin:
    def test_login_from_home_page_button(self, driver):
        # Открываем главную страницу.
        driver.get(Url.home_page)

        # Нажимаем «Войти в аккаунт».
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(L.home_login_button)
        ).click()

        # Ждём открытия страницы входа.
        WebDriverWait(driver, 10).until(
            lambda browser: browser.current_url.rstrip("/")
            == Url.login_page.rstrip("/")
        )

        # Вводим email и пароль заранее зарегистрированного аккаунта.
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(L.email_input)
        ).send_keys(valid_email)
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(L.password_input)
        ).send_keys(valid_password)

        # Нажимаем «Войти».
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(L.login_button)
        ).click()

        # Ждём перехода на главную страницу после входа.
        WebDriverWait(driver, 10).until(
            lambda browser: browser.current_url.rstrip("/")
            == Url.home_page.rstrip("/")
        )

        # Проверяем успешный вход.
        assert driver.current_url.rstrip("/") == Url.home_page.rstrip("/")

    def test_login_via_personal_account_button(self, driver):
        # Открываем главную страницу.
        driver.get(Url.home_page)

        # Нажимаем «Личный кабинет».
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(L.personal_account_link)
        ).click()

        # Ждём открытия страницы входа.
        WebDriverWait(driver, 10).until(
            lambda browser: browser.current_url.rstrip("/")
            == Url.login_page.rstrip("/")
        )

        # Вводим email и пароль аккаунта.
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(L.email_input)
        ).send_keys(valid_email)
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(L.password_input)
        ).send_keys(valid_password)

        # Отправляем форму входа.
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(L.login_button)
        ).click()

        # Ждём перехода на главную страницу после входа.
        WebDriverWait(driver, 10).until(
            lambda browser: browser.current_url.rstrip("/")
            == Url.home_page.rstrip("/")
        )

        # Проверяем успешный вход.
        assert driver.current_url.rstrip("/") == Url.home_page.rstrip("/")

    def test_login_from_registration_page(self, driver):
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

        # Вводим email и пароль аккаунта.
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(L.email_input)
        ).send_keys(valid_email)
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(L.password_input)
        ).send_keys(valid_password)

        # Нажимаем кнопку входа.
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(L.login_button)
        ).click()

        # Ждём перехода на главную страницу после входа.
        WebDriverWait(driver, 10).until(
            lambda browser: browser.current_url.rstrip("/")
            == Url.home_page.rstrip("/")
        )

        # Проверяем успешный вход.
        assert driver.current_url.rstrip("/") == Url.home_page.rstrip("/")

    def test_login_from_forgot_password_page(self, driver):
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

        # Вводим email и пароль аккаунта.
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(L.email_input)
        ).send_keys(valid_email)
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(L.password_input)
        ).send_keys(valid_password)

        # Отправляем форму входа.
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(L.login_button)
        ).click()

        # Ждём перехода на главную страницу после входа.
        WebDriverWait(driver, 10).until(
            lambda browser: browser.current_url.rstrip("/")
            == Url.home_page.rstrip("/")
        )

        # Проверяем успешный вход.
        assert driver.current_url.rstrip("/") == Url.home_page.rstrip("/")