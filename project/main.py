from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def reat_root():
    return {"message": "Welcome! to my FastAPI app"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "query": q}

@app.post("/create-item/")
def create_item(item: dict):
    return {"item_created": item}