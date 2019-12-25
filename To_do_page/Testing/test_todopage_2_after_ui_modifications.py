from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from datetime import datetime
import pytest

driver=webdriver.Chrome()

def test_webpage():
    driver.get('http://localhost:8000/accounts/login/')
    elem_name = driver.find_element_by_name("username")
    elem_name.clear()
    elem_name.send_keys("marcus@abc.com")
    elem_password = driver.find_element_by_name("password")
    elem_password.clear()
    elem_password.send_keys("bluemonday")
    elem_password.send_keys(Keys.RETURN)
    assert "http://localhost:8000/To_do_page/" in driver.current_url

def test_current_user():
    current_user = driver.find_element_by_xpath('//*[@id="navbarNav"]/ul[2]/li[1]/a')
    assert "marcus@abc.com" in current_user.text

def test_display_Owner_item():
    html_table_body = driver.find_element_by_xpath('//*[@id="to-do-table"]/tbody')
    rows = html_table_body.find_elements_by_tag_name('tr')
    count = 0
    for row in rows:
        elem_owner = row.find_element_by_name('owner').text
        if (elem_owner == "marcus@abc.com"):
            count += 1

    assert count == 5

def test_add_null_itemname():
    html_table_body = driver.find_element_by_xpath('//*[@id="to-do-table"]/tbody')
    rows = html_table_body.find_elements_by_tag_name('tr')
    count_1 = len(rows)
    elem_todo = driver.find_element_by_name("Todo")
    elem_todo.send_keys("")
    elem_todo.send_keys(Keys.RETURN)
    html_table_body = driver.find_element_by_xpath('//*[@id="to-do-table"]/tbody')
    rows = html_table_body.find_elements_by_tag_name('tr')
    count_2 = len(rows)
    assert count_1 == count_2

def test_time_add_item():
    elem_todo = driver.find_element_by_name("Todo")
    elem_todo.clear()
    elem_todo.send_keys("to_do_test")
    elem_todo.send_keys(Keys.RETURN)
    time_now = datetime.now()
    html_table_body = driver.find_element_by_xpath('//*[@id="to-do-table"]/tbody')
    rows = html_table_body.find_elements_by_tag_name('tr')
    time_created = rows[0].find_element_by_name("time_created").text
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

    assert timenow == time_created