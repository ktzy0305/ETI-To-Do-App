import pytest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

def test_qatodohistory():
    driver = webdriver.Chrome()
    driver.get("http://127.0.0.1:8000/login/login/")
    username_element = driver.find_element_by_id("id_username")
    password_element = driver.find_element_by_id("id_password")
    login_button_element = driver.find_element_by_xpath("/html/body/div/main/form/button")

    username_element.clear()
    password_element.clear()

    username_element.send_keys("marcus@abc.com")
    password_element.send_keys("bluemonday")

    login_button_element.click()

    time.sleep(2)

    driver.get("http://127.0.0.1:8000/historyItem")

    page_title_element = driver.find_element_by_xpath('/html/body/div/main/h1')

    assert page_title_element.text == "Welcome marcus@abc.com, this is the history page"
