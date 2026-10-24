from geometry_engine.box import Box3D
from geometry_engine.point import Point3D


def path_has_collision(
    points: tuple[Point3D, ...],
    obstacle: Box3D,
) -> bool:
    """Check whether any segment of a path intersects an obstacle."""

    if not points:
        raise ValueError("A path must contain at least one point.")

    if len(points) == 1:
        return obstacle.contains_point(points[0])

    for i in range(len(points) - 1):
        start = points[i]
        end = points[i + 1]

        if obstacle.intersects_segment(start, end):
            return True

    return False