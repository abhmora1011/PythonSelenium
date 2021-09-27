import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path="../chromedriver")

driver.maximize_window()

driver.get("https://www.rahulshettyacademy.com/AutomationPractice/#")

# driver.execute_script("window.scrollTo(0, document.body.scrollHeight);") # [SCROLL PAGE]

assert driver.find_element(By.ID, "displayed-text").is_displayed()

driver.find_element(By.ID, "hide-textbox").click()

assert not(driver.find_element(By.ID, "displayed-text").is_displayed()) # using negation "not" to validate if not displayed

time.sleep(2)

driver.quit() # close the session of the driver

