from pathlib import Path
import os

import pandas as pd

# Preprocesses the raw data by splitting it into the different CSVs that can be
# inserted into the PostgreSQL database tables

RAW_DIR = "../data/raw/"
PREPROCESS_DIR = "../data/preprocessed/"

def create_players_db(df: pd.DataFrame):
    players_df = df.drop_duplicates(subset="playerid")
    players_df = players_df["playerid"]
    
    players_df.to_csv(PREPROCESS_DIR + "player_db.csv", index=False)

def create_matches_db(df: pd.DataFrame):
    # create dataframe of all rows with match info
    match_df = df[df.position == "team"]
    match_df = match_df[["gameid", "url", "league", "playoffs", "date", "game",
                        "patch", "side", "teamname", "gamelength", "result", "inhibitors",
                        "opp_inhibitors", "gspd", "gpr"]]
   
   # move columns around to match sql table ordering 
    match_keys = match_df["gameid"] + "_" + match_df["side"]
    game_lengths = match_df["gamelength"]
    
    match_df = match_df.drop(columns=["gameid", "gamelength"])
    match_df.insert(0, "match_key", match_keys)
    match_df = match_df.join(game_lengths)
    
    match_df.to_csv(PREPROCESS_DIR + "match_stat_db.csv", index=False)        

def create_player_stats_db(df: pd.DataFrame):
    stats_df = df[df.position != "team"]
    stats_df = stats_df[["gameid", "participantid", "side", "playerid",
                                    "position", "kills", "deaths", "assists", "teamkills",
                                    "teamdeaths", "doublekills", "triplekills",
                                    "quadrakills", "pentakills", "firstblood", "firstbloodkill",
                                    "firstbloodassist", "damagetochampions",
                                    "dpm", "damageshare", "damagetakenperminute",
                                    "damagemitigatedperminute", "wardsplaced", "wpm",
                                    "controlwardsbought", "visionscore", "vspm", "totalgold",
                                    "earnedgold", "earned gpm", "earnedgoldshare",
                                    "goldspent", "total cs", "cspm",
                                    "goldat10", "xpat10", "csat10", "opp_goldat10", "opp_xpat10",
                                    "opp_csat10", "golddiffat10", "xpdiffat10",
                                    "csdiffat10", "killsat10", "assistsat10", "deathsat10",
                                    "opp_killsat10", "opp_assistsat10", "opp_assistsat10",
                                    "goldat15", "xpat15", "csat15", "opp_goldat15", "opp_xpat15",
                                    "opp_csat15", "golddiffat15", "xpdiffat15",
                                    "csdiffat15", "killsat15", "assistsat15", "deathsat15",
                                    "opp_killsat15", "opp_assistsat15", "opp_assistsat15",
                                    "goldat20", "xpat20", "csat20", "opp_goldat20", "opp_xpat20",
                                    "opp_csat20", "golddiffat20", "xpdiffat20",
                                    "csdiffat20", "killsat20", "assistsat20", "deathsat20",
                                    "opp_killsat20", "opp_assistsat20", "opp_assistsat20",
                                    "goldat25", "xpat25", "csat25", "opp_goldat25", "opp_xpat25",
                                    "opp_csat25", "golddiffat25", "xpdiffat25",
                                    "csdiffat25", "killsat25", "assistsat25", "deathsat25",
                                    "opp_killsat25", "opp_assistsat25", "opp_assistsat25"]]

    player_stats_keys = stats_df["gameid"] + "_" + stats_df["participantid"].astype(str)
    stats_df.insert(0,"player_stat_key", player_stats_keys)
    
    match_keys = stats_df["gameid"] + "_" + stats_df["side"]
    stats_df.insert(1, "match_key", match_keys)
    
    stats_df = stats_df.drop(columns=["gameid", "participantid"])
  
    print(stats_df.head())
    stats_df.to_csv(PREPROCESS_DIR + "player_stat_db.csv", index=False) 
    

def main():
    df = pd.read_csv(RAW_DIR + "complete_raw_data.csv")
    
    create_players_db(df)
    create_matches_db(df)
    create_player_stats_db(df)
    
    
if __name__=="__main__":
    main()