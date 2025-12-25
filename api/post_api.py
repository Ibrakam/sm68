from typing import Optional

from fastapi import APIRouter
from pydantic import BaseModel

from api import get_result_message
from database.postservice import (
    create_post,
    get_user_posts,
    get_all_posts,
    get_post,
    update_post,
    delete_post,
)

post_router = APIRouter(prefix="/post")


class PostCreate(BaseModel):
    main_text: str
    uid: int


class PostUpdate(BaseModel):
    main_text: str


@post_router.post("/add_post")
async def add_post_api(data: PostCreate):
    post = create_post(main_text=data.main_text, uid=data.uid)
    return get_result_message(post)


@post_router.get("/get_post")
async def get_post_api(pid: Optional[int] = None, uid: Optional[int] = None):
    if pid is not None:
        post = get_post(pid)
        return get_result_message(post)
    if uid is not None:
        posts = get_user_posts(uid)
        return get_result_message(posts)
    posts = get_all_posts()
    return get_result_message(posts)


@post_router.put("/update_post")
async def update_post_api(pid: int, data: PostUpdate):
    result = update_post(pid, data.main_text)
    return get_result_message(result)


@post_router.delete("/delete_post")
async def delete_post_api(pid: int):
    result = delete_post(pid)
    return get_result_message(result)