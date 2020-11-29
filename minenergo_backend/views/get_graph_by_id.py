from aiohttp import web
from db.models import Graphs
from graphs.graphs import get_graph_data, prepare_data
from datetime import datetime, timedelta
import contextlib


def from_timestamp_to_date(timestamp):
    if timestamp is None:
        return timestamp
    else:
        return datetime.strptime(timestamp[:10], '%Y-%m-%d')


def output_date(d):
    if d is None:
        return None
    else:
        return d.strftime('%Y.%m.%d')


def is_valid_date_resolution(date_resolution):
    return date_resolution == 'day' or \
           date_resolution == 'month' or \
           date_resolution == 'year'


def prepare_date(start, end, date_resolution):
    if date_resolution == 'day':
        return start, end
    elif date_resolution == 'month':
        if not (start is None):
            start = datetime(start.year, start.month, 1, 0, 0, 0)
        if not (end is None):
            end = datetime(end.year, end.month, 1, 0, 0, 0)
        return start, end
    else:
        if not (start is None):
            start = datetime(start.year, 1, 1, 0, 0, 0)
        if not (end is None):
            end = datetime(end.year, 1, 1, 0, 0, 0)
        return start, end


def generate_response_data(dates, values):
    response = []
    for i in range(len(dates)):
        response.append(
            {
                'x': output_date(dates[i]),
                'y': values[i]
            }
        )
    return response





async def get_graph_by_id(request):
    session = request.app['session']
    request_json = await request.json()
    id = request_json['id']
    date_resolution = request_json['resolution']
    start, end = prepare_date(
        from_timestamp_to_date(request_json.get('start')),
        from_timestamp_to_date(request_json.get('end')),
        date_resolution
    )

    if not is_valid_date_resolution(date_resolution):
        raise web.HTTPBadRequest()

    with contextlib.closing(session()) as sess:
        graph = sess.query(Graphs).filter(Graphs.graph_id == id).one_or_none()
        if graph is None:
            return web.HTTPNotFound()
        energy_system_id = graph.energy_system_id
        graph_type_id = graph.graph_type_id
        dates, values = get_graph_data(graph_type_id, start, end)
        dates, values = prepare_data(dates, values, date_resolution, graph_type_id)
        response = generate_response_data(dates, values)
        return web.json_response({'color': graph.color, 'data': response, 'ylab': graph.ylab})
