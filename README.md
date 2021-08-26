# MLB Daily Fantasy Sports Analysis

This is a project to do data analysis on baseball and use that insight to hedge bets in daily fantsy sports
### PREREQUISITES:
    Python 3.8+
    numpy
    jupyter
    matplotlib
    scipy
    pandas
    psycopg2
    sqlalchemy
<br>

---
###  PostgreSQL info:
To connect to the postgreSQL servers the python library psycopg2 is used.

The psycopg2.connect function is used along with the parameters in the database.ini file to connect to the proper 
databases.

To change settings on what database is being used make changes in the database.ini file 
(currently is being ignored in .gitignore)

---
### TO RUN:
1. 

---

<br>

### DOWNLOADS:

### Python
#### Windows:  
1. Click [here](https://www.python.org/downloads/) and download the latest version of pythons installer
2. Once finished downloading click the exe and follow the installers instructions

#### Linux:
1. Open a terminal
2. First enter: `sudo apt-get update`
3. After: `sudo apt-get install python`

<br>


<br>

---
### DRAFT KINGS SCORING 
MLB Classic
In salary cap contests, participants will create a lineup by selecting players listed in the Player Pool. Each player listed has an assigned salary and a valid lineup must not exceed the salary cap of $50,000.

Contest results will be determined by the total points accumulated by each individual lineup entry (scoring rules summarized below).

Participation in each contest must be made only as specified in the Terms of Use. Failure to comply with these Terms of Use will result in disqualification and, if applicable, prize forfeiture.

Scoring
Hitters

Single

+3 Pts

Double

+5 Pts

Triple

+8 Pts

Home Run

+10 Pts

Run Batted In

+2 Pts

Run

+2 Pts

Base on Balls

+2 Pts

Hit By Pitch

+2 Pts

Stolen Base

+5 Pts

Pitchers

Inning Pitched

+2.25 Pts

Strikeout

+2 Pts

Win

+4 Pts

Earned Run Allowed

-2 Pts

Hit Against

-0.6 Pts

Base on Balls Against

-0.6 Pts

Hit Batsman

-0.6 Pts

Complete Game

+2.5 Pts

Complete Game Shutout

+2.5 Pts

No Hitter

+5 Pts

Scoring Notes
Hitting statistics for Pitchers will not be counted, and Pitching statistics for Hitters will not be counted.
Lineup Requirements
Lineups will consist of 10 players and must include players scheduled to play in at least 2 different MLB games. Lineups must have no more than 5 hitters from any one team. The 10 roster positions are:

2

P

1

C

1

1B

1

2B

1

3B

1

SS

3

OF

Player Pool
The Player Pool will consist of all MLB players expected to be on the active roster for any team scheduled to play in the contest Game Set. Occasionally a player may be missing from the Player Pool due to trades or other unforeseen circumstances.

In most circumstances, once the Player Pool is established for a Game Set, including positions and salaries, the Player Pool will not be adjusted. In the rare event that there is a mistake within the Player Pool that would significantly impact game quality, DraftKings reserves the right to correct the mistake after contests for that Game Set have become available. This may result in valid lineups becoming invalid. This would most likely occur shortly after the Player Pool becomes available, far in advance of the contest start time, and participants who have entered contests for the Game Set prior to the adjustment will be notified via email.

A "Game Set" is a set of games used for contests; each contest is tied to one Game Set. Contests tied to the same Game Set can be created at different times. Therefore, game policies are based on the timing of a Game Set being made available, not each individual contest.

Position Eligibility
Player positions are determined at the sole discretion of DraftKings.

Lineup Edits
Lineups may be edited at any time leading up to games. Each individual player will become "locked" at the scheduled start time of their team’s game. A locked player cannot be added or removed from a roster spot. Locked roster spots for all entries are displayed in contest GameCenters.

If the scheduled start time for a game changes after contests for a Game Set containing that game become available, DraftKings will take measures to ensure the change is reflected on Draft Screens and for lineup editing purposes. In the rare case that a game starts before the scheduled start time, all players within that game will become locked as soon as our feed reflects that the game has begun. Additionally, any swaps that were made after the real-life start time of the game will result in those lineups being disqualified and refunded.

Cancelled, Postponed, and Rescheduled Games
In the event that a game is canceled, postponed, or rescheduled to a time outside of the original Scoring Period, the game will be disabled from the Game Set and players listed to play in that game will not be eligible to accrue points.

The Scoring Period for MLB is defined as the timeframe between the scheduled start of the first game within the Game Set and 11:59pm ET on the date of the start time of the last scheduled game within the Game Set.

In the event a game is postponed, Draftkings will make a decision no later than 11:59pm ET of the day of the game on how to handle the postponed game.

DraftKings may choose to adjust the Scoring Period for a Game Set at their sole discretion to accommodate schedule changes to any time before 12:00am ET on the day after the Game Set is scheduled to start.

Any games that are disabled will be indicated as such on Draft Screens. Emails and other notifications may also be used to notify users of disabled games.

If canceled or games rescheduled for a later date result in a Game Set including only one active game, then all contests for that Game Set will be canceled and refunded.

Games are "known" to be canceled or postponed once their status is updated as such by DraftKings’ MLB stats-provider, STATS LLC.

Suspended or Shortened Games
DraftKings uses official MLB statistics and only includes statistics from games MLB deems to be official. If the MLB declares a game "suspended" then the statistics generated before the game is suspended will count in Game Sets containing said game. Any statistics generated on a later date when the game resumes will not be included.
---