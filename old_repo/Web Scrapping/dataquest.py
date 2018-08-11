from bs4 import BeautifulSoup
import requests

page = requests.get("http://dataquestio.github.io/web-scraping-pages/simple.html")
print(page)
print(page.status_code)
print(page.content)
soup = BeautifulSoup(page.content, 'html.parser')
print(soup.prettify())
print(list(soup.children))
print([type(item) for item in list(soup.children)])
html = list(soup.children)[2]
body = list(html.children)[3]
p = list(body.children)[1]
print(p.get_text())

soup = BeautifulSoup(page.content, 'html.parser')
print(soup.find_all('p'))
print(soup.find_all('p')[0].get_text())

page = requests.get("http://dataquestio.github.io/web-scraping-pages/ids_and_classes.html")
soup = BeautifulSoup(page.content, 'html.parser')
print(soup.prettify())
print(soup.find_all('p', class_='outer-text'))
print(soup.find_all(id="first"))
print(soup.select("div p"))