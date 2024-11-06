#Волк Тимофей
from selenium import webdriver 
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time
driver = webdriver.Chrome()
driver.get('https://ci.nsu.ru/news')
time.sleep(3)
start_date = driver.find_element(By.CSS_SELECTOR, 'input[name="start_date"]')
start_date.clear()
start_date.send_keys("01.10.2020")
end_date = driver.find_element(By.CSS_SELECTOR, 'input[name="end_date"]')
end_date.clear()
end_date.send_keys("01.10.2024")
apply_filter = driver.find_element(By.CSS_SELECTOR, 'button.apply-filter')
apply_filter.click()
time.sleep(3)
while True:
    try:        
        load_more_button = driver.find_element(By.CSS_SELECTOR, 'button.load-more')
        load_more_button.click()        
        time.sleep(3)
    except:        break
news_cards = driver.find_elements(By.CSS_SELECTOR, '.news-card')
with open('result.txt', 'w', encoding='utf-8') as file:
    for card in news_cards:        
        date = card.find_element(By.CSS_SELECTOR, '.news-date').text.strip()
        title = card.find_element(By.CSS_SELECTOR, '.news-title').text.strip()        
        link = card.find_element(By.TAG_NAME, 'a').get_attribute('href')
        img_url = card.find_element(By.TAG_NAME, 'img').get_attribute('src')        
        file.write(f"{date} {title} {link} {img_url}\n")
driver.quit()
