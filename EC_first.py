from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math
import os


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/explicit_wait2.html")
    WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, "price"), "100"))
    button = browser.find_element(By.ID, "book")
    button.click()
    # button1 = browser.find_element(By.CSS_SELECTOR, 'button.btn')
    # button1.click()
    # first_window = browser.window_handles[0]
    # second_window = browser.window_handles[1]
    # browser.switch_to.window(second_window)
    # alert = browser.switch_to.alert
    # alert.accept()
    x_element = browser.find_element(By.ID, "input_value")
    # x = x_element.get_attribute("valuex")
    x = x_element.text
    y = calc(x)
    field = browser.find_element(By.ID, "answer")
    # browser.execute_script("return arguments[0].scrollIntoView(true);", field)
    field.send_keys(y)
    # in1 = browser.find_element(By.CSS_SELECTOR, "input[placeholder='Enter first name']")
    # in1.send_keys('Ivan')
    # in2 = browser.find_element(By.CSS_SELECTOR, "input[placeholder='Enter last name']")
    # in2.send_keys('Ivanov')
    # in3 = browser.find_element(By.CSS_SELECTOR, "input[placeholder='Enter email']")
    # in3.send_keys('Ivan@mail.com')
    # current_dir = os.path.abspath(os.path.dirname(__file__))
    # file_path = os.path.join(current_dir, 'file.txt')
    # in4 = browser.find_element(By.ID, "file")
    # in4.send_keys(file_path)

    # in2 = browser.find_element(By.ID, "robotsRule")
    # in2.click()
    # print(y)
    # input1 = browser.find_element(By.ID, "num1")
    # input1.send_keys(y)
    # input2 = browser.find_element(By.ID, "num2")
    # input2.click()
    # sel = Select(browser.find_element(By.TAG_NAME, "select"))
    # sel.select_by_value(str(int(input1.text) + int(input2.text)))
    # input3 = browser.find_element(By.CSS_SELECTOR, "input#robotsRule")
    # input3.click()

    # time.sleep(1)

    button = browser.find_element(By.ID, "solve")
    button.click()

    alert = browser.switch_to.alert
    print(alert.text)

finally:
    # успеваем скопировать код за 30 секунд
    # time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
