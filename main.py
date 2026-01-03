#!/c/Users/jrobe/AppData/Local/Microsoft/WindowsApps/python

import argparse, json, sys, datetime, os
from requests import get
from classes.League import League
from classes.Constants import Constants
from classes.cache.updatePlayers import updateStats, updatePlayers

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from math import floor

def getParser(add_help=True):
    parser = argparse.ArgumentParser(description="Allows the creation and manipulation of leagues", add_help=add_help)
    parser.add_argument("--league-id", type=int, help="The LeagueID for the league you wish to manipulate")
    parser.add_argument("--find-leagues", metavar="USERNAME", help="When used, the program finds league IDs associated with the username provided")
    parser.add_argument("--sport", default="nfl", help="Specify which sport. Default: NFL")
    parser.add_argument("--year", default=datetime.date.today().year, type=int, help="The year which you want to reference. Default: {}".format(datetime.date.today().year))
    parser.add_argument("--force-update", action="store_true", help="Forces an update to the players list")
    parser.add_argument("--get-picks", metavar="USERNAME", help="Returns the draft picks for your roster")
    parser.add_argument("--get-players", metavar="USERNAME", help="Returns the players on your roster")
    parser.add_argument("--get-managers", action="store_true", help="Returns the names of team managers")
    parser.add_argument("--age-curve", type=int, nargs="?", help="Plot age curves for players.")
    parser.add_argument("--csv", action="store_true", help="Print CSV instead of strings")

    return parser

def findLeagues(username, sport, year):
    uid = json.loads(get("{}{}".format(Constants.USER_URI, username)).content)["user_id"]
    dirtyLeagues = json.loads(get("{}{}/leagues/{}/{}".format(Constants.USER_URI, uid, sport, year)).content)
    for league in dirtyLeagues:
        print("Name: {}, LeagueID: {}".format(league["name"], league["league_id"]))

def gaussian(x, amp, mean, std_dev):
    return amp * np.exp(-(x-mean)**2 / (2*std_dev**2))

def age_curves(players, percentile=0.25, verbose=False):
    for position in ["QB", "RB", "WR", "TE"]:
        if verbose:
            print(position)
        ages = []
        scores = []
        peakPlayers = 0
        for ii in range(20,40):
            numPlayers = 0
            for player in players:
                if player.age == ii and position in player.positions and player.ppg > 0.0:
                    numPlayers += 1
            peakPlayers = max(peakPlayers, numPlayers)
        for ii in range(20,40):
            numPlayers = 0
            bestScores = []
            for player in players:
                if player.age == ii and position in player.positions and player.ppg > 0.0:
                    numPlayers += 1
                    bestScores.append(player.ppg)
            if len(bestScores):
                bestScores.sort(reverse=True)
                ages.append(ii)
                scores.append(bestScores[floor(len(bestScores)*percentile)] * (1 + 3 * numPlayers / peakPlayers)/4 )
            if verbose:
                print("[{}] {:2d} {:4.1f}".format(ii, numPlayers, bestScores[floor(len(bestScores)*percentile)] * (1 + numPlayers / peakPlayers)/2 ),end="   ")
            if ii == 29 and verbose:
                print()
        if verbose:
            print()
        xdata = np.array(ages)
        ydata = np.array(scores)
        initial_guess = [17.0, 28.0, 4.0]
        popt, pcov = curve_fit(gaussian, xdata, ydata, p0=initial_guess, maxfev=500000)
        amp, mean, std_dev = popt
        print("{}: {} amp, {} mean, {} std".format(position, amp, mean, std_dev))
        plt.scatter(xdata, ydata, label="{} Orig".format(position), s=10)
        if position == "QB":
            plt.plot(xdata, gaussian(xdata, 9, 28, 3)+6, label="QB Fit")
        else:
            plt.plot(xdata, gaussian(xdata, *popt), label="{} Fit".format(position))
    plt.title("Age Curves for top {:.0f}th percentile".format(percentile*100))
    plt.xlabel("Age")
    plt.ylabel("Score")
    plt.legend()
    plt.show()

def main(argv = sys.argv[1:]):
    parser = getParser()
    args = parser.parse_args(argv)

    league_id = Constants.WHITE_HOUSE_LEAGUE_ID if not args.league_id else args.league_id
    sport = args.sport.lower()
    players_cache_dir = os.path.join(os.path.dirname(sys.argv[0]), "classes/cache/")

    if not updatePlayers(os.path.join(players_cache_dir, "NBAplayers.json" if args.sport == "nba" else "NFLplayers.json"), args.force_update, True, args.sport):
        print("Players list updated")
    if not updateStats(os.path.join(players_cache_dir, "NBAstats.json" if args.sport == "nba" else "NFLstats.json"), args.force_update, True, args.sport, datetime.date.today().year-1):
        print("Stats updated")

    if args.find_leagues:
        findLeagues(args.find_leagues, sport, args.year)
    else:
        league = League(league_id, args.year, players_cache_dir)
        # print(json.dumps(league, default=lambda o: o.__dict__))

        players = []
        for user in league.users:
            if args.get_managers:
                print(user.uname)
            if args.get_picks and user.uname == args.get_picks:
                for pick in user.roster.picks:
                    print(pick)
            if args.get_players and user.uname == args.get_players:
                players = user.roster.players
                players.sort()
                for player in players:
                    if args.csv:
                        print(player.csv())
                    else:
                        print(player)
            players.extend(user.roster.players)
        if args.age_curve:
            age_curves(players, args.age_curve/100 if args.age_curve else 0.25)

if __name__ == "__main__":
    main()