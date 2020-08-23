from time import localtime
from meters.models import Meter
from django.db.models.signals import post_save
from django.dispatch import receiver
from asgiref.sync import async_to_sync
from channels import layers
from redis import Redis

from .helpers import (
    get_or_create_redis,
    PushList
)

# docker run --rm -d  -p 6379:6379/tcp redis:latest

@receiver(post_save,  sender=Meter)
def update_charts(signal, instance, **kwargs):
    channel_layer = layers.get_channel_layer()
    now = localtime()
    user = instance.user.name
    value = str(instance.customer_balance)

    db = Redis(host='localhost')
    redis_data = get_or_create_redis(user, db)
    redis_time = get_or_create_redis(str(user) + 'time', db)
    result = PushList(redis_data)
    time = PushList(redis_time, type=str)

    result.add(value)
    time.add(now.tm_hour)

    db.delete(user)
    db.delete(user + 'time')
    db.rpush(user, *result.data)
    db.rpush(user + 'time', *time.data)

    db.close()

    async_to_sync(channel_layer.group_send) (
        user,
        {
            'type' : 'chat_message',
            'text' : {
                'time' : time.data,
                'data' : result.data
            }
        }
    )