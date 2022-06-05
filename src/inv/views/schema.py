from pydantic import BaseModel
from datetime import date


class MovieInSchema(BaseModel):
    title: str
    watch_date: date | str
    director: str
    production_year: int
