from selenium.webdriver.common.by import By


class Locators:
    # Поле «Имя» на странице регистрации.
    NAME_INPUT = (
        By.XPATH,
        "//label[normalize-space(.)='Имя']/following-sibling::input[1]",
    )

    # Поле «Email» на страницах регистрации и входа.
    EMAIL_INPUT = (
        By.XPATH,
        "//label[normalize-space(.)='Email']/following-sibling::input[1]",
    )

    # Поле «Пароль» на страницах регистрации и входа.
    PASSWORD_INPUT = (
        By.XPATH,
        "//label[normalize-space(.)='Пароль']/following-sibling::input[1]",
    )

    # Кнопка отправки формы регистрации.
    REGISTER_BUTTON = (
        By.XPATH,
        "//button[normalize-space(.)='Зарегистрироваться']",
    )

    # Сообщение об ошибке в поле при некорректном пароле.
    PASSWORD_ERROR = (
        By.XPATH,
        "//*[contains(@class, 'input__error')]",
    )

    # Кнопка «Войти в аккаунт» на главной странице.
    HOME_LOGIN_BUTTON = (
        By.XPATH,
        "//*[self::button or self::a]"
        "[normalize-space(.)='Войти в аккаунт']",
    )

    # Ссылка «Личный кабинет» в шапке сайта.
    PERSONAL_ACCOUNT_LINK = (
        By.XPATH,
        "//a[contains(@href, '/account')]",
    )

    # Ссылка для перехода к форме входа.
    LOGIN_LINK = (
        By.XPATH,
        "//a[contains(@href, '/login')]",
    )

    # Кнопка отправки формы входа.
    LOGIN_BUTTON = (
        By.XPATH,
        "//button[normalize-space(.)='Войти']",
    )

    # Кнопка выхода из личного кабинета.
    LOGOUT_BUTTON = (
        By.XPATH,
        "//button[normalize-space(.)='Выйти' "
        "or normalize-space(.)='Выход']",
    )

    # Ссылка «Конструктор» в шапке сайта.
    CONSTRUCTOR_LINK = (
        By.XPATH,
        "//a[.//p[normalize-space(.)='Конструктор']]",
    )

    # Логотип, ведущий на главную страницу.
    LOGO_LINK = (
        By.XPATH,
        "//a[@href='/' and .//*[local-name()='svg']]",
    )

    # Вкладка конструктора «Булки».
    BUNS_TAB = (
        By.XPATH,
        "//*[contains(@class, 'tab_tab') "
        "and .//span[normalize-space(.)='Булки']]",
    )

    # Вкладка конструктора «Соусы».
    SAUCES_TAB = (
        By.XPATH,
        "//*[contains(@class, 'tab_tab') "
        "and .//span[normalize-space(.)='Соусы']]",
    )

    # Вкладка конструктора «Начинки».
    FILLINGS_TAB = (
        By.XPATH,
        "//*[contains(@class, 'tab_tab') "
        "and .//span[normalize-space(.)='Начинки']]",
    )