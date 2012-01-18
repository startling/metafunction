#!/usr/bin/env python
# -*- coding: utf-8 -*-

from unittest import TestCase, main, expectedFailure
from metafunction import curry, uncurry


class TestCurrying(TestCase):
    def test_curry(self):
        "Test that currying works."
        new_sum = curry(sum)
        self.assertEqual(new_sum(1, 2, 3), 6)

    def test_uncurry(self):
        "Test that uncurrying works."
        # This is silly but I can't think of anything better.
        # Still, uncurrying a curried function should be equivalent
        # to the original function.
        old_sum = uncurry(curry(sum))
        self.assertEqual(old_sum([1, 2, 3]), 6)


if __name__ == "__main__":
    main()
