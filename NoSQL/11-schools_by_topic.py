#!/usr/bin/env python3
"""Where can I learn Python?"""


def schools_by_topic(mongo_collection, topic):
    """Get schools with specific topics"""
    return mongo_collection.find({"topics": topic})
