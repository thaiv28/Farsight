from farsight.nn.dataset import CustomDataset

learning_rate = 1e-5
batch_size = 100
epochs = 5

def split_dataset(cutoff_dates: list[tuple[str, str]]):
    datasets = []
    for start_date, end_date in cutoff_dates:
        datasets.append(CustomDataset(start_date, end_date))
        
    return datasets