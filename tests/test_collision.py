import pytest

from geometry_engine.box import Box3D
from geometry_engine.collision import path_has_collision
from geometry_engine.point import Point3D


@pytest.fixture
def obstacle():
    return Box3D(
        Point3D(3, 3, 2),
        Point3D(7, 7, 8),
    )


def test_direct_path_collision(obstacle):
    points = (
        Point3D(0, 5, 5),
        Point3D(10, 5, 5),
    )
    assert path_has_collision(points, obstacle)


def test_multipoint_path_collision(obstacle):
    points = (
        Point3D(0, 5, 5),
        Point3D(2, 5, 5),
        Point3D(10, 5, 5),
    )
    assert path_has_collision(points, obstacle)


def test_safe_path(obstacle):
    points = (
        Point3D(0, 5, 5),
        Point3D(0, 9, 5),
        Point3D(10, 9, 5),
        Point3D(10, 5, 5),
    )
    assert not path_has_collision(points, obstacle)


def test_path_touching_obstacle(obstacle):
    points = (
        Point3D(0, 5, 5),
        Point3D(3, 5, 5),
    )
    assert path_has_collision(points, obstacle)


def test_single_point_inside(obstacle):
    assert path_has_collision(
        (Point3D(5, 5, 5),), obstacle
    )


def test_single_point_outside(obstacle):
    assert not path_has_collision(
        (Point3D(0, 0, 0),), obstacle
    )


def test_empty_path(obstacle):
    with pytest.raises(ValueError):
        path_has_collision((), obstacle)