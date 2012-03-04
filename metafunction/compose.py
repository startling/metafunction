#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" Function composition! """

def compose(*functions):
    "Given a list of functions, return a composition of them."
    def composition(*args, **kwargs):
        # start off by applying the arguments to the last function.
        output = functions[-1](*args, **kwargs)
        # iterate backwards over the list of functions (except the last).
        for function in functions[-2::-1]:
            # apply the output so far to each function. 
            output = function(output)
        return output
    return composition
