from fastapi import FastAPI
from src.database import engine, Base
from src.routers.users import router
from src.routers.articles import router as article_router


app = FastAPI(
  title="FastAPI Blog",
  # openapi_url="./openapi.json",
)

Base.metadata.create_all(bind=engine)

app.include_router(router)
app.include_router(article_router)
