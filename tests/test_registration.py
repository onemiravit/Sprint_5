import re

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from generators import generate_login, generate_password
from locators import Locators as L
from urls import Url


def test_successful_registration(driver):
    # Создаём данные для нового пользователя.
    name = "Alexey"
    email = generate_login()
    password = generate_password()

    # Проверяем, что имя не пустое, email соответствует формату,
    # а длина пароля не меньше шести символов.
    assert name.strip()
    assert re.fullmatch(r"alexey_mironov56\d{3}@gmail\.com", email)
    assert len(password) >= 6

    # Открываем страницу регистрации.
    driver.get(Url.REGISTER_PAGE)

    # Заполняем поле «Имя».
    name_input = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(L.NAME_INPUT)
    )
    name_input.send_keys(name)

    # Заполняем поле «Email».
    email_input = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(L.EMAIL_INPUT)
    )
    email_input.send_keys(email)

    # Заполняем поле «Пароль».
    password_input = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(L.PASSWORD_INPUT)
    )
    password_input.send_keys(password)

    # Проверяем, что поля содержат введённые значения.
    assert name_input.get_attribute("value") == name
    assert email_input.get_attribute("value") == email
    assert password_input.get_attribute("value") == password

    # Отправляем форму регистрации.
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(L.REGISTER_BUTTON)
    ).click()

    # Ждём перехода на страницу входа после успешной регистрации.
    WebDriverWait(driver, 10).until(
        lambda browser: browser.current_url.rstrip("/")
        == Url.LOGIN_PAGE.rstrip("/")
    )

    # Проверяем, что открылась страница входа.
    assert driver.current_url.rstrip("/") == Url.LOGIN_PAGE.rstrip("/")


def test_registration_shows_error_for_short_password(driver):
    # Для теста ошибки тоже создаём уникальный email,
    # но пароль генерируем длиной меньше шести символов.
    name = "Alexey"
    email = generate_login()
    password = generate_password(length=5)

    # Проверяем, что пароль короче минимальной длины.
    assert len(password) < 6

    # Открываем страницу регистрации.
    driver.get(Url.REGISTER_PAGE)

    # Заполняем поле «Имя».
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(L.NAME_INPUT)
    ).send_keys(name)

    # Заполняем поле «Email».
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(L.EMAIL_INPUT)
    ).send_keys(email)

    # Заполняем поле «Пароль» коротким значением.
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(L.PASSWORD_INPUT)
    ).send_keys(password)

    # Отправляем форму.
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(L.REGISTER_BUTTON)
    ).click()

    # Ждём отображения ошибки валидации.
    error = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(L.PASSWORD_ERROR)
    )

    # Проверяем, что отображается сообщение об ошибке пароля.
    error_text = error.text.lower()
    assert "парол" in error_text or "6" in error_text

    # Проверяем, что регистрация не завершилась переходом на страницу входа.
    assert driver.current_url.rstrip("/") == Url.REGISTER_PAGE.rstrip("/")