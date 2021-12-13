from aiohttp.web_response import Response
from asyncpg import connection
from User import User
from Mess import Mess
import requests
import json
from datetime import datetime
from aiohttp import web
import psycopg2
from MesD import MesD
from py_linq import Enumerable


messages= Enumerable([])

routes = web.RouteTableDef()

# возвращаем свободных пользователей
# для отправки полный список исключа себя
Users = {
    'Nick': 1,
    'Zack': 1,
    'John': 1,
    'Ann': 1
}




@routes.post('/send')
async def sendMessage(request: web.Request)->web.Response:
    
    data = dict(await request.json())
    src = data['src']
    dest = data['dest']
    text = data['text']
    time = data['time']

    messages.append(Mess(text,src,dest,time))
    
    return web.HTTPOk()



@routes.get('/messages')
async def GetMessages(request: web.Request)-> web.Response:
    data = dict(await request.json())
    after = data['after']   
    src = data['src']
    dest = data['dest']
    if  after == 0:
        # after = datetime.min.strftime( "%m/%d/%Y, %H:%M:%S")
        after = datetime.min
    else:
        after= datetime.strptime(after, '%Y-%m-%d %H:%M:%S.%f')

    t = []

    for m in messages.order_by(lambda x: x.Time).to_list():
        if datetime. strptime(m.Time, '%Y-%m-%d %H:%M:%S.%f')> after:
            if (m.Src == src and m.Dest == dest) or (m.Src == dest and m.Dest==src):
             t.append(m.to_json())

    print(t)  
    return web.json_response(t)



@routes.get('/contacts')
async def GetConatcts(request: web.Request)-> web.Response:
    f = []
    data = dict(await request.json())
    user = data['user']
    for key in Users.keys():
        if key != user:
            f.append(str(key))
    
    print (f)
    return web.json_response(f)




@routes.post('/userRefresh')
async def RefreshUser(request: web.Request)-> web.Response:
    data = dict(await request.json())
    user = data['user']
    if  user != '':
        Users[user] = 1

    return web.HTTPOk()

@routes.post('/user')
async def ChooseUser(request: web.Request) ->  web.Response:
    data = dict(await request.json())
    user = data['user']
    Users[user] = 0

    return web.HTTPOk()



@routes.get('/users')
async def getUsers(request: web.Request)-> web.Response:
    
    f = []
    
    for key , value in Users.items():
        if value == 1:
            f.append(str(key))
    
    print (f)
    return web.json_response(f)



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
    for i in range(3):
        messages.append(Mess(str(i),'1','2',str(datetime.now())))

    app = web.Application()
    app.add_routes(routes)
    app['storage'] = connect_to_db()
    web.run_app(app,host ='localhost',port=3333)