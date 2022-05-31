from fastapi import FastAPI

from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

@app.get("/")
def hello_world():
    return {"hello":"world"}

origins = [
    "http://localhost",
    "http://localhost:8080",
    "*",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

