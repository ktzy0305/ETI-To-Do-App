import pytest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

def test_qa_delete_to_do_item():
    # This code is different from Sprint 1's due to Requirements and UI Changes
    driver = webdriver.Chrome()
    driver.get("http://127.0.0.1:8000/accounts/login/")

    # Check To-Do History Page for the delete action


    return