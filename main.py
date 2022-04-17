import uvicorn
from fastapi import FastAPI, Request, Response



app = FastAPI()



@app.get("/")
def read_root():
    return {"Hello": "World"}


if __name__ == "__main__":

    uvicorn.run("main:app", host="::", port=8000)
