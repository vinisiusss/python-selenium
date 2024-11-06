"Волк Тимофей"
import requests
from lxml import html
from bs4 import BeautifulSoup

url = "https://www.python.org/"
web = requests.get(url)

tree = html.fromstring(web.content)

web_content = web.content
soup = BeautifulSoup(web_content, 'html.parser')

img_src = tree.xpath('//h1/img/@src')
print("Ссылка на изображение в заголовке h1:")
if img_src:
    print(f"{url} {img_xpath[0]}")

about = tree.xpath('//li[@id="about"]/ul//a/@href')
print("Ссылки всех элементов 'a' в разделе 'About':")
if about:
    for link in about:
        print(f"{url}{link}" if link.startswitch('/') else link)

h2text = soup.select('h2')
print("Текст всех заголовков h2")
for h2 in h2text:
    print(h2.get_text())


nav_link = soup.select('#mainnav a')
print("Ссылки навигации")
for link in nav_link:
    print(link['href'])
