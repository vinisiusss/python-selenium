from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import base64

# Настройка WebDriver для Chrome
driver = webdriver.Chrome()  # Замените на webdriver.Edge() если используете Edge

# Открываем вкладки
driver.get("https://www.base64encode.org/")
driver.execute_script("window.open('https://ru.wikipedia.org', '_blank');")
driver.execute_script("window.open('https://en.wikipedia.org', '_blank');")

# Получаем все открытые вкладки
tabs = driver.window_handles

# Переходим на русскую википедию
driver.switch_to.window(tabs[1])

# Открываем 5 случайных статей на русской Википедии
titles = []
for _ in range(5):
    driver.get("https://ru.wikipedia.org/wiki/Специальная:Случайная_страница")
    time.sleep(2)  # Ждем загрузки страницы
    title = driver.title
    titles.append(title)

# Скриншот русской Википедии
driver.save_screenshot("ru_wiki_random_articles.png")

# Переходим на английскую Википедию
driver.switch_to.window(tabs[2])

# Открываем 5 случайных статей на английской Википедии
for _ in range(5):
    driver.get("https://en.wikipedia.org/wiki/Special:Random")
    time.sleep(2)  # Ждем загрузки страницы
    title = driver.title
    titles.append(title)

# Скриншот английской Википедии
driver.save_screenshot("en_wiki_random_articles.png")

# Закрываем все открытые статьи
driver.switch_to.window(tabs[1])  # Переходим обратно на русскую вики

for _ in range(5):
    driver.close()  # Закрываем вкладку случайной статьи
    driver.switch_to.window(driver.window_handles[1])  # Переходим на следующую вкладку

driver.switch_to.window(tabs[2])  # Переходим обратно на английскую вики

for _ in range(5):
    driver.close()  # Закрываем вкладку случайной статьи
    driver.switch_to.window(driver.window_handles[1])  # Переходим на следующую вкладку

# Переходим на вкладку конвертера
driver.switch_to.window(tabs[0])

# Переформатируем заголовки в base64 формат и выводим в консоль
for title in titles:
    encoded_title = base64.b64encode(title.encode()).decode()
    print(f"Title: {title}, Base64: {encoded_title}")

# Скриншот консоли (в данном случае просто делаем скриншот страницы конвертера)
driver.save_screenshot("base64_converter_console.png")

# Закрываем драйвер
driver.quit()
