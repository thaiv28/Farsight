import torch
import pandas as pd

from farsight.data import preprocess
from farsight.db.query_helpers import SAMPLE_DATASET_ROW, SAMPLE_DATASET_LIST

def test_transform_df():
    X = pd.DataFrame(SAMPLE_DATASET_LIST)
    X = X.rename(columns={0:"match_key", 1:"position", 2:"date"})
    X = preprocess.transform_df(X)

def test_to_tensor():
    x = pd.Series(SAMPLE_DATASET_ROW)
    x = x[3:]
    
    assert(isinstance(preprocess.row_to_tensor(x), torch.Tensor))