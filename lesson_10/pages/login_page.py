from selenium.webdriver.common.by import By


class LoginPage:
    """Page Object для страницы авторизации."""

    def __init__(self, driver) -> None:
        """
        Инициализировать страницу авторизации.

        :param driver: экземпляр WebDriver
        :return: None
        """
        self.driver = driver
        self.url = "https://www.saucedemo.com/"

    def open(self) -> None:
        """
        Открыть страницу авторизации.

        :return: None
        """
        self.driver.get(self.url)

    def login(self, username: str, password: str) -> None:
        """
        Ввести логин, пароль и нажать кнопку входа.

        :param username: имя пользователя
        :param password: пароль
        :return: None
        """
        self.driver.find_element(
            By.ID, "user-name"
        ).send_keys(username)
        self.driver.find_element(
            By.ID, "password"
        ).send_keys(password)
        self.driver.find_element(
            By.ID, "login-button"
        ).click()
