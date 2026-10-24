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