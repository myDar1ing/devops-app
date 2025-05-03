import os
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from sqlalchemy.engine.url import URL

db_uri = os.getenv("DATABASE_URL")
ASYNC_URL = db_uri.replace("postgresql://", "postgresql+asyncpg://", 1)
engine = create_async_engine(ASYNC_URL, echo=False, future=True)

AsyncSessionLocal = sessionmaker(bind=engine,
                                 class_=AsyncSession,
                                 expire_on_commit=False)

async def get_db():
    async with AsyncSessionLocal() as session:
        yield session
