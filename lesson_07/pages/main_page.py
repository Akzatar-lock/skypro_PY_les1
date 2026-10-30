from selenium.webdriver.common.by import By


class MainPage:
    def __init__(self, driver):
        self.driver = driver

    def add_to_cart(self, product_name):
        slug = product_name.lower().replace(" ", "-")
        selector = f"[data-test='add-to-cart-{slug}']"
        self.driver.find_element(
            By.CSS_SELECTOR, selector
        ).click()

    def go_to_cart(self):
        self.driver.find_element(
            By.CLASS_NAME, "shopping_cart_link"
        ).click()
