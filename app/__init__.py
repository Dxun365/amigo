from fastapi import FastAPI

def register_api_routers(app: FastAPI) -> None:
    pass


def register_app_plugins(app: FastAPI) -> None:
    pass


def register_celery(app: FastAPI) -> None:
    pass


def register_middlewares(app: FastAPI) -> None:
    pass


def create_app(mode: bool = False) -> FastAPI:
    app = FastAPI()
    register_api_routers(app)
    register_middlewares(app)
    register_app_plugins(app)
    register_celery(app)
    return app


