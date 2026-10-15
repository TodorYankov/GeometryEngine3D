import pytest
from geometry_engine.point import Point3D


def test_distance_between_two_points():
    point_a = Point3D(0, 0, 0)
    point_b = Point3D(1, 2, 2)

    assert point_a.distance_to(point_b) == 3.0

def test_point_translation():
    point = Point3D(2, 3, 4)

    moved_point = point.translate(5, -1, 2)

    assert moved_point.x == 7
    assert moved_point.y == 2
    assert moved_point.z == 6

    # The original point must remain unchanged.
    assert point.x == 2
    assert point.y == 3
    assert point.z == 4

    # Translation preserves the distance between points.
    assert point.distance_to(moved_point) == pytest.approx(
        (5**2 + (-1)**2 + 2**2) ** 0.5
    )

def test_point_scaling():
    point = Point3D(2, 3, 4)

    scaled_point = point.scale(2)

    assert scaled_point.x == 4
    assert scaled_point.y == 6
    assert scaled_point.z == 8

    # Original point remains unchanged.
    assert point.x == 2
    assert point.y == 3
    assert point.z == 4

    # Scaling by a factor of 2 doubles the distance.
    other = Point3D(5, 7, 8)
    scaled_other = other.scale(2)

    assert scaled_point.distance_to(
        scaled_other
    ) == pytest.approx(
        2 * point.distance_to(other)
    )