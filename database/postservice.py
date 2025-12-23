from typing import List, Optional
from database import get_db
from database.models import UserPost


def create_post(main_text: str, uid: int) -> UserPost:
    db = next(get_db())
    post = UserPost(main_text=main_text, uid=uid)
    db.add(post)
    db.commit()
    db.refresh(post)
    return post


def get_user_posts(uid: int) -> List[UserPost]:
    db = next(get_db())
    return db.query(UserPost).filter_by(uid=uid).all()


def get_all_posts() -> List[UserPost]:
    db = next(get_db())
    return db.query(UserPost).all()


def get_post(pid: int) -> Optional[UserPost]:
    db = next(get_db())
    return db.query(UserPost).filter_by(id=pid).first()


def update_post(pid: int, main_text: str) -> bool:
    db = next(get_db())
    post = db.query(UserPost).filter_by(id=pid).first()
    if not post:
        return False
    post.main_text = main_text
    db.commit()
    return True


def delete_post(pid: int) -> bool:
    db = next(get_db())
    post = db.query(UserPost).filter_by(id=pid).first()
    if not post:
        return False
    db.delete(post)
    db.commit()
    return True