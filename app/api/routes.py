from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session
from app.models import User, UserRead
from app.crud.users import get_user, create_user, delete_user, get_all_users
from app.core.database import get_db
router = APIRouter()

@router.post("/users/", response_model=UserRead)
def create_new_user(user: User, db: Session = Depends(get_db)):
    return create_user(db, user)

@router.get("/users/")
def read_users(db: Session = Depends(get_db)):
    return get_all_users(db)

@router.get("/users/{user_id}", response_model=UserRead)
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = get_user(db, user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

@router.delete("/users/{user_id}", response_model=UserRead)
def delete_user(user_id: int, db: Session = Depends(get_db)):
  # Return the deleted user as response (optional)
    return delete_user(db, user_id)