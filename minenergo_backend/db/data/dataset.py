import pandas as pd


dataset_filename = "data/dataset.csv"


def get_dataset():
    return pd.read_csv(dataset_filename)
