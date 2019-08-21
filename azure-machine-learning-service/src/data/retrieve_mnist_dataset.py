import os
import urllib.request

data_raw_folder = '../../notebooks/data/raw'

# create a folder for the dataset if it doesn't exist yet
os.makedirs(data_raw_folder, exist_ok = True)

# load dataset to the directory--as you can see, you must load train sets and test sets separately
urllib.request.urlretrieve('http://yann.lecun.com/exdb/mnist/train-images-idx3-ubyte.gz', filename=f'{data_raw_folder}/train-images.gz')
urllib.request.urlretrieve('http://yann.lecun.com/exdb/mnist/train-labels-idx1-ubyte.gz', filename=f'{data_raw_folder}/train-labels.gz')
urllib.request.urlretrieve('http://yann.lecun.com/exdb/mnist/t10k-images-idx3-ubyte.gz',  filename=f'{data_raw_folder}/test-images.gz')
urllib.request.urlretrieve('http://yann.lecun.com/exdb/mnist/t10k-labels-idx1-ubyte.gz',  filename=f'{data_raw_folder}/test-labels.gz')