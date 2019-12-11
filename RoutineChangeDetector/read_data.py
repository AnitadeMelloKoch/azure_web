import pandas as pd
import numpy as np

def read_data(data_dir):
    data = pd.read_csv(data_dir)
    data_numpy = data.as_matrix()

    return data_numpy