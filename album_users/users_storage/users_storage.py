from .abc import UsersStorageABC
import asyncpg


class UsersStorage(UsersStorageABC):
    @classmethod
    async def connect(cls, dsn: str):
        cls.pool = await asyncpg.create_pool(dsn=dsn)
        return cls()

    async def get_user(self, login: str, password: str) -> dict:
        sql = f"""SELECT * FROM "USERS" WHERE "LOGIN" = '{login}' and "PASSWORD" = '{password}'"""
        async with self.pool.acquire() as con:
            result = await con.fetchrow(sql)
            return dict(result) if result else dict()
