from db.hash import Hash
from sqlalchemy.orm.session import Session
from schemas import UserBase
from db.models import DbUser
import json

def create_user(db: Session, request: UserBase):
    new_user = DbUser(
        username = request.username, 
        email = request.email, 
        password = Hash.bcrypt(request.password)
        )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

def get_all_users(db: Session):
    return db.query(DbUser).all()

def get_specific_user(id: int, db: Session):
    user = db.query(DbUser).filter(DbUser.id == id).first()
    return user

# Update user
def update_user(id: int, request: UserBase, db: Session):
    user = db.query(DbUser).filter(DbUser.id == id).first()
    user.username = request.username
    user.email = request.email
    user.password = Hash.bcrypt(request.password)
    db.commit()
    db.refresh(user)
    return user