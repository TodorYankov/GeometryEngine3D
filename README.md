# GeometryEngine3D

GeometryEngine3D is a Python project for studying three-dimensional geometry and modeling the movement of a point in 3D space.

The project combines mathematical formulas, Python implementations, automated tests, and Jupyter Notebook experiments.

A point in three-dimensional Cartesian space is represented as:

$$
P = (x, y, z)
$$

The main objective is to investigate how geometric objects and movement trajectories can be represented, calculated, and visualized using mathematical models.

## 1. Project Objectives

The project focuses on:

- Representing points, vectors, lines, triangles, and planes in 3D space.
- Performing geometric calculations and transformations.
- Modeling trajectories using parametric equations.
- Constructing paths between two or more control points.
- Visualizing trajectories in three-dimensional coordinate systems.
- Testing mathematical implementations using Python.

## 2. Current Features

### 2.1 Point3D

The `Point3D` class represents a point in three-dimensional Cartesian space.

Implemented operations include:

- Euclidean distance between two points.
- Translation.
- Scaling.

The Euclidean distance formula is:

$$
d(A,B)=\sqrt{(x_2-x_1)^2+(y_2-y_1)^2+(z_2-z_1)^2}
$$

### 2.2 Vector3D

The `Vector3D` class supports:

- Vector magnitude.
- Vector addition and subtraction.
- Dot product.
- Cross product.

The magnitude of a vector is calculated as:

$$
|\vec{v}|=\sqrt{x^2+y^2+z^2}
$$

### 2.3 Trajectory3D

The `Trajectory3D` class models the position of a moving point using a parametric equation:

$$
\mathbf{r}(t)=(t^2,2t,\sin t)
$$

The parameter $t$ determines the position along the trajectory.

### 2.4 Line3D

The `Line3D` class represents a line in three-dimensional space using parametric equations.

### 2.5 Triangle3D

The `Triangle3D` class provides calculations involving:

- Side lengths.
- Perimeter.
- Area.

### 2.6 Plane3D

The `Plane3D` class supports:

- Plane representation.
- Checking whether a point belongs to a plane.
- Calculating the distance between a point and a plane.
- Finding intersections between lines and planes.

### 2.7 LinearPath3D

The `LinearPath3D` class calculates positions along a straight line segment connecting two points.

Linear interpolation is defined as:

$$
P(t)=(1-t)P_0+tP_1,\qquad t\in[0,1]
$$

### 2.8 MultiPointPath3D

The `MultiPointPath3D` class constructs a continuous piecewise linear path through multiple control points.

For a sequence of points:

$$
P_0\rightarrow P_1\rightarrow\cdots\rightarrow P_n
$$

the trajectory is calculated by applying linear interpolation between consecutive points.

Each segment receives an equal portion of the global interpolation parameter.

## 3. Project Structure

```text
GeometryEngine3D/
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
│       └── multipoint_path.py
├── tests/
│   ├── test_point.py
│   ├── test_vector.py
│   ├── test_trajectory.py
│   ├── test_line.py
│   ├── test_triangle.py
│   ├── test_plane.py
│   ├── test_path.py
│   └── test_multipoint_path.py
├── .gitignore
├── pyproject.toml
├── requirements.txt
└── README.md
```

## 4. Jupyter Notebooks

The project includes four Jupyter Notebooks containing mathematical explanations, Python calculations, and experiments.

| Notebook | Content |
|---|---|
| `01_points_and_vectors.ipynb` | Points, vectors, and Euclidean geometry |
| `02_lines_and_triangles.ipynb` | Lines, triangles, and geometric calculations |
| `03_planes_and_transformations.ipynb` | Planes and geometric transformations |
| `04_trajectory_planning.ipynb` | Linear interpolation, multipoint paths, 3D visualization, and speed analysis |

## 5. Trajectory Planning Experiment

A trajectory was constructed through four control points:

$$
P_0=(0,0,0)
$$

$$
P_1=(6,0,0)
$$

$$
P_2=(6,8,0)
$$

$$
P_3=(6,8,10)
$$

The lengths of the three segments are:

| Segment | Length |
|---|---:|
| P0 → P1 | 6 |
| P1 → P2 | 8 |
| P2 → P3 | 10 |
| **Total** | **24** |

The total path length is:

$$
L=\sum_{i=0}^{n-1}\|P_{i+1}-P_i\|
$$

For this example:

$$
L=6+8+10=24
$$

### 5.1 Speed Analysis

The current multipoint interpolation model assigns equal parameter intervals to all segments.

Assuming a total travel time of one second, each segment receives:

$$
\Delta t=\frac{1}{3}\text{ s}
$$

Speed is calculated as:

$$
v_i=\frac{L_i}{\Delta t}
$$

| Segment | Speed (units/s) |
|---|---:|
| P0 → P1 | 18 |
| P1 → P2 | 24 |
| P2 → P3 | 30 |

The results demonstrate that equal time intervals do not guarantee constant speed when segment lengths are different.

The trajectory was also visualized in three-dimensional space using Matplotlib.

## 6. Automated Testing

The project uses `pytest` to verify mathematical calculations and class behavior.

Run the tests from the project root:

```bash
python -m pytest -q
```

Latest verified result:

```text
49 passed
```

## 7. Installation and Usage

The project requires Python 3.12 or newer.

Clone the repository:

```bash
git clone https://github.com/TodorYankov/GeometryEngine3D.git
cd GeometryEngine3D
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate the environment on Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

Install the project and its test dependencies:

```bash
python -m pip install -e .
python -m pip install -r requirements.txt
```

To work with the Jupyter Notebooks and visualizations, install:

```bash
python -m pip install jupyter matplotlib numpy
```

### Example: Multipoint Trajectory

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

Expected coordinates: `(6.0, 4.0, 0.0)` (the exact printed representation depends on `Point3D.__repr__`).

## 8. Conclusions

GeometryEngine3D demonstrates how mathematical concepts from three-dimensional geometry can be implemented and tested using Python.

The trajectory planning experiments show that piecewise linear interpolation can construct a continuous path through multiple control points.

The analysis also shows that equal parameter intervals do not necessarily produce constant physical speed.

The project combines mathematical modeling, programming, automated testing, and numerical experiments.

## 9. Future Development and Research Perspectives

GeometryEngine3D provides a mathematical foundation for modeling geometric objects and trajectories in three-dimensional space.

In the future, the project could be extended to explore more complex spatial and periodic processes, including orbital motion, celestial mechanics, and mathematical patterns in natural phenomena.

Such developments could offer opportunities to investigate the mathematical harmony observed in the universe.

From a broader philosophical perspective, this raises an interesting question:

**Is mathematics merely a tool for describing the universe, or does it reflect fundamental patterns embedded in the structure of reality itself?**

This question may inspire future research based on mathematical modeling, scientific observation, and testable hypotheses.

## 10. Author

**Todor Yankov**

Math Concepts for Developers — SoftUni, September 2026

GitHub: https://github.com/TodorYankov/GeometryEngine3D
