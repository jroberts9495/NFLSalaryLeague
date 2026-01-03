#!/c/Users/jrobe/AppData/Local/Microsoft/WindowsApps/python

import datetime, json, sys, os
from requests import get

def update(dirname, force=False, quiet=False, sport="nba", year=datetime.date.today().year):
    updatePlayers(os.path.join(dirname, "NBAplayers.json"), force, quiet, sport)
    updateStats(os.path.join(dirname, "NBAstats.json"), force, quiet, sport, year)

def updateStats(filename, force=False, quiet=False, sport="nba", year=datetime.date.today().year):
    today = datetime.date.today()

    with open(filename, "r") as rb:
        currPlayers = json.load(rb)

    if currPlayers["lastUpdated"] == str(today):
        if not force:
            if not quiet:
                print("Updated stats already today, reupdate not recommended")
            return 1
        else:
            print("Forcing update of stats (not recommended)")

    updatedStats = json.loads(get("https://api.sleeper.app/v1/stats/{}/regular/{}".format(sport, year)).content)

    with open(filename, "w") as wb:
        json.dump(
            {
                "lastUpdated": str(today),
                "stats": updatedStats
            },
            wb,
            indent=2
        )

    return 0


def updatePlayers(filename, force=False, quiet=False, sport="nba"):
    today = datetime.date.today()

    with open(filename, "r") as rb:
        currPlayers = json.load(rb)

    if currPlayers["lastUpdated"] == str(today):
        if not force:
            if not quiet:
                print("Updated players already today, reupdate not recommended")
            return 1
        else:
            print("Forcing update of players (not recommended)")

    updatedPlayers = json.loads(get("https://api.sleeper.app/v1/players/{}".format(sport)).content)

    with open(filename, "w") as wb:
        json.dump(
            {
                "lastUpdated": str(today),
                "players": updatedPlayers
            },
            wb,
            indent=2
        )

    return 0

def main():
    update(os.path.dirname(sys.argv[0]), year=datetime.date.today().year-1)

if __name__ == "__main__":
    main()
