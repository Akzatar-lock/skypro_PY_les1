from selenium.webdriver.common.by import By


class CartPage:
    """Page Object для страницы корзины."""

    def __init__(self, driver) -> None:
        """
        Инициализировать страницу корзины.

        :param driver: экземпляр WebDriver
        :return: None
        """
        self.driver = driver

    def checkout(self) -> None:
        """
        Нажать кнопку оформления заказа (Checkout).

        :return: None
        """
        self.driver.find_element(By.ID, "checkout").click()

    def get_item_names(self) -> list[str]:
        """
        Получить список названий товаров в корзине.

        :return: список строк с названиями товаров
        """
        items = self.driver.find_elements(
            By.CLASS_NAME, "inventory_item_name"
        )
        return [item.text for item in items]
