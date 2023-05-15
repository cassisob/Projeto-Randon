from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from Banco.database import Base

class Time(Base):
    __tablename__ = 'times'
    id = Column(Integer, primary_key = True, index = True)
    nome = Column(String)
    cidade = Column(String)

class Jogador(Base):
    __tablename__ = 'jogadores'
    id = Column(Integer, primary_key = True, index = True)
    nome = Column(String)
    nick = Column(String)
    patente = Column(String)
    funcao = Column(String)
    steam = Column(String)
    gamersClub = Column(String)

    time_id = Column(Integer, ForeignKey("times.id"))
    time = relationship("Time")

class Coach(Base):
    __tablename__ = 'coachs'
    id = Column(Integer, primary_key = True, index = True)
    nome = Column(String)
    nick = Column(String)

    time_id = Column(Integer, ForeignKey("times.id"))
    time = relationship("Time")