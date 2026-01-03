#!/c/Users/jrobe/AppData/Local/Microsoft/WindowsApps/python

import json

class Player:
    def __init__(self, id: str, players: dict, stats: dict, scoring: dict):
        me = players[id]
        myStats = stats[id]
        self.name = me["full_name"]
        self.positions = me["fantasy_positions"]
        self.rookie = me["years_exp"] == 0
        self.age = me["age"]
        self.team = me["status"] if me["team"] is None else me["team"]
        self.active = me["active"]
        season_score = 0
        for key, value in scoring.items():
            if key in myStats:
                season_score += myStats[key]*value
        self.ppg = round(season_score / (1 if "gp" not in myStats else myStats["gp"]), 2)

    def __eq__(self, obj):
        return isinstance(obj, Player) and self.name == obj.name
    
    def __ne__(self, obj):
        return not self == obj

    def __lt__(self, obj):
        if isinstance(obj, Player):
            if self.ppg != obj.ppg:
                return self.ppg > obj.ppg
            if self.age != obj.age:
                return self.age < obj.age
            if self.rookie != obj.rookie:
                return self.rookie
            if len(self.positions) != len(obj.positions):
                return len(self.positions) > len(obj.positions)
            return self.name < obj.name
        return False

    def __str__(self):
        positions = ""
        for pos in self.positions:
            if pos == self.positions[-1]:
                positions = positions + pos
            else:
                positions = "{}{}, ".format(positions, pos)
        return "Name: '{}', Team: '{}', Positions: '{}', Age: {}, PPG: {}".format(self.name, self.team, positions, self.age, self.ppg)

    def csv(self):
        positions = ""
        for pos in self.positions:
            if pos == self.positions[-1]:
                positions = positions + pos
            else:
                positions = "{}{}, ".format(positions, pos)
        return '"{}", "{}", "{}", "{}", "{}"'.format(self.name, positions, self.ppg, self.age, self.team)