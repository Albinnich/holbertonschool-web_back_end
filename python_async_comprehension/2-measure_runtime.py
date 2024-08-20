#!/usr/bin/env python3
'''
Run time for four parallel comprehensions
'''
import asyncio
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime():
    '''
    Measure the total runtime
    '''
    start_time = time.time()
    await asyncio.gather(async_comprehension(), async_comprehension(), async_comprehension(), async_comprehension())
    total_time = time.time() - start_time
    return total_tie
