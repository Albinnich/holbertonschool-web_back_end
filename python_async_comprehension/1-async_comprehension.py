#!/usr/bin/env python3
'''
Async Comprehensions
'''
from 0-async_generator import async_generator


async def async_comprehension():
    '''
    Collect and return  10 random numbers
    '''
    return [i async for i in async_generator()]
