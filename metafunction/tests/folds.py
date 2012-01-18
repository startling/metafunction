#!/usr/bin/env python
# -*- coding: utf-8 -*-

from unittest import TestCase, expectedFailure, main
from metafunction import foldr, foldl, foldr1, foldl1, cons
from operator import add, pow


class TestFoldl(TestCase):
    @expectedFailure
    def test_foldl_basic(self):
        """ Test that left folds basically work. """
        self.assertEqual(foldl(add, 2, [1, 2, 3]), 8)

    @expectedFailure
    def test_foldl_order(self):
        """Test that left folds are applied in the correct order.

        E.g., foldl(pow, 2, [1, 2, 3]) should be applied like:
        (2^1) = 2
        (2^2) = 4
        (4^3) = 64
        """
        self.assertEqual(foldl(pow, 2, [1, 2, 3]), 64)

    @expectedFailure
    def test_foldl1(self):
        "Test that foldl1 basically works."
        self.assertEqual(foldl1(add, [1, 2, 3]), 6)


class TestFoldr(TestCase):
    @expectedFailure
    def test_foldr_basic(self):
        """Test that right folds basically work."""
        self.assertEqual(foldr(add, 2, [1, 2, 3]), 8)

    @expectedFailure
    def test_foldr_order(self):
        """Test that right fold are applied in the correct order.

        E.g, foldr(pow, 2, [1, 2, 3]) should be applied like:
        (3^2) = 9
        (2^9) = 512
        (1^512) = 1
        """
        self.assertEqual(foldr(pow, 2, [1, 2, 3]), 1)

    @expectedFailure
    def test_foldr1(self):
        "Test that foldr1 basically works."
        self.assertEqual(foldr1(add, [1, 2, 3]), 6)
