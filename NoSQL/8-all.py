#!/usr/bin/env python3
"""List all documents in Python"""


def list_all(mongo_collection):
    """ List all elements in a collection """
    return list(mongo_collection.find())
