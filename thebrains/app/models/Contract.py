#!/c/Users/jrobe/AppData/Local/Microsoft/WindowsApps/python

from classes.Player import Player

class Incentive:
    def isValid(self, player:Player):
        if not isinstance(player, Player) or self.stat not in player.stats:
            player.stats[self.stat] = 0.0
        if self.type == "LE":
            return player.stats[self.stat] > (self.threshold / 1.2)
        if self.type == "GE":
            return player.stats[self.stat] < (self.threshold * 1.2)
        return False

    def hasVested(self, player: Player):
        if not isinstance(player, Player) or self.stat not in player.stats:
            player.stats[self.stat] = 0.0
        if self.type == "LE":
            return player.stats[self.stat] <= self.threshold
        if self.type == "GE":
            return player.stats[self.stat] >= self.threshold
        return False

    def __init__(self, stat, type, threshold, bonus):
        self.stat = stat
        self.type = type
        self.threshold = threshold
        self.bonus = bonus

    def __eq__(self, obj):
        return isinstance(obj, Incentive) and \
            self.stat == obj.stat and \
            self.type == obj.type and \
            self.threshold == obj.threshold and \
            self.bonus == obj.bonus
    
    def __ne__(self, obj):
        return not self == obj

    def __lt__(self, obj):
        if isinstance(obj, Incentive):
            if self.bonus != obj.bonus:
                return self.bonus < obj.bonus
            if self.threshold != obj.threshold:
                return self.threshold > obj.threshold
            if self.stat != obj.stat:
                return self.stat < obj.stat
            return self.type < obj.type
        return False

    @staticmethod
    def GamesPlayed(threshold, bonus):
        return Incentive("gp", "GE", threshold, bonus)

    @staticmethod
    def GamesStarted(threshold, bonus):
        return Incentive("gs", "GE", threshold, bonus)

    @staticmethod
    def GamesActive(threshold, bonus):
        return Incentive("gms_active", "GE", threshold, bonus)

    @staticmethod
    def Fumbles(threshold, bonus):
        return Incentive("fum", "LE", threshold, bonus)

    @staticmethod
    def FumblesLost(threshold, bonus):
        return Incentive("fum_lost", "LE", threshold, bonus)

    @staticmethod
    def Touchdowns(threshold, bonus):
        return Incentive("anytime_tds", "GE", threshold, bonus)

    @staticmethod
    def Penalties(threshold, bonus):
        return Incentive("penalty", "LE", threshold, bonus)

    @staticmethod
    def PenaltyYards(threshold, bonus):
        return Incentive("penalty_yd", "LE", threshold, bonus)

    @staticmethod
    def OffensiveSnaps(threshold, bonus):
        return Incentive("off_snp", "GE", threshold, bonus)

    @staticmethod
    def FantasyPointsPerGame(threshold, bonus):
        return Incentive("pts_half_ppr", "GE", threshold, bonus)

    @staticmethod
    def PositionRank(threshold, bonus):
        return Incentive("pos_rank_half_ppr", "LE", threshold, bonus)

    @staticmethod
    def Rank(threshold, bonus):
        return Incentive("rank_half_ppr", "LE", threshold, bonus)

    @staticmethod
    def PassingTouchdowns(threshold, bonus):
        return Incentive("pass_td", "GE", threshold, bonus)

    @staticmethod
    def PassingYards(threshold, bonus):
        return Incentive("pass_yd", "GE", threshold, bonus)

    @staticmethod
    def PassingAttempts(threshold, bonus):
        return Incentive("pass_att", "GE", threshold, bonus)

    @staticmethod
    def Completions(threshold, bonus):
        return Incentive("pass_cmp", "GE", threshold, bonus)

    @staticmethod
    def Incompletions(threshold, bonus):
        return Incentive("pass_inc", "LE", threshold, bonus)

    @staticmethod
    def CompletionPercentage(threshold, bonus):
        return Incentive("cmp_pct", "GE", threshold, bonus)

    @staticmethod
    def Interceptions(threshold, bonus):
        return Incentive("pass_int", "LE", threshold, bonus)

    @staticmethod
    def Sacks(threshold, bonus):
        return Incentive("pass_sack", "LE", threshold, bonus)

    @staticmethod
    def PassingRushingYards(threshold, bonus):
        return Incentive("pass_rush_yd", "GE", threshold, bonus)

    @staticmethod
    def RedZonePassingAttempts(threshold, bonus):
        return Incentive("pass_rz_att", "GE", threshold, bonus)

    @staticmethod
    def ReceivingTouchdowns(threshold, bonus):
        return Incentive("rec_td", "GE", threshold, bonus)

    @staticmethod
    def ReceivingYards(threshold, bonus):
        return Incentive("rec_yd", "GE", threshold, bonus)

    @staticmethod
    def Targets(threshold, bonus):
        return Incentive("rec_tgt", "GE", threshold, bonus)

    @staticmethod
    def Receptions(threshold, bonus):
        return Incentive("rec", "GE", threshold, bonus)
    
    @staticmethod
    def Drops(threshold, bonus):
        return Incentive("rec_drop", "LE", threshold, bonus)

    @staticmethod
    def RedZoneTargets(threshold, bonus):
        return Incentive("rec_rz_tgt", "GE", threshold, bonus)

    @staticmethod
    def YardsPerTarget(threshold, bonus):
        return Incentive("rec_ypt", "GE", threshold, bonus)

    @staticmethod
    def YardsPerReception(threshold, bonus):
        return Incentive("rec_ypr", "GE", threshold, bonus)

    @staticmethod
    def RushingTouchdowns(threshold, bonus):
        return Incentive("rush_td", "GE", threshold, bonus)

    @staticmethod
    def RushingYards(threshold, bonus):
        return Incentive("rush_yd", "GE", threshold, bonus)

    @staticmethod
    def RushAttempts(threshold, bonus):
        return Incentive("rush_att", "GE", threshold, bonus)

    @staticmethod
    def ScrimmageYards(threshold, bonus):
        return Incentive("rush_rec_yd", "GE", threshold, bonus)

    @staticmethod
    def RedZoneRushAttempts(threshold, bonus):
        return Incentive("rush_rz_att", "GE", threshold, bonus)

    @staticmethod
    def getIncentiveTypes(position = "all"):
        # All incentives are for NFL statistics. Games Started, for example, is in the NFL not on your team.
        # Incentives for all
        options = {
            "Games Played": Incentive.GamesPlayed,
            "Games Started": Incentive.GamesStarted,
            "Games Active": Incentive.GamesActive,
            "Fumbles": Incentive.Fumbles,
            "Fumbles Lost": Incentive.FumblesLost,
            "Touchdowns": Incentive.Touchdowns,
            "Penalties": Incentive.Penalties,
            "Penalty Yards": Incentive.PenaltyYards,
            "Offensive Snaps": Incentive.OffensiveSnaps,
            "Fantasy Points Per Game": Incentive.FantasyPointsPerGame,
            "Position Rank": Incentive.PositionRank,
            "Rank": Incentive.Rank
        }
        # Incentives based on passing
        if position == "qb" or position == "all":
            options.update({
                "Passing Touchdowns": Incentive.PassingTouchdowns,
                "Passing Yards": Incentive.PassingYards,
                "Passing Attempts": Incentive.PassingAttempts,
                "Completions": Incentive.Completions,
                "Incompletions": Incentive.Incompletions,
                "Completion Percentage": Incentive.CompletionPercentage,
                "Interceptions": Incentive.Interceptions,
                "Sacks": Incentive.Sacks,
                "Passing + Rushing Yards": Incentive.PassingRushingYards,
                "Red Zone Passing Attempts": Incentive.RedZonePassingAttempts
            })
        # Incentives based on receptions
        if position == "wr" or position == "te" or position == "rb" or position == "all":
            options.update({
                "Receiving Touchdowns": Incentive.ReceivingTouchdowns,
                "Receiving Yards": Incentive.ReceivingYards,
                "Targets": Incentive.Targets,
                "Receptions": Incentive.Receptions,
                "Red Zone Targets": Incentive.RedZoneTargets,
                "Yards Per Target": Incentive.YardsPerTarget,
                "Yards Per Reception": Incentive.YardsPerReception,
                "Drops": Incentive.Drops
            })
        # Incentives based on rushing
        if position == "rb" or position == "qb" or position == "all":
            options.update({
                "Rushing Touchdowns": Incentive.RushingTouchdowns,
                "Rushing Yards": Incentive.RushingYards,
                "Rush Attempts": Incentive.RushAttempts,
                "Scrimmage Yards": Incentive.ScrimmageYards,
                "Red Zone Rush Attempts": Incentive.RedZoneRushAttempts
            })
        return options

class ContractYear:
    def __init__(self):
        self.salary
        self.rosterBonus
        self.ltbe
        self.nltbe
        self.incentiveTBD

class Contract:
    def __init__(self):
        self.start
        self.rookie
        self.fifthYearOptionAvailable
        self.state # [ACTIVE, BID, DEADMONEY]
        self.taggedYears # TODO. NFL does 3 tags lifetime. If that's the case, this is not the right place for this, probably
        self.contractYears

    def __eq__(self, obj):
        return isinstance(obj, Contract) and \
            self.start == obj.start and \
            self.rookie == obj.rookie and \
            self.fifthYearOptionAvailable == obj.fifthYearOptionAvailable and \
            self.state == obj.state and \
            self.taggedYears == obj.taggedYears and \
            self.contractYears == obj.contractYears
    
    def __ne__(self, obj):
        return not self == obj

    def __lt__(self, obj):
        if isinstance(obj, Contract):
            if self.start != obj.start:
                return self.start < obj.start
            if self.rookie != obj.rookie:
                return self.rookie
            if self.fifthYearOptionAvailable != obj.fifthYearOptionAvailable:
                return self.fifthYearOptionAvailable
            if self.state != obj.state:
                return self.state < obj.state
            if self.taggedYears != obj.taggedYears:
                return self.taggedYears < obj.taggedYears
            if len(self.contractYears) != len(obj.contractYears):
                return len(self.contractYears) < len(obj.contractYears)
            return self.contractYears < obj.contractYears
        return False
