from math import pi

import pytest

from geometry_engine.trajectory import Trajectory3D


def test_position_at_zero():
    trajectory = Trajectory3D()
    point = trajectory.position(0)

    assert point.x == pytest.approx(0)
    assert point.y == pytest.approx(0)
    assert point.z == pytest.approx(0)


def test_position_at_one():
    trajectory = Trajectory3D()
    point = trajectory.position(1)

    assert point.x == pytest.approx(1)
    assert point.y == pytest.approx(2)
    assert point.z == pytest.approx(0.8414709848)


def test_position_at_pi():
    trajectory = Trajectory3D()
    point = trajectory.position(pi)

    assert point.x == pytest.approx(pi**2)
    assert point.y == pytest.approx(2 * pi)
    assert point.z == pytest.approx(0, abs=1e-12)


def test_position_at_negative_time():
    trajectory = Trajectory3D()
    point = trajectory.position(-1)

    assert point.x == pytest.approx(1)
    assert point.y == pytest.approx(-2)
    assert point.z == pytest.approx(-0.8414709848)
