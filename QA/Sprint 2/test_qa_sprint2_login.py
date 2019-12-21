import pytest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class TestLoginSprint2QA:
    driver = webdriver.Chrome()

    def test_login_no_input(self):
        self.driver.get("http://127.0.0.1:8000/accounts/login/")
        username_element = self.driver.find_element_by_id("id_username")
        password_element = self.driver.find_element_by_id("id_password")
        login_button_element = self.driver.find_element_by_xpath("/html/body/div/main/form/button")
        self.driver.execute_script("arguments[0].removeAttribute('required')", username_element)
        self.driver.execute_script("arguments[0].removeAttribute('required')", password_element)

        username_element.clear()
        password_element.clear()

        login_button_element.click()

        invalid_feedback_elements = self.driver.find_elements_by_class_name('invalid-feedback')

        assert (invalid_feedback_elements[0].text == "This field is required.") and (invalid_feedback_elements[0].text == invalid_feedback_elements[1].text)

    def test_login_correct_username_correct_password(self):
        self.driver.get("http://127.0.0.1:8000/accounts/login/")
        username_element = self.driver.find_element_by_id("id_username")
        password_element = self.driver.find_element_by_id("id_password")
        login_button_element = self.driver.find_element_by_xpath("/html/body/div/main/form/button")
        
        username_element.clear()
        password_element.clear()

        username_element.send_keys("marcus@abc.com")
        password_element.send_keys("bluemonday")

        login_button_element.click()

        time.sleep(2)

        welcome_user_element = self.driver.find_element_by_xpath('//*[@id="navbarNav"]/ul[2]/li[1]/a')
        
        assert welcome_user_element.text == "Welcome, marcus@abc.com"

    def test_login_wrong_password(self):
        self.driver.get("http://127.0.0.1:8000/accounts/login/")
        username_element = self.driver.find_element_by_id("id_username")
        password_element = self.driver.find_element_by_id("id_password")
        login_button_element = self.driver.find_element_by_xpath("/html/body/div/main/form/button")
        
        username_element.clear()
        password_element.clear()

        username_element.send_keys("marcus@abc.com")
        password_element.send_keys("redmonday")

        login_button_element.click()

        time.sleep(2)

        error_message_element = self.driver.find_element_by_xpath('/html/body/div/main/form/div[1]')
        expected_error_message = "Please enter a correct username and password. Note that both fields may be case-sensitive."
        
        assert expected_error_message in error_message_element.text

    def test_login_wrong_username(self):
        self.driver.get("http://127.0.0.1:8000/accounts/login/")
        username_element = self.driver.find_element_by_id("id_username")
        password_element = self.driver.find_element_by_id("id_password")
        login_button_element = self.driver.find_element_by_xpath("/html/body/div/main/form/button")
        
        username_element.clear()
        password_element.clear()

        username_element.send_keys("mark@abc.com")
        password_element.send_keys("bluemonday")

        login_button_element.click()

        time.sleep(2)

        error_message_element = self.driver.find_element_by_xpath('/html/body/div/main/form/div[1]')
        expected_error_message = "Please enter a correct username and password. Note that both fields may be case-sensitive."

        assert expected_error_message in error_message_element.text