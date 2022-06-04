from fastapi import APIRouter
from datetime import datetime, date
from sqlalchemy.sql.sqltypes import Date
from starlette.responses import Response
from pydantic import BaseModel

router = APIRouter()


class Movie(BaseModel):
    title: str
    date: date | str
    director: str
    production_year: int

@router.get("/movies")
def movies_list() -> str:
    # TODO
    return "asdfsaf"

@router.post("/movie")
def movie(movie: Movie) -> str:
    # TODO
    print(movie)
    return "asdfsafsdaf"

