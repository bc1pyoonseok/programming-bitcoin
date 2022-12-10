import sys
import os
import random

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import eliptic_curves
import pytest

get_random_number = lambda start, end: random.randint(start, end - 1)


def test_eq():
    p1 = eliptic_curves.Point(-1, -1, 5, 7)
    p2 = eliptic_curves.Point(-1, -1, 5, 7)
    assert p1 == p2
    p3 = eliptic_curves.Point(0, 2, 0, 4)
    assert p1 != p3
    with pytest.raises(ValueError):
        eliptic_curves.Point(2, 3, 4, 5)


def test_add():
    p1 = eliptic_curves.Point(-1, -1, 5, 7)
    p2 = eliptic_curves.Point(-1, 1, 5, 7)
    inf = eliptic_curves.Point(None, None, 5, 7)
    assert p1 + inf == p1
    assert p2 + inf == p2
    assert p1 + p2 == inf



if __name__ == '__main__':
    sys.exit(pytest.main([__file__]))
