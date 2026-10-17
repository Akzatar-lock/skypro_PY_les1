from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


USER1_COOKIES = [
    {
        "name": "SESSION",
        "value": "MTIyMjBlZDItMDE3OS00NzE3LWE2OTUtNDM4ODc3YmI5MmEz",
        "domain": ".gitflic.ru",
        "path": "/",
        "secure": True,
        "httpOnly": True,
    },
    {
        "name": "X-CSRF-TOKEN",
        "value": "be835c2c-f8c3-4ac8-90c2-bc12d94d69c9",
        "domain": ".gitflic.ru",
        "path": "/",
        "secure": True,
        "httpOnly": True,
    },
]

USER2_COOKIES = [
    {
        "name": "SESSION",
        "value": "NGQyYzM0ZTQtZTRiMi00ZmIxLWE3YjYtYTQyNjVmYmViMmQx",
        "domain": ".gitflic.ru",
        "path": "/",
        "secure": True,
        "httpOnly": True,
    },
    {
        "name": "X-CSRF-TOKEN",
        "value": "7b428299-3733-4c3f-9829-04d73c43c1e7",
        "domain": ".gitflic.ru",
        "path": "/",
        "secure": True,
        "httpOnly": True,
    },
]


def add_cookies(driver, cookies):
    for cookie in cookies:
        allowed = {
            "name",
            "value",
            "path",
            "domain",
            "secure",
            "httpOnly",
            "expiry",
            "sameSite",
        }
        driver.add_cookie({k: v for k, v in cookie.items() if k in allowed})


def test_session_storage_auth():
    driver = webdriver.Chrome()

    try:
        driver.get("https://gitflic.ru/")

        add_cookies(driver, USER1_COOKIES)

        driver.refresh()

        driver.get("https://gitflic.ru/user/vladplazun")
        WebDriverWait(driver, 10).until(
            EC.url_contains("https://gitflic.ru/user/vladplazun")
        )
        url_user1 = driver.current_url

        driver.delete_all_cookies()
        driver.get("https://gitflic.ru/")

        add_cookies(driver, USER2_COOKIES)
        driver.refresh()

        driver.get("https://gitflic.ru/user/akzatar")
        WebDriverWait(driver, 10).until(
            EC.url_contains("https://gitflic.ru/user/akzatar")
        )
        url_user2 = driver.current_url

        assert url_user1 != url_user2, (
            f"URL должны различаться: {url_user1} и {url_user2}"
        )

    finally:
        driver.quit()
