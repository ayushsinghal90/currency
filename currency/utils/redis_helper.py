import fakeredis as dummy_redis

from django.conf import settings
from django_redis import get_redis_connection


class RedisUtilities:
    con = get_redis_connection("default") \
        if not settings.IS_CURRENT_TESTING_ENVIRONMENT else dummy_redis.FakeStrictRedis()

    @staticmethod
    def set(key, value, ex=None):
        RedisUtilities.con.set(key, value, ex=ex)

    @staticmethod
    def get(key):
        return RedisUtilities.con.get(key)

