from database import get_db
from database.models import User
from schemas import UserSchema




def create_user_db(user: UserSchema):
    db = next(get_db())
    user_data = user.model_dump()
    new_user = User(**user_data)
    db.add(new_user)
    db.commit()
    return True


def get_all_or_exact_user_db(uid=0):
    db = next(get_db())
    if uid:
        exact_user = db.query(User).filter_by(id=uid).first() #User(id=1)
        if exact_user:
            return exact_user
        return False
    all_users = db.query(User).all() #(User(id=1, name=sdflkjsdf), User(id=2))
    print(type(all_users))
    return all_users


def update_user(uid, change_info, new_info):
    db = next(get_db())
    exact_user = get_all_or_exact_user_db(uid)
    if exact_user:
        if change_info == "name":
            exact_user.name = new_info
        elif change_info == "surname":
            exact_user.surname = new_info
        elif change_info == "email":
            exact_user.email = new_info    
        elif change_info == "password":
            exact_user.password = new_info
        elif change_info == "username":
            exact_user.username = new_info
        elif change_info == "date_of_birth":
            exact_user.date_of_birth = new_info      
        db.commit()
        return True
    return False


