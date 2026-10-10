from dataclasses import dataclass
from math import sin

from geometry_engine.point import Point3D


@dataclass(frozen=True)
class Trajectory3D:
    """A parametric trajectory in 3D space."""

    def position(self, t: float) -> Point3D:
        """Calculate the position at time t."""
        return Point3D(
            x=t**2,
            y=2 * t,
            z=sin(t)
        )
