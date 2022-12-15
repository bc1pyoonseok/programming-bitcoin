import collections
import sys
import os
import random
import collections

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
for path in [
        "/home/hamyoonseok/Desktop/programming-bitcoin/chapter_2",
        "/home/hamyoonseok/Desktop/programming-bitcoin/chapter_1",
]:
    sys.path.append(path)

import field_element
import eliptic_curves

import pytest


def test_on_curve():
    prime = 223
    a = field_element.FieldElement(0, prime)
    b = field_element.FieldElement(7, prime)
    # test with valid_points
    for x_raw, y_raw in ((192, 105), (17, 56), (1, 193)):
        x = field_element.FieldElement(x_raw, prime)
        y = field_element.FieldElement(y_raw, prime)
        eliptic_curves.Point(x, y, a, b)
    # test with invalid_points
    for x_raw, y_raw in ((200, 119), (42, 99)):
        x = field_element.FieldElement(x_raw, prime)
        y = field_element.FieldElement(y_raw, prime)
        with pytest.raises(ValueError):
            eliptic_curves.Point(x, y, a, b)


def test_add():
    prime = 223
    a = field_element.FieldElement(0, prime)
    b = field_element.FieldElement(7, prime)
    InfinitePoint = collections.namedtuple('InfinitePoint', 'x y')
    points = (
        InfinitePoint(170, 142),
        InfinitePoint(60, 139),
        InfinitePoint(47, 71),
        InfinitePoint(17, 56),
        InfinitePoint(143, 98),
        InfinitePoint(76, 66),
    )
    for i in range(0, len(points), 2):
        x1, y1 = points[i].x, points[i].y
        x2, y2 = points[i + 1].x, points[i + 1].y
        x1 = field_element.FieldElement(x1, prime)
        y1 = field_element.FieldElement(y1, prime)
        x2 = field_element.FieldElement(x2, prime)
        y2 = field_element.FieldElement(y2, prime)
        assert (eliptic_curves.Point(x1, y1, a, b) +
                eliptic_curves.Point(x2, y2, a, b))


if __name__ == '__main__':
    sys.exit(pytest.main([__file__]))
