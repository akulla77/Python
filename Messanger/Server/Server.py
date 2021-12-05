from aiohttp import web


routes = web.RouteTableDef()




if __name__ == '__main__':
    app = web.Application()
    app.add_routes(routes)
    web.run_app(app)