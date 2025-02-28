from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from app.database import engine
from app.models import create_db_and_tables
from app.routes.router import include_all_routers


@asynccontextmanager
async def lifespan(app: FastAPI):
    create_db_and_tables(engine)
    include_all_routers(app)
    yield
    engine.dispose()


app = FastAPI(lifespan=lifespan)

app.mount("/static", StaticFiles(directory="app/static"), name="static")
