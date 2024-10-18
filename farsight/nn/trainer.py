import pathlib
import os

import torch
from torch import nn
from torch.utils.data import DataLoader

from farsight.nn.model import NeuralNetwork
from farsight.nn.dataset import CustomDataset

learning_rate = 1e-5
batch_size = 100
epochs = 5

def main():
    train_set, validate_set, test_set = split_dataset([
        ("2014-01-01", "2022-12-31"), 
        ("2023-01-01", "2023-05-31"), 
        ("2023-06-01", "2023-12-31")
    ])
   
    train_dataloader = DataLoader(train_set, batch_size=batch_size, shuffle=True)
    validate_dataloader = DataLoader(validate_set, batch_size=batch_size, shuffle=True)
    
    model = NeuralNetwork()
    
    loss_fn = nn.MSELoss()
    optimizer = torch.optim.SGD(model.parameters(), lr=learning_rate)
    
    epochs = 10
    for i in range(epochs):
        print(f"EPOCH {i} STARTING:")
        train(train_dataloader, model, loss_fn, optimizer)
    
    print(f"VALIDATION SET:")     
    test(validate_dataloader, model, loss_fn)
    
    file_path = os.path.realpath(__file__)
    torch.save(model.state_dict(), file_path + "../models/nn.pt")


def train(dataloader, model, loss_fn, optimizer):
    size = len(dataloader.dataset)
    
    model.train()
    for batch, (X, y) in enumerate(dataloader):
        pred = model(X).squeeze()
        loss = loss_fn(pred, y)
        
        diffs = torch.abs(pred - loss)
        total_diff = torch.sum(diffs)
        avg_diff = total_diff / (batch_size + len(X))
        
        loss.backward()
        optimizer.step()
        optimizer.zero_grad()
        
        if batch % 100 == 0:
            loss, current = loss.item(), batch * batch_size + len(X)
            print(f"loss: {loss:>7f} [{current:>5d}/{size:>5d}]")
            print(f"average difference: {avg_diff:>7f}")
            
def test(dataloader, model, loss_fn):
    model.eval()
    num_batches = len(dataloader)
    test_loss, correct = 0, 0
    
    with torch.no_grad():
        for X, y in dataloader:
            pred = model(X).squeeze()
            test_loss += loss_fn(pred, y).item()
            
    test_loss /= num_batches
    print(f"Average loss: {test_loss:>8f}")
    
def split_dataset(cutoff_dates: list[tuple[str, str]]):
    datasets = []
    for start_date, end_date in cutoff_dates:
        datasets.append(CustomDataset(start_date, end_date))
        
    return datasets
    
    

if __name__=="__main__":
    main()
