from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class CalculatorPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = (
            "https://bonigarcia.dev/selenium-webdriver-java/"
            "slow-calculator.html"
        )

    def open(self):
        self.driver.get(self.url)

    def set_delay(self, seconds):
        delay_input = self.driver.find_element(By.ID, "delay")
        delay_input.clear()
        delay_input.send_keys(str(seconds))

    def click_button(self, text):
        button = self.driver.find_element(
            By.XPATH, f"//span[text()='{text}']"
        )
        button.click()

    def wait_for_result(self, expected, timeout=50):
        wait = WebDriverWait(self.driver, timeout)
        wait.until(
            EC.text_to_be_present_in_element(
                (By.CLASS_NAME, "screen"), expected
            )
        )
        return self.driver.find_element(
            By.CLASS_NAME, "screen"
        ).text
