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
from functools import wraps


def count_calls(method: Callable) -> Callable:
    """define a count_calls decorator that takes
    a single method Callable argument and returns a Callable"""
    key = method.__qualname__

    @wraps(method)
    def wrapper(self, *args, **kwds):
        """Wrapper function"""
        self._redis.incr(key)
        return method(self, *args, **kwds)
    return wrapper


def call_history(method: Callable) -> Callable:
    """define a call_history decorator to store
    the history of inputs and outputs for a particular function"""

    @wraps(method)
    def wrapper(self, *args, **kwds):
        """Wrapper function"""
        self._redis.rpush(method.__qualname__ + ":inputs", str(args))
        outputs = method(self, *args, **kwds)
        self._redis.rpush(method.__qualname__ + ":outputs", outputs)
        return outputs
    return wrapper


def replay(func: callable):
    """display the history of calls of a particular function"""
    r = redis.Redis()
    fun_name = func.__qualname__
    number_of_calls = r.get(fun_name).decode("Utf-8")
    print("{} was called {} times".format(fun_name, number_of_calls))
    inputs = r.lrange(fun_name + ":inputs", 0, -1)
    outputs = r.lrange(fun_name + ":outputs", 0, -1)
    for ins, outs in zip(inputs, outputs):
        ins = ins.decode("Utf-8")
        outs = outs.decode("Utf-8")
        print("{}(*({},)) -> {}".format(fun_name, ins, outs))


class Cache:
    """class Cache"""
    def __init__(self) -> None:
        """Init method"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    @call_history
    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """takes a data argument and returns a string"""
        id_ = str(uuid.uuid4())
        self._redis.set(id_, data)
        return id_

    def get(self, key: str,
            fn: Optional[Callable] = None) -> Union[str, bytes, int, float]:
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
