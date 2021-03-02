import pytest
from Class_data.accum import Accumulator


@pytest.fixture  # decorator
def accum():  # the only thing it does is to create a new Accumulator object
    return Accumulator()


def test_accumulator_init(accum):  # verifies that the new instance of the Accumulator class has a starting count of
    # zero.
    # accum = Accumulator()  # accum is a object of class Accumulator   No need of obj also it will work
    assert accum.count == 0


# verifies that the add() method adds one to the internal count when it is called with no other arguments.
def test_accumulator_add_one(accum):
    # accum = Accumulator()
    accum.add()
    assert accum.count == 1


# verifies that the add() method adds 3 to the count when it is called with the argument of 3.
def test_accumulator_add_three(accum):
    # accum = Accumulator()
    accum.add(3)
    assert accum.count == 3


# verifies that the count increases appropriately with multiple add() calls.
def test_accumulator_add_twice(accum):
    # accum = Accumulator()
    accum.add()
    accum.add()
    assert accum.count == 2


# verifies that the count attribute cannot be assigned directly because it is a read-only property. Notice how we use
# pytest.raises to verify the attribute error. r -> raw string notation eg: r"\n" will be treated as two char string
# '\' and 'n', whereas "\n" will be treated as a single string containing new line
def test_accumulator_cannot_set_count_directly(accum):
    # accum = Accumulator()
    with pytest.raises(AttributeError, match=r"can't set attribute") as e:
        accum.count = 10
