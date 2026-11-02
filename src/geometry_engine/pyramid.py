from __future__ import annotations

from dataclasses import dataclass
from math import sqrt

from .point import Point3D


@dataclass(frozen=True)
class Pyramid3D:
    """A right square pyramid with a horizontal base."""

    center_x: float
    center_y: float
    base_z: float
    base_size: float
    height: float

    def __post_init__(self) -> None:
        if self.base_size <= 0:
            raise ValueError("Base size must be positive.")
        if self.height <= 0:
            raise ValueError("Height must be positive.")

    @property
    def apex(self) -> Point3D:
        return Point3D(
            self.center_x,
            self.center_y,
            self.base_z + self.height,
        )

    @property
    def volume(self) -> float:
        return self.base_size**2 * self.height / 3

    @property
    def surface_area(self) -> float:
        slant_height = sqrt(
            self.height**2 + (self.base_size / 2) ** 2
        )
        return (
            self.base_size**2
            + 2 * self.base_size * slant_height
        )

    def contains_point(
        self,
        point: Point3D,
        clearance: float = 0.0,
    ) -> bool:
        """Check whether a point is inside or on the pyramid.

        Clearance is not implemented for this shape yet.
        """
        if clearance != 0:
            raise NotImplementedError(
                "Pyramid clearance is not implemented yet."
            )

        z = point.z - self.base_z

        if z < 0 or z > self.height:
            return False

        half_width = (
            self.base_size / 2 * (1 - z / self.height)
        )

        return (
            abs(point.x - self.center_x) <= half_width
            and abs(point.y - self.center_y) <= half_width
        )

    def intersects_segment(
            self,
            start: Point3D,
            end: Point3D,
            clearance: float = 0.0,
    ) -> bool:
        """Check intersection with the closed square pyramid.

        Uses clipping against five half-spaces.
        Boundary contact counts as an intersection.
        """
        if clearance != 0:
            raise NotImplementedError(
                "Pyramid clearance is not implemented yet."
            )

        a = self.base_size / 2
        h = self.height

        # Local coordinates relative to the base center.
        x0 = start.x - self.center_x
        y0 = start.y - self.center_y
        z0 = start.z - self.base_z

        dx = end.x - start.x
        dy = end.y - start.y
        dz = end.z - start.z

        # Each half-space has the form:
        # nx*x + ny*y + nz*z <= limit
        planes = (
            (0.0, 0.0, -1.0, 0.0),
            (1.0, 0.0, a / h, a),
            (-1.0, 0.0, a / h, a),
            (0.0, 1.0, a / h, a),
            (0.0, -1.0, a / h, a),
        )

        t_enter = 0.0
        t_exit = 1.0

        for nx, ny, nz, limit in planes:
            numerator = limit - (
                    nx * x0 + ny * y0 + nz * z0
            )
            denominator = (
                    nx * dx + ny * dy + nz * dz
            )

            if abs(denominator) < 1e-12:
                if numerator < -1e-12:
                    return False
                continue

            t = numerator / denominator

            if denominator < 0:
                t_enter = max(t_enter, t)
            else:
                t_exit = min(t_exit, t)

            if t_enter > t_exit + 1e-12:
                return False

        return True