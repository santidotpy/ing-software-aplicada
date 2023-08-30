import os
import time
from dotenv import load_dotenv
from selenium import webdriver

load_dotenv()

# Set up the Chrome WebDriver
driver = webdriver.Chrome()
driver.get(os.environ.get('FORM_URL'))


def authenticate():

    # busco los elementos por id
    username_input = driver.find_element("id", "username")
    password_input = driver.find_element("id", "password")
    login_button = driver.find_element("id", "loginbtn")

    # lleno los campos y logineo
    username_input.send_keys(os.environ.get('MAIL'))
    password_input.send_keys(os.environ.get('PASS'))
    login_button.click()


def fillForm():

    # busco los elementos por id
    question_one = driver.find_element("id", "auto-rb0001")
    dropdown = driver.find_element("id", "dropSelecciòn")

    # busco el boton de submit por name porque no tiene id
    submit_button = driver.find_element("name", "submit")

    question_one.click() # click en la primera pregunta de multiple choice
   
    # como era un dropdown, tuve que hacerlo de esta forma
    dropdown.click()

    # flecha abajo 3 veces
    dropdown.send_keys(u'\ue015')
    dropdown.send_keys(u'\ue015')
    dropdown.send_keys(u'\ue015')

    # enter
    dropdown.send_keys(u'\ue007')

    submit_button.click()


if __name__ == "__main__":
    authenticate()
    fillForm()
    time.sleep(5)
    driver.close()
