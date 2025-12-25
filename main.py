from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from api.comment_api import comment_router
from api.user_api import user_router
from api.post_api import post_router
from database import Base, engine
from database.postservice import get_all_posts
from database.userservice import get_all_or_exact_user_db

app = FastAPI(docs_url="/docs")
templates = Jinja2Templates(directory="templates")

Base.metadata.create_all(engine)


app.include_router(user_router)
app.include_router(comment_router)
app.include_router(post_router)



@app.get("/{uid}", response_class=HTMLResponse)
async def main(request: Request, uid: int):
    all_posts = get_all_posts()
    user = get_all_or_exact_user_db(uid=uid)
    return templates.TemplateResponse(request=request, name="index.html", 
    context={"all_posts": all_posts, "user": user})


@app.get("/", response_class=HTMLResponse)
async def users(request: Request):
    users = get_all_or_exact_user_db(uid=0)
    return templates.TemplateResponse(request=request, name="users.html", 
    context={"users": users})

# uvicorn main:app --reload


