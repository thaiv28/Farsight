from pathlib import Path

import torch
from torch import nn
from torch.utils.data import DataLoader

from farsight.nn.model import NeuralNetwork
from farsight.nn.trainer import test
from farsight.nn import nn_utils

def main():
    model = NeuralNetwork()
   
    path = Path(__file__).parent.absolute()
    
    model.load_state_dict(torch.load(str(path / "../models/nn.pt"), weights_only=True))
    validate_set = nn_utils.split_dataset([("2023-06-01", "2023-12-31")])[0]
    validate_dataloader = DataLoader(validate_set, nn_utils.batch_size, shuffle=True)
    print("BEGINNING VALIDATION:")
    test(validate_dataloader, model, nn.MSELoss())
    

if __name__=="__main__":
    main()