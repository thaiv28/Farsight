import sqlite3

import pandas as pd
from torch.utils.data import Dataset, DataLoader

from farsight.db import connection
from farsight.data import preprocess

class CustomDataset(Dataset): 
    def __init__(self, start_date: str, end_date: str):
        print(f"{start_date=} {end_date=}")
        con, _ = connection.connect()
        self.df = pd.read_sql_query(f"""
                                    SELECT * FROM dataset
                                    WHERE date >= '{start_date}'
                                    AND date <= '{end_date}';
                                    """, 
                                    con)
        con.close()
        
        assert(len(self.df) != 0)
        
        self.df = preprocess.transform_df(self.df)
        
        
    def __len__(self):
        return len(self.df) 
    
    def __getitem__(self, idx):
        row = self.df.iloc[idx]
       
        tensor = preprocess.row_to_tensor(row)
        x = tensor.data[1:]
        label = tensor.data[0]
                
        return x, label
        
        