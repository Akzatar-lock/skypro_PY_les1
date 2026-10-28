import platform
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_01_form():
    # Настройка браузера в зависимости от ОС
    if platform.system() == "Windows":
        edge_options = webdriver.EdgeOptions()
        prefs = {
            "autofill.profile_enabled": False,
            "profile.password_manager_enabled": False,
            "credentials_enable_service": False
        }
        edge_options.add_experimental_option("prefs", prefs)
        driver = webdriver.Edge(options=edge_options)
    elif platform.system() == "Darwin":  # macOS
        driver = webdriver.Safari()
    else:
        driver = webdriver.Chrome()

    url = (
        "https://bonigarcia.dev/"
        "selenium-webdriver-java/data-types.html"
    )
    driver.get(url)
    wait = WebDriverWait(driver, 15)

    # Список полей для заполнения (кроме Email и Zip code)
    fields = [
        ("first-name", "Иван"),
        ("last-name", "Петров"),
        ("address", "Ленина, 55-3"),
        ("phone", "+7985899998787"),
        ("city", "Москва"),
        ("country", "Россия"),
        ("job-position", "QA"),
        ("company", "SkyPro")
    ]

    # Заполняем поля в цикле
    for name, value in fields:
        wait.until(
            EC.presence_of_element_located((By.NAME, name))
        ).send_keys(value)

    # Заполняем Email (используем type='email', чтобы точно найти поле)
    wait.until(
        EC.presence_of_element_located(
            (By.CSS_SELECTOR, "input[type='email']")
        )
    ).send_keys("test@skypro.com")

    # Zip code намеренно оставляем пустым

    # Нажимаем кнопку Submit
    submit_btn = wait.until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']"))
    )
    submit_btn.click()

    # Ждем перехода на страницу с результатами
    # На странице результатов у полей появляются классы alert
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".alert")))

    # 1. Проверяем, что поле Zip code подсвечено красным
    zip_field = driver.find_element(By.ID, "zip-code")
    assert "alert-danger" in zip_field.get_attribute("class"), (
        "Zip code должен быть красным"
    )

    # 2. Проверяем остальные поля на зеленый цвет
    # ВАЖНО: на странице результатов ID у почты меняется на "e-mail"
    valid_ids = [
        "first-name", "last-name", "address", "e-mail",
        "phone", "city", "country", "job-position", "company"
    ]

    for field_id in valid_ids:
        field = driver.find_element(By.ID, field_id)
        assert "alert-success" in field.get_attribute("class"), (
            f"Поле {field_id} должно быть зелёным"
        )

    # Закрываем браузер
    driver.quit()
