#!/usr/bin/env python
# -*- coding: utf-8 -*-

from unittest import TestCase, expectedFailure, main
from metafunction import scanr, scanl, scanr1, scanl1, cons
from operator import add, pow


class TestScanl(TestCase):
    def scan(self, *args):
        "Given some arguments, return a list from the scanl iterator."
        return list(scanl(*args))

    def test_scanl_basic(self):
        """Test that left scans basically work."""
        self.assertEqual(self.scan(add, 2, [1, 2, 3]), [2, 3, 5, 8])

    def test_scanl_order(self):
        """Test that left scans are applied in the correct order.

        E.g., scanl(pow, 2, [1, 2, 3]) should be applied like:
        (2^1) = 2
        (2^2) = 4
        (4^3) = 64
        """
        self.assertEqual(self.scan(pow, 2, [1, 2, 3]), [2, 2, 4, 64])

    def test_scanl1(self):
        "Test that scanl1 basically works."
        self.assertEqual(list(scanl1(add, [1, 2, 3])), [1, 3, 6])


class TestScanr(TestCase):
    def scan(self, *args):
        "Given some arguments, return a list from the scanr iterator."
        return list(scanr(*args))

    def test_scanr_basic(self):
        """Test that right scans basically work."""
        self.assertEqual(self.scan(add, 2, [1, 2, 3]), [2, 5, 7, 8])

    def test_scanr_order(self):
        """Test that right scan are applied in the correct order.

        E.g, scanr(pow, 2, [1, 2, 3]) should be applied like:
        (3^2) = 9
        (2^9) = 512
        (1^512) = 1
        """
        self.assertEqual(self.scan(pow, 2, [1, 2, 3]), [2, 9, 512, 1])

    def test_scanr1(self):
        "Test that scanr1 basically works."
        self.assertEqual(list(scanr1(add, [1, 2, 3])), [3, 5, 6])
