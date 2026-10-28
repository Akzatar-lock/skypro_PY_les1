from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_03_shop():
    driver = webdriver.Firefox()
    driver.get("https://www.saucedemo.com/")
    wait = WebDriverWait(driver, 10)

    # Авторизация
    user_name = wait.until(
        EC.presence_of_element_located((By.ID, "user-name"))
    )
    user_name.send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    # Добавляем товары в корзину
    backpack = wait.until(
        EC.element_to_be_clickable(
            (By.ID, "add-to-cart-sauce-labs-backpack")
        )
    )
    backpack.click()

    t_shirt_id = "add-to-cart-sauce-labs-bolt-t-shirt"
    driver.find_element(By.ID, t_shirt_id).click()

    onesie_id = "add-to-cart-sauce-labs-onesie"
    driver.find_element(By.ID, onesie_id).click()

    # Переходим в корзину
    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()

    # Checkout
    wait.until(EC.element_to_be_clickable((By.ID, "checkout"))).click()

    # Заполняем форму
    first_name = wait.until(
        EC.presence_of_element_located((By.ID, "first-name"))
    )
    first_name.send_keys("Иван")

    driver.find_element(By.ID, "last-name").send_keys("Петров")
    driver.find_element(By.ID, "postal-code").send_keys("123456")
    driver.find_element(By.ID, "continue").click()

    # Читаем итоговую стоимость
    total_element = wait.until(
        EC.presence_of_element_located(
            (By.CLASS_NAME, "summary_total_label")
        )
    )
    total_text = total_element.text  # Например: "Total: $58.29"

    driver.quit()

    # Проверяем сумму
    assert total_text == "Total: $58.29", (
        f"Ожидалось 'Total: $58.29', получено '{total_text}'"
    )
