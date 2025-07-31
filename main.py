import uvicorn
from app import create_app


def main() -> None:
    try:
        uvicorn.run(create_app(), host='0.0.0.0', port=9331)
    except Exception:
        raise


if __name__ == '__main__':
    main()

