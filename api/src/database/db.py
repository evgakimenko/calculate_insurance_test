import os

from fastapi import FastAPI
from tortoise.contrib.fastapi import register_tortoise

db_user = os.getenv('POSTGRES_DB_USER')
db_password = os.getenv('POSTGRES_DB_PASSWORD')
db_host = os.getenv('POSTGRES_DB_HOST')
db_port = os.getenv('POSTGRES_DB_PORT')
db_url = f'postgres://{db_user}:{db_password}@{db_host}:{db_port}/postgresdb'
TORTOISE_ORM_CONFIG = {
    "connections": {"default": db_url},
    "apps": {
        "models": {
            "models": ["models.models", "aerich.models"],
            "default_connection": "default",
        },
    },
}

def init_db(app: FastAPI) -> None:
    register_tortoise(
        app,
        config=TORTOISE_ORM_CONFIG,
        generate_schemas=True,
        add_exception_handlers=True,
    )