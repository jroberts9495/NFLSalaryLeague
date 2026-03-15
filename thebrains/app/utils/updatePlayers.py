#!/usr/local/bin/python3

import datetime, json, sys, os
from requests import get

def update(dirname, force=False, quiet=False, year=datetime.date.today().year):
    updatePlayers(os.path.join(dirname, "NFLplayers_{}.json".format(year)), force, quiet)
    updateStats(os.path.join(dirname, "NFLstats_{}.json".format(year)), force, quiet, year)

def updateStats(filename, force=False, quiet=False, year=datetime.date.today().year):
    today = datetime.date.today()

    if os.path.exists(filename):
        with open(filename, "r") as rb:
            currPlayers = json.load(rb)

        if currPlayers["lastUpdated"] == str(today):
            if not force:
                if not quiet:
                    print("Updated stats already today, reupdate not recommended")
                return 1
            else:
                print("Forcing update of stats (not recommended)")

    updatedStats = json.loads(get("https://api.sleeper.app/v1/stats/nfl/regular/{}".format(year)).content)

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


def updatePlayers(filename, force=False, quiet=False):
    today = datetime.date.today()

    if os.path.exists(filename):
        with open(filename, "r") as rb:
            currPlayers = json.load(rb)

        if currPlayers["lastUpdated"] == str(today):
            if not force:
                if not quiet:
                    print("Updated players already today, reupdate not recommended")
                return 1
            else:
                print("Forcing update of players (not recommended)")

    updatedPlayers = json.loads(get("https://api.sleeper.app/v1/players/nfl").content)

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
    ii = 2010
    while ii < 2026:
        update(os.path.dirname(sys.argv[0]), year=ii) #datetime.date.today().year-1)
        ii += 1

if __name__ == "__main__":
    main()
