import pytest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class TestToDoPageQA:
    driver = webdriver.Chrome()

    def test_add_to_do_item_no_input(self):
        self.driver.get("http://127.0.0.1:8000/login/login/")
        username_element = self.driver.find_element_by_id("id_username")
        password_element = self.driver.find_element_by_id("id_password")
        login_button_element = self.driver.find_element_by_xpath("/html/body/div/main/form/button")
        
        username_element.clear()
        password_element.clear()

        username_element.send_keys("marcus@abc.com")
        password_element.send_keys("bluemonday")

        login_button_element.click()

        time.sleep(2)

        to_do_item_list = self.driver.find_element_by_name('item_list')
        original_item_count = len(to_do_item_list.find_elements_by_tag_name('li'))

        owner_element = self.driver.find_element_by_xpath('/html/body/div/main/form/p[1]/input')
        item_name_element = self.driver.find_element_by_xpath('/html/body/div/main/form/p[2]/input')
        add_button_element = self.driver.find_element_by_xpath('/html/body/div/main/form/input[2]')
        self.driver.execute_script("arguments[0].scrollIntoView(true)", add_button_element)
        self.driver.execute_script("arguments[0].removeAttribute('disabled')", owner_element)
        self.driver.execute_script("arguments[0].removeAttribute('required')", item_name_element)
        time.sleep(2)

        owner_element.clear()
        item_name_element.clear()
        
        add_button_element.click()

        # Page Refreshed (Need to find element again)
        to_do_item_list = self.driver.find_element_by_name('item_list')
        updated_item_count = len(to_do_item_list.find_elements_by_tag_name("li"))

        assert original_item_count == updated_item_count


    def test_add_to_do_item(self):
        self.driver.get("http://127.0.0.1:8000/login/login/")
        username_element = self.driver.find_element_by_id("id_username")
        password_element = self.driver.find_element_by_id("id_password")
        login_button_element = self.driver.find_element_by_xpath("/html/body/div/main/form/button")

        username_element.clear()
        password_element.clear()

        username_element.send_keys("marcus@abc.com")
        password_element.send_keys("bluemonday")

        login_button_element.click()

        time.sleep(2)

        to_do_item_list = self.driver.find_element_by_name('item_list')
        original_item_count = len(to_do_item_list.find_elements_by_tag_name('li'))

        owner_element = self.driver.find_element_by_xpath('/html/body/div/main/form/p[1]/input')
        item_name_element = self.driver.find_element_by_xpath('/html/body/div/main/form/p[2]/input')
        add_button_element = self.driver.find_element_by_xpath('/html/body/div/main/form/input[2]')
        self.driver.execute_script("arguments[0].scrollIntoView(true)", add_button_element)
        self.driver.execute_script("arguments[0].removeAttribute('disabled')", owner_element)
        time.sleep(2)
        
        owner_element.clear()
        item_name_element.clear()

        owner_element.send_keys('marcus@abc.com')
        item_name_element.send_keys('To Do QA Test 2')
        add_button_element.click()

        # Page Refreshed (Need to find element again)
        to_do_item_list = self.driver.find_element_by_name('item_list')
        updated_item_count = len(to_do_item_list.find_elements_by_tag_name("li"))

        assert original_item_count + 1 == updated_item_count

    def test_add_to_do_item_no_owner(self):
        self.driver.get("http://127.0.0.1:8000/login/login/")
        username_element = self.driver.find_element_by_id("id_username")
        password_element = self.driver.find_element_by_id("id_password")
        login_button_element = self.driver.find_element_by_xpath("/html/body/div/main/form/button")
        
        username_element.clear()
        password_element.clear()

        username_element.send_keys("marcus@abc.com")
        password_element.send_keys("bluemonday")

        login_button_element.click()

        time.sleep(2)

        to_do_item_list = self.driver.find_element_by_name('item_list')
        original_item_count = len(to_do_item_list.find_elements_by_tag_name('li'))

        owner_element = self.driver.find_element_by_xpath('/html/body/div/main/form/p[1]/input')
        item_name_element = self.driver.find_element_by_xpath('/html/body/div/main/form/p[2]/input')
        add_button_element = self.driver.find_element_by_xpath('/html/body/div/main/form/input[2]')
        self.driver.execute_script("arguments[0].scrollIntoView(true)", add_button_element)
        self.driver.execute_script("arguments[0].removeAttribute('disabled')", owner_element)
        self.driver.execute_script("arguments[0].removeAttribute('required')", item_name_element)
        time.sleep(2)

        owner_element.clear()
        item_name_element.clear()

        item_name_element.send_keys('To Do QA Test 2')

        
        add_button_element.click()

        # Page Refreshed (Need to find element again)
        to_do_item_list = self.driver.find_element_by_name('item_list')
        updated_item_count = len(to_do_item_list.find_elements_by_tag_name("li"))

        assert original_item_count == updated_item_count
    
    def test_add_to_do_item_no_item_name(self):
        self.driver.get("http://127.0.0.1:8000/login/login/")
        username_element = self.driver.find_element_by_id("id_username")
        password_element = self.driver.find_element_by_id("id_password")
        login_button_element = self.driver.find_element_by_xpath("/html/body/div/main/form/button")
        
        username_element.clear()
        password_element.clear()

        username_element.send_keys("marcus@abc.com")
        password_element.send_keys("bluemonday")

        login_button_element.click()

        time.sleep(2)

        to_do_item_list = self.driver.find_element_by_name('item_list')
        original_item_count = len(to_do_item_list.find_elements_by_tag_name('li'))

        owner_element = self.driver.find_element_by_xpath('/html/body/div/main/form/p[1]/input')
        item_name_element = self.driver.find_element_by_xpath('/html/body/div/main/form/p[2]/input')
        add_button_element = self.driver.find_element_by_xpath('/html/body/div/main/form/input[2]')
        self.driver.execute_script("arguments[0].scrollIntoView(true)", add_button_element)
        self.driver.execute_script("arguments[0].removeAttribute('disabled')", owner_element)
        self.driver.execute_script("arguments[0].removeAttribute('required')", item_name_element)
        time.sleep(2)

        owner_element.clear()
        item_name_element.clear()

        owner_element.send_keys('marcus@abc.com')

        
        add_button_element.click()

        # Page Refreshed (Need to find element again)
        to_do_item_list = self.driver.find_element_by_name('item_list')
        updated_item_count = len(to_do_item_list.find_elements_by_tag_name("li"))

        assert original_item_count == updated_item_count