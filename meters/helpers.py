from decimal import Decimal
from time import time
import random

class PushList:
    def __init__(self, data=None, **kwargs):
        self.type = kwargs.get('type', str)
        if not data:
            self.size = kwargs.get('size', 4)
            self.data = [0 for _ in range(self.size)]
        else:
            self.data = [int(val) for val in data]
            self.size = len(self.data)

    def add(self, data):
        self.__add__(data)

    def __add__(self, value):
        if type(value) != self.type:
            value = self.type(value)
        if 0 in self.data:
            index = self.data.index(0)
            self.data[index] = value
        else:
            self.data = self.data[1:self.size] + [value]

    def __repr__(self):
        return str(self.data)


def get_or_create_redis(key, db):
    data = db.lrange(key, 0, 4)
    if not data:
        result = [0, 0, 0, 0, 0]
        db.rpush(key, *result)
        return result
    else:
        return [int(float(x.decode())) for x in data]

data = {
    'time' : ['5am', '6am', '7am', '8am' '9am'],
    'value' : [0, 0, 0, 0, 0]
}

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

# put = pusher()

# while True:
#     # This is where REDIS should come in
#     await self.send({
#         "type" : "websocket.send",
#         'text': json.dumps(next(put))
#     })
#     await asyncio.sleep(3)