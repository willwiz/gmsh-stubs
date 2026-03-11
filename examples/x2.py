# /// script
# dependencies = []
# ///

import math
import sys

import gmsh

# The API can be used to import a mesh without reading it from a file, by
# creating nodes and elements on the fly and storing them in model
# entities. These model entities can be existing CAD entities, or can be
# discrete entities, entirely defined by the mesh.
#
# Discrete entities can be reparametrized (see `t13.py') so that they can be
# remeshed later on; and they can also be combined with built-in CAD entities to
# produce hybrid models.
#
# We combine all these features in this tutorial to perform terrain meshing,
# where the terrain is described by a discrete surface (that we then
# reparametrize) combined with a CAD representation of the underground.

gmsh.initialize()

gmsh.model.add("x2")

# We will create the terrain surface mesh from N x N input data points:
N = 100


# Helper function to return a node tag given two indices i and j:
def tag(i: int, j: int) -> int:
    return (N + 1) * i + j + 1


# The x, y, z coordinates of all the nodes:
coords: list[float] = []

# The tags of the corresponding nodes:
nodes: list[int] = []

# The connectivities of the triangle elements (3 node tags per triangle) on the
# terrain surface:
tris: list[int] = []

# The connectivities of the line elements on the 4 boundaries (2 node tags
# for each line element):
lin: list[list[int]] = [[], [], [], []]

# The connectivities of the point elements on the 4 corners (1 node tag for each
# point element):
pnt = [tag(0, 0), tag(N, 0), tag(N, N), tag(0, N)]

for i in range(N + 1):
    for j in range(N + 1):
        nodes.append(tag(i, j))
        coords.extend([float(i) / N, float(j) / N, 0.05 * math.sin(10 * float(i + j) / N)])
        if i > 0 and j > 0:
            tris.extend([tag(i - 1, j - 1), tag(i, j - 1), tag(i - 1, j)])
            tris.extend([tag(i, j - 1), tag(i, j), tag(i - 1, j)])
        if (i in (0, N)) and j > 0:
            lin[3 if i == 0 else 1].extend([tag(i, j - 1), tag(i, j)])
        if (j in (0, N)) and i > 0:
            lin[0 if j == 0 else 2].extend([tag(i - 1, j), tag(i, j)])

# Create 4 discrete points for the 4 corners of the terrain surface:
for i in range(4):
    gmsh.model.add_discrete_entity(0, i + 1)
gmsh.model.set_coordinates(1, 0, 0, coords[3 * tag(0, 0) - 1])
gmsh.model.set_coordinates(2, 1, 0, coords[3 * tag(N, 0) - 1])
gmsh.model.set_coordinates(3, 1, 1, coords[3 * tag(N, N) - 1])
gmsh.model.set_coordinates(4, 0, 1, coords[3 * tag(0, N) - 1])
_3D = 3
# Create 4 discrete bounding curves, with their boundary points:
for i in range(4):
    gmsh.model.add_discrete_entity(1, i + 1, [i + 1, i + 2 if i < _3D else 1])

# Create one discrete surface, with its bounding curves:
gmsh.model.add_discrete_entity(2, 1, [1, 2, -3, -4])

# Add all the nodes on the surface (for simplicity... see below):
gmsh.model.mesh.add_nodes(2, 1, nodes, coords)

# Add point elements on the 4 points, line elements on the 4 curves, and
# triangle elements on the surface:
for i in range(4):
    # Type 15 for point elements:
    gmsh.model.mesh.add_elements_by_type(i + 1, 15, [], [pnt[i]])
    # Type 1 for 2-node line elements:
    gmsh.model.mesh.add_elements_by_type(i + 1, 1, [], lin[i])
# Type 2 for 3-node triangle elements:
gmsh.model.mesh.add_elements_by_type(1, 2, [], tris)

# Reclassify the nodes on the curves and the points (since we put them all on
# the surface before with `addNodes' for simplicity)
gmsh.model.mesh.reclassify_nodes()

# Create a geometry for the discrete curves and surfaces, so that we can remesh
# them later on:
gmsh.model.mesh.create_geometry()

# Note that for more complicated meshes, e.g. for on input unstructured STL
# mesh, we could use `classifySurfaces()' to automatically create the discrete
# entities and the topology; but we would then have to extract the boundaries
# afterwards.

# Create other build-in CAD entities to form one volume below the terrain
# surface. Beware that only built-in CAD entities can be hybrid, i.e. have
# discrete entities on their boundary: OpenCASCADE does not support this
# feature.
p1 = gmsh.model.geo.add_point(0, 0, -0.5)
p2 = gmsh.model.geo.add_point(1, 0, -0.5)
p3 = gmsh.model.geo.add_point(1, 1, -0.5)
p4 = gmsh.model.geo.add_point(0, 1, -0.5)
c1 = gmsh.model.geo.add_line(p1, p2)
c2 = gmsh.model.geo.add_line(p2, p3)
c3 = gmsh.model.geo.add_line(p3, p4)
c4 = gmsh.model.geo.add_line(p4, p1)
c10 = gmsh.model.geo.add_line(p1, 1)
c11 = gmsh.model.geo.add_line(p2, 2)
c12 = gmsh.model.geo.add_line(p3, 3)
c13 = gmsh.model.geo.add_line(p4, 4)
ll1 = gmsh.model.geo.add_curve_loop([c1, c2, c3, c4])
s1 = gmsh.model.geo.add_plane_surface([ll1])
ll3 = gmsh.model.geo.add_curve_loop([c1, c11, -1, -c10])
s3 = gmsh.model.geo.add_plane_surface([ll3])
ll4 = gmsh.model.geo.add_curve_loop([c2, c12, -2, -c11])
s4 = gmsh.model.geo.add_plane_surface([ll4])
ll5 = gmsh.model.geo.add_curve_loop([c3, c13, 3, -c12])
s5 = gmsh.model.geo.add_plane_surface([ll5])
ll6 = gmsh.model.geo.add_curve_loop([c4, c10, 4, -c13])
s6 = gmsh.model.geo.add_plane_surface([ll6])
sl1 = gmsh.model.geo.add_surface_loop([s1, s3, s4, s5, s6, 1])
v1 = gmsh.model.geo.add_volume([sl1])
gmsh.model.geo.synchronize()

# Set this to True to build a fully hex mesh:
# transfinite = True
transfinite = False
transfinite_auto = False

if transfinite:
    NN = 30
    for c in gmsh.model.get_entities(1):
        gmsh.model.mesh.set_transfinite_curve(c[1], NN)
    for s in gmsh.model.get_entities(2):
        gmsh.model.mesh.set_transfinite_surface(s[1])
        gmsh.model.mesh.set_recombine(s[0], s[1])
        gmsh.model.mesh.set_smoothing(s[0], s[1], 100)
    gmsh.model.mesh.set_transfinite_volume(v1)
elif transfinite_auto:
    gmsh.option.set_number("Mesh.MeshSizeMin", 0.5)
    gmsh.option.set_number("Mesh.MeshSizeMax", 0.5)
    # setTransfiniteAutomatic() uses the sizing constraints to set the number
    # of points
    gmsh.model.mesh.set_transfinite_automatic()
else:
    gmsh.option.set_number("Mesh.MeshSizeMin", 0.05)
    gmsh.option.set_number("Mesh.MeshSizeMax", 0.05)

gmsh.model.mesh.generate(3)
gmsh.write("x2.msh")

# Launch the GUI to see the results:
if "-nopopup" not in sys.argv:
    gmsh.fltk.run()

gmsh.finalize()
