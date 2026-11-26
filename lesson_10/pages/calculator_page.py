from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class CalculatorPage:
    """Page Object для страницы калькулятора."""

    def __init__(self, driver) -> None:
        """
        Инициализировать страницу калькулятора.

        :param driver: экземпляр WebDriver (Chrome или Firefox)
        :return: None
        """
        self.driver = driver
        self.url = (
            "https://bonigarcia.dev/selenium-webdriver-java/"
            "slow-calculator.html"
        )

    def open(self) -> None:
        """
        Открыть страницу калькулятора в браузере.

        :return: None
        """
        self.driver.get(self.url)

    def set_delay(self, seconds: int) -> None:
        """
        Установить задержку вычислений.

        :param seconds: задержка в секундах
        :return: None
        """
        delay_input = self.driver.find_element(By.ID, "delay")
        delay_input.clear()
        delay_input.send_keys(str(seconds))

    def click_button(self, text: str) -> None:
        """
        Нажать на кнопку калькулятора по её тексту.

        :param text: текст на кнопке (например, "7", "+", "=")
        :return: None
        """
        button = self.driver.find_element(
            By.XPATH, f"//span[text()='{text}']"
        )
        button.click()

    def wait_for_result(self, expected: str, timeout: int = 50) -> str:
        """
        Дождаться появления ожидаемого результата на экране.

        :param expected: ожидаемый текст результата
        :param timeout: максимальное время ожидания (по умолчанию 50)
        :return: фактический текст результата
        """
        wait = WebDriverWait(self.driver, timeout)
        wait.until(
            EC.text_to_be_present_in_element(
                (By.CLASS_NAME, "screen"), expected
            )
        )
        return self.driver.find_element(
            By.CLASS_NAME, "screen"
        ).text
