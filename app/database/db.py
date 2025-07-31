import sys

from typing import AsyncGenerator, Tuple, Annotated

from fastapi import Depends
from sqlalchemy import URL
from sqlalchemy.ext.asyncio import AsyncEngine, async_sessionmaker, AsyncSession, create_async_engine

from app.core.settings import DB_AUTO_FLUSH, DB_EXPIRE_ON_COMMINT, DB_HOST, DB_NAME, DB_PASS, DB_PORT, DB_TYPE, DB_USER, PG_DB_DRIVERNAME, MY_DB_DRIVERNAME


def create_database_uri(db_type: str = 'postgres') -> URL:
    uri = URL.create(
        drivername=PG_DB_DRIVERNAME if db_type == DB_TYPE else MY_DB_DRIVERNAME,
        host=DB_HOST,
        port=DB_PORT,
        database=DB_NAME,
        username=DB_USER,
        password=DB_PASS,
    )

    return uri


def create_engine_and_dbsession(url: str | URL) -> Tuple[AsyncEngine, async_sessionmaker[AsyncSession]]:
    try:
        engine = create_async_engine(
            url=url,
        )
    except Exception as e:
        print(f'[!] create async engine exception cause : {e}')
        sys.exit()
    else:
        db_session = async_sessionmaker(
            bind=engine,
            class_=AsyncSession,
            autoflush=DB_AUTO_FLUSH,
            expire_on_commit=DB_EXPIRE_ON_COMMINT,
        )
        return engine, db_session


async def get_db() -> AsyncGenerator[AsyncSession, None]:
    async with db_async_session() as session:
        yield session


db_async_engine, db_async_session = create_engine_and_dbsession(create_database_uri())

CurrentDBSession = Annotated[AsyncSession, Depends(get_db)]

