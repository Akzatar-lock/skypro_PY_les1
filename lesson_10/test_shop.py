from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from pages.login_page import LoginPage
from pages.main_page import MainPage


def test_shop(firefox_driver):
    login_page = LoginPage(firefox_driver)
    login_page.open()
    login_page.login("standard_user", "secret_sauce")

    main_page = MainPage(firefox_driver)
    main_page.add_to_cart("Sauce Labs Backpack")
    main_page.add_to_cart("Sauce Labs Bolt T-Shirt")
    main_page.add_to_cart("Sauce Labs Onesie")
    main_page.go_to_cart()

    cart_page = CartPage(firefox_driver)
    cart_page.checkout()

    checkout_page = CheckoutPage(firefox_driver)
    checkout_page.fill_form("Иван", "Петров", "123456")
    total = checkout_page.get_total()
    assert total == "$58.29"
