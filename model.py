# coding: utf-8
from sqlalchemy import Column, ForeignKey, Integer, Numeric, String
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class Match(Base):
    __tablename__ = 'matches'
    __table_args__ = {'schema': 'public'}

    matchid = Column(String(100), primary_key=True)
    game_datetime = Column(String(100))
    game_length = Column(String(100))
    game_version = Column(String(100))


class User(Base):
    __tablename__ = 'users'
    __table_args__ = {'schema': 'public'}

    puuid = Column(String(100), primary_key=True)
    name = Column(String(20), nullable=False)
    summoner_level = Column(Integer, nullable=False)


class MatchUserDetail(Base):
    __tablename__ = 'match_user_details'
    __table_args__ = {'schema': 'public'}

    puuid = Column(ForeignKey('public.users.puuid'), primary_key=True, nullable=False)
    matchid = Column(ForeignKey('public.matches.matchid'), primary_key=True, nullable=False)
    gold_left = Column(Integer, nullable=False)
    last_round = Column(Integer, nullable=False)
    level = Column(Integer, nullable=False)
    placement = Column(Integer, nullable=False)
    time_eliminated = Column(Numeric, nullable=False)
    players_eliminated = Column(Integer, nullable=False)
    total_damage_to_players = Column(Integer, nullable=False)

    match = relationship('Match')
    user = relationship('User')
