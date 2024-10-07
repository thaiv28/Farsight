import datetime
import sqlite3
import pathlib

import farsight.db as db

# given a player and a date, find the average of player's stats from player_stat_db
# prior to that date
def calculate_averages(player_id: str, date=None, con=None):
    print(f"{player_id=}, {date=}")
    if date == None:
        date = datetime.date.today()
    
    if con == None: 
        con, _ = db.connect()

    cur = con.cursor()
    res = cur.execute(f"""SELECT avg(player_stat.result), avg(player_stat.length), 
                      avg(player_stat.gold_spent_percent_difference), avg(player_stat.gold_percent_rating),
                      avg(kills), avg(deaths), avg(assists), avg(dmg_to_champs), avg(dmg_per_min),
                      avg(dmg_share), avg(dmg_taken_per_min), avg(wards_per_min), avg(vision_score_per_min),
                      avg(earned_gold_per_min), avg(earned_gold_share), avg(cs_per_min),
                      avg(gold_at_10), avg(xp_at_10), avg(cs_at_10),
                      avg(opp_gold_at_10), avg(opp_xp_at_10), avg(opp_cs_at_10),
                      avg(gold_diff_at_10),
                      avg(xp_diff_at_10), avg(cs_diff_at_10), avg(kills_at_10),
                      avg(assists_at_10), avg(deaths_at_10), avg(opp_kills_at_10),
                      avg(opp_assists_at_10), avg(opp_deaths_at_10),
                      avg(gold_at_15), avg(xp_at_15), avg(cs_at_15),
                      avg(opp_gold_at_15), avg(opp_xp_at_15), avg(opp_cs_at_15),
                      avg(gold_diff_at_15),
                      avg(xp_diff_at_15), avg(cs_diff_at_15), avg(kills_at_15),
                      avg(assists_at_15), avg(deaths_at_15), avg(opp_kills_at_15),
                      avg(opp_assists_at_15), avg(opp_deaths_at_15),
                      avg(gold_at_20), avg(xp_at_20), avg(cs_at_20),
                      avg(opp_gold_at_20), avg(opp_xp_at_20), avg(opp_cs_at_20),
                      avg(gold_diff_at_20),
                      avg(xp_diff_at_20), avg(cs_diff_at_20), avg(kills_at_20),
                      avg(assists_at_20), avg(deaths_at_20), avg(opp_kills_at_20),
                      avg(opp_assists_at_20), avg(opp_deaths_at_20),
                      avg(gold_at_25), avg(xp_at_25), avg(cs_at_25),
                      avg(opp_gold_at_25), avg(opp_xp_at_25), avg(opp_cs_at_25),
                      avg(gold_diff_at_25),
                      avg(xp_diff_at_25), avg(cs_diff_at_25), avg(kills_at_25),
                      avg(assists_at_25), avg(deaths_at_25), avg(opp_kills_at_25),
                      avg(opp_assists_at_25), avg(opp_deaths_at_25)
                      
                      FROM match_stat
                      INNER JOIN player_stat on match_stat.match_key = player_stat.match_key
                      WHERE player_key = '{player_id}'
                      and date < '{date}'
                      """)
    
    return res.fetchone()
    
if __name__=="__main__":
    calculate_averages("oe:player:b728b4a88e70fe2d0f10aae80e56ee1", date="2016-01-01")