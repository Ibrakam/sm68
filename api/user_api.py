from fastapi import APIRouter
from database.userservice import *
from schemas import UserSchema
from api import get_result_message


user_router = APIRouter(prefix="/user")


@user_router.post("/add_user")
async def add_user_api(user: UserSchema):
    result = create_user_db(user)
    return get_result_message(result)


@user_router.get("/get_users")
async def get_users_api(uid: int = 0):
    result = get_all_or_exact_user_db(uid)
    return get_result_message(result)
    


@user_router.put("/update_user")
async def update_user_api(uid: int, change_info: str, new_info: str):
    result = update_user(uid=uid, change_info=change_info, new_info=new_info)
    return get_result_message(result)












