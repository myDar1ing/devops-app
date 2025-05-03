"""
Seed the database with initial data.
Call this once at deploy—or every start-up, it’s idempotent.
"""
import asyncio
from sqlalchemy import select, insert
from .database import engine, AsyncSessionLocal
from .models import User


SEED_DATA = [
    {"name": "Ada Lovelace"},
    {"name": "Grace Hopper"},
    {"name": "Linus Torvalds"},
]


async def run():
    async with AsyncSessionLocal() as db:
        existing = (
            await db.execute(select(User).limit(1))
        ).scalars().first()
        if existing:
            return

        await db.execute(insert(User), SEED_DATA)
        await db.commit()
        print("🌱  Seeded the users table.")


if __name__ == "__main__":
    asyncio.run(run())
