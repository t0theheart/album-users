from abc import ABC, abstractmethod


class UsersABC(ABC):
    @classmethod
    @abstractmethod
    async def start(cls): pass

    @abstractmethod
    async def check_user(self, login: str, password: str) -> bool: pass
