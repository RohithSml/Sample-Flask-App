from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Integer, String
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import mapped_column
import logging
from typing import List

from sqlalchemy import String, Integer,Date, create_engine, UniqueConstraint
from sqlalchemy.orm import DeclarativeBase,Mapped,mapped_column, sessionmaker, relationship

class Base(DeclarativeBase):
  def __repr__(self):
    return f"{self.__class__.__name__}(id={self.id})"

db = SQLAlchemy(model_class=Base)c



class User(Base):
    __tablename__ = "user"
    __table_args__= (UniqueConstraint('firstname','lastname','email'),)
    id    : Mapped[int] = mapped_column(primary_key=True)
    firstname: Mapped[str] = mapped_column(String(50))
    lastname : Mapped[str] = mapped_column(String(50))
    email    : Mapped[str] = mapped_column(String(150))
    ph_no    : Mapped[str] = mapped_column(String(50))


def init_db(db_uri='postgresql://djangouser:djangopassword@localhost:5432/flaskdb'):
    logger = logging.getLogger("FlaskApp")
    engine = create_engine(db_uri)
    Base.metadata.create_all(engine)
    logger.info("Created database")

def get_session(db_uri):
    engine = create_engine(db_uri)
    Session = sessionmaker(bind = engine)
    session = Session()
    return session