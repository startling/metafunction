#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Currying and uncurrying.

Say we have a function f that takes as an argument a list. We can use `curry`
to have it gather the list from its arguments. This can be useful for
composing functions, when you want one function to gather its arguments from
a list returned by another function.

e.g., curry(f(1, 2)) is equivalent to f([1, 2]).
"""


def curry(function):
    """Given a function that takes a list as an argument, return a function
    that gathers that list from its arguments.
    """
    def curried(*args, **kwargs):
        return function(args, **kwargs)
    return curried


def uncurry(function):
    pass
