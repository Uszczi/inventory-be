from pydantic import BaseModel
from datetime import date


class MovieInSchema(BaseModel):
    title: str
    watch_date: date
    director: str
    production_year: int
