#!/usr/bin/env python3
"""
Write a Python function that returns
all students sorted by average score
"""


def top_students(mongo_collection):
    """returns all students sorted by average score"""
    my_list = list(mongo_collection.find())
    my_sum = 0
    average_score_list = []
    for i in my_list:
        topics_dict = i["topics"]
        for m in range(len(topics_dict)):
            my_sum += topics_dict[m]["score"]
        average_score_dict = {}
        average_score_dict["_id"] = i["_id"]
        average_score_dict["name"] = i["name"]
        average_score_dict["averageScore"] = my_sum / len(topics_dict)
        average_score_list.append(average_score_dict)
        my_sum = 0
    newlist = sorted(average_score_list, key=lambda d: d['averageScore']) 
    return reversed(newlist)
