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

driver.get("https://ssts.app")
#driver.get("https://ssts.app/new/ticket")
time.sleep(3)
create_issue_icon = driver.find_element(By.XPATH, ".//a/i[@class='bx bx-edit-alt']")
create_issue_icon.click()
time.sleep(2)
# test inputting text into title
title_input_element = driver.find_element(By.ID, "title")
title_input_element.send_keys('Acceptance Test')
time.sleep(2)
# test inputting text into description
description_input_element = driver.find_element(By.ID, "description")
description_input_element.send_keys('testing selenium automated acceptance testing for website')
time.sleep(2)
#driver.save_screenshot('test1_image.png')
#screenshot = Image.open('test1_image.png')
#print(screenshot)
#screenshot.show()
# test inputting text into worker 
worker_input_element = driver.find_element(By.ID, "worker")
worker_input_element.send_keys('Selenium')
time.sleep(2)
# test inputtin device text
device_input_element = driver.find_element(By.ID, "device")
device_input_element.send_keys('Automated Test')
time.sleep(2)
# test client input
'''client_input_element = driver.find_element(By.ID, "client")
client_input_element.send_keys('Selenium Test')'''
# test team input

team_input_element = driver.find_element(By.ID, "team")
team_input_element.send_keys('Hannah selenium test')
time.sleep(2)

submit_button = driver.find_element(By.CLASS_NAME, "btn")
submit_button.click()
time.sleep(2)

call_icon = driver.find_element(By.XPATH, ".//a/i[@class='bx bx-phone']")
call_icon.click()
time.sleep(2)

book_icon = driver.find_element(By.XPATH, ".//a/i[@class='bx bx-book-open']")
book_icon.click()
time.sleep(2)

brain_icon = driver.find_element(By.XPATH, ".//a/i[@class='bx bx-brain']")
brain_icon.click()
time.sleep(2)

stick_figure_icon = driver.find_element(By.XPATH, ".//a/i[@class='bx bxl-ok-ru']")
stick_figure_icon.click()
time.sleep(2)

setting_icon = driver.find_element(By.XPATH, ".//a/i[@class='bx bx-cog]")
setting_icon.click()
time.sleep(2)

dashboard_icon = driver.find_element(By.XPATH, ".//a/i[@class='bx bx-grid-alt']")
dashboard_icon.click()
time.sleep()

menu_bar_icon = driver.find_element(By.XPATH, ".//a/i[@class='bx bx-menu']")
menu_bar_icon.click()
time.sleep(2)



#driver.save_screenshot('test1_image2.png')
#screenshot = Image.open('test1_image2.png')
#print(screenshot)
#screenshot.show()

time.sleep(20)

#driver.quit()