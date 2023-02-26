from selenium.webdriver.common.by import By
import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_add_to_basket_button(browser):
    browser.get(link)
    time.sleep(30)
    assert browser.find_element(By.CSS_SELECTOR, "[class = 'btn btn-lg btn-primary "
                                                 "btn-add-to-basket']").is_displayed(), 'Button "add to basket" is ' \
                                                                                        'NOT displayed '
