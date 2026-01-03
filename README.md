# Salary Cap League
This document currently serves more as a draft of a CBA/League Agreement combined with some scratch notes for how the project should function. It will likely evolve over time.

## Contracts
Contracts are defined by multiple years and types of burden. Each year should define the amount of money owed to the player which fits each of the following categories:
 - Salary: Money which is guaranteed to the player at time of signing, to be paid in the specified year.
 - Roster Bonus: Money which converts into salary at the start of the League New Year but is forgiven if the player isn't rostered at that time.
 - Incentives: Money which is tied to certain achievable metrics (yards, touchdowns, games, fantasy points). Incentives must be readily perceptable in the Game Log section of a player profile in Sleeper, or must be tied to team success (playoff berth). For example, YPT between weeks 15 and 17 can be an incentive, but not completion percentage. Team owners are responsible for determining which incentives are LTBE vs NLTBE, and for determining whether or not they were earned at the end of the season.
   - Likely To Be Earned (LTBE): An incentive which the player would have met in their previous season. This money counts against the cap, but is given back as credit the following year if not earned.
   - Not Likely To Be Earned (NLTBE): An incentive which the player would not have met in their previous season. This money does not count against the cap, but will count towards next year's cap if earned. A contract may not include NLTBE incentives that exceed 125% of what the player has achieved in the past. For example, a player with a 1000 yard rushing season cannot accept a contract with an incentive for a 1500 yard rushing season. Additionally, NLTBE incentives can make up no more than 25% of a contracts total value.

#### Player Incentives Report
At the end of each season, team owners are responsible to provide the commissioner with a Player Incentives Report. This should include the following:
1. Every player with an LTBE or NLTBE incentive in the current year, the type and value of the incentive, and whether or not it was earned.
2. Every player with an LTBE or NLTBE incentive in the next year, the value of the incentive, and whether or not it would have been earned this year (to determine incentive type for next season's cap table).

This is not meant to discourage the use of incentives, but simply to lower the burden of the Commissioner. If it does decrease your interest in using incentives in contracts, communicate that with the Commissioner and they'll try to accomodate.

#### Average Annual Value
Average Annual Value (AAV) is the total compensation of a player's contract including all guaranteed and non-guaranteed money divided by the contract length.

#### Adjusted Average Annual Value
Several times in the contract section, Adjusted Average Annual Value (AAV) is referenced. Essentially, Adjusted AAV is a tax on longer period contracts and low guarantees; players assume they'll improve and demand to be paid more in later years, and they value non-guaranteed money differently than guaranteed money. To calculate Adjusted AAV, follow these steps:
1. Add 100% of the Salary.
4. Add 75% of the Roster Bonus.
5. Add 50% of LTBE incentives.
6. Add 25% of NLTBE incentives.
7. Divide this total by the number of contract years.
8. Multiply this result by the Adjustment Multiplier in the following chart (based on 10% backloaded contracts):
| Number of Years | Adjustment Multiplier |
|:-|:-|
| 1 | 1.000 |
| 2 | 0.952 |
| 3 | 0.906 |
| 4 | 0.861 |
| 5 | 0.818 |
| 6 | 0.777 |
| 7 | 0.737 |
| 8 | 0.699 |
| 9 | 0.662 |
| 10 | 0.627 |

Roster Bonus may not be included in the first year of a contract offer.

For example, a 4 year contract with a total of $25 million in salary, $10 million in Roster Bonus, and $10 million in NLTBE incentives would have an Adjusted AAV of $7.533 million, despite having a potential $11.25 annual cap burden.

A tool will be provided to all league members to assist in calculating Adjusted AAV. When submitting a Free Agency bid in Sleeper, bid an amount equal to the Adjusted AAV in thousands of dollars. For the above example, you'd bid 7533 FAAB.

#### Contract Distribution
No single year on a contract can have less than 10% of the full burden of that contract.

No single year on a contract can have guaranteed money equal to less than 10% of the full guaranteed burden of that contract.

#### Other Contract Terminology
***Full Burden.*** The total amount of money on a contract, including guaranteed and non-guaranteed from all years at full value.

***Remaining Burden.*** The full burden of a contract, but only counting remaining contract years (including current).

***Future Burden.*** The full burden of a contract, but only counting future contract years (not including current).

***League New Year.*** When contract burdens are counted towards salary cap, among other things mentioned throughout.

***Current Year.*** If between the Championship Game Conclusion and League New Year, this refers to the upcoming season. Otherwise, it refers to the active season.

### Extension
Players can be extended by their current team, provided they meet each of the following requirements.
 - Current contract has not expired.
 - No more than 2 years remain on their contract (including current year).
 - The player participated (IRL) in at least 5 games in their previous or current season.
 - The extended contract will last no more than 5 seasons (including current year), or 4 seasons if signed before League New Year.
 - If they are a rookie, the player has already finished their 3rd season.

A player will sign an extension offer if the extension years (which do not include current contract terms) have an Adjusted AAV greater than or equal to the Nth best contract AAV at their position, where N is equal to half the player's positional finish in fantasy points per game rounded down in the greater of (a) the prior season or (b) the current season, assuming 5 or more games have been played. If N is <= 2 (player's positional finish in fantasy points per game was 5th or better), their expectation is instead an Adjusted AAV of at least 110% of the most valuable contract's actual AAV at their position.

For example, a player who ranked 10th in fantasy points per game at their position expects their contract's Adjusted AAV to be comparable to the actual contract AAV of the 5th highest paid player at their position, whereas a player who ranked 5th in fantasy points per game at their position expects to break the market with an Adjusted AAV of at least 110% the highest actual contract AAV at their position.

When determining which Adjustement Multipler to use when calculating Adjusted AAV for a contract extension, count next season as the contract's first year. For example, a contract with 2 years left which seeks to add 3 years during the offseason would use a contract length of 5 in the Adjustment Multiplier chart.

As part of an extension, teams may renegotiate the remainder of the current contract (excluding the current year, if League New Year has passed). To do this, see the section on restructuring contracts.

### Restructure Contracts
Teams are able to restructure contracts, provided they meet the each of the following requirements.
 - The contract is for a player that is no longer rostered (Dead Cap), or no years are added to their contract during this restructure.
 - Only guaranteed money is restructured, though non-guaranteed money can be converted into guaranteed money prior to restructuring.
 - Only future years are restructured.
 - No more than 2 years remain on their contract (including current year).
 - If they are a rookie, the player has already finished their 3rd season.
 - No more than 5 years remaining burden on the restructured contract (including current year).
 - The total value of the contracts' remaining years must increase by at least 10% and an additional 10% (compounding) per added year.
   - x1.1 for same or fewer years
   - x1.21 for one additional year
   - x1.331 for two additional years
   - x1.4641 for three additional years
   - x1.61051 for four additional years
 - Each contract year pays no less than 50% of what was previously agreed, and no less than 10% of the total remaining burden.
 - The contract adheres to other salary requirements (e.g. Contract Minimums)

For example, a player with $25 million in future burden over the next 3 seasons would agree to restructure his contract into a 5 year deal if the total amount paid is $33.275 million or more. If it was originally a flat contract ($8.333 million / year), the first 3 years could each have a minimum of $4.167 million in cap hit, with the remaining $20.775 million divided among the remaining two years.

You may restructure a contract as a part of a contract extension. To do this, first follow the restructure rules normally. Separately, follow extension offer rules normally to determine extended contract years' compensation, ensuring the number of extended years matches the number of years added in the restructure. Lastly, sum the values for the restructured contract and the extended contract years. Note that any money distributed to later years as part of the restructure does not contribute whatsoever to the Adjusted AAV when calculating a valid contract extension offer.

### Restricted Free Agents
A player who has exactly 3 Accrued Seasons is eligible for Restricted Free Agency. An Accrued Season means they spent any time on an Active Roster (not a Practice Squad or Free Agency) during the league year. RFAs are free to negotiate and sign with any team if they are not issued a Tender Offer by their original team (see Offseason Schedule for deadline to issue an RFA Tender Offer). The following options are available for Tender Offers to teams with RFA eligible players...
 - **First-Round Tender:** A one year contract worth the greater of (a) 8 percent of the Salary Cap or (b) 110 percent of the player's prior-year base salary. If the player signs to another roster, the player's original team is entitled to a first-round draft pick from his new team, valued no less than the team's own first-round pick. If any player drafted outside the first round receives a First-Round Tender, no other players on that roster are eligible to receive this tender.
 - **Second-Round Tender:** A one year contract worth the greater of (a) 5 percent of the Salary Cap or (b) 110 percent of the player's prior-year base salary. If the player signs to another roster, the player's original team is entitled to a second-round draft pick from his new team, valued no less than the team's own second-round pick.
 - **Original-Round Tender:** A one year contract worth the greater of (a) 3 percent of the Salary Cap or (b) 110 percent of the player's prior-year base salary. If the player signs to another roster, the player's original team is entitled to a draft pick in the round the player was originally drafted in from his new team, valued no less than the team's own pick from that round.
 - **Right-Of-First-Refusal Tender:** A one year contract worth the greater of (a) 2 percent of the Salary Cap or (b) 110 percent of the player's prior-year base salary. There is no draft compensation given to the player's original team if they sign with a new team.

Regardless of tender type (assuming a Tender Offer was extended), the issuing team is given Right Of First Refusal for any offer the restricted free agent accepts. This means the original team has the option to either match the contract or receive the appropriate draft compensation from the signing team.

If a team extends an RFA Tender Offer and the player doesn't receive any contract offer by the end of free agency, the RFA Tender Offer becomes an actual contract.

##### Strategy
Draft selections receive 4 year contracts. This means to be RFA eligible, they must be on the Taxi Squad for a full season. In the case of first round picks, they need to either be on the Taxi Squad for an additional year, or their 5th year option must be declined.

### Franchise Tag
Each franchise may designate a tag to only one of their players each offseason whose contract has just expired. There are three types of franchise tag:

***Exclusive Tag.*** This tag acts as a forced one year contract upon the player with no opportunity for other teams to submit a contract offer. This contract has a salary at the greater of (a) 120% of the player's previous year's compensation or (b) the average of the top 5 contract AAVs from last season at the player's own position.

***Non-Exclusive Tag.*** This tag acts as a one year contract offer which is made final if the player does not accept any other offer, with a salary at the greater of (a) 120% their previous year's compensation or (b) the average of the top 5 contract AAVs from last season at the player's own position. Other teams may submit Free Agency offers to the tagged player, but the original team has right of first refusal to match any accepted offer. Submitted offers must have a higher Adjusted AAV than the non-exclusive tag's tendered amount. If the original team does not match the offer, the team who signs the tagged player must relinquish their two most recent first round draft selections no further than two drafts in advance. For example, a team signing a non-exclusive tagged free agent in March 2025 must give two 2025 first round picks if available, one 2025 first and one 2026 first if the prior option is impossible, or two 2026 firsts if neither of the prior two options are possible.

***Transition Tag.*** This tag acts as a one year contract offer which is made final if the player does not accept any other offer, with a salary at the greater of (a) 120% of their previous year's compensation or (b) the average of the top 10 contract AAVs from last season at the player's own position. Other teams may submit Free Agency offers to the tagged player, but the original team has the right of first refusal to match any accepted offer. Submitted offers must have a higher adjusted AAV than the transition tag's tendered amount.

Players can be tagged in consecutive years, but the Transition Tag can be used only during the first year.

If tagging a player for a 3rd consecutive year, the compensation is instead the greater of (a) 144% of the player's previous year's compensation or (b) an average of the top 5 contract AAVs from last season, regardless of position.

A player cannot be tagged more than 3 years in a row.

***Previous Year's Compensation*** includes the player's salary, roster bonus, and all incentives which were earned (LTBE and NLTBE).

### Taxi Squad
Any player may begin the season on the Taxi Squad, but no players may be added to the Taxi Squad after the start of the first game of the regular season. While on the taxi squad, players cannot start in games, nor be added to IR. Any player which remains on the practice squad through the end of the year will not be considered to have accrued a season for the purposes of Restricted Free Agency eligibility.

The Taxi Squad has a total of 6 slots available. 4 of these slots are reserved for players with no more than two accrued seasons.

Teams can submit a Raid Request for a player on another team's Taxi Squad. To do this, the team will submit a public Contract Offer to that player with the same Contract Length and an AAV at least 25% greater than the player's current contract. The team whose Taxi Squad currently hosts the player has 24 hours after seeing this Raid Request to either promote the player to their active roster or relinquish control of the player to the raiding team's active roster at the agreed upon contract value. No dead money is created as a part of a raid.

The Taxi Squad is similar to NFL Practice Squads only in ways specified in this section. For example, the Taxi Squad does not affect players' salary, and they are given contracts under the same rules and restrictions as anyone on the active roster.

### Contract Minimums
| Player Experience | Minimum Salary |
|:-|:-|
| 0-3 | 0.4% of cap |
| 4-6 | 0.5% of cap |
| 7+  | 0.6% of cap |

If a player's existing contract does not meet these minimums in any given year, their salary is incresed for that year to match the league minimum value. Roster bonuses and incentives do not count towards league minmum compliance.

### Compensatory Draft Selections
Certain players are considered Compensatory Eligible when they sign with a new team in free agency. The following chart shows eligibility.
| Compensatory Round | Qualifications |
|:-|:-|
| 2 | Contract AAV >= 18% of Salary Cap AND EITHER Top 3 Positional Finish in Prior Season OR Top 3 Positional AAV in New Contract |
| 3 | Contract AAV >= 16% of Salary Cap AND EITHER Top 6 Positional Finish in Prior Season OR Top 6 Positional AAV in New Contract |
| 4 | Contract AAV >= 14% of Salary Cap AND EITHER Top 9 Positional Finish in Prior Season OR Top 9 Positional AAV in New Contract |
| 5 | Contract AAV >= 12% of Salary Cap AND EITHER Top 12 Positional Finish in Prior Season OR Top 12 Positional AAV in New Contract |

At the end of the Free Agency Compensatory Eligibility period, teams will total the number of Compensatory Eligible players who departed their team and the ones who joined it. Starting with their most valuable departures, cancel out the most equivalent addition as possible with up to 1 round of leeway as required (canceling the most valuable addition in case of a tie). For example, a team with departures which are eligible of one 2nd round selection and a 4th round selection but an addition of a 3rd round eligible player would have their 2nd round departure and 3rd round addition cancel, leaving only a 4th round departure.

All remaining departures after cancellation will be converted into Compensatory Draft Selections. If multiple teams have Compensatory Draft Selections in the same round, the order shall be determined by reverse order of departing player's new Contract AAV.

### Rookie Contracts
First round draft selections will be given 4 year deals with a 5th year team option, to be excersized or waived following their 3rd season. Every dollar of the contract must be guaranteed.

Later draft selections will be given a 4 year deal. Every dollar of the contract must be guaranteed.

The AAV for the contract of a drafted rookie will be the greater of (a) the Contract Minimum for a player with 0 years experience or (b) a percentage of the Salary Cap represented by the equation 0.4 + 4.6*e^((x-1)/-10) where x is the player's overall draft selection. Their contract will be backloaded by 20% annually.

Sample values from the prior equation:
| Draft Selection | Contract AAV As a Percentage of League Salary Cap |
|:-|:-|
| 1.01 | 5%    |
| 1.02 | 4.56% |
| 1.03 | 4.16% |
| 1.06 | 3.19% |
| 2.01 | 1.78% |
| 3.01 | 0.82% |
| 4.01 | 0.53% |
| 5.01 | 0.44% |
| 5.12 | 0.41% |

Actual contract AAV per rookie selection will be published annually.

First round selections will have 5th year team options. This option must be executed in the offseason before the rookie's final contract year prior to the 5th Year Option Deadline. If executed, the 5th year salary will pay based on the rookie's performance in their first three seasons as follows.
| Performance Criteria | 5th Year Salary |
| Multiple Top 5 Positional PPG Finishes | Exclusive Tag Value |
| At Least One Top 5 Positional PPG Finish | Transition Tag Value |
| Otherwise | The Nth Highest Positional AAV, Where N = The Player's Best PPG Finish In First 3 Seasons |

### Salary Cap
The salary cap will follow 67% of the actual NFL salary cap in an attempt to make player salaries roughly align with their real life counterparts. 

If the NFL removes their salary cap (see 2010), the new year's salary cap for this league will increase by 7.5%.

Teams may not have more cap burden than the salary cap at any point in a given season. The burden includes all guaranteed money and LTBE incentives for all active contracts, as well as all dead cap (guaranteed money from players no longer rostered).

##### Strategy
The NFL salary cap has averaged an increase of 7.5% per year over the last 30 years, but there is no guarantee of this. In some seasons, it has been as high as 25% and as low as -7%. Teams will deal with the actual challenges of a flucutating cap, and should they find themselves over the cap as a result of poor planning, they'll be forced to renegotiate contracts at their own expense.

### Cap Credits and Penalties
If a team's largest cap burden during a season is less than the league salary cap, they receive a cap credit equal to the difference in the following season.

If an LTBE incentive from the previous season was not achieved, the team receives a cap credit equal to the value of the incentive.

If an NLTBE incentive from the previous season was achieved, the team receives a cap penalty equal to the value of the incentive.

### Cap Minimum
If a team's salary cap burden at the start of League New Year is below 85% of the league salary cap, all current year contracts' salaries will be increased by an equal amount until the team meets this threshold.

### Projected Spending
A team cannot commit more than 120% of the current salary cap in any future year, including guaranteed contract money and dead cap hit.

### Player Retirement
In the case of player retirement, or otherwise unexpected departure from the NFL, all contract dollars immediately become guaranteed; this includes non-guaranteed dollars that are part of a dead cap contract. This is meant to disincentivise subverting the cap by backloading contracts with non-guaranteed dollars to win a free agent right before their final season.

Non-guaranteed dollars of dead cap contracts do not count towards a team's salary cap burden if the player is still an active participant in the NFL.

### Cap Subversion
While some of the rules attempt to provide strict boundaries for cap subversion, there are almost certainly some gaps which aren't accounted for. Any attempt to subvert the cap in a way that is technically legal but reasonably shouldn't be may be punishable by reversing a contract signing, decreasing a team's cap space, confiscating draft capital, and/or league expulsion at the commissioner's sole discression.

## Offseason Schedule
Below is a sample Offseason Schedule for a typical league year. The first year will be structured much differently.
| Date / Timeframe | Item |
|:-|:-|
| Championship Game Conclusion | Waiver Wire Deadline |
|                              | Contract Extensions Deadline |
|                              | League Year Ends |
| January 7 | Offseaon Survey Released |
|           | Deadline to Opt Out of League Participation (Buy-In Must Be Paid if Opting Out After This Date) |
| January 21 | Survey Responses Due |
|            | Player Incentives Report Due | 
| January 31 | Survey Results Published and Enacted |
| February 1 | Contract Extension Reopens |
|            | Franchise Tag Period Begins |
|            | Player Incentives Report Validated and Contracts Updated |
| March 1 | Deadline to Franchise Tag Players |
|         | Deadline to Tender Offers to RFAs |
|         | Salary Cap Announced |
|         | Rookie Pay Scales Announced |
| March 9 | Free Agency and Trading Begins |
|         | First Free Agency Nominations Due |
| April 13 | Deadline to nominate RFAs for Free Agency Bidding |
| 5 Days After RFA Signs Offer | Club must decide whether to exercise right of first refusal |
| April 20 | Free Agency Ends |
|          | End of Free Agency Compensatory Eligibility Period |
| April 28 | Waiver Wire Runs Begin |
| April 23 | Draft Compensation Published |
| April 30 | Deadline To Excercise 5th Year Options For First Round Rookies Entering 4th Season |
| May 1 | Rookie Draft |
|       | 5th Year Option Deadline |
| May 14 | This Year's Schedule Announced |
|        | Next Year's Offseason Schedule Released |
| July 1 | League New Year |
| Week 1 | Taxi Squad Designation Deadline |
|        | Raid Requests Allowed |
| Week 12 Conclusion | Trade Deadline |
|                    | Deadline to Extend Expiring Contracts |

### Free Agency vs Waiver Wire
Free Agency lasts only a few weeks during the offseason. Each owner in the league may nominate 1 player each week to be bid upon. This nomination must be made by each Monday Morning at 12am, and the 12 nominated players will accept an offer the following Monday Morning at 12am. Between mondays, owners may submit contract offers in Sleeper for the 12 free nominated players based on Adjusted AAV in thousands of dollars. Contract offers are limited to be no more than 4 years in length. In the following week for any winning bids, owners must submit a valid contract to the commissioner for their won bids which is worth at least the Adjusted AAV bid.

After the conclusion of Free Agency, the Waiver Wire will open and run throughout the season. Each Tuesday Morning at 12am, all bids for any player will be accepted as a legitimate contract offer. Unlike Free Agency, contracts offered during Waiver Wire are limited to be no more than 2 years in length. In the following week for any winning bids, owners must submit a valid contract to the commissioner for their won bids which is worth at least the adjust AAV bid.

For both Free Agency and Waiver Wire, if an honest mistake was made with the bid, the owner must make it known immediately so the 2nd highest bidder may submit their contract. If a week passes with no correction and no contract submission to the commissioner, it will be assumed that the full bid is meant as a 1 year, salary only contract; the owner cannot contest this.

## Commisioner Clause
The commisioner reserves the absolute authority to 

## Startup Draft Options
1. Auction draft
2. Snake draft of actual NFL assets (current contract values and 2025 draft selections).

Draft rookie draft selections for the current year and existing contracts, scaled so the greatest AAV for any position = 20% of the salary cap. Undrafted contracts become UFA for the following Free Agency period. Expired contracts can also be drafted and are tagged UFA or RFA appropriately. Drafted UFAs can be (a) franchise tagged or (b) dropped by the franchise tag deadline. Drafted RFAs can be (a) franchise tagged, (b) issued an RFA tender by the tender deadline, or (c) dropped by the RFA tender deadline.

For simplicity, existing contracts consider average salary over the full term of the contract, not going forward. This has some side effects, notably (a) soon to expire contracts are often cheaper, and (b) long contracts are often cheaper like Mahomes'. Specific terms of the contract will be 100% allocation to salary bucket with a 5% backload starting in the original contract year. For example, Mahomes' contract of $450 million over 10 years would have an initial year cost of $35.7 million and a final year cost of $55.5 million (not adusted for top AAV being 20% of cap).

At any point in the startup draft, a team can pass on making a selection. After doing so, they do not participate in the rest of the draft. It is recommended not to pass prior to all rookie draft selections have been claimed.



18 roster spots
3 QBs - $93 million
7 WRs - 
5 RBs - 
3 TEs - 

## Notable Differences From NFL
Some differences between this league and the NFL should be plainly obvious. For example, players cannot negotiate pretend contracts with fantasy football owners, and therefore we have a system to automatically negotiate contract extensions on their behalf (Adjusted AAV and Contract Extension Requirements). Other differences are less obvious, and this section seeks to justify some of the decisions made.

### Signing Bonus, Option Bonus, and Void Years
These contract vehicles in the NFL are mutually beneficial to both the team and the player. The player receives large sums of guaranteed cash up front while the team is allowed to spread the cap burden over many seasons. The reason these exist in the NFL CBA is because of that mutual benefit, and players simply wouldn't see the same benefit in our league. If the league buy-in was dependent on players' contracts, this mutual benefit could arguably exist, however, that is not how we intend to operate league buy-in. Therefore, these contract vehicles are not availble in our league.

As an alternative, we have well defined mechanisms to renegotiate contracts and spread cap burden into future years in a way that players would benefit from. To spread cap burden, the team will ultimately pay a higher total amount to the player but is able to reduce current burdens by up to 50%.

### UFA Tender
While it is a rarely used option in the NFL, the UFA tender is still a valuable tool for teams to ensure draft compensation for departing free agents. However, this primarily exists in the NFL because the actual compensatory draft pick rules are heavily obfuscated by the CBA and teams need a way to protect themselves against this uncertainty. Our league has no such obfuscation; the rules for compensatory draft pick eligibility are written in plain english and should be easy for teams to understand. The introduction of the UFA tender would therefore only complicate the Free Agent period without great benefit.

# App Development Strategy
Team owners use Sleeper to set lineups. Everything else is done on my website.

I'll have my own backend which tracks what moves have been made and where the two are out of sync, then I'll manually adjust Sleeper to comply. This adjustment will be made each Tuesday or Wednesday (may benefit from a co-commissioner).

How does FA bidding work? Will players say how interested they are in an offer? Will bidding be fully public, fully private, or some flavor of hot/cold?

## Pages

League Home Page (readonly)
 - Week's Matchups 
 - Standings / Bracket
 - Recent Activity

Team Page (read - write)
 - Roster
   - Cut
 - Active / Dead Contracts
   - Extend
   - Restructure
   - Tag (offseason)
   - RFA Tender (offseason)
   - Pick Up Option (offseason)
 - Draft Capital
 - Trade Requests in/out
   - Submit Offer
   - Accept/Reject/Counter/Withdraw/Modify Offer

Waiver Wire / Free Agency (read - write)
 - Available
   - Nominate For Bid (Free Agency)
   - Submit Offer (Waiver Wire, or Already Nominated)
 - Active Bids
   - Modify Offer

CBA (readonly)

## Scribble Sheet
Several options that could make it make sense.
 - By League
   - Pros: More realistic, easier to implement
   - Cons: More volatile
   - Consider average annual salaries for each position.
   - Consider salary curve by age in the league
     - Factor in number of players at each age currently in the league
     - Use a best fit curve
       - Age
       - Fantasy Points
       - Salary
       - By Position
 - Average of all leagues
   - Pros: Less volatile, mid difficulty to impl
   - Cons: Less realistic
 - Based on NFL
   - Pros: Mid volatility
   - Cons: Very difficult to impl, less realistic
 - Configurable
   - Peak Age
   - Std Dev
   - Minimum Worth
 - Not curve... linear
   - Every additional year requires X% more money than the previous. NFL increases cap by 7.5% annually (avg)
   - What about prove-its?
   - Extensions?
     - Right... this was the point wasn't it? Argh.....
     - Like a franchise tag... Look at past performance and other contracts at the position; upgrade their expectations by a certain %
     - Rank N, seeking $ == N/2 plus annual increases including in year 1.
       - If player ranked 10th at position, they expect to be paid as if the 5th best.
       - If 5th biggest contract is currently $10M, a 1 year contract would need to be $10M * 1.08 == $10.8M. 2 year contract would be $10M * 1.08 + $10M * 1.08^2 == $22.464M aav
       - But... How to handle injured years?
         - Use averages, not totals when ranking.
         - If fewer than M games played in contract year, they'll refuse to resign.
       - How to handle top players?
         - Players in top 5 at a position set the market...
         - They break the market. Expectation is best contract by at least 10%
       - Legal tampering as well?
  - Retirements?
    - Do teams still pay the full contract?
      - If not, it'd be hard to prevent cap cheating. Example, very low early burden on a 4 year deal for a guy who's announced retirement after next season.
        - Partially helped by preventing future years from exceeding cap + 10%/yr. 
 - Immersion
   - AI driven twitter bots?
     - Trade announcements
     - Etc
   - Power Rankings
   - News