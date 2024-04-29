# selenium site acceptance test file
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from PIL import Image
#from Screenshot import Screenshot_clipping
import time
import sys
sys.path.insert(0, './')



service = Service(executable_path="./chromedriver")
driver = webdriver.Chrome(service=service)

#driver.get("https://ssts.app")
driver.get("https://ssts.app/new/ticket")
#create_issue_element = driver.find_element(By.CLASS_NAME, "bx bx-edit-alt")
#create_issue_element.click()
# test inputting text into title
title_input_element = driver.find_element(By.ID, "title")
title_input_element.send_keys('Acceptance Test')
# test inputting text into description
description_input_element = driver.find_element(By.ID, "description")
description_input_element.send_keys('testing selenium automated acceptance testing for website')
driver.save_screenshot('test1_image.png')
screenshot = Image.open('test1_image.png')
print(screenshot)
screenshot.show()
# test inputting text into worker 
worker_input_element = driver.find_element(By.ID, "worker")
worker_input_element.send_keys('Selenium')
# test inputtin device text
device_input_element = driver.find_element(By.ID, "device")
device_input_element.send_keys('Automated Test')
# test client input
'''client_input_element = driver.find_element(By.ID, "client")
client_input_element.send_keys('Selenium Test')'''
# test team input

team_input_element = driver.find_element(By.ID, "team")
team_input_element.send_keys('Hannah selenium test')

driver.save_screenshot('test1_image2.png')
screenshot = Image.open('test1_image2.png')
print(screenshot)
screenshot.show()

time.sleep(20)

#driver.quit()