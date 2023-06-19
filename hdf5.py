import numpy as np
import h5py
from main import dataset

matrix = dataset.shape

with h5py.File('/home/dalison/Documentos/hdf5_data.h5', 'w') as hdf:
    hdf.create_dataset('dataset', matrix)

