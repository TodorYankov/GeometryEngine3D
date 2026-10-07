from geometry_engine.point import Point3D


def test_distance_between_two_points():
    point_a = Point3D(0, 0, 0)
    point_b = Point3D(1, 2, 2)

    assert point_a.distance_to(point_b) == 3.0
