from selenium import webdriver

driver = webdriver.Chrome()

# Открываем страницу
driver.get("https://www.google.com")

# Выводим заголовок страницы
print("Заголовок:", driver.title)

# Выводим текущий URL
print("URL:", driver.current_url)

# Обновляем страницу
driver.refresh()

# Закрываем браузер
driver.quit()