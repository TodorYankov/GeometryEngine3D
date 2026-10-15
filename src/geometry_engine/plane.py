from dataclasses import dataclass

from geometry_engine.point import Point3D
from geometry_engine.vector import Vector3D


@dataclass(frozen=True)
class Plane3D:
    point: Point3D
    normal: Vector3D

    def __post_init__(self):
        if self.normal.magnitude() == 0:
            raise ValueError(
                "Plane normal vector cannot be zero."
            )

    def contains_point(
        self,
        point: Point3D,
        tolerance: float = 1e-9
    ) -> bool:
        displacement = Vector3D(
            point.x - self.point.x,
            point.y - self.point.y,
            point.z - self.point.z
        )

        return abs(self.normal.dot(displacement)) <= tolerance

    def distance_to_point(self, point: Point3D) -> float:
        displacement = Vector3D(
            point.x - self.point.x,
            point.y - self.point.y,
            point.z - self.point.z
        )

        return abs(self.normal.dot(displacement)) / self.normal.magnitude()