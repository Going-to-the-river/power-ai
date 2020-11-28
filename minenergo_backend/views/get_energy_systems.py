from aiohttp import web
from db.models import Regions, EnergySystems
import contextlib


async def get_energy_systems(request):
    session = request.app['session']
    with contextlib.closing(session()) as sess:
        energy_systems = {}
        for region, energy_system in sess.query(Regions, EnergySystems).join(
                EnergySystems).order_by(Regions.region_id).all():
            region_json = region.to_json()
            energy_system_json = energy_system.to_json()
            energy_system_json['regions'] = []
            energy_systems.setdefault(energy_system_json['energy_system_id'], energy_system_json)['regions'].append(region_json)
        print(list(energy_systems.values()))
        return web.json_response(list(energy_systems.values()))
