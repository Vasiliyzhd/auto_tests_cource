from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest


class Test_registration(unittest.TestCase):
    def test_reg1(self):
        browser = webdriver.Chrome()
        browser.get("http://suninjuly.github.io/registration1.html")
        input_fname = browser.find_element(By.CSS_SELECTOR, "[placeholder='Input your first name']")
        input_fname.send_keys('Ivan')
        input_lname = browser.find_element(By.CSS_SELECTOR, "[placeholder='Input your last name']")
        input_lname.send_keys('Ivanov')
        input_email = browser.find_element(By.CSS_SELECTOR, "[placeholder='Input your email']")
        input_email.send_keys('ivan@mail.com')
        button_submit = browser.find_element(By.CSS_SELECTOR, "[type='submit']")
        button_submit.click()
        browser.quit()

    def test_reg2(self):
        browser = webdriver.Chrome()
        browser.get("http://suninjuly.github.io/registration2.html")
        input_fname = browser.find_element(By.CSS_SELECTOR, "[placeholder='Input your first name']")
        input_fname.send_keys('Ivan')
        input_lname = browser.find_element(By.CSS_SELECTOR, "[placeholder='Input your last name']")
        input_lname.send_keys('Ivanov')
        input_email = browser.find_element(By.CSS_SELECTOR, "[placeholder='Input your email']")
        input_email.send_keys('ivan@mail.com')
        button_submit = browser.find_element(By.CSS_SELECTOR, "[type='submit']")
        button_submit.click()
        browser.quit()


if __name__ == "__main__":
    unittest.main()
