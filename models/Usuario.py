from sqlalchemy import Column, Integer, String, Date, ForeignKey, inspect
from sqlalchemy_serializer import SerializerMixin

import config
from database.database import metadata, Base, engine

class Usuario(Base):
    __tablename__ = 'usuario'
    metadata

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String(100))
    email = Column(String(100))
    senha = Column(String(200))
    tarefas = relationship('Tarefa')

if not inspect(engine).has_table('usuario', schema=config.MYSQL_DATABSE):
    Usuario.__table__.create(engine)