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

def foldr(function, accumulator, folds):
    """Reduce `folds` with the function `function`, starting with
    `function(folds[-1], accumulator)` and working backwards.
    """
    for f in folds[::-1]:
        accumulator = function(f, accumulator)
    return accumulator

def foldl1(function, folds):
    """Reduce `folds` with the function `function`, starting with
    `function(folds[0], folds[1])`.
    """
    return foldl(function, folds[0], folds[1:])

def foldr1():
    pass
