from selenium.webdriver.common.by import By


class CheckoutPage:
    """Page Object для страницы оформления заказа."""

    def __init__(self, driver) -> None:
        """
        Инициализировать страницу оформления заказа.

        :param driver: экземпляр WebDriver
        :return: None
        """
        self.driver = driver

    def fill_form(self, first_name: str,
                  last_name: str, postal_code: str) -> None:
        """
        Заполнить форму данными покупателя и продолжить.

        :param first_name: имя
        :param last_name: фамилия
        :param postal_code: почтовый индекс
        :return: None
        """
        self.driver.find_element(
            By.ID, "first-name"
        ).send_keys(first_name)
        self.driver.find_element(
            By.ID, "last-name"
        ).send_keys(last_name)
        self.driver.find_element(
            By.ID, "postal-code"
        ).send_keys(postal_code)
        self.driver.find_element(By.ID, "continue").click()

    def get_total(self) -> str:
        """
        Получить итоговую сумму заказа без текста 'Total: '.

        :return: строка с итоговой суммой (например, '$58.29')
        """
        total = self.driver.find_element(
            By.CLASS_NAME, "summary_total_label"
        )
        return total.text.replace("Total: ", "")
