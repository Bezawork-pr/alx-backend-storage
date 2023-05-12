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
    print("Methods:")
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
    new_list = []
    new_dict = {"count": 0}
    my_list = list(logs.find())
    count = 0
    another = 0
    for i in range(len(my_list)):
        if len(new_list) != 0:
            for m in range(len(new_list)):
                if my_list[i]["ip"] == new_list[m]["ip"]:
                    new_list[m]["count"] += 1
                else:
                    new_dict["ip"] = my_list[i]["ip"]
                    new_dict["count"] += 1
                    new_list.append(new_dict)
                    new_dict = {"count": 0}
        else:
            new_dict["ip"] = my_list[i]["ip"]
            new_dict["count"] += 1
            new_list.append(new_dict)
            new_dict = {"count": 0}

    print("IPs:")
    print(new_list)



if __name__ == "__main__":
    main()
