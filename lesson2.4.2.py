from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium import webdriver
import time, math
import os

def calc(x):
	return str(math.log(abs(12*math.sin(int(x)))))
    
link = "http://suninjuly.github.io/explicit_wait2.html"
  
try: 
    browser = webdriver.Chrome()
    browser.get(link)
    
    # Дождаться нужной цены
    option1 = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"),'100'))
    
    # Нажимаем на кнопку
    button = browser.find_element_by_id("book").click()

    x = browser.find_element_by_id("input_value").text
    y = calc(x)
    input1 = browser.find_element_by_id("answer").send_keys(y)

    # Отправляем заполненную форму
    button = browser.find_element_by_id("solve")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
   
