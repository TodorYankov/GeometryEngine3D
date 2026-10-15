from math import sqrt


class Point3D:
    """Represents a point in 3D Cartesian space."""

    def __init__(self, x: float, y: float, z: float):
        self.x = x
        self.y = y
        self.z = z

    def distance_to(self, other: "Point3D") -> float:
        """Calculate the Euclidean distance to another 3D point."""
        dx = other.x - self.x
        dy = other.y - self.y
        dz = other.z - self.z

        return sqrt(dx**2 + dy**2 + dz**2)

    def translate(self, dx: float, dy: float, dz: float) -> "Point3D":
        return Point3D(
            self.x + dx,
            self.y + dy,
            self.z + dz
        )

    def scale(self, factor: float) -> "Point3D":
        """Scale the point relative to the coordinate origin."""
        return Point3D(
            self.x * factor,
            self.y * factor,
            self.z * factor
        )

    def __repr__(self) -> str:
        return (
            f"Point3D(x={self.x}, "
            f"y={self.y}, "
            f"z={self.z})"
        )


