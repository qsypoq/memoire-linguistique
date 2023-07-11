from googlesearch import search   
import time, random

def addtolist(url):
    with open(f"presse/url.txt", 'a+') as outfile:
            outfile.write(f"{url}\n")

# to search 
query = {"before:2022-11-01 site:leparisien.fr inurl:leparisien.fr/high-tech informatique",
        "before:2022-11-01 site:leparisien.fr inurl:leparisien.fr/faits-divers google",
        "before:2022-11-01 site:leparisien.fr inurl:leparisien.fr/environnement dechets",
        "before:2022-11-01 site:leparisien.fr inurl:leparisien.fr/economie immobilier",
        "before:2022-11-01 site:leparisien.fr inurl:leparisien.fr/economie crise",
        "before:2022-11-01 site:lavoixdunord.fr inurl:/article/ exposition",
        "before:2022-11-01 site:lavoixdunord.fr inurl:/article/ informatique",
        "before:2022-11-01 site:lavoixdunord.fr inurl:/article/ lille",
        "before:2022-11-01 site:lavoixdunord.fr inurl:/article/ outreau",
        "before:2022-11-01 site:lavoixdunord.fr inurl:/article/ la madeleine",
        }

for dork in query:
    wt = random.uniform(30,60)
    for result in search(dork, tld="fr", num=50, stop=50, pause=wt): 
        addtolist(result)
        time.sleep(5)