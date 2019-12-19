import pytest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

def testqaarchive():
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

    item_List = driver.find_element_by_xpath("/html/body/div/main/ul")
    number_of_items = len(item_List.find_elements_by_tag_name('li'))
    
    archive_item_name = driver.find_element_by_xpath("/html/body/div/main/ul/li[{0}]/div[1]".format(number_of_items)).text
    archive_ButtonElement = driver.find_element_by_xpath("/html/body/div/main/ul/li[{0}]/form[2]/input[2]".format(number_of_items))
    archive_ButtonElement.click()
    driver.get("http://127.0.0.1:8000/historyItem")

    todo_history_list = driver.find_element_by_xpath("/html/body/div/main/ul")
    number_of_items = len(todo_history_list.find_elements_by_tag_name('li'))

    item_name = driver.find_element_by_xpath("/html/body/div/main/ul/li[{0}]/p[1]".format(number_of_items)).text

    assert archive_item_name == item_name
        
