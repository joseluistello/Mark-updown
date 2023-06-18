from typing import Optional
from fastapi import APIRouter, Query, Path, Body
from pydantic import BaseModel

router = APIRouter(
    prefix='/blog',
    tags=['blog']
)

class BlogModel(BaseModel):
    title: str
    content: str
    nb_comments: int
    published: bool 

@router.post('/new/{id}')
def create_blog(
    blog: BlogModel, 
    id: int, 
    version: int = 1
    ):
    return {
        'id': id,
        'data': blog,
        'version': version
        }

@router.post('/new{id}/comment')
def create_comment(blog: BlogModel, id: int, 
                   comment_id: int = Query(None,
                                           title= 'Id of the comment',
                                           description= 'Some description of the comment',
                                           alias= 'comment-id')
    ):
    return {
        'blog': blog,
        'id': id,
        'comment_id': comment_id
    }