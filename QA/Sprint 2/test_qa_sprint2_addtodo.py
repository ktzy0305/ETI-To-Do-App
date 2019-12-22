import pytest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
login_url = "http://127.0.0.1:8000/accounts/login/"
expected_action_text = "Added QA Sprint 2 Test for marcus@abc.com from Todo page"

def test_qa_add_todo_item_no_item_name():
    # This code is different from Sprint 1's due to Requirements and UI Changes
    driver.get(login_url)
    username_element = driver.find_element_by_id("id_username")
    password_element = driver.find_element_by_id("id_password")
    login_button_element = driver.find_element_by_xpath("/html/body/div/main/form/button")
    username_element.clear()
    password_element.clear()
    username_element.send_keys("marcus@abc.com")
    password_element.send_keys("bluemonday")
    login_button_element.click()
    time.sleep(2)
    pagination_count_text = driver.find_element_by_id('pagination-count').text
    pagination_count_text_list = pagination_count_text.split()
    original_item_count = int(pagination_count_text_list[5])
    to_do_item_name_input_element = driver.find_element_by_name('Todo')
    add_new_item_button_element = driver.find_element_by_xpath('//*[@id="add-btn-container"]/button')
    driver.execute_script("arguments[0].removeAttribute('required')", to_do_item_name_input_element)
    to_do_item_name_input_element.clear()
    add_new_item_button_element.click()
    time.sleep(2)
    pagination_count_text = driver.find_element_by_id('pagination-count').text
    pagination_count_text_list = pagination_count_text.split()
    updated_item_count = int(pagination_count_text_list[5])
    error_flag_element = driver.find_element_by_xpath('//*[@id="some_flag"]/p')
    assert (error_flag_element.text == "Item name cannot be empty!") and (original_item_count == updated_item_count)
    

def test_qa_add_todo_item():
    # This code is different from Sprint 1's due to Requirements and UI Changes
    driver.get(login_url)
    username_element = driver.find_element_by_id("id_username")
    password_element = driver.find_element_by_id("id_password")
    login_button_element = driver.find_element_by_xpath("/html/body/div/main/form/button")
    username_element.clear()
    password_element.clear()
    username_element.send_keys("marcus@abc.com")
    password_element.send_keys("bluemonday")
    login_button_element.click()
    time.sleep(2)
    
    # Navigate to To-Do History Page
    # Click on the navigation bar link to To-Do History Page
    to_do_history_nav_link_element = driver.find_element_by_xpath('//*[@id="navbarNav"]/ul[1]/li[2]/a')
    to_do_history_nav_link_element.click()
    # Get the original number of To-Do History Items retrieved from the database
    todohistoryitem_pagination_count_text = driver.find_element_by_id('pagination-count').text
    todohistoryitem_pagination_count_text_list = todohistoryitem_pagination_count_text.split()
    todohistoryitem_original_item_count = int(todohistoryitem_pagination_count_text_list[5])
    # Navigate to To-Do Page
    # Click on the navigation bar link to To-Do Page
    to_do_nav_link_element = driver.find_element_by_xpath('//*[@id="navbarNav"]/ul[1]/li[1]/a')
    to_do_nav_link_element.click()
    # Wait for the webpage to load by sleeping for 2 seconds 
    time.sleep(2)
    # Get the original number of To-Do Items retrieved from the database
    todoitem_pagination_count_text = driver.find_element_by_id('pagination-count').text
    todoitem_pagination_count_text_list = todoitem_pagination_count_text.split()
    todoitem_original_item_count = int(todoitem_pagination_count_text_list[5])
    # Find the To-Do Item Name Input Element
    to_do_item_name_input_element = driver.find_element_by_name('Todo')
    add_new_item_button_element = driver.find_element_by_xpath('//*[@id="add-btn-container"]/button')
    to_do_item_name_input_element.clear()
    to_do_item_name_input_element.send_keys("QA Sprint 2 Test")
    add_new_item_button_element.click()
    time.sleep(2)
    # Get the number of To-Do Items retrieved from the database after clicking "Add New Item"
    todoitem_updated_pagination_count_text = driver.find_element_by_id('pagination-count').text
    todoitem_updated_pagination_count_text_list = todoitem_updated_pagination_count_text.split()
    todoitem_updated_item_count = int(todoitem_updated_pagination_count_text_list[5])
    # Navigate to To-Do History Page
    # Click on the navigation bar link to To-Do History Page
    to_do_history_nav_link_element = driver.find_element_by_xpath('//*[@id="navbarNav"]/ul[1]/li[2]/a')
    to_do_history_nav_link_element.click()
    time.sleep(2)
    # Get the number of To-Do History Items retrieved from the database after clicking "Add New Item" at the To-Do Page
    todohistoryitem_updated_pagination_count_text = driver.find_element_by_id('pagination-count').text
    todohistoryitem_updated_pagination_count_text_list = todohistoryitem_updated_pagination_count_text.split()
    todohistoryitem_updated_item_count = int(todohistoryitem_updated_pagination_count_text_list[5])
    todohistory_table_row_1_action_column = driver.find_element_by_xpath('//*[@id="to-do-history-table"]/tbody/tr[1]/td[1]/div')
    # Assert that the text at the action column of the 1st row of the To-Do History table is the same as the expected value
    # and that the To-Do Item count and the To-Do History Item count is increased by 1.
    assert (todohistory_table_row_1_action_column.text == expected_action_text) and ((todoitem_original_item_count + 1) == todoitem_updated_item_count) and ((todohistoryitem_original_item_count + 1) == todohistoryitem_updated_item_count)

    
