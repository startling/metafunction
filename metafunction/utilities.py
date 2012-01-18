#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Some little things that aren't functions, but need to be in order
to use them in certain contexts, e.g. composing functions.

Also take a look at the `operator` module.
"""


def cons(l, x):
    """Given a list and an object, return the list with that object appended.
    Note that this creates a new list! That is, it doesn't have any side 
    effects. Also note that this isn't really `cons` because python lists
    aren't linked lists; note especially that this *appends* the item rather
    than prepending it.
    """
    return l + [x]
