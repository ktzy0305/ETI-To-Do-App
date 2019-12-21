import pytest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# All these are failing test cases
driver = webdriver.Chrome()
expected_message = "You are not logged in"

def test_qa_todo_page_authentication():
    # This test case is to test if a user who has not logged in
    # can acess the To-Do Page.
    driver.get('http://127.0.0.1:8000/To_do_page/')
    not_logged_in_message_element = driver.find_element_by_xpath('/html/body/div/main/p')
    assert not_logged_in_message_element.text == expected_message


def test_qa_todohistory_page_authentication():
    # This test case is to test if a user who has not logged in
    # can acess the To-Do History Page.
    driver.get('http://127.0.0.1:8000/historyItem/')
    not_logged_in_message_element = driver.find_element_by_xpath('/html/body/div/main/p')
    assert not_logged_in_message_element.text == expected_message


def test_qa_contributions_page_authentication():
    # This test case is to test if a user who has not logged in
    # can acess the Contributions Page.
    driver.get('http://127.0.0.1:8000/contribution/')
    not_logged_in_message_element = driver.find_element_by_xpath('/html/body/div/main/p')
    assert not_logged_in_message_element.text == expected_message