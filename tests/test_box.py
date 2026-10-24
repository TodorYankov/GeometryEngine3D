import pytest

from geometry_engine.box import Box3D
from geometry_engine.point import Point3D


def test_dimensions():
    box = Box3D(Point3D(3, 3, 2), Point3D(7, 7, 8))
    assert box.dimensions() == (4, 4, 6)


def test_volume():
    box = Box3D(Point3D(3, 3, 2), Point3D(7, 7, 8))
    assert box.volume() == 96


def test_surface_area():
    box = Box3D(Point3D(3, 3, 2), Point3D(7, 7, 8))
    assert box.surface_area() == 128


def test_point_inside():
    box = Box3D(Point3D(3, 3, 2), Point3D(7, 7, 8))
    assert box.contains_point(Point3D(5, 5, 5))


def test_point_on_boundary():
    box = Box3D(Point3D(3, 3, 2), Point3D(7, 7, 8))
    assert box.contains_point(Point3D(3, 5, 5))


def test_point_outside():
    box = Box3D(Point3D(3, 3, 2), Point3D(7, 7, 8))
    assert not box.contains_point(Point3D(9, 5, 5))


def test_invalid_box():
    with pytest.raises(ValueError):
        Box3D(Point3D(7, 3, 2), Point3D(3, 7, 8))