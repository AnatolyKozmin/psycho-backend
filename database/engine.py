from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.ext.asyncio import (AsyncAttrs, 
                                    async_sessionmaker, 
                                    create_async_engine, 
                                    AsyncSession)

from config import database_url

engine = create_async_engine(url=database_url)
async_sessionmaker = async_sessionmaker(engine, class_=AsyncSession)


class Base(AsyncAttrs, DeclarativeBase):
    __abstract__= True