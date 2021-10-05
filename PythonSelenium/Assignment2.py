import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

chrome_option = webdriver.ChromeOptions()
chrome_option.add_argument("--start-maximized")  # To maximize the browser
# chrome_option.add_argument("headless") # To switch in headless mode


add_to_cart_item = []
cart_items = []

driver = webdriver.Chrome(executable_path="../chromedriver", options=chrome_option)

driver.get("https://rahulshettyacademy.com/angularpractice/")

driver.find_element(By.XPATH, "//a[text()='Shop']").click()

list_of_products = driver.find_elements(By.XPATH, "//div[@class='card h-100']")

for product in list_of_products:
    item_title = product.find_element(By.XPATH, "div/h4/a")
    item_btn = product.find_element(By.XPATH, "div/h4/a/../../../div/button")
    if item_title.text == "Blackberry":
        item_btn.click()
    add_to_cart_item.append(item_title.text)
    print(product.text)

print("+++++++++++++++++++++++")
print(add_to_cart_item)

action = ActionChains(driver)

checkout = driver.find_element(By.PARTIAL_LINK_TEXT, "Checkout")

time.sleep(3)

action.move_to_element(checkout).click().perform()

list_of_added_to_cart = driver.find_elements(By.XPATH, "//tr/td/div[@class='media']/div/h4")

for list_to_cart in list_of_added_to_cart:
    print(list_to_cart.text)
    cart_items.append(list_to_cart.text)

assert "Blackberry" in cart_items

driver.find_element(By.XPATH, "//button[contains(text(),'Checkout')]").click()

driver.find_element(By.ID, "country").send_keys("Ind")

wait = WebDriverWait(driver, 10)

list_of_countries = wait.until(EC.presence_of_element_located((By.LINK_TEXT, "India")))

driver.find_element(By.LINK_TEXT, "India").click()

checkbox = driver.find_element(By.XPATH, "//div[@class='checkbox checkbox-primary']")

checkbox.click()

driver.find_element(By.CSS_SELECTOR, "[type='submit']").click()

success = driver.find_element(By.CLASS_NAME, "alert-success").text

assert "Success! Thank you!" in success

driver.get_screenshot_as_file("screen.png")

