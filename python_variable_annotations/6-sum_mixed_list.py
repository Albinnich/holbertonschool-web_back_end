#!/usr/bin/env python3

'''
Module defines  a type-annotated function sum_mixed_list
'''


from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    '''
    Function return sum of elements of the list
    '''
    return sum(mxd_lst)
