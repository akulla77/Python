from aiohttp import web
from asyncpg import connection

import psycopg2


routes = web.RouteTableDef()




@routes.get('/')
async def root(_) -> web.Response:
    print(web.HTTPOk)
    raise web.HTTPOk



def connect_to_db():
    try:
        conn = psycopg2.connect( host="localhost",
        database="Test",
        user="postgres",
        password='Tumbochka1' )

        cur = conn.cursor()
        cur.execute('SELECT version()')
        db_version = cur.fetchone()
        print(db_version)
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
       



if __name__ == '__main__':
    
    connect_to_db()


    app = web.Application()
    app.add_routes(routes)
    web.run_app(app,host ='localhost',port=3333)