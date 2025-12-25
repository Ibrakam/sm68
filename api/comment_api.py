from fastapi import APIRouter
from database.commentservice import *
from api import get_result_message

comment_router = APIRouter(prefix="/comment")

@comment_router.post("/add")
async def add_comment_api(uid: int, post_id: int, text: str):
    result = add_comment_db(uid, post_id, text)
    return get_result_message(result)

@comment_router.get("/post")
async def get_post_comments_api(post_id: int):
    result = get_all_post_comments_db(post_id)
    return get_result_message(result)

@comment_router.get("/user")
async def get_user_comments_api(uid: int):
    result = get_all_user_comments_db(uid)
    return get_result_message(result)

@comment_router.get("/get")
async def get_exact_comment_api(comment_id: int):
    result = get_exact_comment_db(comment_id)
    return get_result_message(result)

@comment_router.put("/update")
async def update_comment_api(comment_id: int, new_text: str):
    result = update_comment_db(comment_id, new_text)
    return get_result_message(result)

@comment_router.delete("/delete")
async def delete_comment_api(comment_id: int):
    result = delete_comment_db(comment_id)
    return get_result_message(result)