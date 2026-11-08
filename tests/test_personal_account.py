from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from locators import Locators as L
from data import valid_email, valid_password
from urls import Url


class TestPersonalAccount:
    def test_click_personal_account_opens_account_page(self, driver):
        # Открываем страницу входа.
        driver.get(Url.login_page)

        # Вводим данные заранее зарегистрированного аккаунта.
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(L.email_input)
        ).send_keys(valid_email)
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(L.password_input)
        ).send_keys(valid_password)

        # Входим и ждём открытия главной страницы.
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(L.login_button)
        ).click()
        WebDriverWait(driver, 10).until(
            lambda browser: browser.current_url.rstrip("/")
            == Url.home_page.rstrip("/")
        )

        # Нажимаем «Личный кабинет».
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(L.personal_account_link)
        ).click()

        # Проверяем, что открылся личный кабинет.
        WebDriverWait(driver, 10).until(
            lambda browser: browser.current_url.rstrip("/")
            == Url.account.rstrip("/")
        )
        assert driver.current_url.rstrip("/") == Url.account.rstrip("/")

    def test_constructor_link_from_account_opens_home_page(self, driver):
        # Открываем страницу входа.
        driver.get(Url.login_page)

        # Вводим данные тестового аккаунта.
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(L.email_input)
        ).send_keys(valid_email)
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(L.password_input)
        ).send_keys(valid_password)

        # Входим и ждём главную страницу.
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(L.login_button)
        ).click()
        WebDriverWait(driver, 10).until(
            lambda browser: browser.current_url.rstrip("/")
            == Url.home_page.rstrip("/")
        )

        # Открываем личный кабинет.
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(L.personal_account_link)
        ).click()
        WebDriverWait(driver, 10).until(
            lambda browser: browser.current_url.rstrip("/")
            == Url.account.rstrip("/")
        )

        # Нажимаем «Конструктор».
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(L.constructor_link)
        ).click()

        # Проверяем переход на главную страницу конструктора.
        WebDriverWait(driver, 10).until(
            lambda browser: browser.current_url.rstrip("/")
            == Url.home_page.rstrip("/")
        )
        assert driver.current_url.rstrip("/") == Url.home_page.rstrip("/")

    def test_logo_from_account_opens_home_page(self, driver):
        # Открываем страницу входа.
        driver.get(Url.login_page)

        # Вводим данные тестового аккаунта.
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(L.email_input)
        ).send_keys(valid_email)
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(L.password_input)
        ).send_keys(valid_password)

        # Входим и ждём главную страницу.
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(L.login_button)
        ).click()
        WebDriverWait(driver, 10).until(
            lambda browser: browser.current_url.rstrip("/")
            == Url.home_page.rstrip("/")
        )

        # Переходим в личный кабинет.
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(L.personal_account_link)
        ).click()
        WebDriverWait(driver, 10).until(
            lambda browser: browser.current_url.rstrip("/")
            == Url.account.rstrip("/")
        )

        # Нажимаем логотип Stellar Burgers.
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(L.logo_link)
        ).click()

        # Проверяем, что логотип вернул на главную страницу.
        WebDriverWait(driver, 10).until(
            lambda browser: browser.current_url.rstrip("/")
            == Url.home_page.rstrip("/")
        )
        assert driver.current_url.rstrip("/") == Url.home_page.rstrip("/")

    def test_logout_from_account(self, driver):
        # Открываем страницу входа.
        driver.get(Url.login_page)

        # Вводим данные тестового аккаунта.
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(L.email_input)
        ).send_keys(valid_email)
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(L.password_input)
        ).send_keys(valid_password)

        # Входим и ждём главную страницу.
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(L.login_button)
        ).click()
        WebDriverWait(driver, 10).until(
            lambda browser: browser.current_url.rstrip("/")
            == Url.home_page.rstrip("/")
        )

        # Переходим в личный кабинет.
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(L.personal_account_link)
        ).click()
        WebDriverWait(driver, 10).until(
            lambda browser: browser.current_url.rstrip("/")
            == Url.account.rstrip("/")
        )

        # Нажимаем кнопку выхода.
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(L.logout_button)
        ).click()

        # Проверяем, что после выхода открылась страница входа.
        WebDriverWait(driver, 10).until(
            lambda browser: browser.current_url.rstrip("/")
            == Url.login_page.rstrip("/")
        )
        assert driver.current_url.rstrip("/") == Url.login_page.rstrip("/")