import os
import time
from dotenv import load_dotenv
from selenium import webdriver

load_dotenv()

# Set up the Chrome WebDriver
driver = webdriver.Chrome()
driver.get(os.environ.get('FORM_URL'))


def authenticate():

    # Find username and password input elements
    username_input = driver.find_element("id", "username")
    password_input = driver.find_element("id", "password")

    # Find and click the login button
    login_button = driver.find_element("id", "loginbtn")

    # Fill in the credentials and click login
    username_input.send_keys(os.environ.get('MAIL'))
    password_input.send_keys(os.environ.get('PASS'))
    login_button.click()


def fillForm():
    question_one = driver.find_element("id", "auto-rb0001")
    dropdown = driver.find_element("id", "dropSelecciòn")

    submit_button = driver.find_element("name", "submit")

    question_one.click()
    dropdown.click()

    # press down arrow
    dropdown.send_keys(u'\ue015')
    dropdown.send_keys(u'\ue015')
    dropdown.send_keys(u'\ue015')

    # press enter
    dropdown.send_keys(u'\ue007')

    submit_button.click()


if __name__ == "__main__":
    authenticate()
    fillForm()
    time.sleep(5)
    driver.close()
