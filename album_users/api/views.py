from aiohttp import web
from album_users.api.serializers.request import LoginRequest


routes = web.RouteTableDef()


@routes.post('/album-users/login')
async def login(request):
    data = LoginRequest().load(await request.json())
    print(data)
    return web.json_response(data={'result': 123}, headers={'Access-Control-Allow-Origin': '*'})
