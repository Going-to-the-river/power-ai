from db.models import Dataset
import pandas as pd
from datetime import date, datetime, timedelta
from features.features import get_data_for_prediction, predict_consumption
dataset = pd.read_csv('db/data/dataset_ML1.csv')


def prepare_dataset():
    for index in range(len(dataset['date'])):
        old = date.fromisoformat(dataset['date'][index])
        new = datetime(old.year, old.month, old.day, 0, 0, 0)
        dataset['date'][index] = new


prepare_dataset()

graphs_data_column = {
    1: 'consumption_NW_UES',
    2: 'generation_NW_UES',
    4: 'frequency',
    5: 'temp_NW',
    6: 'USD_to_RUB',
    7: 'gas_avg_price',
    8: 'oil_avg_price',
    9: 'temp_SPB',
    10: 'pressure_SPB',
    11: 'humidity_SPB',
    12: 'wind_speed_SPB',
    13: 'cloudiness_SPB'
}


def is_dates_equal(first_date, second_date, date_resolution):
    if date_resolution == 'day':
        return first_date.day == second_date.day
    elif date_resolution == 'month':
        return first_date.month == second_date.month
    else:
        return first_date.year == second_date.year


def aggregate_data(x, y, date_resolution):
    new_x = []
    new_y = []
    count = []
    if len(x) != 0:
        new_x.append(x[0])
        new_y.append(y[0])
        count.append(1)
    for i in range(1, len(x)):
        if is_dates_equal(x[i - 1], x[i], date_resolution):
            new_y[-1] += y[i]
            count[-1] += 1
        else:
            new_y.append(y[i])
            new_x.append(x[i])
            count.append(1)
    return new_x, new_y, count


def avg_data(x, y, date_resolution):
    new_x, new_y, count = aggregate_data(x, y, date_resolution)
    new_y = [val / count[index] for index, val in enumerate(new_y)]
    return new_x, new_y


def sum_data(x, y, date_resolution):
    new_x, new_y, _ = aggregate_data(x, y, date_resolution)
    return new_x, new_y


graphs_data_preparation = {
    1: sum_data,
    2: sum_data,
    3: sum_data,
    4: avg_data,
    5: avg_data,
    6: avg_data,
    7: avg_data,
    8: avg_data,
    9: avg_data,
    10: avg_data,
    11: avg_data,
    12: avg_data,
    13: avg_data
}


def prepare_data(x, y, date_resolution, graph_type):
    if date_resolution == 'day':
        return x, y
    if not (graphs_data_preparation.get(graph_type) is None):
        return graphs_data_preparation[graph_type](x, y, date_resolution)
    else:
        return [], []


def filter_query_by_date(data, start, end):
    if not (start is None):
        data = data[data.date >= start]
    if not (end is None):
        data = data[data.date < end]
    return data


def extract_data_from_query(data):
    date_list = []
    values_list = []
    for _, value in data.iterrows():
        date_list.append(value[0])
        values_list.append(value[1])
    return date_list, values_list


def generate_dates(n, start):
    dates = [start]
    for i in range(n-1):
        dates.append(dates[-1] + timedelta(days=1))
    return dates

def get_graph_data(graph_type, start=None, end=None):
    if not(graphs_data_column.get(graph_type) is None):
        data = dataset[['date', graphs_data_column.get(graph_type)]].copy()
        data = filter_query_by_date(data, start, end)
        date_list, values_list = extract_data_from_query(data)
        return date_list, values_list
    elif graph_type == 3:
        data = dataset[['date', 'generation_NW_UES', 'consumption_NW_UES']].copy()
        data = filter_query_by_date(data, start, end)
        date_list = []
        values_list = []
        for _, values in data.iterrows():
            date_list.append(values[0])
            values_list.append(values[1]-values[2])
        return date_list, values_list
    else:
        return [], []


