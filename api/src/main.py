import os

from fastapi import FastAPI

from endpoints import insurance
from database.db import init_db

app = FastAPI(
    debug=True,
    title="Insurance",
    docs_url="/api/docs",
    openapi_url="/api/openapi.json",
)

init_db(app)

app.include_router(insurance.router)


