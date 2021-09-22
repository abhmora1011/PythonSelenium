
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome(executable_path="/Users/hnstabe/Documents/chromedriver")

driver.get("https://reekoh.com/")

driver.implicitly_wait(10)

assert "Reekoh" in driver.title

driver.maximize_window()

wait = WebDriverWait(driver, 10)

integration_link = wait.until(EC.element_to_be_clickable((By.XPATH, "//li[@id='menu-item-4210']/a")))

integration_link.click()

assert "Reekoh | Integrations" in driver.title

gateway_link = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@class='plugin-types']/div/li[4]/a")))

gateway_link.click()

assert "Reekoh | Plugins" in driver.title

#driver.find_element(By.ID, "keywords").send_keys("HTTP Gateway")

#driver.find_element(By.ID, "keywords").send_keys(Keys.ENTER)

#driver.find_element(By.XPATH, "//*[@id='dropdownMenu']").click()

# driver.find_element(By.XPATH, "")

container = driver.find_elements(By.XPATH, "//*[@class='plugin-link']")

driver.find_element(By.XPATH, "(//div[@id='plugin']/div/div[2])[2]").text

text = [my_elem.text for my_elem in WebDriverWait(driver, 10).until(EC.visibility_of_all_elements_located((By.XPATH, "//*[@class='plugin-link']")))]

for i in text:
    if "HTTP Gateway" in i:
        print("HTTP Gateway is on the list")




