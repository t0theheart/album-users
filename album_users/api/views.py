from aiohttp import web
from album_users.api.serializers import LoginRequest, LoginResponse


routes = web.RouteTableDef()


@routes.post('/login')
async def login(request):
    data = LoginRequest().load(await request.json())
    user = await request.app['users'].check_user(data['login'], data['password'])
    if user:
        return web.json_response(
            data={'result': LoginResponse().dump({'login': data['login']})},
            headers={'Access-Control-Allow-Origin': '*'}
        )
    return web.Response(status=403)
