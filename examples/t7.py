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
import os
from pathlib import Path

import numpy as np

import gmsh

gmsh.initialize()

# Merge a list-based post-processing view containing the target mesh sizes:
path = Path(__file__).resolve().parent
gmsh.merge(str(path / os.pardir / "t7_bgmesh.pos"))

# If the post-processing view was model-based instead of list-based (i.e. if it
# was based on an actual mesh), we would need to create a new model to contain
# the geometry so that meshing it does not destroy the background mesh. It's not
# necessary here since the view is list-based, but it does no harm:
gmsh.model.add("t7")

# Create a simple rectangular geometry:
lc = 1e-2
gmsh.model.geo.add_point(0, 0, 0, lc, 1)
gmsh.model.geo.add_point(0.1, 0, 0, lc, 2)
gmsh.model.geo.add_point(0.1, 0.3, 0, lc, 3)
gmsh.model.geo.add_point(0, 0.3, 0, lc, 4)
gmsh.model.geo.add_line(1, 2, 1)
gmsh.model.geo.add_line(3, 2, 2)
gmsh.model.geo.add_line(3, 4, 3)
gmsh.model.geo.add_line(4, 1, 4)
pts: np.ndarray[tuple[int], np.dtype[np.int32]] = np.array([4, 1, -2, 3], dtype=np.int32)
gmsh.model.geo.add_curve_loop(pts, 1)
gmsh.model.geo.add_plane_surface([1], 1)
gmsh.model.geo.synchronize()

# Add the post-processing view as a new size field:
bg_field = gmsh.model.mesh.field.add("PostView")
gmsh.model.mesh.field.set_number(bg_field, "ViewIndex", 0)

# Apply the view as the current background mesh size field:
gmsh.model.mesh.field.set_as_background_mesh(bg_field)

# In order to compute the mesh sizes from the background mesh only, and
# disregard any other size constraints, one can set:
gmsh.option.set_number("Mesh.MeshSizeExtendFromBoundary", 0)
gmsh.option.set_number("Mesh.MeshSizeFromPoints", 0)
gmsh.option.set_number("Mesh.MeshSizeFromCurvature", 0)

# See `t10.py' for additional information: background meshes are actually a
# particular case of general "mesh size fields".


gmsh.finalize()
