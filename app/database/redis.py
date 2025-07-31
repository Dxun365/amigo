import sys
from redis import AuthenticationError
from redis.asyncio import Redis
from app.core.settings import REDIS_HEALTH_CHECK_INTERVAL, REDIS_HOST, REDIS_PASSWORD, REDIS_PORT, REDIS_DEFAULT_DB, REDIS_SOCKET_KEEPALIVE, REDIS_SOCKET_TIMEOUT


class RedisClient(Redis):
    def __init__(self, db: int = REDIS_DEFAULT_DB) -> None:
        super(RedisClient, self).__init__(
            db=db,
            host=REDIS_HOST,
            port=REDIS_PORT,
            password=REDIS_PASSWORD,
            socket_timeout=REDIS_SOCKET_TIMEOUT,
            socket_keepalive=REDIS_SOCKET_KEEPALIVE,
            health_check_interval=REDIS_HEALTH_CHECK_INTERVAL,
        )

    async def open(self) -> None:
        try:
            await self.ping()
        except TimeoutError:
            print('[!] redis connect timeout error...')
            sys.exit()
        except AuthenticationError:
            print('[!] redis authentication error...')
            sys.exit()
        except Exception as e:
            print(f'[!] redis connection exception ... error cause : {e}')
            sys.exit()


RedisDB: RedisClient = RedisClient()



