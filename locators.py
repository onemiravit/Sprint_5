from selenium.webdriver.common.by import By

class Locators:
    # Локаторы для Регистрации

    name_reg = (By.XPATH, "//label[text()='Имя']")                          #Поле Имя (регистрация)
    email_reg = (By.XPATH, "//label[text()='Email']")                       #Поле Email (регистрация)
    password_reg = (By.XPATH, "//label[text()='Пароль']")                   #Поле Пароль (регистрация)
    reg_btn = (By.XPATH, "//button[text()='Зарегистрироваться']")       #Кнопка Зарегистрироваться (регистрация)

    # Вход в аккаунт

    login_btn_home_page = (By.XPATH, "//button[text()='Войти в аккаунт']")      #Кнопка войти в аккаунт на гл. странице
    email_login = (By.XPATH, "//input[@name='name' and @type='text']")          #Поле Email для входа в аккаунт
    password_login = (By.XPATH, "//input[@name='Пароль' and @type='password']") #Поле Пароль для входа в аккаунт
    login_btn_personal_account = (By.XPATH, "//button[text()='Войти']")         #Кнопка войти в личном кабинете

    # Кнопки на главной странице

    construktor_btn = (By.XPATH, "//p[text()='Конструктор']")                   #Кнопка Конструктор
    logo_btn = (By.XPATH,"//a[@CLASS='active']")                                #Кнопка - логотип на главной странице
    buns_btn = (By.XPATH, "//span[text()='Булки']")                             #Кнопка Булки
    sauces_btn = (By.XPATH, "//span[text()='Соусы']")                           #Кнопка Соусы
    fillings_btn = (By.XPATH, "//span[text()='Начинки']")                       #Кнопка Начинки