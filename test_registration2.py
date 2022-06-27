import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest


def reg(link):
    browser = webdriver.Chrome()
    browser.get(link)
    try:
        browser.find_element(By.CSS_SELECTOR, "[placeholder='Input your first name']").send_keys('Ivan')
        browser.find_element(By.CSS_SELECTOR, "[placeholder='Input your last name']").send_keys('Ivanov')
        browser.find_element(By.CSS_SELECTOR, "[placeholder='Input your email']").send_keys('ivan@mail.com')
        browser.find_element(By.CSS_SELECTOR, "[type='submit']")

        return browser.find_element(By.TAG_NAME, "h1").text
    finally:
        browser.quit()


class Test_registration:

    def test_reg1(self):
        # self.assertEqual(reg("http://suninjuly.github.io/registration1.html"),
        #                  "Registration", "Registration is failed")
        assert reg("http://suninjuly.github.io/registration1.html") == "Registration", "Registration is failed"

    @pytest.mark.xfail
    def test_reg2(self):
        # self.assertEqual(reg("http://suninjuly.github.io/registration2.html"),
        #                  "Registration", "Registration is failed")
        assert reg("http://suninjuly.github.io/registration2.html") == "Registration", "Registration is failed"

