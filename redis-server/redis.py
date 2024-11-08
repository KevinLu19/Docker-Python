import redis

class RedisServer:
    def __init__(self):
        self.redis_instance = redis.Redis(host='localhost', port=6379, db=0)

    def SetValue(self, key: str, val: str):
        self.redis_instance.set(key, val)
    
    def GetValue(self, key: str):
        value =  self.redis_instance.get(key)

        return value
