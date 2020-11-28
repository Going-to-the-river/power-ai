from aiohttp import web
from db.models import EnergySystems, Groups, Graphs
import contextlib


async def get_location(request):
    session = request.app['session']
    id = request.match_info['id']
    with contextlib.closing(session()) as sess:
        energy_system = sess.query(EnergySystems).filter(EnergySystems.energy_system_id == id).one_or_none()
        if energy_system is None:
            raise web.HTTPNotFound()
        data = sess.query(Graphs, Groups) \
            .join(Groups, Groups.group_id == Graphs.group_id)\
            .filter(Graphs.energy_system_id == id) \
            .order_by(Groups.group_id).order_by(Graphs.graph_id).all()
        location = {'id': energy_system.energy_system_id, 'title': energy_system.energy_system_name, 'graphs': {}}
        for graph, group in data:
            location['graphs'].setdefault(
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
                    'is_group': False
                }
            )
        location['graphs'] = list(location['graphs'].values())
        return web.json_response(location)
