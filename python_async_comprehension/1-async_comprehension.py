#!/usr/bin/env python3
'''
Async Comprehensions
'''
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension():
    '''
    Collect and return  10 random numbers
    '''
    return [i async for i in async_generator()]
