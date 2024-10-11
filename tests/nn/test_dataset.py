from farsight.nn.dataset import CustomDataset

def test_dataset():
	dataset = CustomDataset("2016-07-28", "2016-07-29")
	x, label = dataset.__getitem__(100)
 
	assert(not label.isnan())
	assert(len(x) == 157)