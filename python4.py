#Волк Тимофей
from selenium import webdriver 
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWaitfrom 
from selenium.webdriver.support import expected_conditions as EC
import time
driver = webdriver.Edge(options=options)
time.sleep(5)
link = forYou.get_attribute('href').driver.get(link)
time.sleep(5)
videoLinks = [video.get_attribute('href') for video in videos if 'video' in video.get_attribute('href')]
trends = driver.find_element(By.XPATH, "//a[@data-title='Тренды']").linkTrends = trends.get_attribute('href')
driver.get(linkTrends) 
time.sleep(5)
videosTrends = driver.find_elements(By.XPATH, "//a[contains(@class, 'video_item__thumb_link')]")
videoLinksTrends = [video.get_attribute('href') for video in videosTrends if 'video' in video.get_attribute('href')]
allLinks = videoLinks + videoLinks
TrendsvideoData = []
for link in allLinks:    driver.get(link)
time.sleep(5)  
try:        
        title = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//div[@data-testid='video_modal_title']"))        ).text
        additional_info = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//div[@data-testid='video_modal_additional_info']//span"))        ).text
        views, creation_date = additional_info.split('·')        
        channel_name = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//a[contains(@class, 'Owner-module__ownerName')]"))        ).text
        try:
            sub = WebDriverWait(driver, 10).until(                EC.visibility_of_element_located((By.XPATH,
                                                  "//span[@class='vkuiTypography vkuiSimpleCelltext vkuiSimpleCellsubtitle vkuiFootnote']"))            ).text
        except Exception:            sub = "Нет данных"
        likes = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH,                                              "//span[contains(@class, 'vkuiTypography--normalize') and contains(@class, 'PostFooterAction-module__label--qfx7o')]"))
        ).text
 except Exception as e:
    print(f"Ошибка при обработке ссылки {link}: {e}")
 file.write(f"{len(videoData)}\n")    for data in videoData:
        file.write(str(data) + '\n')        print(str(data))
driver.quit()