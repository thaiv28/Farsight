import pandas as pd
import numpy as np
import torch
from sklearn.preprocessing import OneHotEncoder

def transform_df(df: pd.DataFrame):
    position_series = df["position"]
    df = df.drop(columns=["dataset_id", "match_key", "position", "date"])

    # TODO: Fix dataset to get gspd and gpr from match_stat
    df = df.drop(columns=["player_avg_gold_spent_percent_difference",
                         "player_avg_gold_percent_rating",
                         "opp_avg_gold_spent_percent_difference",
                         "opp_avg_gold_percent_rating"])

    positions = ["top", "jng", "mid", "bot", "sup"]
    enc = OneHotEncoder(categories=[positions], sparse_output=False,
                        dtype=np.int8)
    position_df = position_series.to_frame()
   
    encoded_positions = enc.fit_transform(position_df)
   
    for i, position in enumerate(positions):
        df.insert(i + 1, position, encoded_positions[:,i])
        
    # impute missing values
    for col in df:
        df[col] = df[col].fillna(df[col].mean()).infer_objects(copy=False)
    
    return df
    
def row_to_tensor(row: pd.Series):
    row = row.astype("float32")
    tensor = torch.tensor(row.values)
    return tensor
    
    