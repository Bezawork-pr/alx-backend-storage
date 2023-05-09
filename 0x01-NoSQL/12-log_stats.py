#!/usr/bin/env python3
"""
Write a Python script that provides some
stats about Nginx logs stored in MongoDB"""
from pymongo import MongoClient


def main():
    """provides some stats about Nginx logs stored in MongoDB"""
    client = MongoClient('mongodb://127.0.0.1:27017')
    logs = client.logs.nginx
    print("{} logs".format(logs.count_documents({})))
    print("\tmethod GET: {}".
          format(logs.count_documents({"method": "GET"})))
    print("\tmethod POST: {}".
          format(logs.count_documents({"method": "POST"})))
    print("\tmethod PUT: {}".
          format(logs.count_documents({"method": "PUT"})))
    print("\tmethod PATCH: {}".
          format(logs.count_documents({"method": "PATCH"})))
    print("\tmethod DELETE: {}".
          format(logs.count_documents({"method": "DELETE"})))
    print("{} status check".
          format(logs.count_documents({"method": "GET", "path": "/status"})))


if __name__ == "__main__":
    main()
