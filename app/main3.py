from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware

from . import models
from .database import engine, get_db
from sqlalchemy.orm import Session
from .routers import post, user, auth, vote
from .config import settings
    

print(settings.database_password) 


#models.Base.metadata.create_all(bind=engine)

app = FastAPI()

origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


    

my_post = [{"title": "title of post 1", "content": "content of post 1", "id": 1},
           {"title": "favorite food", "content": "pizza", "id": 2}]


def find_post(id):
    for p in my_post:
        if p['id'] == id:
            return p
        
def find_index_post(id):
    for i, p in enumerate(my_post):
        if p['id'] == id:
            return i


app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)
app.include_router(vote.router)


@app.get("/")
async def root():
    return {"message": "Hello World!!! welocme"}

@app.get("/sqlalchemy")
def test_posts(db: Session = Depends(get_db)):
    posts = db.query(models.Post).all()
    return posts



# tutorial video where I left: 11:56 as of 2025.05.27: 
# pip install --upgrade bcrypt==4.1.1  , newer versiosn are not compatiple
    



