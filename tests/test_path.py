import pytest

from geometry_engine.path import LinearPath3D
from geometry_engine.point import Point3D


def test_start_position():
    path = LinearPath3D(
        Point3D(0, 0, 0),
        Point3D(10, 20, 30),
    )

    point = path.position(0)

    assert (point.x, point.y, point.z) == (0, 0, 0)


def test_end_position():
    path = LinearPath3D(
        Point3D(0, 0, 0),
        Point3D(10, 20, 30),
    )

    point = path.position(1)

    assert (point.x, point.y, point.z) == (10, 20, 30)


def test_midpoint():
    path = LinearPath3D(
        Point3D(0, 0, 0),
        Point3D(10, 20, 30),
    )

    point = path.position(0.5)

    assert (point.x, point.y, point.z) == (5, 10, 15)


def test_intermediate_position():
    path = LinearPath3D(
        Point3D(2, 4, 6),
        Point3D(10, 12, 14),
    )

    point = path.position(0.25)

    assert point.x == pytest.approx(4)
    assert point.y == pytest.approx(6)
    assert point.z == pytest.approx(8)


@pytest.mark.parametrize("t", [-0.1, 1.1])
def test_invalid_parameter(t):
    path = LinearPath3D(
        Point3D(0, 0, 0),
        Point3D(10, 20, 30),
    )

    with pytest.raises(ValueError):
        path.position(t)