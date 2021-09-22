import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


driver = webdriver.Chrome(executable_path="/Users/hnstabe/Documents/chromedriver")

driver.get("https://www.rahulshettyacademy.com/AutomationPractice/")

driver.maximize_window()

checkBoxes = driver.find_elements(By.XPATH, "//input[@type='checkbox']")

print(len(checkBoxes))

for checkBox in checkBoxes:
    if checkBox.get_attribute("value") == "option2":
        checkBox.click()
        assert checkBox.is_selected()

radioBtn = driver.find_elements(By.NAME, "radioButton")

radioBtn[2].click()

assert radioBtn[2].is_selected()


