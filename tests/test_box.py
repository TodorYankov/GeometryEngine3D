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

def test_segment_passes_through_box():
    box = Box3D(Point3D(3, 3, 2), Point3D(7, 7, 8))

    start = Point3D(0, 5, 5)
    end = Point3D(10, 5, 5)

    assert box.intersects_segment(start, end)


def test_segment_outside_box():
    box = Box3D(Point3D(3, 3, 2), Point3D(7, 7, 8))

    start = Point3D(0, 0, 0)
    end = Point3D(10, 0, 0)

    assert not box.intersects_segment(start, end)


def test_segment_touches_box_face():
    box = Box3D(Point3D(3, 3, 2), Point3D(7, 7, 8))

    start = Point3D(0, 5, 5)
    end = Point3D(3, 5, 5)

    assert box.intersects_segment(start, end)


def test_segment_touches_box_edge():
    box = Box3D(Point3D(3, 3, 2), Point3D(7, 7, 8))

    start = Point3D(0, 3, 2)
    end = Point3D(10, 3, 2)

    assert box.intersects_segment(start, end)


def test_segment_above_box():
    box = Box3D(Point3D(3, 3, 2), Point3D(7, 7, 8))

    start = Point3D(0, 5, 10)
    end = Point3D(10, 5, 10)

    assert not box.intersects_segment(start, end)


def test_segment_starts_inside_box():
    box = Box3D(Point3D(3, 3, 2), Point3D(7, 7, 8))

    start = Point3D(5, 5, 5)
    end = Point3D(10, 5, 5)

    assert box.intersects_segment(start, end)


def test_segment_touches_box_vertex():
    box = Box3D(Point3D(3, 3, 2), Point3D(7, 7, 8))

    start = Point3D(0, 0, -1)
    end = Point3D(3, 3, 2)

    assert box.intersects_segment(start, end)


def test_zero_length_segment():
    box = Box3D(Point3D(3, 3, 2), Point3D(7, 7, 8))

    assert box.intersects_segment(
        Point3D(5, 5, 5),
        Point3D(5, 5, 5),
    )

    assert not box.intersects_segment(
        Point3D(0, 0, 0),
        Point3D(0, 0, 0),
    )