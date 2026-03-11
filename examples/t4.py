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


import math
import os
import sys
from pathlib import Path

import gmsh

gmsh.initialize()

gmsh.model.add("t4")

cm = 1e-02
e1 = 4.5 * cm
e2 = 6 * cm / 2
e3 = 5 * cm / 2
h1 = 5 * cm
h2 = 10 * cm
h3 = 5 * cm
h4 = 2 * cm
h5 = 4.5 * cm
R1 = 1 * cm
R2 = 1.5 * cm
r = 1 * cm
Lc1 = 0.01
Lc2 = 0.003


def hypot(a: float, b: float) -> float:
    return math.sqrt(a * a + b * b)


ccos = (-h5 * R1 + e2 * hypot(h5, hypot(e2, R1))) / (h5 * h5 + e2 * e2)
ssin = math.sqrt(1 - ccos * ccos)

# We start by defining some points and some lines. To make the code shorter we
# can redefine a namespace:
factory = gmsh.model.geo
factory.add_point(-e1 - e2, 0, 0, Lc1, 1)
factory.add_point(-e1 - e2, h1, 0, Lc1, 2)
factory.add_point(-e3 - r, h1, 0, Lc2, 3)
factory.add_point(-e3 - r, h1 + r, 0, Lc2, 4)
factory.add_point(-e3, h1 + r, 0, Lc2, 5)
factory.add_point(-e3, h1 + h2, 0, Lc1, 6)
factory.add_point(e3, h1 + h2, 0, Lc1, 7)
factory.add_point(e3, h1 + r, 0, Lc2, 8)
factory.add_point(e3 + r, h1 + r, 0, Lc2, 9)
factory.add_point(e3 + r, h1, 0, Lc2, 10)
factory.add_point(e1 + e2, h1, 0, Lc1, 11)
factory.add_point(e1 + e2, 0, 0, Lc1, 12)
factory.add_point(e2, 0, 0, Lc1, 13)

factory.add_point(R1 / ssin, h5 + R1 * ccos, 0, Lc2, 14)
factory.add_point(0, h5, 0, Lc2, 15)
factory.add_point(-R1 / ssin, h5 + R1 * ccos, 0, Lc2, 16)
factory.add_point(-e2, 0.0, 0, Lc1, 17)

factory.add_point(-R2, h1 + h3, 0, Lc2, 18)
factory.add_point(-R2, h1 + h3 + h4, 0, Lc2, 19)
factory.add_point(0, h1 + h3 + h4, 0, Lc2, 20)
factory.add_point(R2, h1 + h3 + h4, 0, Lc2, 21)
factory.add_point(R2, h1 + h3, 0, Lc2, 22)
factory.add_point(0, h1 + h3, 0, Lc2, 23)

factory.add_point(0, h1 + h3 + h4 + R2, 0, Lc2, 24)
factory.add_point(0, h1 + h3 - R2, 0, Lc2, 25)

factory.add_line(1, 17, 1)
factory.add_line(17, 16, 2)

# Gmsh provides other curve primitives than straight lines: splines, B-splines,
# circle arcs, ellipse arcs, etc. Here we define a new circle arc, starting at
# point 14 and ending at point 16, with the circle's center being the point 15:
factory.add_circle_arc(14, 15, 16, 3)

# Note that, in Gmsh, circle arcs should always be smaller than Pi. The
# OpenCASCADE geometry kernel does not have this limitation.

# We can then define additional lines and circles, as well as a new surface:
factory.add_line(14, 13, 4)
factory.add_line(13, 12, 5)
factory.add_line(12, 11, 6)
factory.add_line(11, 10, 7)
factory.add_circle_arc(8, 9, 10, 8)
factory.add_line(8, 7, 9)
factory.add_line(7, 6, 10)
factory.add_line(6, 5, 11)
factory.add_circle_arc(3, 4, 5, 12)
factory.add_line(3, 2, 13)
factory.add_line(2, 1, 14)
factory.add_line(18, 19, 15)
factory.add_circle_arc(21, 20, 24, 16)
factory.add_circle_arc(24, 20, 19, 17)
factory.add_circle_arc(18, 23, 25, 18)
factory.add_circle_arc(25, 23, 22, 19)
factory.add_line(21, 22, 20)

factory.add_curve_loop([17, -15, 18, 19, -20, 16], 21)
factory.add_plane_surface([21], 22)

# But we still need to define the exterior surface. Since this surface has a
# hole, its definition now requires two curves loops:
factory.add_curve_loop([11, -12, 13, 14, 1, 2, -3, 4, 5, 6, 7, -8, 9, 10], 23)
factory.add_plane_surface([23, 21], 24)

# As a general rule, if a surface has N holes, it is defined by N+1 curve loops:
# the first loop defines the exterior boundary; the other loops define the
# boundaries of the holes.

factory.synchronize()

# Finally, we can add some comments by creating a post-processing view
# containing some strings:
v = gmsh.view.add("comments")

# Add a text string in window coordinates, 10 pixels from the left and 10 pixels
# from the bottom:
gmsh.view.add_list_data_string(v, [10, -10], ["Created with Gmsh"])

# Add a text string in model coordinates centered at (X,Y,Z) = (0, 0.11, 0),
# with some style attributes:
gmsh.view.add_list_data_string(v, [0, 0.11, 0], ["Hole"], ["Align", "Center", "Font", "Helvetica"])

# If a string starts with `file://', the rest is interpreted as an image
# file. For 3D annotations, the size in model coordinates can be specified after
# a `@' symbol in the form `widthxheight' (if one of `width' or `height' is
# zero, natural scaling is used; if both are zero, original image dimensions in
# pixels are used):
png = str(Path(__file__).resolve().parent / os.pardir / "t4_image.png")
gmsh.view.add_list_data_string(v, [0, 0.09, 0], ["file://" + png + "@0.01x0"], ["Align", "Center"])

# The 3D orientation of the image can be specified by proving the direction
# of the bottom and left edge of the image in model space:
gmsh.view.add_list_data_string(v, [-0.01, 0.09, 0], ["file://" + png + "@0.01x0,0,0,1,0,1,0"])

# The image can also be drawn in "billboard" mode, i.e. always parallel to
# the camera, by using the `#' symbol:
gmsh.view.add_list_data_string(v, [0, 0.12, 0], ["file://" + png + "@0.01x0#"], ["Align", "Center"])

# The size of 2D annotations is given directly in pixels:
gmsh.view.add_list_data_string(v, [150, -7], ["file://" + png + "@20x0"])

# These annotations are handled by a list-based post-processing view. For
# large post-processing datasets, that contain actual field values defined on
# a mesh, you should use model-based post-processing views instead, which
# allow to efficiently store continuous or discontinuous scalar, vector and
# tensor fields, or arbitrary polynomial order.

# Views and geometrical entities can be made to respond to double-click
# events, here to print some messages to the console:
gmsh.view.option.set_string(
    v, "DoubleClickedCommand", "Printf('View[0] has been double-clicked!');"
)
gmsh.option.set_string(
    "Geometry.DoubleClickedLineCommand",
    "Printf('Curve %g has been double-clicked!', Geometry.DoubleClickedEntityTag);",
)

# We can also change the color of some entities:
gmsh.model.set_color([(2, 22)], 127, 127, 127)  # Gray50
gmsh.model.set_color([(2, 24)], 160, 32, 240)  # Purple
gmsh.model.set_color([(1, i) for i in range(1, 15)], 255, 0, 0)  # Red
gmsh.model.set_color([(1, i) for i in range(15, 21)], 255, 255, 0)  # Yellow

gmsh.model.mesh.generate(2)

gmsh.write("t4.msh")

# Launch the GUI to see the results:
if "-nopopup" not in sys.argv:
    gmsh.fltk.run()

gmsh.finalize()
