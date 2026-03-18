#!/c/Users/jrobe/AppData/Local/Microsoft/WindowsApps/python

from app.models.Player import Player
from app.models.Constants import Constants

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
    def convertIncentiveTBD(self, player: Player):
        for incentive in self.incentiveTBD:
            if incentive.hasVested(player):
                self.ltbe.append(incentive)
            else:
                self.nltbe.append(incentive)
        self.incentiveTBD = []

    def total(self):
        return self.salary + self.rosterBonus + self.ltbe + self.nltbe + self.incentiveTBD

    def __init__(self,
                  salary: float = 0.0,
                  rosterBonus: float = 0.0,
                  ltbe: list[Incentive] = None,
                  nltbe: list[Incentive] = None,
                  incentiveTBD: list[Incentive] = None):
        self.salary = salary
        self.rosterBonus = rosterBonus
        self.ltbe = ltbe if ltbe is not None else []
        self.nltbe = nltbe if nltbe is not None else []
        self.incentiveTBD = incentiveTBD if incentiveTBD is not None else []

    def __add__(self, oth):
        if isinstance(oth, ContractYear):
            return ContractYear(
                salary=self.salary + oth.salary,
                rosterBonus=self.rosterBonus + oth.rosterBonus,
                ltbe=self.ltbe + oth.ltbe,
                nltbe=self.nltbe + oth.nltbe,
                incentiveTBD=self.incentiveTBD + oth.incentiveTBD
            )
        return NotImplemented

class ContractType(Enum):
    ACTIVE = "Active"
    DEAD_MONEY = "Dead Money"
    FREE_AGENT_OFFER = "Free Agent Offer"
    EXTENSION_OFFER = "Extension Offer"
    RESTRUCTURE_OFFER = "Restructure Offer"

class Contract:
    def getFullBurden(self):
        burden = 0
        for year, contract in self.contractYears.items():
            burden += contract.total()
        return burden

    def getAdjustedAAV(self, player: Player):
        collapsedYear = ContractYear()
        maxYear = Constants.LEAGUE_YEAR
        for year, contract in self.contractYears.items():
            maxYear = max(maxYear, year)
            collapsedYear += contract
        collapsedYear.convertIncentiveTBD()
        fullBurden = collapsedYear.total()
        adjustedAAV = collapsedYear.salary
        if collapsedYear.rosterBonus < fullBurden * 0.25:
            adjustedAAV += collapsedYear.rosterBonus * 0.75
        else:
            adjustedAAV += fullBurden * 0.25 * 0.75
            if collapsedYear.rosterBonus < fullBurden * 0.5:
                adjustedAAV += (collapsedYear.rosterBonus - fullBurden * 0.25) * 0.5
            else:
                adjustedAAV += fullBurden * 0.25 * 0.5
        if collapsedYear.ltbe < fullBurden * 0.2:
            adjustedAAV += collapsedYear.ltbe * 0.5
        else:
            adjustedAAV += fullBurden * 0.2 * 0.5
        if collapsedYear.nltbe < fullBurden * 0.2:
            adjustedAAV += collapsedYear.nltbe * 0.25
        else:
            adjustedAAV += fullBurden * 0.2 * 0.25
        adjustedAAV /= len(self.contractYears)
        return adjustedAAV * [
            1.000, # 0 year contract
            1.000, # 1 year contract
            0.952, # 2 year contract
            0.906, # 3 year contract
            0.861, # 4 year contract
            0.818, # 5 year contract
            0.777, # 6 year contract
            0.737, # 7 year contract
            0.699, # 8 year contract
            0.662, # 9 year contract
            0.627  # 10 year contract
        ][1 + maxYear - self.start]

    def isValid(self):
        errors = []
        if self.fifthYearOptionAvailable and not self.rookie:
            errors.append("Fifth Year Option on Non Rookie Deal")
        if not len(self.contractYears):
            errors.append("No contract years")
        self.contractYears = dict(sorted(self.contractYears.items()))
        if next(iter(self.contractYears)) != self.start:
            errors.append("Start year is not the same as first contract year")
        fullBurden = self.getFullBurden()
        if fullBurden <= 0.0:
            errors.append("No money offered")
        if len(self.contractYears) > 5:
            errors.append("More than 5 contract years")
        prevYear = self.start - 1
        for year, contractYear in sorted(self.contractYears.items()):
            if year != prevYear + 1:
                errors.append("Skipped year {}".format(prevYear+1))
            prevYear = year
            if contractYear.total() < fullBurden * 0.1:
                errors.append("{} doesn't share at least 10 percent of full burden".format(year))
        if self.state == ContractType.EXTENSION_OFFER:
            errors.extend(self.isValidExtension())
        if self.state == ContractType.RESTRUCTURE_OFFER:
            errors.extend(self.isValidRestructure())
        return bool(len(errors)), errors

    def isValidExtension(self):
        return NotImplemented

    def isValidRestructure(self):
        return NotImplemented

    def __init__(self,
                  rookie : bool = False,
                  fifthYearOptionAvailable : bool = False,
                  state : ContractType = ContractType.FREE_AGENT_OFFER,
                  taggedYears : int = 0,
                  contractYears : dict = None):
        self.rookie = rookie
        self.fifthYearOptionAvailable = fifthYearOptionAvailable
        self.state = state
        self.taggedYears = taggedYears # TODO. NFL does 3 tags lifetime. If that's the case, this is not the right place for this, probably
        self.contractYears = contractYears if contractYears is not None else {}
        if len(self.contractYears):
            self.contractYears = dict(sorted(self.contractYears.items()))
            self.start = next(iter(self.contractYears))
        else:
            self.start = None

    def __add__(self, oth):
        return NotImplemented

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
