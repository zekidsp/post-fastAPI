from enum import Enum
from typing import Optional, List
from fastapi import FastAPI, Query, Path, Body

from pydantic import BaseModel, Field, HttpUrl 
from typing import Optional
app = FastAPI()


"""
@app.get("/")
async def root():
    return {"message": "hello world!"}


@app.post("/")
async def post():
    return {"message": "hello world from the post route"}

@app.put("/")
async def put():
    return {"message": "hello world from the put route"}

@app.get("/users")
async def list_users():
    return {"message": "list users route"} 

@app.get("/users/me")
async def get_current_user():
    return {"message": "this is the current user"}

@app.get("/users/{user_id}")
async def get_user(user_id: str):
    return {"user_id": user_id}

class FoodEnum(str, Enum):
    fruits = "fruits"
    vegetables = "vegetables"
    dairy = "dairy"



@app.get("/foods/{food_name}")
async def get_food(food_name: FoodEnum):
    if food_name == FoodEnum.fruits:
        return {"food_name": food_name,
                "message": "I like fruit but it has sugar"}
    
    if food_name.value == "vegetables":
        return {"food_name": food_name,
                "message": "your are healty"}
    
    return {"food_name": food_name,
            "message": "your are fresh"}
 
fake_item_db = [{"item_name": "foo"}, {"item_name": "alo"}, {"item_name": "hey"}]

@app.get("/items")
async def list_item(skip: int = 0, limit: int = 10):
    return fake_item_db[skip : skip + limit]

@app.get("/items/{item_id}")
async def get_item(item_id: str, q: Optional[str] = None):
    if q:
        return {"item_id": item_id, "q": q}
    return {"item_id": item_id}

class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: int
    tax: Optional[float] = None

@app.post("/items")
async def create_item(item: Item):
    item_dict = item.dict()
    if item.tax:
        price_with_tax = item.price + item.tax 
        item_dict.update({"price_with_tax": price_with_tax})
    return item_dict

@app.put("/items/{item_id}")
async def create_item_with_put(item_id: int, item: Item, q: Optional[str] = None):
    result = {"item_id": item_id, **item.dict()}
    if q:
        result.update({"q": q})
    return result 

@app.get("/items2")
async def read_items(q: Optional[list[str]] = Query(None)):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results  

@app.get("/items_validation/{item_id}")
async def read_items_validation(
    *,
    item_id: int = Path(..., title="The ID of the item to get", ge=1000, le=100),
    q: str
):
    results = {"item_id": item_id}
    if q:
        results.update({"q": q})
    return results


"""

"""
Part 7 -> Body - Multiple Parameters
"""

"""
class Item(BaseModel):
    name: str
    description: Optional[str] = None 
    price: float
    tax : Optional[float] = None

class User(BaseModel):
     username: str
     full_name: Optional[str] = None 

@app.put("/items/{item_id}")
async def update_item(
        *,
        item_id: int = Path(..., title="The ID of the item", ge=0, le=150),
        q: Optional[str] = None,
        item: Optional[Item] = None,
        user: User,
        importance: int = Body(...)):

        results = {"item_id": item_id}
        if q:
            results.update({"q": q}) 
        if item:
            results.update({"item": item})
        if user:
             results.update({"user": user})
        if importance:
             results.update({"importance": importance})
        return results
      
"""

### Part 8 --> Body- Field 


""" class Item(BaseModel):
    name: str
    desription: Optional[str] = Field(None, title="description of the item", max_length=130)
    price: float = Field(..., gt=0, description="The price must be greater than zero")
    tax: Optional[float] = None 


@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item = Body(..., embed=True)):
    results = {"item_id": item_id, "item": item}
    return results  """


## Part 9 --> Body - Nested Models

class Image(BaseModel):
    url: HttpUrl 
    name: str

class Item(BaseModel):
    name: str
    desription: Optional[str] = None
    price: float
    tax: Optional[str] = None
    tags: set[str] = set()
    image: Optional[Image] = None

@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item):
    results = {"item_id": item_id, "item": item}
    return results 


