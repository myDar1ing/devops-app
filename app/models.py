from sqlalchemy.orm import DeclarativeBase, mapped_column
from sqlalchemy import Integer, String

class Base(DeclarativeBase):
    pass

class User(Base):
    __tablename__ = "users"
    id   = mapped_column(Integer, primary_key=True, index=True)
    name = mapped_column(String(50), unique=True, nullable=False)
