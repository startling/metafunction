#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" Function composition! """

def compose(a, b):
    "Given a list of functions, return a composition of them."
    def composition(*args, **kwargs):
        return a(b(*args, **kwargs))
    return composition
