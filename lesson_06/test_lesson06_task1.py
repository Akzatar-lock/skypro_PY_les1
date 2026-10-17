import os

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_dynamic_loading():
    driver = webdriver.Chrome()

    try:
        # 1. Открываем страницу
        driver.get("https://the-internet.herokuapp.com/dynamic_loading/2")

        # 2. Находим и нажимаем кнопку Start
        start_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "#start button"))
        )
        start_button.click()

        # 3. Явно ждём появления текста Hello World!
        WebDriverWait(driver, 10).until(
            EC.text_to_be_present_in_element(
                (By.CSS_SELECTOR, "#finish"), "Hello World!"
            )
        )

        text = driver.find_element(By.CSS_SELECTOR, "#finish h4").text

        # 4. Скриншот
        screenshot_path = os.path.join(
            os.path.dirname(__file__), "dynamic_loading.png"
        )
        driver.save_screenshot(screenshot_path)

        # 5. Проверка
        assert text == "Hello World!"

    finally:
        driver.quit()
