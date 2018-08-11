import requests
from bs4 import BeautifulSoup
import time

url_to_scrape = 'http://www.lolesports.com/en_US/na-lcs/na_2017_summer/standings/regular_season'
r = requests.get(url_to_scrape)

# parse the text of the URL
soup = BeautifulSoup(r.text, "html.parser")

# get the "stats-container" table
stats_table = soup.find("table", class_="stats-container")

# Each row is: Rank/Team/Wins/Losses
format_string = "%-4s %-20s %-s %-s"

print ("Current NA LCS STANDINGS")
print ("-----------------------------")
print (format_string % ("RANK", "TEAM", "W", "L"))
for row in stats_table.find_all("tr"):
    cells = row.find_all("td")
    if len(cells) > 0:
        print (format_string % (cells[0].text.strip(), cells[2].text.strip(), cells[3].text.strip(), cells[4].text.strip()))