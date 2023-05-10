#!/usr/bin/env python3
""" uses the requests module to obtain
the HTML content of a particular URL and returns it."""
import redis
import requests


def get_page(url: str) -> str:
    """Use request module to obtain HTML content"""
    r = redis.Redis()
    count = 0
    html_request = requests.get(url)
    r.set("count:{url}", count)
    r.incr("count:{url}")
    r.setex("count:{url}", 10, count)
    return html_request.text
