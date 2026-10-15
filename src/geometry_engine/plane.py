from dataclasses import dataclass
from geometry_engine.line import Line3D
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

    def intersect_line(self, line: Line3D) -> Point3D | None:
        denominator = self.normal.dot(line.direction)

        displacement = Vector3D(
            self.point.x - line.point.x,
            self.point.y - line.point.y,
            self.point.z - line.point.z
        )

        numerator = self.normal.dot(displacement)

        if abs(denominator) < 1e-12:
            if abs(numerator) < 1e-12:
                raise ValueError(
                    "The line lies entirely in the plane; "
                    "there are infinitely many intersection points."
                )

            return None

        t = numerator / denominator

        return line.point_at(t)