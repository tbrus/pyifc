"""
pyifc._utils
------------

Utility functions.
"""

import functools


def timeit(func):
    """Decorator function for measuring function execution time.
    
    The time is printed to stdout up to 4 decimal places.
    """
    @functools.wraps(func)
    def new_func(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        elapsed_time = time.time() - start_time
        print('function [{}] finished in {} s'.format(
            func.__name__, round(elapsed_time, 4)))
        return result
    return new_func