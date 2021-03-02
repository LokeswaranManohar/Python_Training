# Parameterized Test Cases

# Tests can have different kinds of inputs and outputs.
# They may also have specific boundary cases that should be tested.

# for Eg: multiplication ->two + int,by 1, by 0, one +ve and one -ve, two -ve, float value
# to overcome Don't Repeat Yourself we use parameterized test cases

# @pytest.mark.parametrize -> one test function that takes multiple parametrized inputs

# its is a decorator for a function which takes two parameters, one is the parameters used by the function(string)
# and other is the list which we are passing

# Decorator -> it is function that wraps another function, and also allows a user to add new functionality to an
# existing object without modifying its structure


import pytest

products = [  # one tuple for each usecase
    (2, 3, 6),  # positive integers
    (1, 99, 99),  # identity
    (0, 99, 0),  # zero
    (3, -4, -12),  # positive by negative
    (-5, -5, 25),  # negative by negative
    (2.5, 6.7, 16.75)  # floats
]


@pytest.mark.parametrize('a, b, product', products)  # outer  function -> this outer function will call the inner
# function once per tuple
def test_multiplication(a, b, product):  # inner function #testcase function through which we re passing arguments
    assert a * b == product


#@ refers to decorator