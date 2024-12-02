# -*- coding: utf-8 -*-
"""
Created on Mon Dec  2 18:44:28 2024

@author: gowtham.balachan
"""

# tests/test_calculator.py

import pytest
from src.calculator import add, subtract

def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0

def test_subtract():
    assert subtract(5, 3) == 2
    assert subtract(0, 3) == -3
