from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from db.models import Base, Regions, EnergySystems, Dataset, Groups, Graphs, Features
from db.data.energy_systems import ENERGY_SYSTEMS
from db.data.dataset import get_dataset
from db.data.graphs import groups, graphs, features
from datetime import datetime


def fill_energy_systems_table():
    energy_systems_rows = []
    for energy_system in ENERGY_SYSTEMS:
        energy_systems_rows.append(
            EnergySystems(
                energy_system_id=energy_system['energy_system_id'],
                energy_system_name=energy_system['energy_system_name'],
            )
        )
    return energy_systems_rows


def fill_nw_dataset_table():
    dataset_rows = []
    df = get_dataset()
    for index, row in df.iterrows():
        dataset_rows.append(
            Dataset(
                data_id=index,
                date=datetime.fromisoformat(row.date),
                consumption_ues=row.consumption_UES,
                temp_ues=row.temp_UES,
                consumption_nw_ues=row.consumption_NW_UES,
                temp_nw=row.temp_NW,
                temp_spb=row.temp_SPB,
                pressure_spb=row.pressure_SPB,
                humidity_spb=row.wind_speed_SPB,
                wind_speed_spb=row.wind_speed_SPB,
                cloudiness_spb=row.cloudiness_SPB,
                usd_to_rub=row.USD_to_RUB,
                gas_avg_price=row.gas_avg_price,
                oil_avg_price=row.oil_avg_price,
                frequency=row.frequency,
                year=row.year,
                month=row.month,
                day=row.day,
                day_of_week=row.dayofweek,
                consumption_ues_rm=row.consumption_UES_rm,
                consumption_nw_rm=row.consumption_NW_rm,
                energy_system_id=0,

            )
        )
    return dataset_rows


def fill_groups_table(groups):
    groups_rows = []
    for row in groups:
        groups_rows.append(
            Groups(
                group_id=row['group_id'],
                energy_system_id=row['energy_system_id'],
                title=row['title'],
                is_group=row['is_group'],
                group_type_id=row['group_type_id']
            )
        )

    return groups_rows


def fill_graphs_table(graphs):
    graphs_rows = []
    for row in graphs:
        graphs_rows.append(
            Graphs(
                graph_id=row['graph_id'],
                group_id=row['group_id'],
                energy_system_id=row['energy_system_id'],
                graph_type_id=row['graph_type_id'],
                title=row['title'],
                ylab=row['ylab'],
                is_group=row['is_group'],
                group_type_id=row['group_type_id'],
                color=row['color']
            )
        )

    return graphs_rows


def fill_features_table(features):
    features_rows = []
    for row in features:
        features_rows.append(
            Features(
                feature_id=row['feature_id'],
                feature_type_id=row['feature_type_id'],
                graph_id=row['graph_id'],
                title=row['title'],
                energy_system_id=row['energy_system_id']
            )
        )

    return features_rows


def create_and_fill_tables():
    engine = create_engine('sqlite:///testdb', echo=True)
    tables = [
        EnergySystems.__table__,
        Groups.__table__,
        Graphs.__table__,
        Features.__table__
    ]
    Base.metadata.drop_all(engine, tables=tables)
    Base.metadata.create_all(engine, tables=tables)

    session = sessionmaker(bind=engine)
    sess = session()

    sess.add_all(fill_energy_systems_table())
    sess.commit()
    # sess.add_all(fill_nw_dataset_table())
    # sess.commit()
    sess.add_all(fill_groups_table(groups))
    sess.commit()
    sess.add_all(fill_graphs_table(graphs))
    sess.commit()
    sess.add_all(fill_features_table(features))
    sess.commit()


if __name__ == '__main__':
    create_and_fill_tables()
