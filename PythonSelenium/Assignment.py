import time

from selenium import webdriver
from selenium.webdriver.common.by import By

expected_vegetable = ["Brocolli - 1 Kg", "Beetroot - 1 Kg", "Carrot - 1 Kg", "Mushroom - 1 Kg"]
actual_vegetable = []

driver = webdriver.Chrome(executable_path="../chromedriver")

driver.maximize_window()

driver.get("https://rahulshettyacademy.com/seleniumPractise/#")

driver.find_element(By.CSS_SELECTOR, "input.search-keyword").send_keys("ro")

time.sleep(4)

buttons = driver.find_elements(By.XPATH, "//div[@class='product-action']/button")

for btn in buttons:
    actual_vegetable.append(btn.find_element(By.XPATH, "parent::div/parent::div/h4").text) # connection xpath by traversing back
    btn.click()

assert expected_vegetable == actual_vegetable

driver.quit()

