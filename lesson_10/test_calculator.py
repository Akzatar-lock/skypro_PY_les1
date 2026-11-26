from pages.calculator_page import CalculatorPage


def test_calculator(chrome_driver):
    page = CalculatorPage(chrome_driver)
    page.open()
    page.set_delay(45)
    page.click_button("7")
    page.click_button("+")
    page.click_button("8")
    page.click_button("=")

    result = page.wait_for_result("15")
    assert result == "15"
