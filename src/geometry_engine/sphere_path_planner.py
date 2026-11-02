import math

from geometry_engine.point import Point3D
from geometry_engine.sphere import Sphere3D


def _distance(a: Point3D, b: Point3D) -> float:
    return math.dist(
        (a.x, a.y, a.z),
        (b.x, b.y, b.z),
    )


def _is_safe(path, sphere, clearance):
    return all(
        not sphere.intersects_segment(a, b, clearance)
        for a, b in zip(path, path[1:])
    )


def plan_path_around_sphere(
    start: Point3D,
    end: Point3D,
    sphere: Sphere3D,
    clearance: float = 1.0,
    samples: int = 24,
) -> tuple[Point3D, ...]:
    """
    Find a collision-free polygonal route around a sphere.

    Uses sampled waypoint candidates and collision checking.
    Does not guarantee the globally shortest path.
    """
    if clearance < 0:
        raise ValueError("Clearance cannot be negative.")

    if samples < 4:
        raise ValueError("At least 4 samples are required.")

    radius = sphere.radius + clearance

    for point in (start, end):
        if _distance(point, sphere.center) <= radius:
            raise ValueError(
                "Start and end must lie outside the inflated sphere."
            )

    if not sphere.intersects_segment(start, end, clearance):
        return (start, end)

    # Construct an orthonormal basis perpendicular to the
    # direction from start to end.
    dx = end.x - start.x
    dy = end.y - start.y
    dz = end.z - start.z

    length = math.sqrt(dx * dx + dy * dy + dz * dz)
    direction = (dx / length, dy / length, dz / length)

    reference = (
        (0.0, 0.0, 1.0)
        if abs(direction[2]) < 0.9
        else (0.0, 1.0, 0.0)
    )

    ux = direction[1] * reference[2] - direction[2] * reference[1]
    uy = direction[2] * reference[0] - direction[0] * reference[2]
    uz = direction[0] * reference[1] - direction[1] * reference[0]

    norm = math.sqrt(ux * ux + uy * uy + uz * uz)
    u = (ux / norm, uy / norm, uz / norm)

    v = (
        direction[1] * u[2] - direction[2] * u[1],
        direction[2] * u[0] - direction[0] * u[2],
        direction[0] * u[1] - direction[1] * u[0],
    )

    # Sample candidate bypass directions.
    candidates = []
    margin = max(0.05, radius * 0.05)
    offset = radius + margin

    for i in range(samples):
        angle = 2 * math.pi * i / samples

        nx = math.cos(angle) * u[0] + math.sin(angle) * v[0]
        ny = math.cos(angle) * u[1] + math.sin(angle) * v[1]
        nz = math.cos(angle) * u[2] + math.sin(angle) * v[2]

        waypoint1 = Point3D(
            start.x + offset * nx,
            start.y + offset * ny,
            start.z + offset * nz,
        )
        waypoint2 = Point3D(
            end.x + offset * nx,
            end.y + offset * ny,
            end.z + offset * nz,
        )

        path = (start, waypoint1, waypoint2, end)

        if _is_safe(path, sphere, clearance):
            candidates.append(path)

    if not candidates:
        raise ValueError(
            "No collision-free route found with sampled candidates."
        )

    return min(
        candidates,
        key=lambda path: sum(
            _distance(a, b)
            for a, b in zip(path, path[1:])
        ),
    )