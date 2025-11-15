from typing import Optional

import fastapi
from fastapi import FastAPI, Body
from pydantic import BaseModel

app = FastAPI()


class Post(BaseModel):
    title: str
    content: str
    published: bool = False
    rating: Optional[float] = None

#path operation or route
@app.get("/")  #this decorator makes the function to api. get is http method
#It is function so we add async because we will do asynchronous coding
#this function logins a user
async def root():
    return {"message": "Welcome to my API"}# It will be converted to json, language of api

@app.get("/posts")
def get_posts():
    return {"data": "This is your post"}

@app.post("/createpost")
def create_post(new_post: Post):
    print(new_post.rating)
    return {"data": "This is your post"}

    # you can also translate a pydantic model into a dictionary
    # print(new_post.dict()) to list all the dictionaries


