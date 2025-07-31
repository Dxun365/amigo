import pathlib

BASE_DIR = pathlib.Path(__file__).resolve().parent.parent # 项目基础目录

PG_DB_DRIVERNAME: str = 'postgresql+asyncpg' # postgre sql 数据库驱动

MY_DB_DRIVERNAME: str = 'mysql+asyncmy' # MySQL 数据库驱动

DB_TYPE: str = 'postgres'

DB_NAME: str = 'amigo_db'

DB_USER: str = 'amigo'

DB_PASS: str = 'amigo123456'

DB_HOST: str = '0.0.0.0'

DB_PORT: int = 5432

DB_AUTO_FLUSH: bool = True

DB_POOL_SIZE: int = 10

DB_TIMEOUT: int = 30

DB_RECYCLE: int = 3600

DB_PRE_PING: bool = True

DB_USE_LIFO: bool = False

DB_EXPIRE_ON_COMMINT: bool = False

DB_ECHO: bool = False

DB_FUTURE: bool = True

DB_ECHO_POOL: bool = True

REDIS_HOST: str = '0.0.0.0'

REDIS_PORT: int = 6379

REDIS_PASSWORD: str = 'redis_client123456'

REDIS_DEFAULT_DB: int = 0

REDIS_CONNECT_TIMEOUT: int = 60

REDIS_SOCKET_KEEPALIVE: bool = True

REDIS_SOCKET_TIMEOUT: int = 60

REDIS_HEALTH_CHECK_INTERVAL: int = 30

CACHEDB_1: int = 1

CACHEDB_2: int = 2
