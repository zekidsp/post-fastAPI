from fastapi import FastAPI, Response, status, HTTPException
from pydantic import BaseModel  
from typing import Optional
from random import randrange


app = FastAPI()

@app.get("/posts")
async def get_posts():
    return {"data": my_posts}


my_posts = [
    {"title": "title1", "content": "content1", "id": 1},
    {"title": "title2", "content": "content2", "id": 2},
]

class Post(BaseModel):
    title: str
    description: str 
    published: Optional[bool] = True
    rating: Optional[int] = None 

@app.post("/posts", status_code=status.HTTP_201_CREATED)
def create_posts(post: Post):
    post_dict = post.dict()
    post_dict["id"] = randrange(0, 10**6)
    my_posts.append(post_dict)

    return {"data": post_dict} 

def find_post(id):
    for p in my_posts:
        if p["id"] == id:
            return p 

def find_post_index(id):
    for i, p in enumerate(my_posts):
        print(i)
        if p["id"] == id:
            return i



@app.get("/posts/latest")
def get_latest_post():
    post = my_posts[len(my_posts)-1]
    return {"message": post}


@app.get("/posts/{id}")
def get_post(id: int, response: Response):
    post = find_post(id)
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"the post with the id : {id} was not found" )
    return {"message": post}

@app.delete("/posts/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_posts(id: int):
    index = find_post_index(id)
    if index == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"the post with the id : {id} was not found" )

    my_posts.pop(index)
    return Response(status_code=status.HTTP_204_NO_CONTENT) 

@app.put("/posts/{id}")
def update_post(id: int, post: Post):
    index = find_post_index(id)
    if index == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"the post with the id : {id} was not found" )
    post_dict = post.dict()
    post_dict["id"] = id
    my_posts[index] = post_dict 
    return {"data": post_dict}
    


