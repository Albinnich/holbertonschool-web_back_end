#!/usr/bin/env python3

'''
Module defines a type-annotated function make_multiplier
'''
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    '''
    Declaration
    '''
    def multiplier_function(value: float) -> float:
        return value * multiplier
    return multiplier_function
