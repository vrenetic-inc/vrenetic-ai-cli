#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pytest
from vrenetic_ai.skeleton import fib

__author__ = "kris"
__copyright__ = "kris"
__license__ = "mit"


def test_fib():
    assert fib(1) == 1
    assert fib(2) == 1
    assert fib(7) == 13
    with pytest.raises(AssertionError):
        fib(-10)
