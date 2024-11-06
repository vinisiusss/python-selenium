"Волк Тимофей 107а"
from selenium import webdriver
from selenium.webdriver.common.by import By 

driver = webdriver.Chrome()
driver.get("https://www.python.org")

button = driver.find_element(By.ID, "downloads")
button.click()

search = driver.find_element(By.ID, "id-search-field")
search.click()
search.send_keys("python 3.11")

submit = driver.find_element(By.ID, 'submit')
submit.click()
