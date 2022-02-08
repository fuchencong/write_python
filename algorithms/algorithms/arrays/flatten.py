"""
Implement Flatten Arrays.
Given an array that may contain nested arrays,
produce a single resultant array.
"""

from collections.abc import Iterable


def flatten(input_arr, output_arr=None):
    if output_arr is None:
        output_arr = []

    for ele in input_arr:
        if not isinstance(ele, str) and isinstance(ele, Iterable):
            flatten(ele, output_arr)
        else:
            output_arr.append(ele)

    return output_arr


def flatten_iter(input_arr):
    for ele in input_arr:
        if not isinstance(ele, str) and isinstance(ele, Iterable):
            yield from ele
        else:
            yield ele
