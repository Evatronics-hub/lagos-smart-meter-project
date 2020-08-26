import asyncio
import json
import random

from django.shortcuts import render
from django.conf import settings
from channels.consumer import AsyncConsumer

from redis import Redis
from meters.helpers import get_or_create_redis

db = Redis(host=settings.REDIS_HOST)

class RealTimeCommsConsumer(AsyncConsumer):
    async def websocket_connect(self, event):
        self.user = self.scope['user'].name
        await self.channel_layer.group_add(
            self.user,
            self.channel_name)
        data = get_or_create_redis(self.user, db)
        time = get_or_create_redis(self.user + 'time', db)
        result = {
            'data' : data,
            'time' : time
        }
        await self.send({
            "type" : "websocket.accept",
        })
        await self.channel_layer.group_send(
            self.user,
            {
                'type' :    'chat_message',
                'text' :    result
            })

    async def websocket_receive(self, event):
        await self.channel_layer.group_send(
            self.user,
            {
                'type' :    'chat_message',
                'text' :    event['text']
            })

    async def chat_message(self, event):
        await self.send({
            'type'  :   'websocket.send',
            'text' :    json.dumps(event['text'])
        })

    async def websocket_disconnect(self, event):
        await self.channel_layer.group_discard(
            self.user,
            self.channel_name
        )
        print('Disconnected', event)