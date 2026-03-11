# /// script
# dependencies = []
# ///

import os
import sys
from pathlib import Path

import gmsh

gmsh.initialize()

gmsh.model.add("t17")

# Create a square
gmsh.model.occ.add_rectangle(-2, -2, 0, 4, 4)
gmsh.model.occ.synchronize()

# Merge a post-processing view containing the target anisotropic mesh sizes

path = Path(__file__).parent
gmsh.merge(str(path / os.pardir / "t17_bgmesh.pos"))

# Apply the view as the current background mesh
bg_field = gmsh.model.mesh.field.add("PostView")
gmsh.model.mesh.field.set_number(bg_field, "ViewIndex", 0)
gmsh.model.mesh.field.set_as_background_mesh(bg_field)

# Use bamg
gmsh.option.set_number("Mesh.SmoothRatio", 3)
gmsh.option.set_number("Mesh.AnisoMax", 1000)
gmsh.option.set_number("Mesh.Algorithm", 7)

gmsh.model.mesh.generate(2)
gmsh.write("t17.msh")

# Launch the GUI to see the results:
if "-nopopup" not in sys.argv:
    gmsh.fltk.run()

gmsh.finalize()
