import math

import pytest

from geometry_engine.point import Point3D
from geometry_engine.pyramid import Pyramid3D


@pytest.fixture
def pyramid():
    return Pyramid3D(
        center_x=5,
        center_y=5,
        base_z=0,
        base_size=4,
        height=6,
    )


def test_volume(pyramid):
    assert pyramid.volume == pytest.approx(32.0)


def test_surface_area(pyramid):
    expected = 16 + 8 * math.sqrt(40)
    assert pyramid.surface_area == pytest.approx(expected)


def test_apex(pyramid):
    assert pyramid.apex.x == 5
    assert pyramid.apex.y == 5
    assert pyramid.apex.z == 6


def test_point_inside(pyramid):
    assert pyramid.contains_point(Point3D(5, 5, 2))


def test_point_outside(pyramid):
    assert not pyramid.contains_point(Point3D(9, 5, 2))


def test_point_on_base(pyramid):
    assert pyramid.contains_point(Point3D(5, 5, 0))


def test_point_at_apex(pyramid):
    assert pyramid.contains_point(Point3D(5, 5, 6))


def test_point_above_apex(pyramid):
    assert not pyramid.contains_point(Point3D(5, 5, 7))


def test_invalid_base_size():
    with pytest.raises(ValueError):
        Pyramid3D(0, 0, 0, 0, 5)


def test_invalid_height():
    with pytest.raises(ValueError):
        Pyramid3D(0, 0, 0, 4, 0)


def test_clearance_not_implemented(pyramid):
    with pytest.raises(NotImplementedError):
        pyramid.contains_point(Point3D(5, 5, 2), clearance=0.5)

def test_segment_through_pyramid(pyramid):
    start = Point3D(0, 5, 2)
    end = Point3D(10, 5, 2)
    assert pyramid.intersects_segment(start, end)


def test_segment_above_pyramid(pyramid):
    start = Point3D(0, 5, 8)
    end = Point3D(10, 5, 8)
    assert not pyramid.intersects_segment(start, end)


def test_segment_below_pyramid(pyramid):
    start = Point3D(0, 5, -1)
    end = Point3D(10, 5, -1)
    assert not pyramid.intersects_segment(start, end)


def test_segment_touching_apex(pyramid):
    start = Point3D(0, 5, 6)
    end = Point3D(10, 5, 6)
    assert pyramid.intersects_segment(start, end)


def test_segment_inside_pyramid(pyramid):
    start = Point3D(5, 5, 1)
    end = Point3D(5, 5, 3)
    assert pyramid.intersects_segment(start, end)


def test_zero_length_segment_inside(pyramid):
    point = Point3D(5, 5, 2)
    assert pyramid.intersects_segment(point, point)


def test_zero_length_segment_outside(pyramid):
    point = Point3D(10, 10, 10)
    assert not pyramid.intersects_segment(point, point)


def test_segment_clearance_not_implemented(pyramid):
    with pytest.raises(NotImplementedError):
        pyramid.intersects_segment(
            Point3D(0, 5, 2),
            Point3D(10, 5, 2),
            clearance=0.5,
        )