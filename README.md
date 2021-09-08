# TypeRacerScraper
Given a username and quantity of scores. Will scrape and return a CSV of scores in type racer.


>>> from typeracerScraper_package import typeracerScraper as t
>>> df = t.TypeRacerScraper("not_not_mk", "1000").result_dataframe()
>>> print(df)
    Race   Speed Accuracy Points Place
0    753  58 WPM    96.9%     24   4/5
1    752  49 WPM    92.8%     26   5/5
2    751  54 WPM    93.3%     29   5/5
3    750  54 WPM    97.0%     37   3/5
4    749  52 WPM    94.8%     48   2/5
..   ...     ...      ...    ...   ...
748    5  42 WPM    94.4%     33   4/5
749    4  44 WPM    94.7%     23   5/5
750    3  48 WPM    95.7%     29   2/5
751    2  42 WPM    97.2%     20   3/5
752    1  43 WPM    94.8%     26   2/5

[753 rows x 5 columns]
>>> 



