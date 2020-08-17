import asyncio
import json
from channels.consumer import AsyncConsumer
from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'index.html')

class TestConsumer(AsyncConsumer):

    async def websocket_connect(self, event):
        await self.send({
            "type" : "websocket.accept",
        })

        await self.send({
            "type" : "websocket.send",
            'text':"Hello World"
        })
        print('Connected', event)

    async def websocket_recieve(self, event):
        print('recieved', event)

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