
import pytest


def calc_addition(a, b):
    return a + b
 
 
def calc_multiply(a, b):
    return a * b
     
 
def calc_substraction(a, b):
    return a - b


def test_calc_addition():
    output = calc_addition(2,4)
    assert output == 6
 
def test_calc_substraction():
    output = calc_substraction(2, 4)
    assert output == -2
     
def test_calc_multiply():
    output = calc_multiply(2,4)
    assert output == 8