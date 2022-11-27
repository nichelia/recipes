from redis import asyncio as aioredis

from app import config

global_settings = config.Settings()


async def init_queue_pool() -> aioredis.Redis:
    queue_client = await aioredis.from_url(
        global_settings.queue_url,
        encoding="utf-8",
        db=global_settings.queue_db,
        decode_responses=True,
    )
    return queue_client