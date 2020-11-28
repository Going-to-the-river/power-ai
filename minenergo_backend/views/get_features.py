from aiohttp import web
from db.models import Features
import contextlib


async def get_features(request):
    session = request.app['session']
    with contextlib.closing(session()) as sess:
        data = sess.query(Features).filter(Features.energy_system_id == 0).order_by(Features.feature_id).all()
        feature_list = []
        for feature in data:
            feature_list.append(
                {
                    'id': feature.feature_id,
                    'title': feature.title,
                    'graph_id': feature.graph_id,
                }
            )
    return web.json_response({'features' : feature_list})
