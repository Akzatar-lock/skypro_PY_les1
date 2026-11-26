from selenium.webdriver.common.by import By


class MainPage:
    """Page Object для главной страницы магазина."""

    def __init__(self, driver) -> None:
        """
        Инициализировать главную страницу.

        :param driver: экземпляр WebDriver
        :return: None
        """
        self.driver = driver

    def add_to_cart(self, product_name: str) -> None:
        """
        Добавить товар в корзину по его названию.

        :param product_name: название товара
        :return: None
        """
        slug = product_name.lower().replace(" ", "-")
        selector = f"[data-test='add-to-cart-{slug}']"
        self.driver.find_element(
            By.CSS_SELECTOR, selector
        ).click()

    def go_to_cart(self) -> None:
        """
        Перейти в корзину.

        :return: None
        """
        self.driver.find_element(
            By.CLASS_NAME, "shopping_cart_link"
        ).click()
