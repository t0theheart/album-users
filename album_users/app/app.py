from aiohttp import web
from album_users.api.views import routes
from album_users.users import Users


async def create_app():
    app = web.Application()
    app.add_routes(routes)
    app['users'] = await Users.start()
    return app


if __name__ == '__main__':
    app = create_app()
    web.run_app(app)
