import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import field_element
import random
import pytest
import operator


def test_eq_nq():
    with pytest.raises(ValueError):
        error_f = field_element.FieldElement(20, 10)

    f1 = field_element.FieldElement(1, 10)
    f2 = field_element.FieldElement(1, 10)
    assert f1 == f2
    f1 = field_element.FieldElement(1, 10)
    f2 = field_element.FieldElement(1, 9)
    assert f1 != f2
    f1 = field_element.FieldElement(1, 10)
    f2 = field_element.FieldElement(2, 10)
    assert f1 != f2


def test_operations():
    def test_operation(operator_func):
        f1 = field_element.FieldElement(1, 10)
        f2 = field_element.FieldElement(1, 10)
        assert operator_func(f1, f2) == field_element.FieldElement(
            operator_func(1, 1) % 10, 10)
        prime = 100
        TEST_COUNT = 10
        for _ in range(TEST_COUNT):
            f1_num = random.randint(0, prime - 1)
            f2_num = random.randint(0, prime - 1)
            f1 = field_element.FieldElement(f1_num, prime)
            f2 = field_element.FieldElement(f2_num, prime)
            f3 = operator_func(f1, f2)
            assert f3.num == operator_func(f1_num, f2_num) % prime
            assert f3 == field_element.FieldElement(
                operator_func(f1_num, f2_num) % prime,
                prime,
            )

    map(test_operation, [
        operator.add,
        operator.sub,
        operator.mul,
        operator.pow,
    ])


if __name__ == '__main__':
    sys.exit(pytest.main([__file__]))
