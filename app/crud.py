from .models import User
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

async def list_users(db: AsyncSession):
    result = await db.execute(select(User))
    return result.scalars().all()
