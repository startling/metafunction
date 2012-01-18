#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Folds!

Folds are similar to python's `reduce` (RIP), only more so; they give you
control over direction, starting value, etc etc. The most similar to python's
`reduce` is foldl1, which starts with the first value of a list.
"""

from metafunction import scanr, scanl, scanr1, scanl1, compose, return_last
from functools import partial


construct_fold = partial(compose, return_last)


# Reduce `folds` with the function `function`, starting with
#    `function(accumulator, folds[0])`.
foldl = construct_fold(scanl)


# Reduce `folds` with the function `function`, starting with
#   `function(folds[-1], accumulator)` and working backwards.
foldr = construct_fold(scanr)


# Reduce `folds` with the function `function`, starting with
#   `function(folds[0], folds[1])`.
foldl1 = construct_fold(scanl1)


# Reduce `folds` with the function `function`, starting with
#   `function(folds[-2], folds[-1])` and working backwards.
foldr1 = construct_fold(scanr1)
