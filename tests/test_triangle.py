import math

import pytest

from geometry_engine.point import Point3D
from geometry_engine.triangle import Triangle3D


def test_side_lengths():
    triangle = Triangle3D(
        Point3D(0, 0, 0),
        Point3D(3, 0, 0),
        Point3D(0, 4, 0),
    )

    assert triangle.side_lengths() == (3.0, 5.0, 4.0)


def test_perimeter():
    triangle = Triangle3D(
        Point3D(0, 0, 0),
        Point3D(3, 0, 0),
        Point3D(0, 4, 0),
    )

    assert triangle.perimeter() == pytest.approx(12.0)


def test_area():
    triangle = Triangle3D(
        Point3D(0, 0, 0),
        Point3D(3, 0, 0),
        Point3D(0, 4, 0),
    )

    assert triangle.area() == pytest.approx(6.0)


def test_triangle_in_3d():
    triangle = Triangle3D(
        Point3D(0, 0, 0),
        Point3D(2, 0, 0),
        Point3D(0, 0, 3),
    )

    assert triangle.area() == pytest.approx(3.0)


def test_collinear_points():
    with pytest.raises(ValueError):
        Triangle3D(
            Point3D(0, 0, 0),
            Point3D(1, 1, 1),
            Point3D(2, 2, 2),
        )