from abc import ABC, abstractmethod


class UsersStorageABC(ABC):
    @classmethod
    @abstractmethod
    async def connect(cls, dsn: str): pass

    @abstractmethod
    async def get_user(self, login: str, password: str) -> dict: pass
