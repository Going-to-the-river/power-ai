from aiohttp import web
from db.models import Graphs
import contextlib


async def get_graphs(request):
    session = request.app['session']
    with contextlib.closing(session()) as sess:
        graphs = sess.query(Graphs).all()
        response = [graph.to_json() for graph in graphs]
        return web.json_response(response)
