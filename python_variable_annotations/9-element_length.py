#!/usr/bin/env python3
'''
Module for duck type
'''

from typing import Iterable, Sequence, Tuple, List


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    '''
    Annotate the below function's parameters
    '''
    return [(i, len(i)) for i in lst]
