from bs4 import BeautifulSoup
import requests

MATCH_HISTORY = "http://matchhistory.na.leagueoflegends.com/en/#match-details/TRLH1/1002310123?gameHash=84cb73aecb92af83&tab=overview"
STANDINGS = "http://www.lolesports.com/en_US/na-lcs/na_2017_summer/standings/regular_season"
DL = "https://lol.gamepedia.com/Doublelift"
page = requests.get(DL)
soup = BeautifulSoup(page.content, 'html.parser')
print(soup.prettify().encode("utf-8"))