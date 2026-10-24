import pytest

from geometry_engine.box import Box3D
from geometry_engine.collision import path_has_collision
from geometry_engine.path_planner import plan_path
from geometry_engine.point import Point3D


def test_plan_path_around_obstacle():
    obstacle = Box3D(
        Point3D(3, 3, 2),
        Point3D(7, 7, 8),
    )

    start = Point3D(0, 5, 5)
    end = Point3D(10, 5, 5)

    path = plan_path(
        start,
        end,
        obstacle,
        clearance=1.0,
    )

    print("\nCalculated route:")
    for i, point in enumerate(path):
        print(f"P{i}: ({point.x}, {point.y}, {point.z})")

    assert len(path) >= 2
    assert (path[0].x, path[0].y, path[0].z) == (0, 5, 5)
    assert (path[-1].x, path[-1].y, path[-1].z) == (10, 5, 5)

    assert not path_has_collision(path, obstacle)