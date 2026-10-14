import pytest

from geometry_engine.line import Line3D
from geometry_engine.point import Point3D
from geometry_engine.vector import Vector3D


def test_point_at_zero():
    line = Line3D(Point3D(1, 2, 3), Vector3D(2, 1, -1))
    result = line.point_at(0)

    assert (result.x, result.y, result.z) == (1, 2, 3)


def test_point_at_two():
    line = Line3D(Point3D(1, 2, 3), Vector3D(2, 1, -1))
    result = line.point_at(2)

    assert (result.x, result.y, result.z) == (5, 4, 1)


def test_point_at_negative_parameter():
    line = Line3D(Point3D(1, 2, 3), Vector3D(2, 1, -1))
    result = line.point_at(-1)

    assert (result.x, result.y, result.z) == (-1, 1, 4)


def test_zero_direction_vector():
    with pytest.raises(ValueError):
        Line3D(Point3D(1, 2, 3), Vector3D(0, 0, 0))
