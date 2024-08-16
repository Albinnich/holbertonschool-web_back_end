#!/usr/bin/env python3

'''
Module defines a type-annotated function to_kv
'''
from typing import Union, Tuple
from math import pow


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    '''
    Function taht returns a tuple
    '''
    return k, float(pow(v, 2))
