from tortoise import BaseDBAsyncClient


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        CREATE TABLE IF NOT EXISTS "insurancebase" (
    "id" UUID NOT NULL  PRIMARY KEY,
    "cargo_type" VARCHAR(255) NOT NULL,
    "base_value" DECIMAL(5,2) NOT NULL,
    "start_date" DATE NOT NULL,
    "end_date" DATE NOT NULL
);
CREATE TABLE IF NOT EXISTS "aerich" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "version" VARCHAR(255) NOT NULL,
    "app" VARCHAR(100) NOT NULL,
    "content" JSONB NOT NULL
);"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        """
