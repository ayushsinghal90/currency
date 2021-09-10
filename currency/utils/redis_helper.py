import fakeredis as dummy_redis

from django.conf import settings
from django_redis import get_redis_connection


class RedisUtilities:
    con = get_redis_connection("default") \
        if not settings.IS_CURRENT_TESTING_ENVIRONMENT else dummy_redis.FakeStrictRedis()

    @staticmethod
    def sadd(key, *args):
        RedisUtilities.con.sadd(key, *args)

    @staticmethod
    def rpush(key, *args):
        RedisUtilities.con.rpush(key, *args)

    @staticmethod
    def lrem(key, count, value):
        RedisUtilities.con.lrem(key, count, value)

    @staticmethod
    def delete(*args):
        RedisUtilities.con.delete(*args)

    @staticmethod
    def set(key, value, ex=None):
        RedisUtilities.con.set(key, value, ex=ex)

    @staticmethod
    def hset(name, key, value):
        RedisUtilities.con.hset(name, key, value)

    @staticmethod
    def hdel(name, *keys):
        RedisUtilities.con.hdel(name, *keys)

    @staticmethod
    def hexists(name, key):
        return RedisUtilities.con.hexists(name, key)

    @staticmethod
    def exists(key):
        return bool(RedisUtilities.con.exists(key))

    @staticmethod
    def get(key):
        return RedisUtilities.con.get(key)

    @staticmethod
    def lrange(key, start, end):
        return RedisUtilities.con.lrange(key, start, end)

    @staticmethod
    def lread_all(key):
        return RedisUtilities.con.lrange(key, 0, -1)

    @staticmethod
    def expire(key, *args):
        return RedisUtilities.con.expire(key, *args)

    @staticmethod
    def flush_all():
        return RedisUtilities.con.flushall()
