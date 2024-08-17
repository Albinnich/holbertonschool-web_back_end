#!/usr/bin/env python3
'''
Module to measure runtime
'''
import time
import asyncio
from typing import List
from 1-concurrent_coroutines import wait_n


def measure_time(n: int, max_delay: int) -> float:
    """Measures the total execution time for wait_n(n, max_delay) and returns total_time / n."""
    start_time = time.time()
    asyncio.run(wait_n(n, max_delay))
    end_time = time.time()
    total_time = end_time - start_time
    return total_time / n
