from typing import TypeVar
from fastapi import Depends
from sqlalchemy.orm import Session

from inv.main.db import get_db
from inv.models.movies import MovieModel
from inv.views.schema import MovieInSchema


class MoviesRepo:
    _model = MovieModel

    def __init__(self, db: Session = Depends(get_db)) -> None:
        self.db = db

    def list(self) -> list[MovieModel]:
        models = self.db.query(self._model).all()
        return models

    def get_by_id(self, id: int) -> MovieModel:
        model = self.db.query(self._model).get(id)
        return model

    def create(self, movie: MovieInSchema):
        model = MovieModel(
            # id=1,
            title=movie.title,
            watch_date=movie.watch_date,
            director=movie.director,
            production_year=movie.production_year,
        )
        self.db.add(model)
        self.db.commit()
        self.db.refresh(model)
        return model
