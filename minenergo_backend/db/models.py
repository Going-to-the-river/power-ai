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
    consumption_ues = Column(Float)
    temp_ues = Column(Float)
    consumption_nw_ues = Column(Float)
    temp_nw = Column(Float)

    temp_spb = Column(Float)
    pressure_spb = Column(Float)
    humidity_spb = Column(Float)
    wind_speed_spb = Column(Float)
    cloudiness_spb = Column(Float)

    usd_to_rub = Column(Float)
    gas_avg_price = Column(Float)
    oil_avg_price = Column(Float)
    frequency = Column(Float)

    year = Column(Integer)
    month = Column(Integer)
    day = Column(Integer)
    day_of_week = Column(Integer)

    consumption_ues_rm = Column(Float)
    consumption_nw_rm = Column(Float)

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


class PlotEconomic(Base):
    __tablename__ = 'PlotEconomic'

    id = Column(Integer, primary_key=True)
    date = Column(DateTime)
    consumption = Column(Float)
    consumption_speed = Column(Float)
    vrp_speed = Column(Float)

    to_json = to_json_method
