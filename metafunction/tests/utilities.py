#!/usr/bin/env python
# -*- coding: utf-8 -*-

from unittest import TestCase, expectedFailure, main
from metafunction import cons


class TestUtilities(TestCase):
    def test_cons(self):
        "Test whether `cons` generally works."
        self.assertEqual(cons([], 5), [5])

    def test_cons_side_effects(self):
        "Test that `cons` has no side effects."
        l = [1, 2, 3]
        self.assertIsNot(l, cons(l, 5))


if __name__ == "__main__":
    main()
