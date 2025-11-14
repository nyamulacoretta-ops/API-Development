import fastapi
from fastapi import FastAPI, Body

app = FastAPI()
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
def create_post(name: dict = Body(...)):
    print(name)
    return {"new_post": f"title {name['title']} content {name['content']}"}
    return {"message": "Successfully created post"}