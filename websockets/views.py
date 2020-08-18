import asyncio
import json
from channels.consumer import AsyncConsumer
from django.shortcuts import render
import random

# Create your views here.
def pusher():
    data = [0, 0, 0, 0, 0]
    counter = 0
    while True:
        rand = random.randint(1, 4)
        if 0 in data:
            data[counter] = rand
            counter += 1
        else:
            del data[0]
            data.append(rand)
        yield data

put = pusher()

def home(request):
    return render(request, 'index.html')

class TestConsumer(AsyncConsumer):

    async def websocket_connect(self, event):
        await self.send({
            "type" : "websocket.accept",
        })

        while True:
            # This is where REDIS should come in
            await self.send({
                "type" : "websocket.send",
                'text': json.dumps(next(put))
            })
            await asyncio.sleep(3)



    async def websocket_receive(self, event):
        print('recieved', event)
        await self.send({
            'type' : 'websocket.send',
            'text' : event['text']
        })

    async def websocket_disconnect(self, event):
        print('Disconnected', event)

class ChartConsumer(AsyncConsumer):

    async def websocket_connect(self, event):
        await self.send({
            "type" : "websocket.accept"
        })

        await self.send({
            "type" : "websocket.send",
            "text": "Hello World"
        })