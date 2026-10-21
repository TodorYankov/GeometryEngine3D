from dataclasses import dataclass

from geometry_engine.point import Point3D


@dataclass(frozen=True)
class LinearPath3D:
    """A linear path between two points in 3D space."""

    start: Point3D
    end: Point3D

    def position(self, t: float) -> Point3D:
        """Calculate a point along the path for 0 <= t <= 1."""
        if not 0 <= t <= 1:
            raise ValueError("Parameter t must be between 0 and 1.")

        return Point3D(
            x=self.start.x + t * (self.end.x - self.start.x),
            y=self.start.y + t * (self.end.y - self.start.y),
            z=self.start.z + t * (self.end.z - self.start.z),
        )