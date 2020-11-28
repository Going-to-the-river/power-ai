from aiohttp import web
from db.models import Groups
import contextlib


async def get_groups(request):
    session = request.app['session']
    with contextlib.closing(session()) as sess:
        groups = sess.query(Groups).all()
        response = [group.to_json() for group in groups]
        return web.json_response(response)
