import pytest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
login_url = 'http://127.0.0.1:8000/accounts/login/'

def test_qa_retrieve_todohistory():
    # This test case is to test if the To-Do History items
    # are retrieved as intended at the To-Do History Page. 
    # Login into the To-Do application
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

    # Click on the navigation bar link to To-Do History Page
    to_do_history_nav_link_element = driver.find_element_by_xpath('//*[@id="navbarNav"]/ul[1]/li[2]/a')
    to_do_history_nav_link_element.click()

    # Compare the number of rows in the first page based on the pagination count.
    # Example of pagination count: "Showing 1 to 5 of 12 items"
    # Using split function: ["Showing", "1", "to", "5", "of", "12", "items"]
    # The 5th index is the total number of items.
    to_do_history_table_tbody_element = driver.find_element_by_xpath('//*[@id="to-do-history-table"]/tbody')
    pagination_count_text = driver.find_element_by_id('pagination-count').text
    pagination_count_text_list = pagination_count_text.split()

    page_1_row_count = len(to_do_history_table_tbody_element.find_elements_by_tag_name('tr'))
    total_number_of_todo_history_items = int(pagination_count_text_list[5])

    if total_number_of_todo_history_items >= 5:
        assert page_1_row_count == 5
    else:
        assert page_1_row_count == total_number_of_todo_history_items