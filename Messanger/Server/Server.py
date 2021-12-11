from typing import List
from aiohttp.web_response import Response
from asyncpg import connection
from User import User
from Message import Message
from ContentType import ContentType
import requests
import json

from aiohttp import web
import psycopg2
messages = [Message]

routes = web.RouteTableDef()

# @routes.post('/add')
# async def add():
messages = [Message]


def first():

        u1 = User('1','p')
        u2 = User('2','p')
        m = Message('t\i',u1,u2,ContentType.TEXT)
        messages.append(m)


@routes.get('/')
async def root(_) -> web.Response:
    mm = messages.pop()
    mmj = mm.to_json()
    print(str(mmj))
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
    first()

    app = web.Application()
    app.add_routes(routes)
    web.run_app(app,host ='localhost',port=3333)