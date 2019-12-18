import pytest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

def test_qadeletetodo():
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

    #This is to add to do item prevent database changes
    owner_element = driver.find_element_by_xpath('/html/body/div/main/form/p[1]/input')
    item_name_element = driver.find_element_by_xpath('/html/body/div/main/form/p[2]/input')
    add_button_element = driver.find_element_by_xpath('/html/body/div/main/form/input[2]')
    driver.execute_script("arguments[0].scrollIntoView(true)", add_button_element)
    driver.execute_script("arguments[0].removeAttribute('disabled')", owner_element)
    time.sleep(2)


    owner_element.clear()
    item_name_element.clear()

    owner_element.send_keys('marcus@abc.com')
    item_name_element.send_keys('To Do QA Test 2')
    add_button_element.click()
    
    item_List = driver.find_element_by_xpath("/html/body/div/main/ul")
    number_of_items = len(item_List.find_elements_by_tag_name('li'))
    delete_addedItems = driver.find_element_by_xpath("/html/body/div/main/ul/li[{0}]/form[1]/input[2]".format(number_of_items))
    delete_addedItems.click()
    
    #Page refreshes
    item_List = driver.find_element_by_xpath("/html/body/div/main/ul")
    updatedNumberOfItems = len(item_List.find_elements_by_tag_name('li'))
    assert number_of_items-1 == updatedNumberOfItems
    
