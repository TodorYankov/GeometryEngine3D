from dataclasses import dataclass

from geometry_engine.point import Point3D
from geometry_engine.vector import Vector3D


@dataclass(frozen=True)
class Line3D:
    point: Point3D
    direction: Vector3D

    def __post_init__(self):
        if self.direction.magnitude() == 0:
            raise ValueError("Direction vector cannot be zero.")

    def point_at(self, t: float) -> Point3D:
        return Point3D(
            self.point.x + t * self.direction.x,
            self.point.y + t * self.direction.y,
            self.point.z + t * self.direction.z,
        )
