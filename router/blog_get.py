from fastapi import APIRouter, status, Response
from enum import Enum
from typing import Optional

router = APIRouter(
    prefix='/blog',
    tags=['blog']
)


### Order matters :) ###

# @app.get('/blog/all')
# def get_all_blogs():
#    return {'message': 'You are reading all blogs'}

@router.get(
        '/all',
        summary='Get all blogs from web',
        description='Get all blogs from the database',
        response_class=Response,
        response_description='List of blogs'
        )
def get_all_blogs(page = 1 , page_size: Optional[str] = None):
    return {'message': f'You are reading page {page} with size {page_size}'}

@router.get('/{id}/comments/{comment_id}', tags=['comment'])
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

@router.get('/type/{type}')
def get_blog_type(type: BlogType):
    return {'message': f'You are reading a {type} blog'}


@router.get('/{id}', status_code=status.HTTP_200_OK)
def get_blog(id: int, response: Response):
    if id >= 5:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {'error': f'Blog with id {id} not found'}
    else:
        response.status_code = status.HTTP_200_OK
        return {'message': f'You are reading blog {id}'}