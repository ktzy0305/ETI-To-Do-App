import pytest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

expected_action_text = "Deleted Delete Item Test for marcus@abc.com from Todo page"

def test_qa_delete_to_do_item():
    # This code is different from Sprint 1's due to Requirements and UI Changes
    driver = webdriver.Chrome()
    driver.get("http://127.0.0.1:8000/accounts/login/")
    # Find the username, password input elements and the login button element
    username_element = driver.find_element_by_id("id_username")
    password_element = driver.find_element_by_id("id_password")
    login_button_element = driver.find_element_by_xpath("/html/body/div/main/form/button")
    username_element.clear()
    password_element.clear()
    username_element.send_keys("marcus@abc.com")
    password_element.send_keys("bluemonday")
    login_button_element.click()
    time.sleep(2)
    
    # Create a To-Do Item to delete
    # Find the To-Do Item Name Input Element
    to_do_item_name_input_element = driver.find_element_by_name('Todo')
    # Find the "Add New Item" Button Element
    add_new_item_button_element = driver.find_element_by_xpath('//*[@id="add-btn-container"]/button')
    # Clear the input for the To-Do Item Name Input Element
    to_do_item_name_input_element.clear()
    # Type "QA Sprint 2 Test" into To-Do Item Name Input Element
    to_do_item_name_input_element.send_keys("Delete Item Test")
    # Click the "Add New Item" Button Element
    add_new_item_button_element.click()

    # Navigate to To-Do History Page
    # Click on the navigation bar link to To-Do History Page
    to_do_history_nav_link_element = driver.find_element_by_xpath('//*[@id="navbarNav"]/ul[1]/li[2]/a')
    to_do_history_nav_link_element.click()
    todohistoryitem_pagination_count_text = driver.find_element_by_id('pagination-count').text
    todohistoryitem_pagination_count_text_list = todohistoryitem_pagination_count_text.split()
    todohistoryitem_original_item_count = int(todohistoryitem_pagination_count_text_list[5])

    # Navigate to To-Do Page
    # Click on the navigation bar link to To-Do Page
    to_do_nav_link_element = driver.find_element_by_xpath('//*[@id="navbarNav"]/ul[1]/li[1]/a')
    to_do_nav_link_element.click()
    time.sleep(2)
    todoitem_pagination_count_text = driver.find_element_by_id('pagination-count').text
    todoitem_pagination_count_text_list = todoitem_pagination_count_text.split()
    todoitem_original_item_count = int(todoitem_pagination_count_text_list[5])
    delete_button_for_earlier_todoitem = driver.find_element_by_xpath('//*[@id="to-do-table"]/tbody/tr[1]/td[4]/form/button')
    delete_button_for_earlier_todoitem.click()

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

    # Get the text in the "Action" column first row of the To-Do History table
    todohistory_table_row_1_action_column = driver.find_element_by_xpath('//*[@id="to-do-history-table"]/tbody/tr[1]/td[1]/div')

    # Assert that the text at the action column of the 1st row of the To-Do History table is the same as the expected value
    # and that the To-Do Item count and the To-Do History Item count is increased by 1.
    assert (todohistory_table_row_1_action_column.text == expected_action_text) and ((todoitem_original_item_count - 1) == todoitem_updated_item_count) and ((todohistoryitem_original_item_count + 1) == todohistoryitem_updated_item_count)
