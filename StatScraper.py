import requests
from bs4 import BeautifulSoup


URL = "https://leagueoflegends.fandom.com/wiki/Garen/LoL"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")


results = soup.find(id="mw-content-text")

ability_dmg = results.find_all("div", class_="skill_leveling")

for ability in ability_dmg:
    damage_scaling = ability.find("dd")
    print(damage_scaling)


