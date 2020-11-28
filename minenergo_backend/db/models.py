from sqlalchemy import Column, Integer, Float, String, Boolean, ForeignKey, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


def to_json_method(self):
    this_dict = {}
    for k, v in self.__dict__.items():
        if k.startswith('_'):
            continue

        if k[-4:] == '_rel':
            continue

        this_dict[k] = v

    return this_dict


class EnergySystems(Base):
    __tablename__ = "EnergySystems"

    energy_system_id = Column(Integer, primary_key=True)
    energy_system_name = Column(String)

    to_json = to_json_method


class Regions(Base):
    __tablename__ = "Regions"

    region_id = Column(Integer, primary_key=True)
    region_name = Column(String)
    energy_system_id = Column(Integer, ForeignKey('EnergySystems.energy_system_id'))

    to_json = to_json_method


class Dataset(Base):
    __tablename__ = "Dataset"

    data_id = Column(Integer, primary_key=True)
    date = Column(DateTime)
    generation = Column(Float)
    consumption = Column(Float)
    temp_nw_ues = Column(Float)
    usd_to_rub = Column(Float)
    gas_avg_price = Column(Float)
    coal_close_price = Column(Float)
    oil_avg_price = Column(Float)
    frequency = Column(Float)
    day_of_week = Column(Integer)
    energy_system_id = Column(Integer, ForeignKey('EnergySystems.energy_system_id'))

    to_json = to_json_method


class Groups(Base):
    __tablename__ = "Groups"

    group_id = Column(Integer, primary_key=True)
    energy_system_id = Column(Integer, ForeignKey('EnergySystems.energy_system_id'))
    title = Column(String)
    is_group = Column(Boolean)
    group_type_id = Column(Integer)

    to_json = to_json_method


class Graphs(Base):
    __tablename__ = "Graphs"

    graph_id = Column(Integer, primary_key=True)
    group_id = Column(Integer, ForeignKey('Groups.group_id'))
    energy_system_id = Column(Integer, ForeignKey('EnergySystems.energy_system_id'))
    graph_type_id = Column(Integer)
    title = Column(String)
    ylab = Column(String)
    is_group = Column(Boolean)
    group_type_id = Column(Integer)
    color = Column(String)

    to_json = to_json_method


class Features(Base):
    __tablename__ = 'Features'

    feature_id = Column(Integer, primary_key=True)
    feature_type_id = Column(Integer)
    graph_id = Column(Integer, ForeignKey('Graphs.graph_id'))
    energy_system_id = Column(Integer, ForeignKey('EnergySystems.energy_system_id'))
    title = Column(String)

    to_json = to_json_method

