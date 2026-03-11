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


# Create an example geometry
gmsh.model.add("t14")

m = 0.5  # mesh size
h = 2  # geometry height in the z-direction

gmsh.model.geo.add_point(0, 0, 0, m, 1)
gmsh.model.geo.add_point(10, 0, 0, m, 2)
gmsh.model.geo.add_point(10, 10, 0, m, 3)
gmsh.model.geo.add_point(0, 10, 0, m, 4)

gmsh.model.geo.add_point(4, 4, 0, m, 5)
gmsh.model.geo.add_point(6, 4, 0, m, 6)
gmsh.model.geo.add_point(6, 6, 0, m, 7)
gmsh.model.geo.add_point(4, 6, 0, m, 8)

gmsh.model.geo.add_point(2, 0, 0, m, 9)
gmsh.model.geo.add_point(8, 0, 0, m, 10)
gmsh.model.geo.add_point(2, 10, 0, m, 11)
gmsh.model.geo.add_point(8, 10, 0, m, 12)

gmsh.model.geo.add_line(1, 9, 1)
gmsh.model.geo.add_line(9, 10, 2)
gmsh.model.geo.add_line(10, 2, 3)

gmsh.model.geo.add_line(2, 3, 4)
gmsh.model.geo.add_line(3, 12, 5)
gmsh.model.geo.add_line(12, 11, 6)

gmsh.model.geo.add_line(11, 4, 7)
gmsh.model.geo.add_line(4, 1, 8)
gmsh.model.geo.add_line(5, 6, 9)

gmsh.model.geo.add_line(6, 7, 10)
gmsh.model.geo.add_line(7, 8, 11)
gmsh.model.geo.add_line(8, 5, 12)

gmsh.model.geo.add_curve_loop([6, 7, 8, 1, 2, 3, 4, 5], 13)
gmsh.model.geo.add_curve_loop([11, 12, 9, 10], 14)
gmsh.model.geo.add_plane_surface([13, 14], 15)

e = gmsh.model.geo.extrude([(2, 15)], 0, 0, h)

gmsh.model.geo.synchronize()

# Create physical groups, which are used to define the domain of the
# (co)homology computation and the subdomain of the relative (co)homology
# computation.

# Whole domain
domain_tag = e[1][1]
domain_physical_tag = 1001
gmsh.model.add_physical_group(3, [domain_tag], domain_physical_tag, "Whole domain")

# Four "terminals" of the model
terminal_tags = [e[3][1], e[5][1], e[7][1], e[9][1]]
terminals_physical_tag = 2001
gmsh.model.add_physical_group(2, terminal_tags, terminals_physical_tag, "Terminals")

# Find domain boundary tags
boundary_dimtags = gmsh.model.get_boundary([(3, domain_tag)], combined=False, oriented=False)
print(boundary_dimtags)
reveal_type(boundary_dimtags)
boundary_tags: list[int] = []
complement_tags: list[int] = []
for tag in boundary_dimtags:
    complement_tags.append(tag[1])
    boundary_tags.append(tag[1])
for tag in terminal_tags:
    complement_tags.remove(tag)

# Whole domain surface
boundary_physical_tag = 2002
gmsh.model.add_physical_group(2, boundary_tags, boundary_physical_tag, "Boundary")

# Complement of the domain surface with respect to the four terminals
complement_physical_tag = 2003
gmsh.model.add_physical_group(2, complement_tags, complement_physical_tag, "Complement")

# Find bases for relative homology spaces of the domain modulo the four
# terminals.
gmsh.model.mesh.add_homology_request(
    "Homology", [domain_physical_tag], [terminals_physical_tag], [0, 1, 2, 3]
)

# Find homology space bases isomorphic to the previous bases: homology spaces
# modulo the non-terminal domain surface, a.k.a the thin cuts.
gmsh.model.mesh.add_homology_request(
    "Homology", [domain_physical_tag], [complement_physical_tag], [0, 1, 2, 3]
)

# Find cohomology space bases isomorphic to the previous bases: cohomology
# spaces of the domain modulo the four terminals, a.k.a the thick cuts.
gmsh.model.mesh.add_homology_request(
    "Cohomology", [domain_physical_tag], [terminals_physical_tag], [0, 1, 2, 3]
)


gmsh.finalize()
