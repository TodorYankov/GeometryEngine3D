from dataclasses import dataclass

from geometry_engine.point import Point3D


@dataclass(frozen=True)
class Box3D:
    """An axis-aligned rectangular solid in 3D space."""

    min_point: Point3D
    max_point: Point3D

    def __post_init__(self):
        if (
            self.min_point.x >= self.max_point.x
            or self.min_point.y >= self.max_point.y
            or self.min_point.z >= self.max_point.z
        ):
            raise ValueError(
                "Maximum coordinates must be greater than minimum coordinates."
            )

    def dimensions(self) -> tuple[float, float, float]:
        """Return the width, depth, and height of the box."""
        return (
            self.max_point.x - self.min_point.x,
            self.max_point.y - self.min_point.y,
            self.max_point.z - self.min_point.z,
        )

    def volume(self) -> float:
        """Calculate the volume of the box."""
        a, b, c = self.dimensions()
        return a * b * c

    def surface_area(self) -> float:
        """Calculate the total surface area of the box."""
        a, b, c = self.dimensions()
        return 2 * (a * b + a * c + b * c)

    def contains_point(self, point: Point3D) -> bool:
        """Check whether a point is inside or on the box boundary."""
        return (
            self.min_point.x <= point.x <= self.max_point.x
            and self.min_point.y <= point.y <= self.max_point.y
            and self.min_point.z <= point.z <= self.max_point.z
        )

    def intersects_segment(self, start: Point3D, end: Point3D) -> bool:
        """Check whether a segment intersects or touches the box."""
        t_min = 0.0
        t_max = 1.0

        for axis in ("x", "y", "z"):
            start_value = getattr(start, axis)
            end_value = getattr(end, axis)
            direction = end_value - start_value

            lower = getattr(self.min_point, axis)
            upper = getattr(self.max_point, axis)

            if direction == 0:
                if start_value < lower or start_value > upper:
                    return False
                continue

            t1 = (lower - start_value) / direction
            t2 = (upper - start_value) / direction

            t_enter = min(t1, t2)
            t_exit = max(t1, t2)

            t_min = max(t_min, t_enter)
            t_max = min(t_max, t_exit)

            if t_min > t_max:
                return False

        return True