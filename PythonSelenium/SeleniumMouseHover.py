import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path="../chromedriver")

# driver.maximize_window()

driver.get("https://www.rahulshettyacademy.com/AutomationPractice/#")

action = ActionChains(driver)

mouse_to_hover= driver.find_element(By.ID, "mousehover")

action.move_to_element(mouse_to_hover).perform()

top = driver.find_element(By.LINK_TEXT, "Top")

action.move_to_element(top).click().perform()

time.sleep(2)

driver.quit() # close the session of the driver

