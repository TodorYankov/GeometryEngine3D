# GeometryEngine3D

**3D Motion Planning, Collision Detection, and Obstacle Avoidance**

GeometryEngine3D is a Python project for mathematical modeling, trajectory planning, and collision detection in three-dimensional space.

The project's practical goal is to calculate a path between two points, detect whether it intersects a solid obstacle, and generate and visualize an alternative collision-free route. It combines Euclidean geometry, vector algebra, analytic geometry, numerical experiments, automated tests, and Jupyter Notebook visualizations.

The motion-planning demonstrations model a moving **point** and one obstacle at a time: either an **axis-aligned rectangular solid (Box3D)** or a **sphere (Sphere3D)**. These are geometric simulations, not physical vehicle controllers.

## 1. Project Objectives

- Represent points, vectors, lines, triangles, planes, rectangular solids, and spheres in 3D.
- Perform geometric calculations and transformations.
- Construct linear and multipoint trajectories using parametric equations.
- Detect intersections and first contact points between trajectories and solid obstacles.
- Generate and verify collision-free candidate routes.
- Compare the lengths of direct and planned paths.
- Visualize geometric objects and animate movement in 3D.
- Validate implementations using automated tests.

## 2. Mathematical Models and Implemented Features

### 2.1 Point3D

A point in Cartesian space is represented by $P=(x,y,z)$. The `Point3D` class supports distance calculation, translation, and scaling.

$$
d(A,B)=\sqrt{(x_2-x_1)^2+(y_2-y_1)^2+(z_2-z_1)^2}
$$

### 2.2 Vector3D

The `Vector3D` class supports vector magnitude, addition, subtraction, dot product, and cross product.

$$
|\vec v|=\sqrt{x^2+y^2+z^2}
$$

$$
\vec a\cdot\vec b=a_xb_x+a_yb_y+a_zb_z
$$

### 2.3 Trajectory3D

`Trajectory3D` models a point's position with a parametric equation:

$$
\mathbf r(t)=(t^2,2t,\sin t)
$$

### 2.4 Line3D

`Line3D` represents a line using a point and direction vector:

$$
\mathbf r(t)=P_0+t\vec v
$$

### 2.5 Triangle3D

`Triangle3D` calculates side lengths, perimeter, and area. The area of a triangle with vertices $A,B,C$ is:

$$
S=\frac12\left|(\vec B-\vec A)\times(\vec C-\vec A)\right|
$$

### 2.6 Plane3D

`Plane3D` supports plane representation, point membership, point-to-plane distance, and line-plane intersections. A plane can be written as:

$$
ax+by+cz+d=0
$$

### 2.7 LinearPath3D

`LinearPath3D` interpolates between two points:

$$
P(t)=(1-t)P_0+tP_1,\qquad 0\leq t\leq1
$$

### 2.8 MultiPointPath3D

`MultiPointPath3D` constructs a continuous piecewise linear trajectory through multiple control points:

$$
P_0\rightarrow P_1\rightarrow\cdots\rightarrow P_n
$$

Each segment receives an equal interval of the global interpolation parameter.

### 2.9 Box3D

`Box3D` models an axis-aligned rectangular solid defined by two opposite corners:

$$
P_{\min}=(x_{\min},y_{\min},z_{\min}),\qquad
P_{\max}=(x_{\max},y_{\max},z_{\max})
$$

It supports dimension validation, volume, surface area, point containment, segment intersection, and first contact point calculations.

For side lengths $a,b,c$:

$$
V=abc,\qquad S=2(ab+ac+bc)
$$

For corners $(3,3,2)$ and $(7,7,8)$, the dimensions are $(4,4,6)$, the volume is $96$, and the surface area is $128$.

### 2.10 Collision Detection

The project detects intersections between a line segment and an axis-aligned rectangular solid using the slab intersection method. A segment is represented as:

$$
P(t)=A+t(B-A),\qquad 0\leq t\leq1
$$

- `Box3D.intersects_segment()` checks intersection or contact with a box.
- `Box3D.first_contact()` calculates the first contact point.
- `path_has_collision()` checks all consecutive segments of a multipoint path.

A path is considered colliding if any of its segments intersects or touches the obstacle.

### 2.11 Sphere3D and Spherical Collision Detection

`Sphere3D` represents a sphere with center $C=(c_x,c_y,c_z)$ and radius $r>0$. A point $P$ lies inside or on the sphere when:

$$
\|P-C\|^2\leq r^2
$$

For a segment $P(t)=A+t(B-A)$, $0\leq t\leq1$, the closest point to the sphere center is found using the clamped projection parameter:

$$
t^*=\max\left(0,\min\left(1,\frac{(C-A)\cdot(B-A)}{\|B-A\|^2}\right)\right)
$$

A collision (including boundary contact) occurs when $\|P(t^*)-C\|\leq r+c$, where $c\geq0$ is the safety clearance. Zero-length segments are handled separately.

### 2.12 Automatic Path Planning

`plan_path()` attempts to find a route around one rectangular obstacle:

1. Check the direct path for a collision.
2. If the direct path is clear, return it.
3. Otherwise, generate alternative candidate routes using a specified clearance.
4. Reject candidates that collide with the obstacle.
5. Select the shortest among the remaining candidates.

**Limitation:** This is a candidate-based planner for one axis-aligned box. It does **not** guarantee a globally shortest route, and it may fail to find a path even if another valid route exists.

### 2.13 Spherical Obstacle Avoidance

`plan_path_around_sphere()` first tests whether the direct segment is clear. If blocked, it samples lateral bypass directions in a plane perpendicular to the start-to-end direction, constructs four-point candidate routes, rejects those intersecting the **inflated sphere** (radius $R=r+c$), and selects the shortest valid candidate. The planner requires start and end points outside the inflated sphere.

This is a **sampling-based heuristic for one sphere**, not a complete or globally optimal motion planner. Failure to find a candidate does not prove that no collision-free route exists.

## 3. Project Structure

```text
GeometryEngine3D/
├── docs/
│   └── geometry3d_obstacle_avoidance.gif
├── notebooks/
│   ├── 01_points_and_vectors.ipynb
│   ├── 02_lines_and_triangles.ipynb
│   ├── 03_planes_and_transformations.ipynb
│   └── 04_trajectory_planning.ipynb
├── src/
│   └── geometry_engine/
│       ├── point.py
│       ├── vector.py
│       ├── trajectory.py
│       ├── line.py
│       ├── triangle.py
│       ├── plane.py
│       ├── path.py
│       ├── multipoint_path.py
│       ├── box.py
│       ├── collision.py
│       ├── path_planner.py
│       ├── sphere.py
│       └── sphere_path_planner.py
├── tests/
│   ├── test_point.py
│   ├── test_vector.py
│   ├── test_trajectory.py
│   ├── test_line.py
│   ├── test_triangle.py
│   ├── test_plane.py
│   ├── test_path.py
│   ├── test_multipoint_path.py
│   ├── test_box.py
│   ├── test_collision.py
│   ├── test_path_planner.py
│   ├── test_sphere.py
│   └── test_sphere_path_planner.py
├── .gitignore
├── pyproject.toml
├── requirements.txt
└── README.md
```

## 4. Jupyter Notebooks

| Notebook | Content |
|---|---|
| [01 — Points and Vectors](notebooks/01_points_and_vectors.ipynb) | Points, vectors, and Euclidean geometry |
| [02 — Lines and Triangles](notebooks/02_lines_and_triangles.ipynb) | Lines, triangles, and geometric calculations |
| [03 — Planes and Transformations](notebooks/03_planes_and_transformations.ipynb) | Planes and geometric transformations |
| [04 — Trajectory Planning](notebooks/04_trajectory_planning.ipynb) | Multipoint paths, box and sphere collision detection, obstacle avoidance, Monte Carlo experiments, 3D visualization, and animation |

## 5. Multipoint Trajectory Experiment

A trajectory passes through four control points:

$$
P_0=(0,0,0),\quad P_1=(6,0,0),\quad P_2=(6,8,0),\quad P_3=(6,8,10)
$$

The total length is:

$$
L=\sum_{i=0}^{n-1}\|P_{i+1}-P_i\|=6+8+10=24
$$

### 5.1 Speed Analysis

With equal parameter intervals and an assumed total travel time of one second, each of the three segments takes $\Delta t=1/3$ second.

$$
v_i=\frac{L_i}{\Delta t}
$$

| Segment | Length | Speed (units/s) |
|---|---:|---:|
| P0 → P1 | 6 | 18 |
| P1 → P2 | 8 | 24 |
| P2 → P3 | 10 | 30 |

Equal time intervals do not guarantee constant speed when segment lengths differ.

## 6. 3D Collision Detection Experiment

Consider a direct trajectory from $A=(0,5,5)$ to $B=(10,5,5)$:

$$
P(t)=(10t,5,5),\qquad 0\leq t\leq1
$$

The obstacle occupies:

$$
3\leq x\leq7,\qquad 3\leq y\leq7,\qquad 2\leq z\leq8
$$

The program calculates:

```text
Collision detected: True
First contact point: Point3D(x=3.0, y=5.0, z=5.0)
```

Thus the first contact occurs at $P_{\text{contact}}=(3,5,5)$.

## 7. Automatic Obstacle Avoidance Experiment

For the same start, goal, and obstacle, the planner generates:

| Point | Coordinates |
|---|---|
| P0 | (0, 5, 5) |
| P1 | (0, 2, 5) |
| P2 | (10, 2, 5) |
| P3 | (10, 5, 5) |

The middle segment lies on $y=2$, one unit away from the box's minimum $y$ boundary. The path collision checker returns `False`.

### 7.1 Path Length Comparison

$$
L_{\text{direct}}=10
$$

$$
L_{\text{planned}}=3+10+3=16
$$

$$
\text{Additional distance}=\frac{16-10}{10}\cdot100\%=60\%
$$

| Property | Direct Path | Planned Path |
|---|---:|---:|
| Path length | 10 | 16 |
| Collision detected | Yes | No |
| Number of segments | 1 | 3 |

The generated route is 60% longer but avoids the obstacle. This demonstrates the trade-off between travel distance and collision avoidance; it does not establish global optimality.

## 8. 3D Visualization and Animation

The fourth notebook visualizes a solid obstacle, a direct colliding path, a planned collision-free path, the first contact point, and start and goal positions.

### 8.1 Animated Demonstration

![GeometryEngine3D — Animated Obstacle Avoidance](docs/geometry3d_obstacle_avoidance.gif)

The animation samples the planned path at equal distance intervals and shows a point moving along it. This is a geometric animation rather than a physical simulation of acceleration, forces, or vehicle dynamics.

See [Notebook 04 — Trajectory Planning](notebooks/04_trajectory_planning.ipynb) for the calculations, plots, and animation code.

## 9. Spherical Obstacle Avoidance Experiment

The notebook studies a sphere centered at $C=(5,5,5)$ with radius $r=2$ and safety clearance $c=1$, between $A=(0,5,5)$ and $B=(10,5,5)$. The effective collision radius is $R=3$.

| Metric | Result |
|---|---:|
| Direct path length | 10.000 |
| Selected collision-free candidate length | 16.300 |
| Additional distance | 6.300 (63.0%) |
| Path points | 4 |
| Segment collision check with clearance | No collision |

The 3D plot shows the physical sphere, a transparent orange safety boundary, the intersecting direct segment, and the verified bypass. The chosen candidate is not claimed to be the globally shortest route.

### 9.1 Monte Carlo Experiment (Box3D)

The notebook also evaluates the box planner using **1,000 randomly generated axis-aligned box obstacles** under the documented sampling setup. In that experiment, **386** direct routes were blocked; the planner produced verified detours for all **386** blocked cases. This is an empirical result for the chosen obstacle distribution, **not** a general success-rate guarantee for arbitrary environments or multiple obstacles.

## 10. Automated Testing

The project uses `pytest` to verify geometric operations, path interpolation, solid geometry, segment-box and segment-sphere intersections, contact detection, multipoint collision checks, and box/sphere path planning.

Run from the project root:

```bash
python -m pytest -q
```

Latest locally verified result (2 November 2026):

```text
89 passed in 0.19s
```

## 11. Installation and Usage

Python 3.12 or newer is required.

```bash
git clone https://github.com/TodorYankov/GeometryEngine3D.git
cd GeometryEngine3D
python -m venv .venv
```

Activate on Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

Install the project and test dependencies:

```bash
python -m pip install -e .
python -m pip install -r requirements.txt
```

For notebooks, plotting, and GIF export:

```bash
python -m pip install jupyter matplotlib numpy pillow
```

### 11.1 Multipoint Trajectory Example

```python
from geometry_engine.point import Point3D
from geometry_engine.multipoint_path import MultiPointPath3D

points = (
    Point3D(0, 0, 0),
    Point3D(6, 0, 0),
    Point3D(6, 8, 0),
    Point3D(6, 8, 10),
)

path = MultiPointPath3D(points)
position = path.position(0.5)
print(position)
```

Expected coordinates: `(6.0, 4.0, 0.0)`.

### 11.2 Automatic Obstacle Avoidance Example

```python
from geometry_engine.point import Point3D
from geometry_engine.box import Box3D
from geometry_engine.collision import path_has_collision
from geometry_engine.path_planner import plan_path

obstacle = Box3D(Point3D(3, 3, 2), Point3D(7, 7, 8))
start = Point3D(0, 5, 5)
goal = Point3D(10, 5, 5)

safe_path = plan_path(start, goal, obstacle, clearance=1.0)

for point in safe_path:
    print(point)

print("Collision detected:", path_has_collision(safe_path, obstacle))
```

Expected final line:

```text
Collision detected: False
```

## 12. Methodology

1. Define a geometric problem and its assumptions.
2. Express the problem using mathematical models.
3. Implement the algorithms in Python.
4. Construct tests with known results and boundary cases.
5. Compare computed results with expectations.
6. Visualize experiments in Jupyter Notebooks.
7. Analyze results, trade-offs, and limitations.

The experiments investigate whether piecewise linear routes can connect two points without intersecting a rectangular solid or a sphere, and how safety clearance changes the resulting path.

## 13. Limitations

- Implemented obstacles are axis-aligned rectangular solids and spheres; each planner supports its own obstacle type.
- The planner handles one obstacle at a time.
- Generated routes consist of straight segments.
- The planner does not guarantee globally optimal routes or completeness.
- The moving object is treated as a point without physical dimensions.
- Forces, acceleration, turning constraints, and vehicle dynamics are not modeled.
- The current simulation does not model transitions between air, water, and other physical media.

## 14. Conclusions

GeometryEngine3D demonstrates how three-dimensional geometry can support a practical motion-planning task. In the box example, a direct path of length 10 intersects the obstacle while a planned path of length 16 avoids it. In the sphere example, the selected collision-free candidate has length 16.300 compared with a direct length of 10. Both examples are checked for collisions and visualized in 3D. The Monte Carlo box experiment provides additional empirical validation under a specific randomized setup.

The project connects mathematical definitions with implemented algorithms, automated verification, and reproducible experiments. Its planners are heuristic and their limitations are explicitly documented.

## 15. References

1. **Weisstein, Eric W.**  
   *MathWorld — A Wolfram Web Resource.*  
   https://mathworld.wolfram.com/  
   Mathematical reference for Euclidean geometry, vectors,
   planes, and three-dimensional solids.

2. **Ericson, Christer. (2005).**  
   *Real-Time Collision Detection.* Morgan Kaufmann.  
   https://realtimecollisiondetection.net/  
   Reference for geometric intersection tests,
   bounding volumes, and collision detection.

3. **LaValle, Steven M. (2006).**  
   *Planning Algorithms.* Cambridge University Press.  
   https://lavalle.pl/planning/  
   Reference for motion planning, path planning,
   and obstacle avoidance.

4. **Python Software Foundation.**  
   *Python 3 Documentation.*  
   https://docs.python.org/3/

5. **Matplotlib Development Team.**  
   *Matplotlib Documentation.*  
   https://matplotlib.org/stable/

6. **NumPy Developers.**  
   *NumPy Documentation.*  
   https://numpy.org/doc/stable/

7. **pytest Development Team.**  
   *pytest Documentation.*  
   https://docs.pytest.org/

## 16. Author

**Todor Yankov**

Math Concepts for Developers — SoftUni, September 2026

GitHub: https://github.com/TodorYankov/GeometryEngine3D
