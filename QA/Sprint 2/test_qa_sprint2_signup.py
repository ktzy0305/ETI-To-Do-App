import pytest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
admin_page_url = "http://127.0.0.1:8000/admin/"
sign_up_url = "http://127.0.0.1:8000/accounts/signup/"

# All these test cases will only pass once (Meaning if the user already exists in the database it will fail)
# To overcome this issue we automate the process of deleting the Test User if it already exists when 
# running the test.
def handle_if_test_user_exists():
    # Go to Django Admin page and log in as the super user to remove the Test user if they exist.
    driver.get(admin_page_url)
    # Find the username and password elements for the Admin Login Page.
    admin_page_username_input_element = driver.find_element_by_id('id_username')
    admin_page_password_input_element = driver.find_element_by_id('id_password')
    # Find the Login Button element.
    login_button_element = driver.find_element_by_xpath('//*[@id="login-form"]/div[3]/input')
    # Clear any text from username and password elements.
    admin_page_username_input_element.clear()
    admin_page_password_input_element.clear()
    # Type in admin credentials
    admin_page_username_input_element.send_keys('marcus@abc.com')
    admin_page_password_input_element.send_keys('bluemonday')
    # Click the Login Button element.
    login_button_element.click()
    # Wait for the webpage to load by sleeping for 2 seconds 
    time.sleep(2)
    # Navigate to the User Authorization and Authentication Admin Page
    user_auth_page_link_element = driver.find_element_by_xpath('//*[@id="content-main"]/div/table/tbody/tr[2]/th/a')
    user_auth_page_link_element.click()
    # Wait for the webpage to load by sleeping for 2 seconds 
    time.sleep(2)
    # Check if the test user exists, if exists delete, else sign out of Django Admin Page
    users_table_body_element = driver.find_element_by_xpath('/html/body/div/div[3]/div/div/form/div[2]/table/tbody')
    number_of_users = len(users_table_body_element.find_elements_by_tag_name('tr'))
    for i in range(number_of_users):
        username_column_link_element = driver.find_element_by_xpath('//*[@id="result_list"]/tbody/tr[{0}]/th/a'.format(i+1))
        if username_column_link_element.text == "sprint2@abc.com":
            username_column_link_element.click()
            user_delete_link_element = driver.find_element_by_xpath('//*[@id="user_form"]/div/div/p/a')
            user_delete_link_element.click()
            confirm_delete_element = driver.find_element_by_xpath('//*[@id="content"]/form/div/input[2]')
            confirm_delete_element.click()
            break
    logout_link_element = driver.find_element_by_xpath('//*[@id="user-tools"]/a[3]')
    logout_link_element.click()


# Code for Automation of Test Case Scenario 

# User Sign Up with no input (Failing Test Case)
def test_qa_signup_no_input():
    handle_if_test_user_exists()
    driver.get(sign_up_url)
    username_input_element = driver.find_element_by_id("id_username")
    password_input_element = driver.find_element_by_id("id_password1")
    confirm_password_input_element = driver.find_element_by_id("id_password2")
    signup_button_element = driver.find_element_by_xpath("/html/body/div/main/form/button")
    # Remove the required attribute for the username, password and confirm password input elements (Only for this test case)
    driver.execute_script("arguments[0].removeAttribute('required')", username_input_element)
    driver.execute_script("arguments[0].removeAttribute('required')", password_input_element)
    driver.execute_script("arguments[0].removeAttribute('required')", confirm_password_input_element)

    username_input_element.clear()
    password_input_element.clear()
    confirm_password_input_element.clear()
    #Click on the signup button
    signup_button_element.click()
    # Wait for the webpage to load by sleeping for 2 seconds 
    time.sleep(2)
    # Find the Invalid Feedback elements for username, password and confirm password input elements
    invalid_feedback_elements = driver.find_elements_by_class_name('invalid-feedback')
    error_count = 0
    for invalid_feedback_element in invalid_feedback_elements:
        if invalid_feedback_element.text == "This field is required.":
            error_count += 1
    # The expected value of error_count variable should be 3 because there are 
    # a total of 3 input elements (username, password and confirm password) that are empty.
    assert error_count == 3
    

# Username field containing more than 150 characters (Failing Test Case)
def test_qa_signup_username_field_more_than_150_characters():
    driver.get(sign_up_url)
    username_input_element = driver.find_element_by_id("id_username")
    password_input_element = driver.find_element_by_id("id_password1")
    confirm_password_input_element = driver.find_element_by_id("id_password2")
    signup_button_element = driver.find_element_by_xpath("/html/body/div/main/form/button")

    username_input_element.clear()
    password_input_element.clear()
    confirm_password_input_element.clear()

    # Before typing in the test data, the maxlength value for the Username Input element
    # has to be modified from 150 to 160 to allow more than 150 characters to be entered.
    driver.execute_script("arguments[0].setAttribute('maxlength','160')", username_input_element)
    username_input_element.send_keys("A"*151)
    password_input_element.send_keys("QApa55w0rd")
    confirm_password_input_element.send_keys("QApa55w0rd")
    signup_button_element.click()
    invalid_feedback_elements = driver.find_elements_by_class_name('invalid-feedback')
    assert invalid_feedback_elements[0].text == "Ensure this value has at most 150 characters (it has 151)." 
    

# Username containing unallowed symbols (Failing Test Case)
def test_qa_signup_username_contains_unallowed_symbols():
    driver.get(sign_up_url)
    username_input_element = driver.find_element_by_id("id_username")
    password_input_element = driver.find_element_by_id("id_password1")
    confirm_password_input_element = driver.find_element_by_id("id_password2")
    signup_button_element = driver.find_element_by_xpath("/html/body/div/main/form/button")

    username_input_element.clear()
    password_input_element.clear()
    confirm_password_input_element.clear()

    username_input_element.send_keys("sprint#2@abc.com")
    password_input_element.send_keys("QApa55w0rd")
    confirm_password_input_element.send_keys("QApa55w0rd")
    signup_button_element.click()
    invalid_feedback_elements = driver.find_elements_by_class_name('invalid-feedback')
    assert invalid_feedback_elements[0].text == "Enter a valid username. This value may contain only letters, numbers, and @/./+/-/_ characters."
    

# Password less than 8 characters (Failing Test Case)
def test_qa_signup_password_less_than_8_characters():
    driver.get(sign_up_url)
    username_input_element = driver.find_element_by_id("id_username")
    password_input_element = driver.find_element_by_id("id_password1")
    confirm_password_input_element = driver.find_element_by_id("id_password2")
    signup_button_element = driver.find_element_by_xpath("/html/body/div/main/form/button")

    username_input_element.clear()
    password_input_element.clear()
    confirm_password_input_element.clear()

    username_input_element.send_keys("sprint2@abc.com")
    password_input_element.send_keys("QApa55w")
    confirm_password_input_element.send_keys("QApa55w")
    signup_button_element.click()
    invalid_feedback_elements = driver.find_elements_by_class_name('invalid-feedback')
    assert invalid_feedback_elements[0].text == "This password is too short. It must contain at least 8 characters."


# Password that is entirely numeric (Failing Test Case)
def test_qa_signup_password_entirely_numeric():
    driver.get(sign_up_url)
    username_input_element = driver.find_element_by_id("id_username")
    password_input_element = driver.find_element_by_id("id_password1")
    confirm_password_input_element = driver.find_element_by_id("id_password2")
    signup_button_element = driver.find_element_by_xpath("/html/body/div/main/form/button")

    username_input_element.clear()
    password_input_element.clear()
    confirm_password_input_element.clear()

    username_input_element.send_keys("sprint2@abc.com")
    password_input_element.send_keys("12345678")
    confirm_password_input_element.send_keys("12345678")
    signup_button_element.click()
    invalid_feedback_elements = driver.find_elements_by_class_name('invalid-feedback')
    assert invalid_feedback_elements[0].text == "This password is too common." and invalid_feedback_elements[1].text == "This password is entirely numeric."


# Confirm Password is different from Password (Failing Test Case)
def test_qa_signup_confirm_password_and_password_different():
    driver.get(sign_up_url)
    username_input_element = driver.find_element_by_id("id_username")
    password_input_element = driver.find_element_by_id("id_password1")
    confirm_password_input_element = driver.find_element_by_id("id_password2")
    signup_button_element = driver.find_element_by_xpath("/html/body/div/main/form/button")

    username_input_element.clear()
    password_input_element.clear()
    confirm_password_input_element.clear()

    username_input_element.send_keys("sprint2@abc.com")
    password_input_element.send_keys("QApa55w0rd")
    confirm_password_input_element.send_keys("QApa55w0rk")
    signup_button_element.click()
    invalid_feedback_elements = driver.find_elements_by_class_name('invalid-feedback')
    assert invalid_feedback_elements[0].text == "The two password fields didn't match."
    

# User Registration with valid input (Passing Test Case)
def test_qa_signup_valid_input():
    driver.get(sign_up_url)
    username_input_element = driver.find_element_by_id("id_username")
    password_input_element = driver.find_element_by_id("id_password1")
    confirm_password_input_element = driver.find_element_by_id("id_password2")
    signup_button_element = driver.find_element_by_xpath("/html/body/div/main/form/button")

    username_input_element.clear()
    password_input_element.clear()
    confirm_password_input_element.clear()

    username_input_element.send_keys("sprint2@abc.com")
    password_input_element.send_keys("QApa55w0rd")
    confirm_password_input_element.send_keys("QApa55w0rd")
    signup_button_element.click()
    assert driver.title == "Login"


# Username already exists (Failing Test Case)
def test_qa_signup_username_already_exists():
    driver.get(sign_up_url)
    username_input_element = driver.find_element_by_id("id_username")
    password_input_element = driver.find_element_by_id("id_password1")
    confirm_password_input_element = driver.find_element_by_id("id_password2")
    signup_button_element = driver.find_element_by_xpath("/html/body/div/main/form/button")

    username_input_element.clear()
    password_input_element.clear()
    confirm_password_input_element.clear()

    username_input_element.send_keys("sprint2@abc.com")
    password_input_element.send_keys("QApa55w0rd")
    confirm_password_input_element.send_keys("QApa55w0rd")
    signup_button_element.click()
    invalid_feedback_elements = driver.find_elements_by_class_name('invalid-feedback')
    assert invalid_feedback_elements[0].text == "A user with that username already exists."