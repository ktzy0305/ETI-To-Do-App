from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pytest
driver=webdriver.Chrome()

def  test_webpage():
    driver.get('http://localhost:8000/login/login/')
    elem_name = driver.find_element_by_name("username")
    elem_name.clear()
    elem_name.send_keys("marcus@abc.com")
    elem_password = driver.find_element_by_name("password")
    elem_password.clear()
    elem_password.send_keys("bluemonday")
    elem_password.send_keys(Keys.RETURN)
    assert "http://localhost:8000/To_do_page/" in driver.current_url

def test_user_detection():
    driver.get('http://localhost:8000/To_do_page/')
    #greeting = driver.find_element_by_name("username").text
    assert "Welcome marcus@abc.com, this is the to do page" in driver.find_element_by_name("greeting").text
    
def test_display():
    html_list = driver.find_element_by_name("item_list")
    items = html_list.find_elements_by_tag_name("li")
    count = 0
    for item in items:
        count += 1
    assert count == 4

def test_delete():
    html_list = driver.find_element_by_name("item_list")
    items = html_list.find_elements_by_tag_name("li")
    count_1 = 0
    count_2 = 0
    for item in items:
        count_1 += 1
    dele = items[1].find_element_by_name("delete")
    dele.send_keys(Keys.RETURN)
    html_list = driver.find_element_by_name("item_list")
    items = html_list.find_elements_by_tag_name("li")
    for item in items:
        count_2 += 1
    assert (count_1 - 1) == count_2
        
def test_null_add_item():
    html_list = driver.find_element_by_name("item_list")
    items = html_list.find_elements_by_tag_name("li")
    count_1 = 0
    count_2 = 0
    for item in items:
        count_1 += 1
    elem_owner = driver.find_element_by_name("Owner")
    elem_owner.clear()
    elem_owner.send_keys("")
    elem_todo = driver.find_element_by_name("Todo")
    elem_todo.clear()
    elem_todo.send_keys("")
    elem_todo.send_keys(Keys.RETURN)
    html_list = driver.find_element_by_name("item_list")
    items = html_list.find_elements_by_tag_name("li")
    for item in items:
        count_2 += 1
    assert count_1 == count_2

def test_correct_add_item():
    html_list = driver.find_element_by_name("item_list")
    items = html_list.find_elements_by_tag_name("li")
    count_1 = 0
    count_2 = 0
    for item in items:
        count_1 += 1
    elem_owner = driver.find_element_by_name("Owner")
    elem_owner.clear()
    elem_owner.send_keys("testuser1")
    elem_todo = driver.find_element_by_name("Todo")
    elem_todo.clear()
    elem_todo.send_keys("test to do")
    elem_todo.send_keys(Keys.RETURN)
    html_list = driver.find_element_by_name("item_list")
    items = html_list.find_elements_by_tag_name("li")
    for item in items:
        count_2 += 1
    assert (count_1 + 1) == count_2

def test_bypass_login():
    driver.find_element_by_link_text("Log Out").click()
    driver.get('http://localhost:8000/To_do_page/')
    #elem = driver.find_element_by_name
    msg = driver.find_element_by_css_selector("p.error_msg").text
    assert 'You are not logged in' == msg
    
