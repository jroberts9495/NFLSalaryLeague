#!/c/Users/jrobe/AppData/Local/Microsoft/WindowsApps/python

class DraftPick:
    def __init__(self, year: int, round: int, owner: str):
        self.year = year
        self.round = round
        self.orig_owner = owner

    def __eq__(self, obj):
        return isinstance(obj, DraftPick) and self.year == obj.year and self.round == obj.round and self.orig_owner == obj.orig_owner
    
    def __ne__(self, obj):
        return not self == obj

    def __lt__(self, obj):
        if isinstance(obj, DraftPick):
            if self.year != obj.year:
                return self.year < obj.year
            if self.round != obj.round:
                return self.round < obj.round
            if self.orig_owner != obj.orig_owner:
                return self.orig_owner < obj.orig_owner
        return False

    def __str__(self):
        fancyRound = {
            1: "1st",
            2: "2nd",
            3: "3rd",
            4: "4th",
            5: "5th",
            6: "6th"
        }

        return "{} {} ({})".format(self.year, fancyRound.get(self.round), self.orig_owner)