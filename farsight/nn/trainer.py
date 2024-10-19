from pathlib import Path
import os

import torch
from torch import nn
from torch.utils.data import DataLoader
from sklearn.metrics import r2_score, mean_absolute_error

from farsight.nn.model import NeuralNetwork
from farsight.nn.dataset import CustomDataset
from farsight.nn import nn_utils



def main():
    train_set, validate_set, test_set = nn_utils.split_dataset([
        ("2014-01-01", "2022-12-31"), 
        ("2023-01-01", "2023-05-31"), 
        ("2023-06-01", "2023-12-31")
    ])
   
    train_dataloader = DataLoader(train_set, batch_size=nn_utils.batch_size, shuffle=True)
    validate_dataloader = DataLoader(validate_set, batch_size=nn_utils.batch_size, shuffle=True)
    
    model = NeuralNetwork()
    
    loss_fn = nn.MSELoss()
    optimizer = torch.optim.SGD(model.parameters(), lr=nn_utils.learning_rate)
    
    epochs = 10
    for i in range(epochs):
        print(f"EPOCH {i} STARTING:")
        train(train_dataloader, model, loss_fn, optimizer)
    
    print(f"VALIDATION SET:")     
    test(validate_dataloader, model, loss_fn)
   
    path = Path(__file__).parent.absolute()
    torch.save(model.state_dict(), str(path / "../models/nn.pt"))


def train(dataloader, model, loss_fn, optimizer):
    size = len(dataloader.dataset)
    
    model.train()
    for batch, (X, y) in enumerate(dataloader):
        pred = model(X).squeeze()
        loss = loss_fn(pred, y)
        
        diffs = torch.abs(pred - loss)
        total_diff = torch.sum(diffs)
        avg_diff = total_diff / (nn_utils.batch_size + len(X))
        
        loss.backward()
        optimizer.step()
        optimizer.zero_grad()
        
        if batch % 100 == 0:
            loss, current = loss.item(), batch * nn_utils.batch_size + len(X)
            print(f"loss: {loss:>7f} [{current:>5d}/{size:>5d}]")
            print(f"average difference: {avg_diff:>7f}")
            
def test(dataloader, model, loss_fn):
    model.eval()
    num_batches = len(dataloader)
    test_loss, correct = 0, 0
    preds = []
    ys = []
     
    with torch.no_grad():
        for X, y in dataloader:
            pred = model(X).squeeze()
            preds.append(pred)
            ys.append(y)
            test_loss += loss_fn(pred, y).item()
            
    test_loss /= num_batches
    y_true = torch.cat(ys, 0)
    y_pred = torch.cat(preds, 0)
    r2 = r2_score(y_true, y_pred)
    mae = mean_absolute_error(y_true, y_pred)
    print(f"Average loss: {test_loss:>8f}")
    print(f"r2 score: {r2:>8f}")
    print(f"MAE: {mae:>8f}")
    
    
    

if __name__=="__main__":
    main()
