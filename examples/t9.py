# /// script
# dependencies = []
# ///
import os
import sys
from pathlib import Path

import gmsh

# Plugins can be added to Gmsh in order to extend its capabilities. For example,
# post-processing plugins can modify views, or create new views based on
# previously loaded views. Several default plugins are statically linked with
# Gmsh, e.g. Isosurface, CutPlane, CutSphere, Skin, Transform or Smooth.
#
# Plugins can be controlled through the API functions with the `gmsh.plugin'
# prefix, or from the graphical interface (right click on the view button, then
# `Plugins').

gmsh.initialize()

# Let us for example include a three-dimensional scalar view:
path = Path(__file__).resolve().parent
gmsh.merge(str(path / os.pardir / "view3.pos"))
v = gmsh.view.get_tags()
if len(v) != 1:
    gmsh.logger.write("Wrong number of views!", "error")
    gmsh.finalize()
    sys.exit()

# We then set some options for the `Isosurface' plugin (which extracts an
# isosurface from a 3D scalar view), and run it:
gmsh.plugin.set_number("Isosurface", "Value", 0.67)
gmsh.plugin.set_number("Isosurface", "View", 0)
v1 = gmsh.plugin.run("Isosurface")

# We also set some options for the `CutPlane' plugin (which computes a section
# of a 3D view using the plane A*x+B*y+C*z+D=0), and then run it:
gmsh.plugin.set_number("CutPlane", "A", 0)
gmsh.plugin.set_number("CutPlane", "B", 0.2)
gmsh.plugin.set_number("CutPlane", "C", 1)
gmsh.plugin.set_number("CutPlane", "D", 0)
gmsh.plugin.set_number("CutPlane", "View", 0)
v2 = gmsh.plugin.run("CutPlane")

# Add a title (By convention, for window coordinates a value greater than 99999
# represents the center. We could also use `General.GraphicsWidth / 2', but that
# would only center the string for the current window size.):
gmsh.plugin.set_string("Annotate", "Text", "A nice title")
gmsh.plugin.set_number("Annotate", "X", 1.0e5)
gmsh.plugin.set_number("Annotate", "Y", 50)
gmsh.plugin.set_string("Annotate", "Font", "Times-BoldItalic")
gmsh.plugin.set_number("Annotate", "FontSize", 28)
gmsh.plugin.set_string("Annotate", "Align", "Center")
gmsh.plugin.set_number("Annotate", "View", 0)
gmsh.plugin.run("Annotate")

gmsh.plugin.set_string("Annotate", "Text", "(and a small subtitle)")
gmsh.plugin.set_number("Annotate", "Y", 70)
gmsh.plugin.set_string("Annotate", "Font", "Times-Roman")
gmsh.plugin.set_number("Annotate", "FontSize", 12)
gmsh.plugin.run("Annotate")

# We finish by setting some options:
gmsh.view.option.set_number(v[0], "Light", 1)
gmsh.view.option.set_number(v[0], "IntervalsType", 1)
gmsh.view.option.set_number(v[0], "NbIso", 6)
gmsh.view.option.set_number(v[0], "SmoothNormals", 1)
gmsh.view.option.set_number(v1, "IntervalsType", 2)
gmsh.view.option.set_number(v2, "IntervalsType", 2)

# Launch the GUI to see the results:
if "-nopopup" not in sys.argv:
    gmsh.fltk.run()

gmsh.finalize()
