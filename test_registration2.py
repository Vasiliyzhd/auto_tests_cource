from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest
import time


def reg(link):
    browser = webdriver.Chrome()
    browser.get(link)

    browser.find_element(By.CSS_SELECTOR, "[placeholder='Input your first name']").send_keys('Ivan')
    browser.find_element(By.CSS_SELECTOR, "[placeholder='Input your last name']").send_keys('Ivanov')
    browser.find_element(By.CSS_SELECTOR, "[placeholder='Input your email']").send_keys('ivan@mail.com')
    browser.find_element(By.CSS_SELECTOR, "[type='submit']")

    return browser.find_element(By.TAG_NAME, "h1").text


class Test_registration(unittest.TestCase):

    def test_reg1(self):
        self.assertEqual(reg("http://suninjuly.github.io/registration1.html"),
                         "Registration", "Registration is failed")

    def test_reg2(self):
        self.assertEqual(reg("http://suninjuly.github.io/registration2.html"),
                         "Registration", "Registration is failed")


if __name__ == "__main__":
    unittest.main()
