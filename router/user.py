from schemas import UserBase, UserDisplay
from fastapi import APIRouter, Depends
from sqlalchemy.orm.session import Session
from db.database import get_db
from db import db_user

router = APIRouter(
    prefix='/user',
    tags=['user']
)


@router.post('/', response_model=UserDisplay)
def create_user(request: UserBase, db: Session = Depends(get_db)): 
    return db_user.create_user(db, request)

# Read all users
@router.get('/', response_model=list[UserDisplay])
def get_all_users(db: Session = Depends(get_db)):
    return db_user.get_all_users(db)

# Read one user
@router.get('/{id}', response_model=UserDisplay)
def get_specific_user(id: int, db: Session = Depends(get_db)):
    return db_user.get_specific_user(id, db)

# Update user
@router.put('/{id}', response_model=UserDisplay)
def update_user(id: int, request: UserBase, db: Session = Depends(get_db)):
    return db_user.update_user(id, request, db)