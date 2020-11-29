import pandas as pd


dataset_filename = "data/dataset_ML1.csv"


def get_dataset():
    return pd.read_csv(dataset_filename)