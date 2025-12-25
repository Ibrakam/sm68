from fastapi import FastAPI
from api.comment_api import comment_router
from api.user_api import user_router
from api.post_api import post_router
from database import Base, engine

app = FastAPI(docs_url="/")

Base.metadata.create_all(engine)


app.include_router(user_router)
app.include_router(comment_router)
app.include_router(post_router)



