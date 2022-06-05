from fastapi import APIRouter
from datetime import datetime, date
from fastapi import Depends
from sqlalchemy.sql.sqltypes import Date
from starlette.requests import Request
from starlette.responses import Response
from pydantic import BaseModel
from inv.models.movies import MovieModel
from fastapi import FastAPI, HTTPException
from inv.views.schema import MovieInSchema

from inv.repo.movies import MoviesRepo

router = APIRouter()


@router.get("/movies")
def movies_list(repo: MoviesRepo = Depends(MoviesRepo)) -> list[MovieModel]:
    models = repo.list()
    return models


@router.post("/movie")
def movie(
    request: Request, movie: MovieInSchema, repo: MoviesRepo = Depends(MoviesRepo)
) -> str:
    movie = repo.create(movie)
    return request.url_for("get_movie", id=movie.id)


@router.get("/movie/{id}")
def get_movie(id: int, repo: MoviesRepo = Depends(MoviesRepo)) -> MovieModel:
    movie = repo.get_by_id(id)
    if not movie:
        raise HTTPException(status_code=404, detail="Item not found")
    return movie
