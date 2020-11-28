from db.data.energy_systems import ENERGY_SYSTEMS

groups = [
    {
        'title': 'Энегретические показатели',
        'is_group': True,
        'group_type_id': 1
    },
    {
        'title': 'Индикаторы работы ЕЭС/ОЭС',
        'is_group': True,
        'group_type_id': 2
    },
    {
        'title': 'Экономические показатели',
        'is_group': True,
        'group_type_id': 3
    },
    ]


graphs = [
    {
        'graph_type_id': 1,
        'title': 'Потребление электроэнергии',
        'ylab': "МВт*ч",
        'is_group': False,
        'group_type_id': 1,
        'color': '#c10020',
        'feature_type_id': 1,
    },
    {
        'graph_type_id': 2,
        'title': 'Генерация электроэнергии',
        'ylab': "МВт*ч",
        'is_group': False,
        'group_type_id': 1,
        'color': '#e34234',
        'feature_type_id': 2,
    },
    {
        'graph_type_id': 3,
        'title': 'Баланс электроэнергии',
        'ylab': "МВт*ч",
        'is_group': False,
        'group_type_id': 1,
        'color': '#c51d34',
    },
    {
        'graph_type_id': 4,
        'title': 'Частота',
        'ylab': 'Гц',
        'is_group': False,
        'group_type_id': 2,
        'color': '#7d7aff',
        'feature_type_id': 3,
    },
    {
        'graph_type_id': 5,
        'title': 'Средняя температура',
        'ylab': '°C',
        'is_group': False,
        'group_type_id': 2,
        'color': '#1814ff',
        'feature_type_id': 4,
    },
    {
        'graph_type_id': 6,
        'title': 'Курс Доллара',
        'ylab': '₽',
        'is_group': False,
        'group_type_id': 3,
        'color': '#aaff12',
        'feature_type_id': 5,
    },
    {
        'graph_type_id': 7,
        'title': 'Средняя цена на газ',
        'ylab': '$/BTU',
        'is_group': False,
        'group_type_id': 3,
        'color': '#00ff00',
        'feature_type_id': 6,
    },
    {
        'graph_type_id': 8,
        'title': 'Цена на уголь',
        'ylab': '$/Т',
        'is_group': False,
        'group_type_id': 3,
        'color': '#4cbb17',
        'feature_type_id': 7,
    },
    {
        'graph_type_id': 9,
        'title': 'Средняя цена на нефть',
        'ylab': '$/bbls',
        'is_group': False,
        'group_type_id': 3,
        'color': '#00ff7f',
        'feature_type_id': 8,
    }
    ]

features = {
    1: {
        'feature_type_id': 1,
        'title': 'Потребление электроэнергии',
    },
    2: {
        'feature_type_id': 2,
        'title': 'Генерация электроэнергии',
    },
    3: {
        'feature_type_id': 3,
        'title': 'Частота',
    },
    4: {
        'feature_type_id': 4,
        'title': 'Средняя температура',
    },
    5: {
        'feature_type_id': 5,
        'title': 'Курс Доллара',
    },
    6: {
        'feature_type_id': 6,
        'title': 'Средняя цена на газ',
    },
    7: {
        'feature_type_id': 7,
        'title': 'Цена на уголь',
    },
    8: {
        'feature_type_id': 8,
        'title': 'Средняя цена на нефть',
    },
}


def generate_groups_graphs_features():
    groups_id = 0
    graphs_id = 0
    features_id = 0
    all_groups = []
    all_graphs = []
    all_features = []

    for energy_system in ENERGY_SYSTEMS:
        for group in groups:
            new_group = group.copy()
            new_group['group_id'] = groups_id + new_group['group_type_id']
            new_group['energy_system_id'] = energy_system['energy_system_id']
            all_groups.append(new_group)

        for graph in graphs:
            new_graph = graph.copy()
            new_graph['group_id'] = groups_id + new_graph['group_type_id']
            new_graph['graph_id'] = graphs_id + new_graph['graph_type_id']
            new_graph['energy_system_id'] = energy_system['energy_system_id']
            # new_graph['subtitle'] = new_graph['title'] + " " + energy_system['energy_system_name']
            all_graphs.append(new_graph)

            if not (new_graph.get('feature_type_id') is None):
                new_feature = features[new_graph['feature_type_id']].copy()
                new_feature['feature_id'] = new_feature['feature_type_id'] + features_id
                new_feature['graph_id'] = new_graph['graph_id']
                new_feature['energy_system_id'] = energy_system['energy_system_id']
                all_features.append(new_feature)

        groups_id += len(groups)
        graphs_id += len(graphs)
        features_id += len(features)

    return all_groups, all_graphs, all_features