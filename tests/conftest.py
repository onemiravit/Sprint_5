import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture
def driver():
    # Настраиваем запуск Chrome.
    options = Options()

    # Для запуска браузера без окна можно раскомментировать:
    # options.add_argument("--headless=new")

    # Создаём отдельный браузер для текущего теста.
    driver = webdriver.Chrome(options=options)

    try:
        # Разворачиваем окно браузера.
        driver.maximize_window()

        # Передаём браузер тесту.
        yield driver
    finally:
        # Закрываем браузер после завершения теста.
        driver.quit()