#!/usr/bin/env python3
""" Write a Python function that lists all documents in a collection """


def list_all(mongo_collection):
    """List all documents in collection"""
    list_all = list(mongo_collection.find())
    return [] if list_all is None else list_all
