groups = [
    {
        'title': 'Энегретические показатели',
        'is_group': True,
        'group_type_id': 1,
        'energy_system_id': 0,
        'group_id': 1,
    },
    {
        'title': 'Индикаторы работы ЕЭС/ОЭС',
        'is_group': True,
        'group_type_id': 2,
        'energy_system_id': 0,
        'group_id': 2,
    },
    {
        'title': 'Экономические показатели',
        'is_group': True,
        'group_type_id': 3,
        'energy_system_id': 0,
        'group_id': 3,
    },
    {
        'title': 'Физические показатели в Санкт-Петербурге',
        'is_group': True,
        'group_type_id': 4,
        'energy_system_id': 0,
        'group_id': 4
    }
    ]


graphs = [
    {
        'graph_type_id': 1,
        'title': 'Потребление электроэнергии',
        'ylab': "МВт*ч",
        'is_group': False,
        'group_type_id': 1,
        'color': '#c10020',
        'graph_id': 1,
        'group_id': 1,
        'energy_system_id': 0
    },
    {
        'graph_type_id': 2,
        'title': 'Генерация электроэнергии',
        'ylab': "МВт*ч",
        'is_group': False,
        'group_type_id': 1,
        'color': '#e34234',
        'graph_id': 2,
        'group_id': 1,
        'energy_system_id': 0
    },
    {
        'graph_type_id': 3,
        'title': 'Баланс электроэнергии',
        'ylab': "МВт*ч",
        'is_group': False,
        'group_type_id': 1,
        'color': '#c51d34',
        'graph_id': 3,
        'group_id': 1,
        'energy_system_id': 0
    },
    {
        'graph_type_id': 4,
        'title': 'Частота',
        'ylab': 'Гц',
        'is_group': False,
        'group_type_id': 2,
        'color': '#7d7aff',
        'graph_id': 4,
        'group_id': 2,
        'energy_system_id': 0
    },
    {
        'graph_type_id': 5,
        'title': 'Средняя температура',
        'ylab': '°C',
        'is_group': False,
        'group_type_id': 2,
        'color': '#1814ff',
        'graph_id': 5,
        'group_id': 2,
        'energy_system_id': 0
    },
    {
        'graph_type_id': 6,
        'title': 'Курс Доллара',
        'ylab': '₽',
        'is_group': False,
        'group_type_id': 3,
        'color': '#aaff12',
        'graph_id': 6,
        'group_id': 3,
        'energy_system_id': 0
    },
    {
        'graph_type_id': 7,
        'title': 'Средняя цена на газ',
        'ylab': '$/BTU',
        'is_group': False,
        'group_type_id': 3,
        'color': '#00ff00',
        'graph_id': 7,
        'group_id': 3,
        'energy_system_id': 0
    },
    {
        'graph_type_id': 8,
        'title': 'Средняя цена на нефть',
        'ylab': '$/bbls',
        'is_group': False,
        'group_type_id': 3,
        'color': '#00ff7f',
        'graph_id': 8,
        'group_id': 3,
        'energy_system_id': 0
    },
    {
        'graph_type_id': 9,
        'title': 'Температура в СПб',
        'ylab': '°C',
        'is_group': False,
        'group_type_id': 4,
        'color': '#00ff7f',
        'graph_id': 9,
        'group_id': 4,
        'energy_system_id': 0
    },
    {
        'graph_type_id': 10,
        'title': 'Давление в СПб',
        'ylab': 'мм. рт. ст',
        'is_group': False,
        'group_type_id': 4,
        'color': '#00ff7f',
        'graph_id': 10,
        'group_id': 4,
        'energy_system_id': 0
    },
    {
        'graph_type_id': 11,
        'title': 'Влажность в СПб',
        'ylab': '%',
        'is_group': False,
        'group_type_id': 4,
        'color': '#00ff7f',
        'graph_id': 11,
        'group_id': 4,
        'energy_system_id': 0
    },
    {
        'graph_type_id': 12,
        'title': 'Скорость ветра в СПб',
        'ylab': 'мм. рт. ст',
        'is_group': False,
        'group_type_id': 4,
        'color': '#00ff7f',
        'graph_id': 12,
        'group_id': 4,
        'energy_system_id': 0
    },
    {
        'graph_type_id': 13,
        'title': 'Облачность СПб',
        'ylab': '%',
        'is_group': False,
        'group_type_id': 4,
        'color': '#00ff7f',
        'graph_id': 13,
        'group_id': 4,
        'energy_system_id': 0
    }
]

features = [
    {
        'feature_type_id': 1,
        'title': 'Потребление электроэнергии',
        'energy_system_id': 0,
        'feature_id': 1,
        'graph_id': 1,
    },
    # {
    #     'feature_type_id': 2,
    #     'title': 'Средняя температура',
    #     'energy_system_id': 0,
    #     'feature_id': 2,
    #     'graph_id': 5,
    # },
    {
        'feature_type_id': 3,
        'title': 'Курс Доллара',
        'energy_system_id': 0,
        'feature_id': 3,
        'graph_id': 6,
    },
    {
        'feature_type_id': 4,
        'title': 'Средняя цена на газ',
        'energy_system_id': 0,
        'feature_id': 4,
        'graph_id': 7,
    },
    {
        'feature_type_id': 5,
        'title': 'Средняя цена на нефть',
        'energy_system_id': 0,
        'feature_id': 5,
        'graph_id': 8,
    },
    # {
    #     'feature_type_id': 6,
    #     'title': 'Температура в СПб',
    #     'energy_system_id': 0,
    #     'feature_id': 6,
    #     'graph_id': 9,
    # },
    # {
    #     'feature_type_id': 7,
    #     'title': 'Давление в СПб',
    #     'energy_system_id': 0,
    #     'feature_id': 7,
    #     'graph_id': 10,
    # },
    # {
    #     'feature_type_id': 8,
    #     'title': 'Влажность в СПб',
    #     'energy_system_id': 0,
    #     'feature_id': 8,
    #     'graph_id': 11,
    # },
    # {
    #     'feature_type_id': 9,
    #     'title': 'Скорость ветра в СПб',
    #     'energy_system_id': 0,
    #     'feature_id': 9,
    #     'graph_id': 12,
    # },
    # {
    #     'feature_type_id': 10,
    #     'title': 'Облачность в СПб',
    #     'energy_system_id': 0,
    #     'feature_id': 10,
    #     'graph_id': 13,
    # }
]
