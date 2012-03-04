#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
from functools import wraps
from metafunction.memoize import memoize


class TestMemoize(unittest.TestCase):
    def assert_memoizes(inputs):
        "Test that a memoized function works the same as the normal version."
        def testing_memoize(function):
            memoized = memoize(function)
            @wraps(function)
            def test_each(self):
                for i in inputs:
                    self.assertEqual(memoized(self, i), function(self, i))
            return test_each
        return testing_memoize

    @assert_memoizes([1, 2, 3, 4, 5])
    def test_add_one_memoized(self, num):
        return num + 1

    @assert_memoizes([(1, 2), (2, 3)])
    def test_add_together_memoized(self, args):
        a, b = args
        return a + b
