from typing import Any, Union, Dict, List
from enum import Enum

from fastapi import FastAPI, Body, Query
from fastapi.responses import HTMLResponse

from pydantic import BaseModel

app = FastAPI()

class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"
    mandaravordinet = "ashkan"


class PageOption(str, Enum):
    page1 = 1
    page2 = 2
    page3 = 3
    page4 = 4


class BookName(str, Enum):
    python= "python"
    java = "java"


class User(BaseModel):
    id: int
    name: str
    age: int
    active: bool = True


@app.get("/", response_class=HTMLResponse)
def read_root():
    return """
        <html>
            <body>
                <h1> Salam </h1>
            </body>
        </html>
    """

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


@app.post("/items/")
def read_item(users: List[User], name: Any = Body(), q: Union[int, None] = None):
    return {"q": q, "result": users, "name": name}


@app.get("/models/{model_name}")
async def get_model(model_name: ModelName):
    if model_name == ModelName.alexnet:
        return {"model_name": model_name, "message": "Deep Learning FTW!"}

    if model_name.value == "lenet":
        return {"model_name": model_name, "message": "LeCNN all the images"}

    return {"model_name": model_name, "message": "Have some residuals"}


@app.get("/book/{book_name}/{page_number}/")
async def get_model(book_name: BookName, page_number: PageOption):
    if book_name == BookName.python:
        return {"book_name": book_name, "page": page_number, "framework": "Django"}

    return {"book_name": book_name, "page": page_number}


@app.get("/tmp/{file_path:path}")
async def read_file(file_path: str):
    with open(f"/tmp/{file_path}") as f:
        print(f.readlines())
    return {"file_path": file_path}


@app.get("/items/")
async def read_items(q: Union[List[str], None] = Query(default=..., alias="item-parameter", min_length=3)):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results