from fastapi import FastAPI

from fastapi.middleware.cors import CORSMiddleware
from inv.views.movies import router as movie_router

def get_app():
    app = FastAPI()

    origins = [
        "*",
    ]

    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    @app.get("/")
    def hello_world():
        return {"Hello": "World"}

    app.include_router(movie_router, tags=["Movies"], prefix="/api")
    return app
