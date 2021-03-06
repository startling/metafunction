#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
from functools import wraps
from metafunction.memoize import memoize_hashable


class TestMemoize(unittest.TestCase):
    def assert_memoizes(inputs):
        "Test that a memoized function works the same as the normal version."
        def testing_memoize(function):
            memoized = memoize_hashable(function)
            @wraps(function)
            def test_each(self):
                for i in inputs:
                    self.assertEqual(memoized(self, i), function(self, i))
            return test_each
        return testing_memoize

    @assert_memoizes([1, 2, 3, 4, 5])
    def test_add_one_memoized(self, num):
        return num + 1

    @assert_memoizes([(1, 2), (2, 3), (7, 13), (53, 97)])
    def test_add_together_memoized(self, args):
        a, b = args
        return a + b

    @unittest.expectedFailure
    @assert_memoizes([[1, 2, 3], [5, 6, 7], []])
    def test_unhashables_append(self, l):
        l.append(True)
        return l

    @unittest.expectedFailure
    @assert_memoizes([({1: 12, 2:13}, 12), ([1, 2, 3], 13)])
    def test_unhashables_nested(self, l):
        return l[0]

    @unittest.expectedFailure
    @assert_memoizes([({1: 12, 2:{1:12, 2:13}}, 12), ([1, 2, 3], 13)])
    def test_unhashables_more_nested(self, l):
        return l[0]
