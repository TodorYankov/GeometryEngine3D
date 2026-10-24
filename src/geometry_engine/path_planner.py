from math import dist

from geometry_engine.box import Box3D
from geometry_engine.collision import path_has_collision
from geometry_engine.point import Point3D


def plan_path(
    start: Point3D,
    end: Point3D,
    obstacle: Box3D,
    clearance: float = 1.0,
) -> tuple[Point3D, ...]:
    """Find a collision-free path around one axis-aligned box."""

    if clearance <= 0:
        raise ValueError("Clearance must be positive.")

    if obstacle.contains_point(start) or obstacle.contains_point(end):
        raise ValueError("Start and goal must be outside the obstacle.")

    direct = (start, end)

    if not path_has_collision(direct, obstacle):
        return direct

    candidates = []

    for axis in ("x", "y", "z"):
        lower = getattr(obstacle.min_point, axis) - clearance
        upper = getattr(obstacle.max_point, axis) + clearance

        for value in (lower, upper):
            start_coords = [start.x, start.y, start.z]
            end_coords = [end.x, end.y, end.z]

            axis_index = ("x", "y", "z").index(axis)

            start_coords[axis_index] = value
            end_coords[axis_index] = value

            waypoint1 = Point3D(*start_coords)
            waypoint2 = Point3D(*end_coords)

            candidate = (
                start,
                waypoint1,
                waypoint2,
                end,
            )

            if not path_has_collision(candidate, obstacle):
                candidates.append(candidate)

    if not candidates:
        raise ValueError("No collision-free path found.")

    def path_length(points):
        return sum(
            dist(
                (a.x, a.y, a.z),
                (b.x, b.y, b.z),
            )
            for a, b in zip(points, points[1:])
        )

    return min(candidates, key=path_length)