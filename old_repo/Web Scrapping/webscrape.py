from urllib.request import urlopen

wiki = "https://en.wikipedia.org/wiki/List_of_state_and_union_territory_capitals_in_India"
page = urlopen(wiki)

from bs4 import BeautifulSoup

soup = BeautifulSoup(page, "html5lib")
print (soup.prettify().encode('utf-8'))
