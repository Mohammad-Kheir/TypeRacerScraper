# TypeRacerScraper
Given a username and quantity of scores. Will scrape and return a JSON of scores in type racer. https://pypi.org/project/typeRacerScraper-pkg/

from typeracerScraper_package import typeracerScraper as t

df = t.TypeRacerScraper("not_not_mk", "1000").result_json()

print(df)
