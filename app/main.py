from fastapi import FastAPI, Depends
from .database import get_db, engine
from .models import Base
from .crud import list_users
from . import seed 

app = FastAPI(title="Demo Web App")

@app.on_event("startup")
async def startup():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


@app.on_event("startup")
async def seed_if_needed():
    await seed.run()

@app.get("/")
async def home():
    return {"msg": "Hello, world v2.  Ships to prod before your coffee cools ☕️"}

@app.get("/users")
async def users(db=Depends(get_db)):
    return await list_users(db)


