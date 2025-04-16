# app/crud/users.py
from sqlmodel import select, Session
from app.models import User, UserRead

def get_user(db: Session, user_id: int) -> UserRead | None:
    user = db.get(User, user_id)
    return UserRead.from_orm(user) if user else None

def create_user(db: Session, user: User) -> UserRead:
    db.add(user)
    db.commit()
    db.refresh(user)
    return UserRead.from_orm(user)

def get_all_users(db: Session) -> list[UserRead]:
    users = db.exec(select(User)).all()
    return [UserRead.from_orm(user) for user in users]


def delete_user(db: Session, user_id: int) -> Session:
    db_user = db.get(User, user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    
    db.delete(db_user)  # Delete the user from the session
    db.commit()  # Commit the changes to the database
    
    return db_user