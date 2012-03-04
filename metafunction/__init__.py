#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""A set of Haskell-inspired higher-order functions for Python."""

from metafunction.compose import compose
from metafunction.currying import curry, uncurry
from metafunction.utilities import cons, return_last
from metafunction.scans import scanr, scanl, scanr1, scanl1
from metafunction.folds import foldr, foldl, foldr1, foldl1
from metafunction.memoize import memoize


__version__ = "0.00.0dev"
