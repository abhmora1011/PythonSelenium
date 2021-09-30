# JS DOM can access any elements on the web page just like how selenium does
# selenium has a method to execute javascript code in it
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path="../chromedriver")

driver.get("https://rahulshettyacademy.com/angularpractice/")

driver.maximize_window()

driver.find_element(By.NAME, "name").send_keys("hello")

print(driver.find_element(By.NAME, "name").text) # This will not print the text input

print(driver.find_element(By.NAME, "name").get_attribute("value")) # There's no javascript executor yet

print(driver.execute_script("return document.getElementsByName('name')[0].value")) # Using the javascript value

shopBtn = driver.find_element(By.CSS_SELECTOR, "a[href='/angularpractice/shop']")

driver.execute_script("arguments[0].click();", shopBtn) # Click using JS || Argument shopBtn is passed to the arguments array

# Use JS script executor if there are no way to get some element
# Selenium do not provides scroll function but JS does

driver.execute_script("window.scrollBy(0,250)", "")

# driver.quit()