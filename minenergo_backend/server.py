from aiohttp import web
from views.simple_handler import hello
from views.get_energy_system import get_energy_system
from views.get_energy_systems import get_energy_systems
from views.get_groups import get_groups
from views.get_graphs import get_graphs
from views.get_locations import get_locations
from views.get_location import get_location
from views.get_graph_by_id import get_graph_by_id
from views.get_features import get_features
from views.get_prediction import get_prediction

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///db/testdb')
session = sessionmaker(bind=engine)


def start_server():
    app = web.Application()
    app['session'] = session
    get_requests = [
        ('/backend/', hello),
        ('/backend/energy-systems/', get_energy_systems),
        (r'/backend/energy-systems/{id:\d+}/', get_energy_system),
        ('/backend/groups/', get_groups),
        ('/backend/graphs/', get_graphs),
        (r'/backend/locations/{id:\d+}/', get_location),
    ]
    post_requests = [
        ('/backend/get_graph_by_id/', get_graph_by_id),
        ('/backend/get_locations/', get_locations),
        ('/backend/get_features/', get_features),
        ('/backend/get_prediction/', get_prediction)

    ]

    get_routes = [web.get(path, handler) for path, handler in get_requests]
    post_routes = [web.post(path, handler) for path, handler in post_requests]
    routes = get_routes + post_routes

    app.add_routes(routes)
    web.run_app(app, host='127.0.0.1', port=54321)


if __name__ == '__main__':
    start_server()
