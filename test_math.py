import pytest


def test_divide_by_zero():
    num = 1 / 0


def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError) as e:
        num = 1 / 0
        assert 'division by zero' in str(e.value)  # verify attribute of exception


def test_add_one():
 assert 1+1 ==0

# parametrize test function  --> @pytest.mark.parametrize
# To overcome the DRY - Don't repeat yourself
# decorater --> that allows a user to add new functionality to an existing object without modifying its structure

products = [
    (2, 3, 6),
    (1, 99, 99),
    (5, -3, -15),
]


@pytest.mark.parametrize("a,b,product", products)
def test_parametrize(a, b, product):
    assert a * b == product
