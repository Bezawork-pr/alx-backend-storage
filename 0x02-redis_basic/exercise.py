#!/usr/bin/env python3
"""
Create a Cache class. In the __init__ method,
store an instance of the Redis client as a
private variable named _redis
(using redis.Redis()) and flush the
instance using flushdb
"""
import redis
import uuid
from typing import Union, Optional, Callable


class Cache:
    """class Cache"""
    def __init__(self) -> None:
        """Init method"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """takes a data argument and returns a string"""
        id_ = str(uuid.uuid4())
        self._redis.set(id_, data)
        return id_

    def get(self, key: str, fn: Optional[Callable] = None) ->  Union[str, bytes, int, float]:
        """convert the data back to the desired format"""
        get = self._redis.get(key)
        if fn:
            return fn(key)
        return get

    def get_str(self, key: str) -> str:
        """Str decoding"""
        get = self._redis.get(key)
        if get is not None:
            return get.decode('utf-8')

    def get_int(self, key: str) -> int:
        """Int coversion"""
        get = self._redis.get(key)
        try:
            get = int(get.decode('utf-8'))
        except Exception as notInt:
            get = 0
        return get

