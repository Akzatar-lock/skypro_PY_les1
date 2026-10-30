import os
import sys

import pytest
from selenium import webdriver

# Чтобы импорты вида "from pages..." работали при запуске
# pytest lesson_07 из корня проекта
sys.path.insert(0, os.path.dirname(__file__))


@pytest.fixture
def chrome_driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


@pytest.fixture
def firefox_driver():
    driver = webdriver.Firefox()
    yield driver
    driver.quit()
