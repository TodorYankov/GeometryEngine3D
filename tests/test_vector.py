import pytest

from geometry_engine.vector import Vector3D


def test_vector_magnitude():
    vector = Vector3D(3, 4, 0)

    assert vector.magnitude() == pytest.approx(5.0)


def test_dot_product():
    a = Vector3D(3, 4, 0)
    b = Vector3D(1, 2, 3)

    assert a.dot(b) == pytest.approx(11.0)


def test_zero_vector():
    vector = Vector3D(0, 0, 0)

    assert vector.magnitude() == pytest.approx(0.0)


def test_perpendicular_vectors():
    a = Vector3D(1, 0, 0)
    b = Vector3D(0, 1, 0)

    assert a.dot(b) == pytest.approx(0.0)
def test_vector_addition():
    a = Vector3D(3, 4, 0)
    b = Vector3D(1, 2, 3)

    assert a + b == Vector3D(4, 6, 3)


def test_vector_subtraction():
    a = Vector3D(3, 4, 0)
    b = Vector3D(1, 2, 3)

    assert a - b == Vector3D(2, 2, -3)

def test_cross_product():
    a = Vector3D(3, 4, 0)
    b = Vector3D(1, 2, 3)

    assert a.cross(b) == Vector3D(12, -9, 2)
