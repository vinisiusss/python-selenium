#Волк Тимофей
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Edge()  
driver.get("https://the-internet.herokuapp.com/context_menu")
time.sleep(2)
element = driver.find_element(By.ID, "hot-spot")
webdriver.ActionChains(driver).context_click(element).perform()
time.sleep(2)
driver.save_screenshot("context_menu_screenshot.png")
alert = driver.switch_to.alert
alert.accept()
driver.get("https://the-internet.herokuapp.com/upload")
time.sleep(2)
file_path = "empty_file.txt" 
upload_element = driver.find_element(By.ID, "file-upload")
upload_element.send_keys(file_path)
submit_button = driver.find_element(By.ID, "file-submit")
submit_button.click()
time.sleep(2)
driver.save_screenshot("upload_screenshot.png")
driver.quit()
print("Скриншоты успешно сохранены.")