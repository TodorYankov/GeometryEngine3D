# GeometryEngine3D

GeometryEngine3D is a mathematical engine for defining, calculating,
transforming, simulating, and visualizing motion trajectories in
three-dimensional space.

The project explores the mathematical foundations of 3D geometry using Python,
with a focus on points, vectors, distances, transformations, and trajectories.

A moving object is represented as a point in 3D Cartesian space:

\[
P = (x, y, z)
\]

The engine is designed as a general mathematical model rather than for one
specific machine. Possible applications include robotic arms, drones, CNC
machines, cameras, and other systems that move through three-dimensional space.

## Current Features

Representation of points in three-dimensional Cartesian space using Point3D.

Calculation of Euclidean distances between 3D points.

Representation of 3D vectors using Vector3D.

Vector magnitude, addition, and subtraction.

Dot product and cross product calculations.

Mathematical modeling of a moving point using Trajectory3D.

Position calculation along the parametric trajectory:
$$
\mathbf{r}(t) = (t^2, 2t, \sin t)
$$

Automated verification using pytest (12 passing tests).

## Future Extensions

GeometryEngine3D may be extended in the future with Data Science, Machine Learning, and Deep Learning techniques.
