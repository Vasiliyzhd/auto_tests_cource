import time
import math
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.mark.parametrize('link_id', ["236895", "236896", "236897", "236898", "236899", "236903", "236904", "236905"])
def test_local_time(browser, link_id):
    link = f"https://stepik.org/lesson/{link_id}/step/1"
    browser.get(link)
    browser.find_element(By.CSS_SELECTOR, "textarea[placeholder='Напишите ваш ответ здесь...']"). \
        send_keys(math.log(int(time.time())))
    browser.find_element(By.CSS_SELECTOR, "button.submit-submission").click()
    assert browser.find_element(By.CSS_SELECTOR, "p.smart-hints__hint").text == "Correct!"
