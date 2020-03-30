import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_product_page_contains_a_button_to_add_to_cart(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
    browser.implicitly_wait(10)
    browser.get(link)
    # time.sleep(30)

    add_btn = WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, 'btn-add-to-basket'))
    )

    assert add_btn, 'success if add button exist'