from selenium import webdriver
from selenium.webdriver.common.by import By

# Headless Test will not invoke the browser but we can see the result

chrome_option = webdriver.ChromeOptions()
chrome_option.add_argument("--start-maximized") # To maximize the browser
chrome_option.add_argument("headless") # To switch in headless mode
chrome_option.add_argument("--ignore-certificate-errors")

driver = webdriver.Chrome(executable_path="../chromedriver", options=chrome_option)

driver.get("https://rahulshettyacademy.com/angularpractice/")

print(driver.title)
