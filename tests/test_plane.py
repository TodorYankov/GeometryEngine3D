import pytest
from geometry_engine.line import Line3D
from geometry_engine.point import Point3D
from geometry_engine.vector import Vector3D
from geometry_engine.plane import Plane3D


def test_plane_contains_point():
    plane = Plane3D(
        Point3D(0, 0, 0),
        Vector3D(0, 0, 1)
    )

    assert plane.contains_point(Point3D(3, 4, 0))


def test_plane_does_not_contain_point():
    plane = Plane3D(
        Point3D(0, 0, 0),
        Vector3D(0, 0, 1)
    )

    assert not plane.contains_point(Point3D(3, 4, 5))


def test_plane_with_nonzero_reference_point():
    plane = Plane3D(
        Point3D(1, 2, 3),
        Vector3D(0, 0, 1)
    )

    assert plane.contains_point(Point3D(5, 6, 3))


def test_plane_rejects_zero_normal():
    with pytest.raises(ValueError):
        Plane3D(
            Point3D(0, 0, 0),
            Vector3D(0, 0, 0)
        )

def test_distance_to_plane():
    plane = Plane3D(
        Point3D(0, 0, 0),
        Vector3D(0, 0, 1)
    )

    assert plane.distance_to_point(Point3D(3, 4, 5)) == pytest.approx(5.0)


def test_distance_of_point_on_plane():
    plane = Plane3D(
        Point3D(0, 0, 0),
        Vector3D(0, 0, 1)
    )

    assert plane.distance_to_point(Point3D(3, 4, 0)) == pytest.approx(0.0)


def test_distance_with_non_unit_normal():
    plane = Plane3D(
        Point3D(0, 0, 0),
        Vector3D(0, 0, 2)
    )

    assert plane.distance_to_point(Point3D(3, 4, 5)) == pytest.approx(5.0)

def test_line_plane_intersection():
    line = Line3D(
        Point3D(1, 2, 5),
        Vector3D(0, 0, -1)
    )

    plane = Plane3D(
        Point3D(0, 0, 0),
        Vector3D(0, 0, 1)
    )

    intersection = plane.intersect_line(line)

    assert intersection is not None
    assert intersection.x == pytest.approx(1)
    assert intersection.y == pytest.approx(2)
    assert intersection.z == pytest.approx(0)


def test_parallel_line_no_intersection():
    line = Line3D(
        Point3D(1, 2, 5),
        Vector3D(1, 0, 0)
    )

    plane = Plane3D(
        Point3D(0, 0, 0),
        Vector3D(0, 0, 1)
    )

    assert plane.intersect_line(line) is None


def test_line_contained_in_plane():
    line = Line3D(
        Point3D(1, 2, 0),
        Vector3D(1, 0, 0)
    )

    plane = Plane3D(
        Point3D(0, 0, 0),
        Vector3D(0, 0, 1)
    )

    with pytest.raises(
        ValueError,
        match="infinitely many intersection points"
    ):
        plane.intersect_line(line)