import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome(executable_path="/Users/hnstabe/Documents/chromedriver")

driver.get("https://rahulshettyacademy.com/dropdownsPractise/")

driver.maximize_window()

driver.find_element(By.ID, "autosuggest").send_keys("In")

time.sleep(2)

countries = driver.find_elements(By.CSS_SELECTOR, "li[class='ui-menu-item'] a")

print(len(countries))

for country in countries:
    if country.text == "Burkina Faso":
        country.click()
        break

selected = driver.find_element(By.ID, "autosuggest").get_attribute("value")  # getting the new value by using get_attribute()

# assert selected == "Burkina Faso"
if selected == "Burkina Faso":
    print("Test Case Passed")
else:
    print("Test Case Failed")
