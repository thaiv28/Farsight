import farsight.db as db
import farsight.data as data
import farsight.sql_helpers as sql_helpers

def main():
    # for every match in match_stats
    #   for every player in player_stats for that match:
    #      calculate averages for that player
    #   create dataset
    
    con, cur = db.connect()
    for year in range(2014, 2024):
        check_year = cur.execute(f"""
                                 SELECT date
                                 FROM dataset
                                 WHERE strftime('%Y', date) = '{year}'
                                 """)
        if check_year.fetchone() is not None:
            print(f"Skipping {year} because already in dataset")
            continue

        match_info = cur.execute(f"""
                        SELECT match_stat.match_key, player_stat.player_key, date,
                        position, player_stat.kills
                        FROM match_stat
                        INNER JOIN player_stat 
                            ON match_stat.match_key = player_stat.match_key
                        WHERE strftime('%Y', date) = '{year}'
                        ORDER BY date ASC;
                        """)
    
        
        for match_key, player_key, date, position, kills in match_info.fetchall():
            if match_key.endswith("_Red"):
                opponent_match_key = match_key[:-4] + "_Blue"
            elif match_key.endswith("_Blue"):
                opponent_match_key = match_key[:-5] + "_Red"
            else:
                raise Exception("Match key doesn't end with Blue or Red: %s", match_key)
            
            opponent_info = cur.execute(f"""
                            SELECT player_key
                            FROM player_stat
                            WHERE position = '{position}'
                                and match_key = '{opponent_match_key}';
                            """) 
            opponent_key = opponent_info.fetchone()[0]
            
            player_stats = data.calculate_averages(player_key, date=date, con=con)
            opponent_stats = data.calculate_averages(opponent_key, date=date, con=con)
        
            data_point = (match_key, position, date, kills) + player_stats + opponent_stats
            
            print(f"Adding data point for {match_key} {position} on {date}")
            cur.execute(sql_helpers.INSERT_DATASET_SQL, data_point)
        
        con.commit()
                


if __name__=="__main__":
    main()