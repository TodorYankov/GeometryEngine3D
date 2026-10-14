from dataclasses import dataclass

from geometry_engine.point import Point3D
from geometry_engine.vector import Vector3D


@dataclass(frozen=True)
class Triangle3D:
    a: Point3D
    b: Point3D
    c: Point3D

    def __post_init__(self):
        if self.area() == 0:
            raise ValueError(
                "Three collinear points cannot form a triangle."
            )

    def side_lengths(self) -> tuple[float, float, float]:
        return (
            self.a.distance_to(self.b),
            self.b.distance_to(self.c),
            self.c.distance_to(self.a),
        )

    def perimeter(self) -> float:
        return sum(self.side_lengths())

    def area(self) -> float:
        ab = Vector3D(
            self.b.x - self.a.x,
            self.b.y - self.a.y,
            self.b.z - self.a.z,
        )

        ac = Vector3D(
            self.c.x - self.a.x,
            self.c.y - self.a.y,
            self.c.z - self.a.z,
        )

        return 0.5 * ab.cross(ac).magnitude()