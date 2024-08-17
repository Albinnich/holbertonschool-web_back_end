#!/usr/bin/env python3

'''
Module on regular function syntax
'''
import asyncio
from 0-basic_async_syntax import wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    '''
    Returns an asyncio
    '''
    return asyncio.create_task(wait_random(max_delay))
