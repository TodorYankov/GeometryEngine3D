from dataclasses import dataclass

from geometry_engine.path import LinearPath3D
from geometry_engine.point import Point3D


@dataclass(frozen=True)
class MultiPointPath3D:
    """A piecewise linear path through multiple 3D points."""

    points: tuple[Point3D, ...]

    def __post_init__(self):
        if len(self.points) < 2:
            raise ValueError("A path requires at least two points.")

    def position(self, t: float) -> Point3D:
        """Calculate a position along the path for 0 <= t <= 1."""
        if not 0 <= t <= 1:
            raise ValueError("Parameter t must be between 0 and 1.")

        segment_count = len(self.points) - 1

        if t == 1:
            return self.points[-1]

        scaled_t = t * segment_count
        segment_index = int(scaled_t)
        local_t = scaled_t - segment_index

        segment = LinearPath3D(
            self.points[segment_index],
            self.points[segment_index + 1],
        )

        return segment.position(local_t)