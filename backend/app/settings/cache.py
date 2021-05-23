import os

REDIS_HOST = os.getenv('REDIS_HOST', 'localhost')

CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": f"redis://{REDIS_HOST}:6379",
        "OPTIONS": {
            "DB": 1,
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        }
    }
}