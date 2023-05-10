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
from typing import TypeVar, Generic, Union
T = TypeVar('T')


class Cache(Generic[T]):
    """class Cache"""
    def __init__(self) -> None:
        """Init method"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, arg: Union[str, bytes]) -> int:
        """takes a data argument and returns a string"""
        id_ = str(uuid.uuid4())
        self._redis.set(id_, arg)
        return int(id_)
