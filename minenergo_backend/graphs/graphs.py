from db.models import Dataset
from time import mktime

graphs_data_column = {
    1: Dataset.generation,
    2: Dataset.consumption,
    4: Dataset.frequency,
    5: Dataset.temp_nw_ues,
    6: Dataset.usd_to_rub,
    7: Dataset.gas_avg_price,
    8: Dataset.coal_close_price,
    9: Dataset.oil_avg_price,
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
    9: avg_data
}


def prepare_data(x, y, date_resolution, graph_type):
    if date_resolution == 'day':
        return x, y
    if not (graphs_data_preparation.get(graph_type) is None):
        return graphs_data_preparation[graph_type](x, y, date_resolution)
    else:
        return [], []


def filter_query_by_date(query, start, end):
    if not (start is None):
        query = query.filter(Dataset.date >= start)
    if not (end is None):
        query = query.filter(Dataset.date < end)
    return query


def extract_data_from_query(query):
    date_list = []
    values_list = []
    for id, d, value in query.order_by(Dataset.date).all():
        date_list.append(d)
        values_list.append(value)
    return date_list, values_list


def get_graph_data(graph_type, energy_system_id, sess, start=None, end=None):
    if not(graphs_data_column.get(graph_type) is None):
        query = sess.query(Dataset.data_id, Dataset.date, graphs_data_column[graph_type])\
            .filter(Dataset.energy_system_id==energy_system_id)
        query = filter_query_by_date(query, start, end)
        date_list, values_list = extract_data_from_query(query)
        return date_list, values_list
    elif graph_type == 3:
        query = sess.query(Dataset.data_id, Dataset.date, Dataset.generation, Dataset.consumption)\
            .filter(Dataset.energy_system_id == energy_system_id)
        query = filter_query_by_date(query, start, end)
        date_list = []
        values_list = []
        for id, date, generation, consumption in query.order_by(Dataset.date).all():
            date_list.append(date)
            values_list.append(generation-consumption)
        return date_list, values_list
    else:
        return [], []


