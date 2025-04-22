from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)# keeps chrome open

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://secure-retreat-92358.herokuapp.com/")

first_name = driver.find_element(By.NAME, "fName")
first_name.send_keys("Philip")
last_name = driver.find_element(By.NAME, "lName")
last_name.send_keys("Mueller")
email = driver.find_element(By.NAME, "email")
email.send_keys("pknath761@gmail.com")
submit = driver.find_element(By.CSS_SELECTOR, "form button")
submit.click()
