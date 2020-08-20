import asyncio

import asyncpg

from data import config


class Database:
    def __init__(self, loop: asyncio.AbstractEventLoop):
        self.pool: asyncio.pool.Pool = loop.run_until_complete(
            asyncpg.create_pool(
                user=config.PG_USER,
                password=config.PG_PASS,
                host=config.host
            )
        )

    async def create_table_users(self):
        sql = """
        CREATE TABLE IF NOT EXISTS Users (
        id SERIAL PRIMARY KEY,
        name VARCHAR(255) NOT NULL,
        phone_number VARCHAR(20) NOT NULL,
        region VARCHAR(30) NOT NULL,
        corruption BOOLEAN NOT NULL,
        feedback TEXT
        )
        """
        await self.pool.execute(sql)

    @staticmethod
    def format_args(sql, parameters: dict):
        sql += " AND ".join([
            f"{item} = ${num}" for num, item in enumerate(parameters, start=1)
        ])
        return sql, tuple(parameters.values())

    async def add_user(self, name: str, phone_number: str, region: str, corruption: bool,
                       feedback: str = None):
        sql = "INSERT INTO Users (name,phone_number,region,corruption,feedback) VALUES ($1,$2,$3,$4,$5)"
        try:
            await self.pool.execute(sql, name, phone_number, region, corruption, feedback)
        except asyncpg.exceptions.UniqueViolationError:
            pass

    async def select_all_users(self):
        sql = "SELECT * FROM Users"
        return await self.pool.fetch(sql)

    async def select_user(self, **kwargs):
        sql = "SELECT * FROM Users WHERE "
        sql, parameters = self.format_args(sql, kwargs)
        return await self.pool.fetchrow(sql, *parameters)

    async def count_users(self):
        return await self.pool.fetchval("SELECT COUNT(*) FROM Users")
