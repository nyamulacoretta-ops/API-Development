from random import randrange
from typing import Optional

import fastapi
from fastapi import FastAPI, Body, Response, HTTPException,status
from pydantic import BaseModel

app = FastAPI()


class Post(BaseModel):
    title: str
    content: str
    rating: Optional[float] = None


#array
my_posts = [
    {"title": "post title", "content": "post content","id": 1},
    {"title": "My favourate colour", "content": "Color content", "id": 2 },
]

#path operation or route
@app.get("/")  #this decorator makes the function to api. get is http method
#It is function so we add async because we will do asynchronous coding
#this function logins a user
async def root():
    return {"message": "Welcome to my API"}# It will be converted to json, language of api

@app.get("/posts")
def get_posts():
    print(my_posts)
    return {"data": my_posts}

@app.post("/posts", status_code=status.HTTP_201_CREATED)
def create_post(post: Post):
    post_dict = post.dict()
    post_dict['id'] = randrange(0, 100000000)
    my_posts.append(post_dict)
    return {"data": post_dict}

    # you can also translate a pydantic model into a dictionary
    # print(new_post.dict()) to list all the dictionaries
def find_post(id: int) -> Optional[Post]:
    for p in my_posts:
        if p['id'] == id:
            return p
    return None

@app.post("/posts/1")
def latest_post(post: Post):
    var = my_posts[len(my_posts) - 1]
    return {"data": var}

    #@app.get("/posts/{id}")
#def get_post(id: int):
    print(id)
    return {"data": "{id}".format(id=id)}
@app.get("/posts/{id}")
def get_post(id: int, response: Response):
    post = find_post(id)
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Post with {id} not found")
    return {"data": post}
#to get latest post

@app.delete("/posts/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id: int, response: Response):
    post = find_post(id)
    if post:
        my_posts.remove(post)
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Post with {id} not found")
    #return{"message": "post with {id} was deleted".format(id=id)}
    return Response(status_code=status.HTTP_204_NO_CONTENT)

@app.put("/posts/{id}")
def update_post(id: int, post: Post):
    post_dict = find_post(id)
    updated_post = post.dict(exclude_unset=True)
    if not post_dict:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Post with {id} not found")
    else:
       post_dict.update(updated_post)

    return {"message": "Updated post with {id}".format(id=id)}




