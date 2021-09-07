from bs4 import BeautifulSoup
import requests as r


class TypeRacerScraper:
    def __init__(self, userID, numberOfResults):
        self.userID = userID
        self.numberOfResults = numberOfResults
        self.url = "https://data.typeracer.com/pit/race_history?user=" + self.userID + "&n=" + self.numberOfResults
        self.source = r.get(self.url)
        self.parsedSource = BeautifulSoup(self.source.content, "html.parser")


    def get_url(self):
        with open("source.html", "+w") as f:
            values = self.parsedSource.find("table", class_="scoresTable").find_all("tr")
            for value in values:
                try:
                    items = value.find_all("td")
                    for item in items:
                        f.write(item.string.strip() + ' ')
                    
                except Exception as e:
                    print(e)

                f.write('------------\n')



def quickTest():
    pass

TypeRacerScraper("not_not_mk", "1000").get_url()
