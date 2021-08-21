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

    abilities = []

    # Find all their ability dmg info
    results = soup.find(id="mw-content-text")
    passive_ability = results.find("div", class_="skill skill_innate")
    abilities.append(results.find("div", class_="skill skill_q"))
    abilities.append(results.find("div", class_="skill skill_w"))
    abilities.append(results.find("div", class_="skill skill_e"))
    abilities.append(results.find("div", class_="skill skill_r"))
    
    print("Current champ: {}".format(champion))

    fileName = "ScrapedData\{}Test.txt".format(champion)
    file = open(fileName, "w", encoding="utf-8")

    # Passive is written sepretley, different format from normal abilites
    file.write("Passive:\n{}\n".format(passive_ability.find("span").text))

    ability_char = ["Q", "W", "E", "R"]
    for i in range(4):
        # For each ability the champ the champ has, find all damage stats present
        file.write("{} ability :\n".format(ability_char[i]))
        try: 
            # If champ has multiple attributes to their ability, get them all
            all_stats = abilities[i].find_all("dd")
            for stat in all_stats:
                file.write(stat.text.replace("<small>", ".").replace("</small>", ""))
                file.write("\n")
        except:
            # If only one attribute, just get it
            single_stat = abilities[i].find("dd")
            file.write(single_stat.text.replace("<small>", ".").replace("</small>", ""))
        file.write("\n")     
    file.close()

for champ in champions:
    getStats(champ.replace(" ", "_").replace("\n",""))


