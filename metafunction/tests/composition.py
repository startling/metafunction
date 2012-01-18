#!/usr/bin/env python
# -*- coding: utf-8 -*-

from unittest import TestCase, main, expectedFailure
from functools import partial
from metafunction import compose


class TestComposition(TestCase):
    @expectedFailure
    def test_basic(self):
        """A trivial example for composition; sum numbers that are not 5.

        This is not the most pythonic way to do it, but it makes for a good
        example of function composition.
        """
        # a function that returns a list without any fives.
        filter_fives = partial(filter, lambda x: x != 5)
        # a function that sums the result of filter_fives on a list.
        function = compose(sum, filter_fives)
        # for each of these cases, check that we get the expected result.
        cases = [
            ([1, 2, 3, 4, 5], 10),
            ([5, 5], 0),
            ([10, 15, 5], 25),
        ]
        for input, output in cases:
            self.assertEqual(function(input), output)

    @expectedFailure
    def test_multiple(self):
        "Test whether we can compose more than one function."
        # basically, add 3 to the sum of a list.
        function = compose(lambda x: x + 1, lambda x: x + 2, sum)
        self.assertEqual(function([5, 3]), 11)


if __name__ == "__main__":
    main()
