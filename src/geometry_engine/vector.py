from dataclasses import dataclass
from math import sqrt


@dataclass(frozen=True)
class Vector3D:
    x: float
    y: float
    z: float

    def magnitude(self) -> float:
        """Calculate the Euclidean length of the vector."""
        return sqrt(self.x**2 + self.y**2 + self.z**2)

    def dot(self, other: "Vector3D") -> float:
        """Calculate the dot product of two vectors."""
        return (
            self.x * other.x
            + self.y * other.y
            + self.z * other.z
        )

    def __add__(self, other: "Vector3D") -> "Vector3D":
        """Add two 3D vectors."""
        return Vector3D(
            self.x + other.x,
            self.y + other.y,
            self.z + other.z
        )

    def __sub__(self, other: "Vector3D") -> "Vector3D":
        """Subtract two 3D vectors."""
        return Vector3D(
            self.x - other.x,
            self.y - other.y,
            self.z - other.z
        )

    def cross(self, other: "Vector3D") -> "Vector3D":
        """Calculate the cross product of two 3D vectors."""
        return Vector3D(
            self.y * other.z - self.z * other.y,
            self.z * other.x - self.x * other.z,
            self.x * other.y - self.y * other.x
        )
