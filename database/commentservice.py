from database import get_db
from database.models import Comment

def add_comment_db(uid, post_id, text):
    db = next(get_db())
    new_comment = Comment(uid=uid, pid=post_id, text=text)
    db.add(new_comment)
    db.commit()
    return True

def get_all_post_comments_db(post_id):
    db = next(get_db())
    comments = db.query(Comment).filter_by(pid=post_id).all()
    return comments

def get_all_user_comments_db(uid):
    db = next(get_db())
    comments = db.query(Comment).filter_by(uid=uid).all()
    return comments

def get_exact_comment_db(comment_id):
    db = next(get_db())
    exact_comment = db.query(Comment).filter_by(id=comment_id).first()
    if exact_comment:
        return exact_comment
    return False

def update_comment_db(comment_id, new_text):
    db = next(get_db())
    exact_comment = db.query(Comment).filter_by(id=comment_id).first()
    if exact_comment:
        exact_comment.text = new_text
        db.commit()
        return True
    return False

def delete_comment_db(comment_id):
    db = next(get_db())
    exact_comment = db.query(Comment).filter_by(id=comment_id).first()
    if exact_comment:
        db.delete(exact_comment)
        db.commit()
        return True
    return False