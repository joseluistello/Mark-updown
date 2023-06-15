from typing import Optional
from fastapi import FastAPI, status, Response
from enum import Enum

app = FastAPI()

@app.get("/hello")
def index():
    return {"message": "Hello, World!"}

### Order matters :) ###

# @app.get('/blog/all')
# def get_all_blogs():
#    return {'message': 'You are reading all blogs'}


@app.get(
        '/blog/all',
        tags=['blog'],
        summary='Get all blogs from web',
        description='Get all blogs from the database',
        response_class=Response,
        response_description='List of blogs'
        )
def get_all_blogs(page = 1 , page_size: Optional[str] = None):
    return {'message': f'You are reading page {page} with size {page_size}'}

@app.get('/blog/{id}/comments/{comment_id}', tags=['blog', 'comment'])
def get_comment(id: int, comment_id: int, valid: bool = True, username: Optional[str] = None):
    """
    Recupera los detalles de un artículo según su ID.

    Parámetros:
    - **item_id**: El ID del artículo a recuperar.
    - **q**: Una cadena de búsqueda opcional que debe estar en el título del artículo.
    - **short**: Si se establece en 1, devuelve solo la versión corta del artículo.
    """
    return {'message': f'blog_id {id}, comment_id {comment_id}, valid {valid}, username {username}'}

class BlogType(str, Enum):
    short: str = 'short'
    story: str = 'story'
    howto: str = 'howto'

@app.get('/blog/type/{type}', tags=['blog'])
def get_blog_type(type: BlogType):
    return {'message': f'You are reading a {type} blog'}


@app.get('/blog/{id}', status_code=status.HTTP_200_OK, tags=['blog'])
def get_blog(id: int, response: Response):
    if id >= 5:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {'error': f'Blog with id {id} not found'}
    else:
        response.status_code = status.HTTP_200_OK
        return {'message': f'You are reading blog {id}'}