#!/usr/bin/env python
# -*- coding: utf-8 -*-

from functools import wraps


def freeze_dict(d):
    "Given a dictionary, return a hashable representation of it."
    return frozenset(d.items())


def memoize(function):
    """A decorator to memoize a function. This works by intercepting the given
    arguments and keyword arguments. If they exist in the `memo` dictionary,
    return that saved value; otherwise, apply the arguments and keyword args
    to the function, save the result into the memo dictionary, and return the
    result.
    """
    memo = {}
    @wraps(function)
    def memoized(*args, **kwargs):
        combination = (args, freeze_dict(kwargs))
        try:
            return memo[combination]
        except KeyError:
            memo[combination] = function(*args, **kwargs)
            return memo[combination]

    return memoized
