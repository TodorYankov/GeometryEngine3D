import pytest

from geometry_engine.point import Point3D
from geometry_engine.sphere import Sphere3D


def test_point_inside_sphere():
    sphere = Sphere3D(Point3D(5, 5, 5), 2)
    assert sphere.contains_point(Point3D(6, 5, 5))


def test_point_outside_sphere():
    sphere = Sphere3D(Point3D(5, 5, 5), 2)
    assert not sphere.contains_point(Point3D(8, 5, 5))


def test_segment_intersects_sphere():
    sphere = Sphere3D(Point3D(5, 5, 5), 2)
    assert sphere.intersects_segment(
        Point3D(0, 5, 5),
        Point3D(10, 5, 5),
    )


def test_segment_avoids_sphere():
    sphere = Sphere3D(Point3D(5, 5, 5), 2)
    assert not sphere.intersects_segment(
        Point3D(0, 9, 5),
        Point3D(10, 9, 5),
    )


def test_clearance_detects_collision():
    sphere = Sphere3D(Point3D(5, 5, 5), 2)

    start = Point3D(0, 8, 5)
    end = Point3D(10, 8, 5)

    assert not sphere.intersects_segment(start, end)
    assert sphere.intersects_segment(start, end, clearance=1)


def test_invalid_radius():
    with pytest.raises(ValueError):
        Sphere3D(Point3D(0, 0, 0), 0)


def test_zero_length_segment():
    sphere = Sphere3D(Point3D(5, 5, 5), 2)
    point = Point3D(5, 5, 5)

    assert sphere.intersects_segment(point, point)
