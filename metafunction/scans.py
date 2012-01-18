#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Scans are a sort of difficult topic. Suffice it to say that they're
kind of like folds, only they yield every value instead of just the last.

`scanr` and `scanr1` are a little bit different than Haskell's scanrs in that
they return the list "backwards" (or rightwards, depending on how you look at
it). This is because python's lists are not linked lists, so things make a 
a little more sense this way.

Also, the things here are all generators, so it makes sense to yield the
values as you go along.
"""


def scanl(function, accumulator, scans):
    """Reduce `scans` with the function `function`, starting with
    `function(accumulator, scans[0])`.
    """
    yield accumulator
    for f in scans:
        accumulator = function(accumulator, f)
        yield accumulator


def scanr(function, accumulator, scans):
    """Reduce `scans` with the function `function`, starting with
    `function(scans[-1], accumulator)` and working backwards.
    """
    yield accumulator
    for f in scans[::-1]:
        accumulator = function(f, accumulator)
        yield accumulator


def scanl1(function, scans):
    """Reduce `scans` with the function `function`, starting with
    `function(scans[0], scans[1])`.
    """
    return scanl(function, scans[0], scans[1:])


def scanr1(function, scans):
    """Reduce `scans` with the function `function`, starting with
    `function(scans[-2], scans[-1])` and working backwards.
    """
    return scanr(function, scans[-1], scans[:-1])
