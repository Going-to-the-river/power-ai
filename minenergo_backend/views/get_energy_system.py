from aiohttp import web
from db.models import Regions, EnergySystems
import contextlib


async def get_energy_system(request):
    session = request.app['session']
    id = request.match_info['id']
    with contextlib.closing(session()) as sess:
        db_response = sess.query(Regions, EnergySystems).join(EnergySystems).filter(EnergySystems.energy_system_id == id).order_by(Regions.region_id).all()
        if len(db_response) == 0:
            raise web.HTTPNotFound()
        else:
            regions = []
            for region, energy_system in db_response:
                region_json = region.to_json()
                regions.append(region_json)
            response = energy_system.to_json()
            response['regions'] = regions
            return web.json_response(response)