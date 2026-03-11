# /// script
# dependencies = []
# ///
# ------------------------------------------------------------------------------
#
#  Gmsh Python tutorial 1
#
#  Geometry basics, elementary entities, physical groups
#
# ------------------------------------------------------------------------------

# The Python API is entirely defined in the `gmsh.py' module (which contains the
# full documentation of all the functions in the API):
from typing import reveal_type

import gmsh

gmsh.initialize()
# Copied from `t1.py'...


lc = 1e-2
gmsh.model.geo.add_point(0, 0, 0, lc, 1)
gmsh.model.geo.add_point(0.1, 0, 0, lc, 2)
gmsh.model.geo.add_point(0.1, 0.3, 0, lc, 3)
gmsh.model.geo.add_point(0, 0.3, 0, lc, 4)
gmsh.model.geo.add_line(1, 2, 1)
gmsh.model.geo.add_line(3, 2, 2)
gmsh.model.geo.add_line(3, 4, 3)
gmsh.model.geo.add_line(4, 1, 4)
gmsh.model.geo.add_curve_loop([4, 1, -2, 3], 1)
res = gmsh.model.geo.add_plane_surface([1], 1)
print(res)
reveal_type(res)
# We change the mesh size to generate a coarser mesh
lc = lc * 4
res = gmsh.model.geo.mesh.set_size([(0, 1), (0, 2), (0, 3), (0, 4)], lc)
print(res)
reveal_type(res)
# We define a new point
gmsh.model.geo.add_point(0.02, 0.02, 0.0, lc, 5)

# We have to synchronize before embedding entites:
gmsh.model.geo.synchronize()

# One can force this point to be included ("embedded") in the 2D mesh, using the
# `embed()' function:
res = gmsh.model.mesh.embed(0, [5], 2, 1)
print(res)
reveal_type(res)

# In the same way, one can use `embed()' to force a curve to be embedded in the
# 2D mesh:
gmsh.model.geo.add_point(0.02, 0.12, 0.0, lc, 6)
gmsh.model.geo.add_point(0.04, 0.18, 0.0, lc, 7)
gmsh.model.geo.add_line(6, 7, 5)

gmsh.model.geo.synchronize()
gmsh.model.mesh.embed(1, [5], 2, 1)

# Points and curves can also be embedded in volumes
res = gmsh.model.geo.extrude([(2, 1)], 0, 0, 0.1)
print(res)
reveal_type(res)


p = gmsh.model.geo.add_point(0.07, 0.15, 0.025, lc)

gmsh.model.geo.synchronize()
gmsh.model.mesh.embed(0, [p], 3, 1)

gmsh.model.geo.add_point(0.025, 0.15, 0.025, lc, p + 1)
llll = gmsh.model.geo.add_line(7, p + 1)

gmsh.model.geo.synchronize()
gmsh.model.mesh.embed(1, [llll], 3, 1)

# Finally, we can also embed a surface in a volume:
gmsh.model.geo.add_point(0.02, 0.12, 0.05, lc, p + 2)
gmsh.model.geo.add_point(0.04, 0.12, 0.05, lc, p + 3)
gmsh.model.geo.add_point(0.04, 0.18, 0.05, lc, p + 4)
gmsh.model.geo.add_point(0.02, 0.18, 0.05, lc, p + 5)

gmsh.model.geo.add_line(p + 2, p + 3, llll + 1)
gmsh.model.geo.add_line(p + 3, p + 4, llll + 2)
gmsh.model.geo.add_line(p + 4, p + 5, llll + 3)
gmsh.model.geo.add_line(p + 5, p + 2, llll + 4)

ll = gmsh.model.geo.add_curve_loop([llll + 1, llll + 2, llll + 3, llll + 4])
s = gmsh.model.geo.add_plane_surface([ll])

gmsh.model.geo.synchronize()
gmsh.model.mesh.embed(2, [s], 3, 1)

# Note that with the OpenCASCADE kernel (see `t16.py'), when the `fragment()'
# function is applied to entities of different dimensions, the lower dimensional
# entities will be autmatically embedded in the higher dimensional entities if
# necessary.

gmsh.model.mesh.generate(3)


gmsh.finalize()
