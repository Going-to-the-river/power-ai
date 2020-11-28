from aiohttp import web
from db.models import EnergySystems, Groups, Graphs
import contextlib


async def get_locations(request):
    session = request.app['session']
    with contextlib.closing(session()) as sess:
        data = sess.query(Graphs, Groups, EnergySystems) \
            .join(Groups, Groups.group_id == Graphs.group_id)\
            .join(EnergySystems, EnergySystems.energy_system_id == Graphs.energy_system_id) \
            .order_by(Groups.group_id).order_by(Graphs.graph_id).all()
        locations = {}
        for graph, group, energy_system in data:
            locations.setdefault(
                energy_system.energy_system_id,
                {
                    'id': energy_system.energy_system_id,
                    'title': energy_system.energy_system_name,
                    'graphs': {}
                }
            )['graphs'].setdefault(
                group.group_id,
                {
                    'group_id': group.group_id,
                    'title': group.title,
                    'is_group': True,
                    'children': []
                }
            )['children'].append(
                {
                    'id': graph.graph_id,
                    'title': graph.title,
                    'ylab': graph.ylab,
                    'is_group': False,
                    'color': graph.color
                }
            )
        response = list(locations.values())
        for item in response:
            item['graphs'] = list(item['graphs'].values())
        return web.json_response({'locations': response})
