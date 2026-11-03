import pytest

from geometry_engine.point import Point3D
from geometry_engine.box import Box3D
from geometry_engine.sphere import Sphere3D
from geometry_engine.pyramid import Pyramid3D
from geometry_engine.composite_obstacle import CompositeObstacle3D


@pytest.fixture
def composite():
    return CompositeObstacle3D([
        Box3D(
            Point3D(0, 0, 0),
            Point3D(2, 2, 2),
        ),
        Sphere3D(
            Point3D(5, 1, 1),
            1,
        ),
        Pyramid3D(
            center_x=9,
            center_y=1,
            base_z=0,
            base_size=2,
            height=3,
        ),
    ])


def test_point_inside_box(composite):
    assert composite.contains_point(Point3D(1, 1, 1))


def test_point_inside_sphere(composite):
    assert composite.contains_point(Point3D(5, 1, 1))


def test_point_inside_pyramid(composite):
    assert composite.contains_point(Point3D(9, 1, 1))


def test_point_outside_all(composite):
    assert not composite.contains_point(
        Point3D(20, 20, 20)
    )


def test_segment_through_multiple_shapes(composite):
    assert composite.intersects_segment(
        Point3D(-2, 1, 1),
        Point3D(11, 1, 1),
    )


def test_segment_misses_all(composite):
    assert not composite.intersects_segment(
        Point3D(-2, 10, 10),
        Point3D(11, 10, 10),
    )


def test_empty_composite_rejected():
    with pytest.raises(ValueError):
        CompositeObstacle3D([])


def test_negative_clearance_rejected(composite):
    with pytest.raises(ValueError):
        composite.intersects_segment(
            Point3D(0, 0, 0),
            Point3D(10, 0, 0),
            clearance=-1,
        )

def test_positive_clearance_point_not_implemented(composite):
    with pytest.raises(NotImplementedError):
        composite.contains_point(
            Point3D(1, 1, 1),
            clearance=0.5,
        )


def test_positive_clearance_segment_not_implemented(composite):
    with pytest.raises(NotImplementedError):
        composite.intersects_segment(
            Point3D(-2, 1, 1),
            Point3D(11, 1, 1),
            clearance=0.5,
        )