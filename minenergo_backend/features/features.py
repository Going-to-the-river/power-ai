from db.models import Dataset
from datetime import datetime
# from graphs.graphs import dataset
from joblib import load
from features.feature_order import feature_order
import pandas as pd

dataset = pd.read_csv('db/data/dataset_ML1.csv')
model = load('features/forest2.joblib')


def predict_consumption(data):
    return model.predict([data])[0][1:]


features_map = {
    1: ['consumption_NW_UES_lag_1',
                 'consumption_NW_UES_lag_2', 'consumption_NW_UES_lag_3', 'consumption_NW_UES_lag_4',
                 'consumption_NW_UES_lag_5', 'consumption_NW_UES_lag_6', 'consumption_NW_UES_lag_7',
                 'consumption_NW_UES_lag_8', 'consumption_NW_UES_lag_9', 'consumption_NW_UES_lag_10',
                 'consumption_NW_UES_lag_11', 'consumption_NW_UES_lag_12', 'consumption_NW_UES_lag_13',
                 'consumption_NW_UES_lag_14', 'consumption_NW_UES_lag_15', 'consumption_NW_UES_lag_16',
                 'consumption_NW_UES_lag_17', 'consumption_NW_UES_lag_18', 'consumption_NW_UES_lag_19',
                 'consumption_NW_UES_lag_20', 'consumption_NW_UES_lag_21', 'consumption_NW_UES_lag_22',
                 'consumption_NW_UES_lag_23', 'consumption_NW_UES_lag_24', 'consumption_NW_UES_lag_25',
                 'consumption_NW_UES_lag_26', 'consumption_NW_UES_lag_27', 'consumption_NW_UES_lag_28',
                 'consumption_NW_UES_lag_29', 'consumption_NW_UES_lag_30', 'consumption_NW_rm'],
    3: ['USD_to_RUB_lag_1', 'USD_to_RUB_lag_2', 'USD_to_RUB_lag_3', 'USD_to_RUB_lag_4', 'USD_to_RUB_lag_5',
                 'USD_to_RUB_lag_6', 'USD_to_RUB_lag_7', 'USD_to_RUB_lag_8', 'USD_to_RUB_lag_9', 'USD_to_RUB_lag_10',
                 'USD_to_RUB_lag_11', 'USD_to_RUB_lag_12', 'USD_to_RUB_lag_13', 'USD_to_RUB_lag_14',
                 'USD_to_RUB_lag_15', 'USD_to_RUB_lag_16', 'USD_to_RUB_lag_17', 'USD_to_RUB_lag_18',
                 'USD_to_RUB_lag_19', 'USD_to_RUB_lag_20', 'USD_to_RUB_lag_21', 'USD_to_RUB_lag_22',
                 'USD_to_RUB_lag_23', 'USD_to_RUB_lag_24', 'USD_to_RUB_lag_25', 'USD_to_RUB_lag_26',
                 'USD_to_RUB_lag_27', 'USD_to_RUB_lag_28', 'USD_to_RUB_lag_29', 'USD_to_RUB_lag_30'],
    4: ['gas_avg_price_lag_1', 'gas_avg_price_lag_2', 'gas_avg_price_lag_3', 'gas_avg_price_lag_4',
                 'gas_avg_price_lag_5', 'gas_avg_price_lag_6', 'gas_avg_price_lag_7', 'gas_avg_price_lag_8',
                 'gas_avg_price_lag_9', 'gas_avg_price_lag_10', 'gas_avg_price_lag_11', 'gas_avg_price_lag_12',
                 'gas_avg_price_lag_13', 'gas_avg_price_lag_14', 'gas_avg_price_lag_15', 'gas_avg_price_lag_16',
                 'gas_avg_price_lag_17', 'gas_avg_price_lag_18', 'gas_avg_price_lag_19', 'gas_avg_price_lag_20',
                 'gas_avg_price_lag_21', 'gas_avg_price_lag_22', 'gas_avg_price_lag_23', 'gas_avg_price_lag_24',
                 'gas_avg_price_lag_25', 'gas_avg_price_lag_26', 'gas_avg_price_lag_27', 'gas_avg_price_lag_28',
                 'gas_avg_price_lag_29', 'gas_avg_price_lag_30'],
    5: ['oil_avg_price_lag_1', 'oil_avg_price_lag_2',
                 'oil_avg_price_lag_3', 'oil_avg_price_lag_4', 'oil_avg_price_lag_5', 'oil_avg_price_lag_6',
                 'oil_avg_price_lag_7', 'oil_avg_price_lag_8', 'oil_avg_price_lag_9', 'oil_avg_price_lag_10',
                 'oil_avg_price_lag_11', 'oil_avg_price_lag_12', 'oil_avg_price_lag_13', 'oil_avg_price_lag_14',
                 'oil_avg_price_lag_15', 'oil_avg_price_lag_16', 'oil_avg_price_lag_17', 'oil_avg_price_lag_18',
                 'oil_avg_price_lag_19', 'oil_avg_price_lag_20', 'oil_avg_price_lag_21', 'oil_avg_price_lag_22',
                 'oil_avg_price_lag_23', 'oil_avg_price_lag_24', 'oil_avg_price_lag_25', 'oil_avg_price_lag_26',
                 'oil_avg_price_lag_27', 'oil_avg_price_lag_28', 'oil_avg_price_lag_29', 'oil_avg_price_lag_30'],
}


def get_data_for_prediction(data):
    new_data = []
    for features_name in feature_order:
        new_data.append(data[features_name])
    return new_data


def get_dataset():
    return dataset.iloc[-1].copy()


# {"id":1,"title":"Потребление электроэнергии","graph_id":1,"scale_percent":100}
def change_values(feature_scaling, data):
    for feature in feature_scaling:
        feature_list = features_map[feature['id']]
        for feature_name in feature_list:
            data[feature_name] = data[feature_name] * (feature['scale_percent'] / 100.0)
    return data