import pytest

from geometry_engine.point import Point3D
from geometry_engine.sphere import Sphere3D
from geometry_engine.sphere_path_planner import plan_path_around_sphere


def test_direct_path_without_collision():
    sphere = Sphere3D(Point3D(5, 5, 5), 2)

    start = Point3D(0, 9, 5)
    end = Point3D(10, 9, 5)

    path = plan_path_around_sphere(start, end, sphere)

    assert path == (start, end)


def test_path_avoids_sphere():
    sphere = Sphere3D(Point3D(5, 5, 5), 2)

    start = Point3D(0, 5, 5)
    end = Point3D(10, 5, 5)

    path = plan_path_around_sphere(start, end, sphere)

    assert len(path) > 2

    for a, b in zip(path, path[1:]):
        assert not sphere.intersects_segment(a, b, clearance=1)


def test_invalid_clearance():
    sphere = Sphere3D(Point3D(5, 5, 5), 2)

    with pytest.raises(ValueError):
        plan_path_around_sphere(
            Point3D(0, 5, 5),
            Point3D(10, 5, 5),
            sphere,
            clearance=-1,
        )


def test_start_inside_sphere():
    sphere = Sphere3D(Point3D(5, 5, 5), 2)

    with pytest.raises(ValueError):
        plan_path_around_sphere(
            Point3D(5, 5, 5),
            Point3D(10, 5, 5),
            sphere,
        )