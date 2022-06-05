from sqlalchemy.sql.schema import Column
from sqlalchemy.sql.sqltypes import Integer, String
from .base import Base


class MovieModel(Base):
    __tablename__ = "movies"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    watch_date = Column(String)
    director = Column(String)
    production_year = Column(String)
