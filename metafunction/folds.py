#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Folds!

Folds are similar to python's `reduce` (RIP), only more so; they give you
control over direction, starting value, etc etc. The most similar to python's
`reduce` is foldl1, which starts with the first value of a list.
"""

def foldl(function, accumulator, folds):
    """Reduce `folds` with the function `function`, starting with
    `function(accumulator, folds[0])`.
    """
    for f in folds:
        accumulator = function(accumulator, f)
    return accumulator

def foldr():
    pass

def foldl1():
    pass

def foldr1():
    pass
