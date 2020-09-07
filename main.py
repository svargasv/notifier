import feedparser
import requests
import json
import time

webhook='https://maker.ifttt.com/trigger/nuevo_cap/with/key/mmgAHPsC2HCTjn4T204ejMGZNImJ-9yg6KpBItbeyzn'

def createDict():
    animes=dict()
    with open('season.txt','r') as file:
        lines = file.readlines()
        for line in  lines:
            animes.update({line.rstrip().lower():0})
    return animes

def checkNew(animeDict):
    crunchyroll = feedparser.parse('https://www.crunchyroll.com/rss/anime?lang=esLA')
    content = list()
    for i in range(len(crunchyroll.entries)):
        entrada=crunchyroll.entries[i].title
        content.append(entrada.split(' - ')[0].lower())

    #print(content)
    for titulo in animeDict.keys():
        if titulo in content and animeDict[titulo]==0:
            animeDict[titulo]=1
            notify(titulo)
        if titulo not in content and animeDict[titulo]==1:
            animeDict[titulo]=0
            



     
def notify(title):
    data = {'value1':title}  # Dict de datos que se envian
    try:
        print('Entre a notificar')
        r = requests.get(url=webhook, params=data)
        r.raise_for_status
    except requests.HTTPError as err:
        print(err)


if __name__ == "__main__":
    animeDict=createDict()
    checkNew(animeDict)
    # while True:
    #     checkNew(animeDict)
    #     time.sleep(50)
        

    
