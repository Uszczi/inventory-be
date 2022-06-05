from datetime import date
import os

from fastapi import Depends
from fastapi import APIRouter
from starlette.routing import Router

from inv.repo.movies import MoviesRepo
import re

from inv.views.schema import MovieInSchema

router = APIRouter()


def get_example_data_paths():
    path = "/app/example_data"
    files = os.listdir(path)
    files = sorted(files)
    print(files)
    files = [f"{path}/{file}" for file in files]
    return files


def extract_directors(line: str) -> tuple[str, str]:
    directors = re.findall("\*\*.*\*\*", line)
    if not directors:
        # TODO for now just raise
        raise Exception

    directors = directors[0]
    line = line.removesuffix(directors).strip()

    directors = directors.removesuffix("**").removeprefix("**")
    return line, directors


def extract_production_year(line: str) -> tuple[str, int]:
    production_year = re.findall("\([0-9]*\)", line)
    if not production_year:
        # TODO for now just raise
        raise Exception

    production_year = production_year[0]
    line = line.removesuffix(production_year).strip()

    production_year = production_year[1:-1]
    return line, int(production_year)


def process_line(line: str, watch_year: int, repo: MoviesRepo):
    line = line.strip()
    line, directors = extract_directors(line)
    title, production_year = extract_production_year(line)
    print(watch_year)
    watch_date = date(watch_year, 1, 1)
    movie = MovieInSchema(
        title=title,
        director=directors,
        production_year=production_year,
        watch_date=watch_date,
    )
    print(movie)
    repo.create(movie)


@router.get("/fill_movies")
def fill_db_with_movies(repo: MoviesRepo = Depends(MoviesRepo)):
    paths = get_example_data_paths()
    for path in paths:
        year = int(path[-7:-3])
        with open(path, "r") as f:
            for line in f.readlines():
                if not line:
                    continue
                try:
                    process_line(line, watch_year=year, repo=repo)
                except Exception:
                    pass
