# request =
# {
#     'features': [
#         {
#             'id': 5,
#             'scale': (0-10)
#         }
#     ]
# }
#
# response
# {'color': graph.color, 'data': response, 'ylab': graph.ylab}

from aiohttp import web
from db.models import Features, Graphs
from features.features import get_dataset, change_values, predict_consumption, get_data_for_prediction
from datetime import datetime, timedelta
import contextlib


def generate_dates(n, start=datetime(2020, 11, 28, 0, 0, 0)):
    dates = [start]
    for i in range(n - 1):
        dates.append(dates[-1] + timedelta(days=1))
    return dates


def output_date(d):
    if d is None:
        return None
    else:
        return d.strftime('%Y.%m.%d')


async def get_prediction(request):
    session = request.app['session']
    request_json = await request.json()
    feature_scaling = request_json['features']

    with contextlib.closing(session()) as sess:
        feature = sess.query(Features).filter(Features.graph_id == feature_scaling[0]['id']).one_or_none()
        if feature is None:
            return web.HTTPNotFound()

        baseline_input = get_dataset()
        prediction_input = get_dataset()
        prediction_input = change_values(feature_scaling, prediction_input)

        baseline_consumption = predict_consumption(get_data_for_prediction(baseline_input))
        prediction_consumption = predict_consumption(get_data_for_prediction(prediction_input))
        dates = generate_dates(len(baseline_consumption))

        response = {
            'baseline': [],
            'prediction': []
        }
        for i in range(len(dates)):
            response['baseline'].append({'x': output_date(dates[i]), 'y': baseline_consumption[i]})
            response['prediction'].append({'x': output_date(dates[i]), 'y': prediction_consumption[i]})

        return web.json_response(response)
