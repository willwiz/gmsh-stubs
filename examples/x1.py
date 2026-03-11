# /// script
# dependencies = []
# ///

import sys

import gmsh

gmsh.initialize()

if len(sys.argv) > 1 and sys.argv[1][0] != "-":
    # If an argument is provided, handle it as a file that Gmsh can read, e.g. a
    # mesh file in the MSH format (`python x1.py file.msh')
    gmsh.open(sys.argv[1])
else:
    # Otherwise, create and mesh a simple geometry
    gmsh.model.occ.add_cone(1, 0, 0, 1, 0, 0, 0.5, 0.1)
    gmsh.model.occ.synchronize()
    gmsh.model.mesh.generate()

# Print the model name and dimension:
print("Model " + gmsh.model.get_current() + " (" + str(gmsh.model.get_dimension()) + "D)")

# Geometrical data is made of elementary model `entities', called `points'
# (entities of dimension 0), `curves' (entities of dimension 1), `surfaces'
# (entities of dimension 2) and `volumes' (entities of dimension 3). As we have
# seen in the other Python tutorials, elementary model entities are identified
# by their dimension and by a `tag': a strictly positive identification
# number. Model entities can be either CAD entities (from the built-in `geo'
# kernel or from the OpenCASCADE `occ' kernel) or `discrete' entities (defined
# by a mesh). `Physical groups' are collections of model entities and are also
# identified by their dimension and by a tag.

# Get all the elementary entities in the model, as a vector of (dimension, tag)
# pairs:
entities = gmsh.model.get_entities()

for e in entities:
    # Dimension and tag of the entity:
    dim = e[0]
    tag = e[1]

    # Mesh data is made of `elements' (points, lines, triangles, ...), defined
    # by an ordered list of their `nodes'. Elements and nodes are identified by
    # `tags' as well (strictly positive identification numbers), and are stored
    # ("classified") in the model entity they discretize. Tags for elements and
    # nodes are globally unique (and not only per dimension, like entities).

    # A model entity of dimension 0 (a geometrical point) will contain a mesh
    # element of type point, as well as a mesh node. A model curve will contain
    # line elements as well as its interior nodes, while its boundary nodes will
    # be stored in the bounding model points. A model surface will contain
    # triangular and/or quadrangular elements and all the nodes not classified
    # on its boundary or on its embedded entities. A model volume will contain
    # tetrahedra, hexahedra, etc. and all the nodes not classified on its
    # boundary or on its embedded entities.

    # Get the mesh nodes for the entity (dim, tag):
    node_tags, node_coords, node_params = gmsh.model.mesh.get_nodes(dim, tag)

    # Get the mesh elements for the entity (dim, tag):
    elem_types, elem_tags, elem_nodetags = gmsh.model.mesh.get_elements(dim, tag)

    # Elements can also be obtained by type, by using `getElementTypes()'
    # followed by `getElementsByType()'.

    # Let's print a summary of the information available on the entity and its
    # mesh.

    # * Type and name of the entity:
    type = gmsh.model.get_type(dim, tag)
    name = gmsh.model.get_entity_name(dim, tag)
    if len(name):
        name += " "
    print("Entity " + name + str(e) + " of type " + type)

    # * Number of mesh nodes and elements:
    num_elem = sum(len(i) for i in elem_tags)
    print(" - Mesh has " + str(len(node_tags)) + " nodes and " + str(num_elem) + " elements")

    # * Upward and downward adjacencies:
    up, down = gmsh.model.get_adjacencies(dim, tag)
    if len(up):
        print(" - Upward adjacencies: " + str(up))
    if len(down):
        print(" - Downward adjacencies: " + str(down))

    # * Does the entity belong to physical groups?
    physical_tags = gmsh.model.get_physical_groups_for_entity(dim, tag)
    if len(physical_tags):
        s = ""
        for p in physical_tags:
            n = gmsh.model.get_physical_name(dim, p)
            if n:
                n += " "
            s += n + "(" + str(dim) + ", " + str(p) + ") "
        print(" - Physical groups: " + s)

    # * Is the entity a partition entity? If so, what is its parent entity?
    partitions = gmsh.model.get_partitions(dim, tag)
    if len(partitions):
        print(
            " - Partition tags: "
            + str(partitions)
            + " - parent entity "
            + str(gmsh.model.get_parent(dim, tag))
        )

    # * List all types of elements making up the mesh of the entity:
    for t in elem_types:
        name, dim, order, numv, parv, _ = gmsh.model.mesh.get_element_properties(t)
        print(
            " - Element type: "
            + name
            + ", order "
            + str(order)
            + " ("
            + str(numv)
            + " nodes in param coord: "
            + str(parv)
            + ")"
        )

# Launch the GUI to see the model:
if "-nopopup" not in sys.argv:
    gmsh.fltk.run()

# We can use this to clear all the model data:
gmsh.clear()

gmsh.finalize()
