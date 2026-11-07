from selenium.webdriver.common.by import By


class Locators:
    # Поле «Имя» на странице регистрации.
    name_input = (
        By.XPATH,
        "//label[normalize-space(.)='Имя']/following-sibling::input[1]",
    )

    # Поле «Email» на страницах регистрации и входа.
    email_input = (
        By.XPATH,
        "//label[normalize-space(.)='Email']/following-sibling::input[1]",
    )

    # Поле «Пароль» на страницах регистрации и входа.
    password_input = (
        By.XPATH,
        "//label[normalize-space(.)='Пароль']/following-sibling::input[1]",
    )

    # Кнопка отправки формы регистрации.
    register_button = (
        By.XPATH,
        "//button[normalize-space(.)='Зарегистрироваться']",
    )

    # Сообщение об ошибке в поле при некорректном пароле.
    password_error = (
        By.XPATH,
        "//*[contains(@class, 'input__error')]",
    )

    # Кнопка «Войти в аккаунт» на главной странице.
    home_login_button = (
        By.XPATH, 
        "//*[self::button or self::a]"
        "[normalize-space(.)='Войти в аккаунт']",
    )
        

    # Ссылка «Личный кабинет» в шапке сайта.
    personal_account_link = (
        By.XPATH,
        "//a[contains(@href, '/account')]",
    )

    # Ссылка для перехода к форме входа.
    login_link = (
        By.XPATH,
        "//a[text()= 'Войти']",
    )

    # Кнопка отправки формы входа.
    login_button = (
        By.XPATH,
        "//button[normalize-space(.)='Войти']",
    )

    # Кнопка выхода из личного кабинета.
    logout_button = (
        By.XPATH,
        "//button[normalize-space(.)='Выйти' "
        "or normalize-space(.)='Выход']",
    )

    # Ссылка «Конструктор» в шапке сайта.
    constructor_link = (
        By.XPATH,
        "//a[.//p[normalize-space(.)='Конструктор']]",
    )

    # Логотип, ведущий на главную страницу.
    logo_link = (
        By.XPATH,
        "//a[@href='/' and .//*[local-name()='svg']]",
    )

    # Вкладка конструктора «Булки».
    buns_tab = (
        By.XPATH,
        "//*[contains(@class, 'tab_tab') "
        "and .//span[normalize-space(.)='Булки']]",
    )

    # Вкладка конструктора «Соусы».
    sauces_tab = (
        By.XPATH,
        "//*[contains(@class, 'tab_tab') "
        "and .//span[normalize-space(.)='Соусы']]",
    )

    # Вкладка конструктора «Начинки».
    fillings_tab = (
        By.XPATH,
        "//*[contains(@class, 'tab_tab') "
        "and .//span[normalize-space(.)='Начинки']]",
    )