from fastapi import FastAPI

app = FastAPI()

@app.get("/dehmovlaei")
def read_root():
    return{"hello": "world"}