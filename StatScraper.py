import requests
from bs4 import BeautifulSoup

champions_file = open("AllChamps.txt", "r")
champions = champions_file.readlines()
champions_file.close()


def getStats(champion):
    # Go to champs wiki page
    URL = "https://leagueoflegends.fandom.com/wiki/{}/LoL".format(champion)
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, "html.parser")

    # Find all their ability dmg info
    results = soup.find(id="mw-content-text")
    abilities = results.find_all("div", class_="skill_leveling")
    
    print("Current champ: {}".format(champion))

    fileName = "ScrapedData\{}Test.txt".format(champion)
    file = open(fileName, "w", encoding="utf-8")

    for ability in abilities:
        damage_scaling = ability.find("dd")
        try: 
            file.write(damage_scaling.text.replace("<small>", ".").replace("</small>", ""))
        except:
            print("Went wrong at {}".format(champion))
        file.write("\n")

    file.close()

for champ in champions:
    getStats(champ.replace(" ", "_").replace("\n",""))


