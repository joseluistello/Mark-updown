from typing import Optional
from fastapi import FastAPI
from enum import Enum

app = FastAPI()

@app.get("/hello")
def index():
    return {"message": "Hello, World!"}

### Order matters :) ###

# @app.get('/blog/all')
# def get_all_blogs():
#    return {'message': 'You are reading all blogs'}


@app.get('/blog/all')
def get_all_blogs(page = 1 , page_size: Optional[str] = None):
    return {'message': f'You are reading page {page} with size {page_size}'}

@app.get('/blog/{id}/comments/{comment_id}')
def get_comment(id: int, comment_id: int, valid: bool = True, username: Optional[str] = None):
    return {'message': f'blog_id {id}, comment_id {comment_id}, valid {valid}, username {username}'}

class BlogType(str, Enum):
    short: str = 'short'
    story: str = 'story'
    howto: str = 'howto'

@app.get('/blog/type/{type}')
def get_blog_type(type: BlogType):
    return {'message': f'You are reading a {type} blog'}


@app.get('/blog/{id}')
def get_blog(id: int):
    return {'message': f'You are reading blog {id}'}
