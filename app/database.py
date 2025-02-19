import logging

from sqlalchemy import URL
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine

from app.config import settings

db_url_object = URL.create(
    drivername=settings.db_driver,
    username=settings.db_user,
    password=settings.db_password.get_secret_value(),
    host=settings.db_host,
    database=settings.db_name,
    port=settings.db_port,
)

logging.info("Using db url: %s", db_url_object.render_as_string(hide_password=True))
engine = create_async_engine(db_url_object, echo=False, future=True)


async def get_session() -> AsyncSession:
    """Returns the async session object to use for db queries"""
    async_session = async_sessionmaker(engine, expire_on_commit=False, autocommit=False)
    async with async_session() as session:
        yield session
