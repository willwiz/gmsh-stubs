# /// script
# dependencies = []
# ///

import math
import sys

import gmsh

gmsh.initialize()


def create_geomesh() -> None:
    # Clear all models and create a new one
    gmsh.clear()
    gmsh.model.add("t3")

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
    gmsh.model.geo.add_plane_surface([1], 1)
    gmsh.model.geo.synchronize()
    gmsh.model.add_physical_group(1, [1, 2, 4], 5)
    gmsh.model.add_physical_group(2, [1], name="My surface")

    # As in `t2.py', we plan to perform an extrusion along the z axis.  But
    # here, instead of only extruding the geometry, we also want to extrude the
    # 2D mesh. This is done with the same `extrude()' function, but by
    # specifying element 'Layers' (2 layers in this case, the first one with 8
    # subdivisions and the second one with 2 subdivisions, both with a height of
    # h/2). The number of elements for each layer and the (end) height of each
    # layer are specified in two vectors:
    h = 0.1
    ov = gmsh.model.geo.extrude([(2, 1)], 0, 0, h, [8, 2], [0.5, 1])

    # The extrusion can also be performed with a rotation instead of a
    # translation, and the resulting mesh can be recombined into prisms (we use
    # only one layer here, with 7 subdivisions). All rotations are specified by
    # an an axis point (-0.1, 0, 0.1), an axis direction (0, 1, 0), and a
    # rotation angle (-Pi/2):
    ov = gmsh.model.geo.revolve([(2, 28)], -0.1, 0, 0.1, 0, 1, 0, -math.pi / 2, [7])

    # Using the built-in geometry kernel, only rotations with angles < Pi are
    # supported. To do a full turn, you will thus need to apply at least 3
    # rotations. The OpenCASCADE geometry kernel does not have this limitation.

    # A translation (-2 * h, 0, 0) and a rotation ((0, 0.15, 0.25), (1, 0, 0),
    # angle * Pi / 180) can also be combined to form a "twist".  The last
    # (optional) argument for the extrude() and twist() functions specifies
    # whether the extruded mesh should be recombined or not. The `angle'
    # parameter is retrieved from the ONELAB database (it can be set
    # interactively in the GUI -- see below):
    angle = gmsh.onelab.get_number("Parameters/Twisting angle")[0]
    ov = gmsh.model.geo.twist(
        [(2, 50)],
        0,
        0.15,
        0.25,
        -2 * h,
        0,
        0,
        1,
        0,
        0,
        angle * math.pi / 180.0,
        [10],
        [],
        recombine=True,
    )

    gmsh.model.geo.synchronize()

    # All the extrusion functions return a vector of extruded entities: the
    # "top" of the extruded surface (in `ov[0]'), the newly created volume (in
    # `ov[1]') and the tags of the lateral surfaces (in `ov[2]', `ov[3]', ...).

    # We can then define a new physical volume (with tag 101) to group all the
    # elementary volumes:
    gmsh.model.add_physical_group(3, [1, 2, ov[1][1]], 101)

    gmsh.model.mesh.generate(3)
    gmsh.write("t3.msh")


# Let us now change some options... Since all interactive options are accessible
# through the API, we can for example make point tags visible or redefine some
# colors:
gmsh.option.set_number("Geometry.PointNumbers", 1)
gmsh.option.set_color("Geometry.Color.Points", 255, 165, 0)
gmsh.option.set_color("General.Color.Text", 255, 255, 255)
gmsh.option.set_color("Mesh.Color.Points", 255, 0, 0)

# Note that for conciseness "Color." can be ommitted in color options:
r, g, b, a = gmsh.option.get_color("Geometry.Points")
gmsh.option.set_color("Geometry.Surfaces", r, g, b, a)

# We create a ONELAB parameter to define the angle of the twist. ONELAB
# parameters can be modified interactively in the GUI, and can be exchanged with
# other codes connected to the same ONELAB database. The database can be
# accessed through the Gmsh Python API using JSON-formatted strings (see
# https://gitlab.onelab.info/doc/tutorials/-/wikis/ONELAB-JSON-interface for
# more information):
gmsh.onelab.set("""[
  {
    "type":"number",
    "name":"Parameters/Twisting angle",
    "values":[90],
    "min":0,
    "max":120,
    "step":1
  }
]""")

# Create the geometry and mesh it:
create_geomesh()


# Launch the GUI and handle the "check" event (recorded in the "ONELAB/Action"
# parameter) to recreate the geometry with a new twisting angle if necessary:
def check_for_event() -> bool:
    action = gmsh.onelab.get_string("ONELAB/Action")
    if len(action) and action[0] == "check":
        gmsh.onelab.set_string("ONELAB/Action", [""])
        create_geomesh()
        gmsh.graphics.draw()
    return True


if "-nopopup" not in sys.argv:
    gmsh.fltk.initialize()
    while gmsh.fltk.is_available() and check_for_event():
        gmsh.fltk.wait()

# When the GUI is launched, you can use the `Help->Current Options and
# Workspace' menu to see the current values of all options. To save the options
# in a file, use `File->Export->Gmsh Options', or through the api:

# gmsh.write("t3.opt");

gmsh.finalize()
