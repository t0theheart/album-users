from .abc import UsersABC
from album_users.users_storage import UsersStorage


class Users(UsersABC):
    @classmethod
    async def start(cls):
        cls.storage = await UsersStorage.connect('postgresql://user:password@postgres:5432/users')
        return cls()

    async def check_user(self, login: str, password: str) -> bool:
        user = await self.storage.get_user(login, password)
        if user.get('ID'):
            return True
