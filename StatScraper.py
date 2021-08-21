import requests
from bs4 import BeautifulSoup


URL = "https://leagueoflegends.fandom.com/wiki/Garen/LoL"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")


results = soup.find(id="mw-content-text")

abilities = results.find_all("div", class_="skill_leveling")

file = open("ScrapedData\GarenTest.txt", "w", encoding="utf-8")

for ability in abilities:
    damage_scaling = ability.find("dd")
    file.write(damage_scaling.text.replace("<small>", ".").replace("</small>", ""))
    file.write("\n")

file.close()
    


