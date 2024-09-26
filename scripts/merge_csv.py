from pathlib import Path
import os

import pandas as pd

# Merges every year of the Lol Esports match data from Oracles Elixir into a single
# csv file that contains every row, sorted by date

# Input: directory containing 2+ csv files
# Output: 1 csv file which merges the results

def main():
    DATA_PATH = "../data/"
    
    raw_dir = Path(DATA_PATH + "raw/")
  
    df_list = [] 
    for file in os.listdir(raw_dir):
        if not file.endswith(".csv") or "complete" in file:
            continue
      
        df_list.append(pd.read_csv(raw_dir / file))
   
    df = pd.concat(df_list, ignore_index=True) 
    
    df = df.sort_values("date")
    df.to_csv(raw_dir / "complete_raw_data.csv") 
      
   
if __name__ == "__main__":
    main()