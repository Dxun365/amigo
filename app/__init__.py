from fastapi import FastAPI


def create_app(mode: bool = False) -> FastAPI:
    app = FastAPI()
    return app

