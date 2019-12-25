from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from datetime import datetime
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

def test_auto_owner_input():
    elem_owner = driver.find_element_by_name("Owner")
    value = elem_owner.get_attribute('value')
    assert "marcus@abc.com" == value
    
def test_change_owner_name():
    elem_owner = driver.find_element_by_name("Owner")
    valid = True
    try:
        elem_owner.send_keys("testuser1")
        valid = True
    except:
        valid = False
    assert valid == False

def test_display_Owner_item():
    html_list = driver.find_element_by_name("item_list")
    items = html_list.find_elements_by_tag_name("li")
    count = 0
    for item in items:
        elem_owner = driver.find_element_by_name("owner").text
        if (elem_owner == "Owner: marcus@abc.com"):
            count += 1
    assert count == 2

def test_add_null_itemname():
    html_list = driver.find_element_by_name("item_list")
    items = html_list.find_elements_by_tag_name("li")
    count_1 = 0
    count_2 = 0
    for item in items:
        count_1 += 1
    elem_todo = driver.find_element_by_name("Todo")
    elem_todo.clear()
    elem_todo.send_keys("")
    elem_todo.send_keys(Keys.RETURN)
    html_list = driver.find_element_by_name("item_list")
    items = html_list.find_elements_by_tag_name("li")
    for item in items:
        count_2 += 1
    assert count_1 == count_2

def test_time_add_item():
    html_list = driver.find_element_by_name("item_list")
    items = html_list.find_elements_by_tag_name("li")
    count_1 = 0
    for item in items:
        count_1 += 1
    elem_todo = driver.find_element_by_name("Todo")
    elem_todo.clear()
    elem_todo.send_keys("to_do_test")
    elem_todo.send_keys(Keys.RETURN)
    time_now = datetime.now()
    if (time_now.strftime("%I:%M %p") == "12:00 AM"):
        timenow=time_now.strftime("%b. ")+time_now.strftime("%d").lstrip('0')+time_now.strftime(", %Y, ")+"midnight"
    elif(time_now.strftime("%I:%M %p") == "12:00 PM"):
        timenow=timenow=time_now.strftime("%b. ")+time_now.strftime("%d").lstrip('0')+time_now.strftime(", %Y, ")+"noon"
    elif(time_now.strftime("%p") == "PM"):
        if (time_now.strftime("%M") == "00"):
            timenow=time_now.strftime("%b. ")+time_now.strftime("%d").lstrip('0')+time_now.strftime(", %Y, ")+ time_now.strftime("%I").lstrip('0') +  ' p.m.'
        else:
            timenow=time_now.strftime("%b. ")+time_now.strftime("%d").lstrip('0')+time_now.strftime(", %Y, ")+ time_now.strftime("%I").lstrip('0') +  time_now.strftime(":%M ") + 'p.m.'
    elif(time_now.strftime("%p") == "AM"):
        if(time_now.strftime("%M") == "00"):
            timenow=time_now.strftime("%b. ")+time_now.strftime("%d").lstrip('0')+time_now.strftime(", %Y, ")+ time_now.strftime("%I").lstrip('0') +' a.m.'
        else:
            timenow=time_now.strftime("%b. ")+time_now.strftime("%d").lstrip('0')+time_now.strftime(", %Y, ")+ time_now.strftime("%I").lstrip('0') +  time_now.strftime(":%M ") + 'a.m.'
    html_list = driver.find_element_by_name("item_list")
    items = html_list.find_elements_by_tag_name("li")
    time_created = items[count_1].find_element_by_name("time_created").text
    assert ("Time Created: " + timenow) == time_created

    
