from aiohttp import web
from album_users.api.views import routes


app = web.Application()
app.add_routes(routes)
web.run_app(app)
# docker run -t -p 8080:8080 album_users
