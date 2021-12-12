from typing import Any, Dict, List
from aiohttp.web_response import Response
from asyncpg import connection
from User import User
from Mess import Mess
import requests
import json
from datetime import datetime
from aiohttp import web
import psycopg2


messages = [Mess]

routes = web.RouteTableDef()



@routes.post('/send')
async def sendMessage(request: web.Request)->web.Response:
    
    data = dict(await request.json())
    name = data['name']
    text = data['text']
    messages.append(Mess(text,name,'2'))
    print(messages.pop())
    return web.HTTPOk()



@routes.get('/messages')
async def GetMessages(request: web.Request)-> Dict[str,Any]:

    data = dict(await request.json())
    after = data['after']   
    d= {'time': str(datetime.now()) ,'text':'message text','name':'Iliya'  }
    
    return d




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
        return cur
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
       



if __name__ == '__main__':
    app = web.Application()
    app.add_routes(routes)
    app['storage'] = connect_to_db()
    web.run_app(app,host ='localhost',port=3333)