# Farsight (Work in Progress)
A neural network that can predict player props for League of Legends esports matches.

<p align="center">

  <img src="/docs/images/farsight_alteration.webp" alt="Farsight Alteration" width="300"/>
</p>

## Building the Dataset

### Raw Data
The raw data is all provided by [Oracles Elixir](https://oracleselixir.com). 
They provide data for all competitive League of Legends matches from 2014 - 2024. 
The stats are tracked per player and per team, but for our purposes we care about player stats. 

This includes basic stats such as Kills, Deaths, and Assists and more advanced stats such as Exp@15 (Experience at 15 minutes) and GoldDiff@15 (Gold difference at 15 minutes). 

In total, this raw data consists of nearly 100,000 matches. Each match contains
a row for each of the 10 players and two teams, meaning the dataset is 900,000 rows large. This data is stored in an AWS-hosted PostegreSQL database.

### Our Dataset

During inference, we aim to predict the amount of kills that a player will obtain
during an upcoming match. Intuitively, the most relevant features for this task are
the stats of the given player, their teammates, and their opponents. 

Therefore, each row in our dataset will represent a specific player in a specific
match. The features will be various statistics for themselves, their teammates, 
and their opponents.

For example, we can imagine that we only used 3 career averages as the relevant statistics: kills, deaths, and assists for every player. Since there are 10 total
players in the game, our dataset will have 3 * 10 = 30 features.

This presents a data leakage problem. If we use career averages as features, the
games that we are trying to predict will be present in those players' career
averages. Additionally, future games (past the one we are trying to predict) will
be present in the data. This is problematic because we don't have access to that
same data during inference on present-day games.

Our solution is create a dataset where the features are the career averages of the
players *up to that match*. Each row represents a specific player for a specific
match. The features are every player's career averages prior to that match taking
place.

The scripts that we use to transform from raw data to our dataset and described in
the [scripts directory README](scripts/README.md).