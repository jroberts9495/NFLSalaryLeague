#!/usr/local/bin/python3

import datetime, json, sys, os
from requests import get

def update(dirname, force=False, quiet=False, maxyear=2025):
    lastupdatedfile = os.path.join(dirname, "updated.txt")
    if os.path.exists(lastupdatedfile):
        with open(lastupdatedfile, "r") as rb:
            if rb.readline() == str(datetime.date.today()):
                if not force:
                    if not quiet:
                        print("Already updated stats today, reupdate not recommended")
                        return 1
                else:
                    print("Forcing update of stats (not recommended)")

    year = 2010
    while year <= 2025:
        updateStats(os.path.join(dirname, "NFLstats_{}.json".format(year)), force, quiet, year)
        year += 1
    updatePlayers(os.path.join(dirname, "NFLplayers.json".format()), force, quiet)

    with open(lastupdatedfile, "w") as wb:
        wb.write(str(datetime.date.today()))
    return 0

def updateStats(filename, force=False, quiet=False, year=datetime.date.today().year):
    statsContent = json.loads(get("https://api.sleeper.app/v1/stats/nfl/regular/{}".format(year)).content)

    with open(filename, "w") as wb:
        json.dump(statsContent, wb, separators=[',',':'])
    return 0


def updatePlayers(filename, force=False, quiet=False):
    playersContent= json.loads(get("https://api.sleeper.app/v1/players/nfl").content)

    with open(filename, "w") as wb:
        json.dump(playersContent, wb, separators=[',',':'])
    return 0

def main(args=sys.argv[1:]):
    if len(args):
        dir = args[0]
    else:
        dir = "/app/data"
    update(dir) #datetime.date.today().year-1)

if __name__ == "__main__":
    main()
