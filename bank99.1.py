from selenium import webdriver

link = "http://www.demo.guru99.com/V4/"
  
try: 
    browser = webdriver.Chrome()
    browser.get(link)
    
    # Заполняем логин и пароль
    input1 = browser.find_element_by_name('uid').send_keys("mngr251053")
    input2 = browser.find_element_by_name('password').send_keys("yzEgArY")
    
    # Отправляем заполненную форму
    button = browser.find_element_by_name("btnLogin").click()
   
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    #time.sleep(2)
    # закрываем браузер после всех манипуляций
    #browser.quit()