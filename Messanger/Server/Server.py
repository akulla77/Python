from aiohttp import web
import asyncpg


routes = web.RouteTableDef()


@routes.get('/')
async def root(_) -> web.Response:
    print(web.HTTPOk)
    raise web.HTTPOk











if __name__ == '__main__':
    app = web.Application()
    app.add_routes(routes)
    web.run_app(app,host ='localhost',port=3333)