import pytest

from geometry_engine.multipoint_path import MultiPointPath3D
from geometry_engine.point import Point3D


@pytest.fixture
def path():
    return MultiPointPath3D((
        Point3D(0, 0, 0),
        Point3D(6, 0, 0),
        Point3D(6, 8, 0),
        Point3D(6, 8, 10),
    ))


def test_start_position(path):
    point = path.position(0)

    assert (point.x, point.y, point.z) == (0, 0, 0)


def test_end_position(path):
    point = path.position(1)

    assert (point.x, point.y, point.z) == (6, 8, 10)


def test_first_control_point(path):
    point = path.position(1 / 3)

    assert point.x == pytest.approx(6)
    assert point.y == pytest.approx(0)
    assert point.z == pytest.approx(0)


def test_second_control_point(path):
    point = path.position(2 / 3)

    assert point.x == pytest.approx(6)
    assert point.y == pytest.approx(8)
    assert point.z == pytest.approx(0)


def test_midpoint_of_first_segment(path):
    point = path.position(1 / 6)

    assert point.x == pytest.approx(3)
    assert point.y == pytest.approx(0)
    assert point.z == pytest.approx(0)


def test_midpoint_of_second_segment(path):
    point = path.position(0.5)

    assert point.x == pytest.approx(6)
    assert point.y == pytest.approx(4)
    assert point.z == pytest.approx(0)


def test_midpoint_of_third_segment(path):
    point = path.position(5 / 6)

    assert point.x == pytest.approx(6)
    assert point.y == pytest.approx(8)
    assert point.z == pytest.approx(5)


@pytest.mark.parametrize("t", [-0.1, 1.1])
def test_invalid_parameter(path, t):
    with pytest.raises(ValueError):
        path.position(t)


def test_insufficient_points():
    with pytest.raises(ValueError):
        MultiPointPath3D((Point3D(0, 0, 0),))