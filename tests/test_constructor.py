from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from locators import Locators as L
from urls import Url


class TestConstructor:
    def test_buns_tab_can_be_selected(self, driver):
        # Открываем конструктор.
        driver.get(Url.home_page)

        # Сначала выбираем «Соусы», чтобы переход на «Булки» был проверяемым.
        sauces_tab = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(L.sauces_tab)
        )
        sauces_tab.click()

        # Ждём, пока «Соусы» станут активной вкладкой.
        WebDriverWait(driver, 10).until(
            lambda browser: "tab_type_current"
            in (browser.find_element(*L.sauces_tab).get_attribute("class") or "")
        )

        # Переходим на вкладку «Булки».
        buns_tab = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(L.buns_tab)
        )
        buns_tab.click()

        # Ждём, пока «Булки» станут активной вкладкой.
        WebDriverWait(driver, 10).until(
            lambda browser: "tab_type_current"
            in (browser.find_element(*L.buns_tab).get_attribute("class") or "")
        )

        # Проверяем, что вкладка «Булки» активна.
        assert "tab_type_current" in (buns_tab.get_attribute("class") or "")


    def test_sauces_tab_can_be_selected(self, driver):
        # Открываем конструктор.
        driver.get(Url.home_page)


        # Переходим на вкладку «Соусы».
        sauces_tab = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(L.sauces_tab)
        )
        sauces_tab.click()

        # Ждём, пока «Соусы» станут активной вкладкой.
        WebDriverWait(driver, 10).until(
            lambda browser: "tab_type_current"
            in (browser.find_element(*L.sauces_tab).get_attribute("class") or "")
        )

        # Проверяем, что вкладка «Соусы» активна.
        assert "tab_type_current" in (sauces_tab.get_attribute("class") or "")


    def test_fillings_tab_can_be_selected(self, driver):
        # Открываем конструктор.
        driver.get(Url.home_page)

    
        # Переходим на вкладку «Начинки».
        fillings_tab = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(L.fillings_tab)
        )
        fillings_tab.click()

        # Ждём, пока «Начинки» станут активной вкладкой.
        WebDriverWait(driver, 10).until(
            lambda browser: "tab_type_current"
            in (browser.find_element(*L.fillings_tab).get_attribute("class") or "")
        )

        # Проверяем, что вкладка «Начинки» активна.
        assert "tab_type_current" in (fillings_tab.get_attribute("class") or "")