import requests
from bs4 import BeautifulSoup

champions_file = open("AllChamps.txt", "r")
champions = champions_file.readlines()
champions_file.close()


def getStats(champion):
    URL = "https://leagueoflegends.fandom.com/wiki/{}/LoL".format(champion.replace("\n",""))
    # Debug
    print("Going to url {}".format(URL))
    page = requests.get(URL)

    soup = BeautifulSoup(page.content, "html.parser")

    results = soup.find(id="mw-content-text")

    abilities = results.find_all("div", class_="skill_leveling")

    fileName = "ScrapedData\{}Test.txt".format(champion.replace("\n",""))
    file = open(fileName, "w", encoding="utf-8")

    for ability in abilities:
        damage_scaling = ability.find("dd")
        file.write(damage_scaling.text.replace("<small>", ".").replace("</small>", ""))
        file.write("\n")

    file.close()

for champ in champions:
    getStats(champ.replace(" ", "_"))


