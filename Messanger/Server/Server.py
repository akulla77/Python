from aiohttp.web_response import Response
from Mess import Mess
import requests
import json
from datetime import datetime
from aiohttp import web
from py_linq import Enumerable


messages= Enumerable([])

routes = web.RouteTableDef()

# возвращаем свободных пользователей
# для отправки полный список исключая себя
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
 
    return web.json_response(t)



@routes.get('/contacts')
async def GetConatcts(request: web.Request)-> web.Response:
    f = []
    data = dict(await request.json())
    user = data['user']
    for key in Users.keys():
        if key != user:
            f.append(str(key))

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

    return web.json_response(f)







if __name__ == '__main__':
    
    app = web.Application()
    app.add_routes(routes)
    web.run_app(app,host ='localhost',port=3333)