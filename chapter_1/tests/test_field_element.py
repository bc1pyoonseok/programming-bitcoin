import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import field_element
import random
import pytest
import operator

get_random_number = lambda start, end: random.randint(start, end - 1)


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
    def test_operation_add_mul_sub(operator_func):
        f1 = field_element.FieldElement(1, 10)
        f2 = field_element.FieldElement(1, 10)
        assert operator_func(f1, f2) == field_element.FieldElement(
            operator_func(1, 1) % 10, 10)
        prime = 100
        TEST_COUNT = 100
        for _ in range(TEST_COUNT):
            f1_num = get_random_number(0, prime - 1)
            f2_num = get_random_number(0, prime - 1)
            f1 = field_element.FieldElement(f1_num, prime)
            f2 = field_element.FieldElement(f2_num, prime)
            f3 = operator_func(f1, f2)
            assert f3.num == operator_func(f1_num, f2_num) % prime
            assert f3 == field_element.FieldElement(
                operator_func(f1_num, f2_num) % prime,
                prime,
            )

    def test_operation_pow(operator_func):
        TEST_COUNT = 100
        prime = 100
        for _ in range(TEST_COUNT):
            f1_num = get_random_number(1, prime - 1)
            f1 = field_element.FieldElement(f1_num, prime)
            exponent = get_random_number(-prime, prime - 1)
            assert (f1**exponent).num == operator_func(
                f1_num,
                exponent % (prime - 1),
            ) % prime

    def test_operation_truediv(operator_func):
        TEST_COUNT = 100
        prime = 100
        for _ in range(TEST_COUNT):
            f1_num = get_random_number(1, prime - 1)
            f2_num = get_random_number(1, prime - 1)
            f1 = field_element.FieldElement(f1_num, prime)
            f2 = field_element.FieldElement(f2_num, prime)
            assert (f1 / f2).num == f1_num * pow(
                f2_num,
                prime - 2,
                prime,
            ) % prime

    for test_operater in (
            operator.add,
            operator.sub,
            operator.mul,
    ):
        test_operation_add_mul_sub(test_operater)
    test_operation_pow(operator.pow)
    test_operation_truediv(operator.truediv)


if __name__ == '__main__':
    sys.exit(pytest.main([__file__]))
