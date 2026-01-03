#!/c/Users/jrobe/AppData/Local/Microsoft/WindowsApps/python

import json, os
from requests import get
from .DraftPick import DraftPick
from .Constants import Constants
from .Roster import Roster
from .User import User
from .Player import Player

class League:
    def __init__(self, leagueId, year, cachedir):
        self.leagueId = leagueId
        dirtyUsers = json.loads(get("{}{}/users".format(Constants.LEAGUE_URI, leagueId)).content)
        dirtyRosters = json.loads(get("{}{}/rosters".format(Constants.LEAGUE_URI, leagueId)).content)
        dirtyTradedPicks = json.loads(get("{}{}/traded_picks".format(Constants.LEAGUE_URI, leagueId)).content)
        league = json.loads(get("{}{}".format(Constants.LEAGUE_URI, leagueId)).content)
        dirtyScoring = league["scoring_settings"]
        sport = league["sport"]
        with open(os.path.join(cachedir, "NBAplayers.json" if sport == "nba" else "NFLplayers.json")) as rb:
            playerRef = json.load(rb)["players"]
        with open(os.path.join(cachedir, "NBAstats.json" if sport == "nba" else "NFLstats.json")) as rb:
            statsRef = json.load(rb)["stats"]
        ridToName = {}
        for roster in dirtyRosters:
            for user in dirtyUsers:
                if roster["owner_id"] == user["user_id"]:
                    ridToName[roster["roster_id"]] = user["display_name"]
        tradedAway = {}
        tradedTo = {}
        largestRound = 3
        for pick in dirtyTradedPicks:
            if pick["roster_id"] not in tradedAway:
                tradedAway[pick["roster_id"]] = []
            tradedAway[pick["roster_id"]].append(DraftPick(
                int(pick["season"]),
                pick["round"],
                ridToName[pick["roster_id"]]
            ))
            if pick["owner_id"] not in tradedTo:
                tradedTo[pick["owner_id"]] = []
            tradedTo[pick["owner_id"]].append(DraftPick(
                int(pick["season"]),
                pick["round"],
                ridToName[pick["roster_id"]]
            ))
            if pick["round"] > largestRound:
                largestRound = pick["round"]
        cleanRosters = {}
        for roster in dirtyRosters:
            uid = roster["owner_id"]
            rid = roster["roster_id"]
            picks = []
            for theYear in range(year, year+3):
                for thePick in range(1, largestRound+1):
                    pick = DraftPick(theYear, thePick, ridToName[rid])
                    if rid not in tradedAway or pick not in tradedAway[rid]:
                        picks.append(pick)
            if rid in tradedTo:
                for pick in tradedTo[rid]:
                    picks.append(pick)
            picks.sort()
            dirtyPlayers = roster["players"]
            players = []
            for player in dirtyPlayers:
                players.append(Player(player, playerRef, statsRef, dirtyScoring))
            cleanRosters[uid] = Roster(
                players,
                picks
            )
        self.users = []
        for user in dirtyUsers:
            if user["user_id"] in cleanRosters:
                self.users.append(User(
                    user["display_name"],
                    user["user_id"],
                    None if "team_name" not in user["metadata"] else user["metadata"]["team_name"],
                    cleanRosters[user["user_id"]]
                ))