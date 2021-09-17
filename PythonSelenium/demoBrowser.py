from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(executable_path="/Users/hnstabe/Documents/chromedriver")
#driver = webdriver.Firefox(executable_path="/Users/hnstabe/Documents/geckodriver")
#driver = webdriver.Safari(executable_path="")

driver.get("https://www.google.com")

print(driver.title)
print(driver.current_url)
#driver.find_element_by_name("q").send_keys("Hello")
driver.maximize_window()
driver.find_element(By.NAME, "q").send_keys("hello")
#driver.back()
#driver.refresh()

#driver.close()