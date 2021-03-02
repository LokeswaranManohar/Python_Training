import pytest

from Class_data.accum import Accumulator


@pytest.fixture  # decorator
def accum():  # the only thing it does is to create a new Accumulator object
    return Accumulator()


# A test case can also use multiple fixtures, just make sure each fixture has a unique name

# Sample
# @pytest.fixture
# Def accum():
#  Return Accumulator()

# @pytest.fixture
# Def accum2():
#  Return Accumulator()

# Def  test_Accumulator_init(accum,accum2):
#  Assert accum.count == 0


@pytest.fixture
def accum():
    yield Accumulator()  # before yield setup after cleanup
    print("DONE-ZO!")


# fixture -> fuction scope


@pytest.fixture
def accum(scope="session"):
    return Accumulator()

# rule in pytest  it will be accessible to all under project and dir
# session, class, module
# opening
