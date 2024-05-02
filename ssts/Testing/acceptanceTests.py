# selenium site acceptance test file
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from PIL import Image
import pytest
#from Screenshot import Screenshot_clipping
import time
import sys
sys.path.insert(0, './')


service = Service(executable_path="./chromedriver")
driver = webdriver.Chrome(service=service)


def check_login():
    driver.get("https://ssts.app/login")
    username_element = driver.find_element(By.ID, "email")
    username_element.send_keys("hannahpenado@gmail.com")
    password_element = driver.find_element(By.ID, "password")
    password_element.send_keys("1234")
    sign_in_button = driver.find_element(By.XPATH, ".//form/button[@type='submit']")
    sign_in_button.click()
    expected_url = "https://ssts.app/"
    current_url = driver.current_url
    assert expected_url == current_url, "sign in url not matching"

def check_create_ticket():
    create_issue_icon = driver.find_element(By.XPATH, ".//a/i[@class='bx bx-edit-alt']")
    create_issue_icon.click()
    # test inputting text into title
    title_input_element = driver.find_element(By.ID, "title")
    title_input_element.send_keys('Acceptance Test')
    # test inputting text into description
    description_input_element = driver.find_element(By.ID, "description")
    description_input_element.send_keys('testing selenium automated acceptance testing for website')
    # test inputting text into worker 
    worker_input_element = driver.find_element(By.ID, "worker")
    worker_input_element.send_keys('Selenium')
    # test inputtin device text
    device_input_element = driver.find_element(By.ID, "device")
    device_input_element.send_keys('Automated Test')
    # test team input

    submit_button = driver.find_element(By.CLASS_NAME, "btn")
    submit_button.click()
    expected_url = "https://ssts.app/view/ticket"
    current_url = driver.current_url
    assert expected_url == current_url, "Sumbitted ticket url not matching"


def check_book_icon():
    book_icon = driver.find_element(By.XPATH, ".//a/i[@class='bx bx-book-open']")
    book_icon.click()
    expected_url = "https://ssts.app/view/ticket"
    current_url = driver.current_url
    print(current_url)
    assert expected_url == current_url, "book icon url not matching"


def check_brain_icon():
    brain_icon = driver.find_element(By.XPATH, ".//a/i[@class='bx bx-brain']")
    brain_icon.click()
    expected_url = "https://ssts.app/view/kb"
    current_url = driver.current_url
    print(current_url)
    assert expected_url == current_url, "brain icon url not matching"


def check_figure_icon():
    stick_figure_icon = driver.find_element(By.XPATH, ".//a/i[@class='bx bxl-ok-ru']")
    stick_figure_icon.click()
    expected_url = "https://ssts.app/"
    current_url = driver.current_url
    print(current_url)
    assert expected_url == current_url, "figure icon url not matching"

def check_setting_icon():
    setting_icon = driver.find_element(By.XPATH, ".//a/i[@class='bx bx-cog']")
    setting_icon.click()
    expected_url = "https://ssts.app/settings"
    current_url = driver.current_url
    print(current_url)
    assert expected_url == current_url, "setting icon url not matching"

def check_dashboard_icon():
    dashboard_icon = driver.find_element(By.XPATH, ".//a/i[@class='bx bx-grid-alt']")
    dashboard_icon.click()
    expected_url = "https://ssts.app/"
    current_url = driver.current_url
    print(current_url)
    assert expected_url == current_url, "dashboard icon url not matching"

def check_new_ticket_icon():
    create_issue_icon = driver.find_element(By.XPATH, ".//a/i[@class='bx bx-edit-alt']")
    create_issue_icon.click()
    expected_url = "https://ssts.app/new/ticket"
    current_url = driver.current_url
    print(current_url)
    assert expected_url == current_url, "new ticket icon url not matching"



def test_site():
    check_login()
    check_new_ticket_icon()
    check_create_ticket()
    check_brain_icon()
    check_book_icon()
    check_dashboard_icon()
    check_setting_icon()
    check_figure_icon()

test_site()

time.sleep(5)

driver.quit()