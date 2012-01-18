#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Some little things that aren't functions, but need to be in order
to use them in certain contexts, e.g. composing functions.

Also take a look at the `operator` module.
"""

from operator import itemgetter


def cons(l, x):
    """Given a list and an object, return the list with that object appended.
    Note that this creates a new list! That is, it doesn't have any side 
    effects. Also note that this isn't really `cons` because python lists
    aren't linked lists; note especially that this *appends* the item rather
    than prepending it.
    """
    return l + [x]


def return_last(iter):
    """Return the last thing an iterator yields. This can be useful for, e.g.,
    constructing `foldl` and `foldr`. It's better than list(iter)[-1] because
    it doesn't store a big list in memory.
    """
    for thing in iter:
        pass
    return thing
