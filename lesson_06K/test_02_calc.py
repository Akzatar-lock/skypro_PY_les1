from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_02_calc():
    driver = webdriver.Chrome()
    url = (
        "https://bonigarcia.dev/"
        "selenium-webdriver-java/slow-calculator.html"
    )
    driver.get(url)

    # Вводим задержку 45
    delay_input = driver.find_element(By.ID, "delay")
    delay_input.clear()
    delay_input.send_keys("45")

    # Нажимаем кнопки: 7 + 8 =
    driver.find_element(By.XPATH, "//span[text()='7']").click()
    driver.find_element(By.XPATH, "//span[text()='+']").click()
    driver.find_element(By.XPATH, "//span[text()='8']").click()
    driver.find_element(By.XPATH, "//span[text()='=']").click()

    # Ждём результат 15 (таймаут больше 45 секунд)
    wait = WebDriverWait(driver, 50)
    result = wait.until(
        EC.text_to_be_present_in_element(
            (By.CSS_SELECTOR, ".screen"), "15"
        )
    )
    assert result, "Результат 15 не отобразился за отведённое время"

    driver.quit()
