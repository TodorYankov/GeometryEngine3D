from dataclasses import dataclass

from geometry_engine.point import Point3D


@dataclass(frozen=True)
class Sphere3D:
    """A sphere defined by its center and radius."""

    center: Point3D
    radius: float

    def __post_init__(self):
        if self.radius <= 0:
            raise ValueError("Sphere radius must be positive.")

    def contains_point(self, point: Point3D) -> bool:
        """Check whether a point lies inside or on the sphere."""
        dx = point.x - self.center.x
        dy = point.y - self.center.y
        dz = point.z - self.center.z

        distance_squared = dx**2 + dy**2 + dz**2

        return distance_squared <= self.radius**2

    def intersects_segment(
        self,
        start: Point3D,
        end: Point3D,
        clearance: float = 0.0,
    ) -> bool:
        """Check whether a segment intersects the inflated sphere."""
        if clearance < 0:
            raise ValueError("Clearance cannot be negative.")

        effective_radius = self.radius + clearance

        dx = end.x - start.x
        dy = end.y - start.y
        dz = end.z - start.z

        length_squared = dx**2 + dy**2 + dz**2

        if length_squared == 0:
            t = 0.0
        else:
            t = (
                (self.center.x - start.x) * dx
                + (self.center.y - start.y) * dy
                + (self.center.z - start.z) * dz
            ) / length_squared

            t = max(0.0, min(1.0, t))

        closest_x = start.x + t * dx
        closest_y = start.y + t * dy
        closest_z = start.z + t * dz

        distance_squared = (
            (closest_x - self.center.x) ** 2
            + (closest_y - self.center.y) ** 2
            + (closest_z - self.center.z) ** 2
        )

        return distance_squared <= effective_radius**2