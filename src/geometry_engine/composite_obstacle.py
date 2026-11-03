from __future__ import annotations

from dataclasses import dataclass
from typing import Protocol

from .point import Point3D


class Obstacle3D(Protocol):
    """Interface for 3D obstacles without safety clearance."""

    def contains_point(self, point: Point3D) -> bool:
        ...

    def intersects_segment(
        self,
        start: Point3D,
        end: Point3D,
    ) -> bool:
        ...


@dataclass(frozen=True)
class CompositeObstacle3D:
    """Union of multiple geometric obstacles."""

    obstacles: tuple[Obstacle3D, ...]

    def __init__(self, obstacles):
        items = tuple(obstacles)

        if not items:
            raise ValueError(
                "At least one obstacle is required."
            )

        object.__setattr__(self, "obstacles", items)

    @staticmethod
    def _validate_clearance(clearance: float) -> None:
        if clearance < 0:
            raise ValueError("Clearance cannot be negative.")

        if clearance != 0:
            raise NotImplementedError(
                "Composite obstacle clearance is not implemented."
            )

    def contains_point(
        self,
        point: Point3D,
        clearance: float = 0.0,
    ) -> bool:
        """Check if any obstacle contains the point."""
        self._validate_clearance(clearance)

        return any(
            obstacle.contains_point(point)
            for obstacle in self.obstacles
        )

    def intersects_segment(
        self,
        start: Point3D,
        end: Point3D,
        clearance: float = 0.0,
    ) -> bool:
        """Check if a segment intersects any obstacle."""
        self._validate_clearance(clearance)

        return any(
            obstacle.intersects_segment(start, end)
            for obstacle in self.obstacles
        )