import uvicorn
from fastapi import FastAPI, Request, Response



app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


if __name__ == "__main__":
    print("Heeelefalfae")
    uvicorn.run("main:app", host="0.0.0.0", port=8010)
