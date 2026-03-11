# /// script
# dependencies = []
# ///

import sys

import gmsh

gmsh.initialize(sys.argv)

gmsh.model.add("x7")

# Meshes are fully described in Gmsh by nodes and elements, both associated to
# model entities. The API can be used to generate and handle other mesh
# entities, i.e. mesh edges and faces, which are not stored by default.

# Let's create a simple model and mesh it:
gmsh.model.occ.add_box(0, 0, 0, 1, 1, 1)
gmsh.model.occ.synchronize()
gmsh.option.set_number("Mesh.MeshSizeMin", 2.0)
gmsh.model.mesh.generate(3)

# Like elements, mesh edges and faces are described by (an ordered list of)
# their nodes. Let us retrieve the edges and the (triangular) faces of all the
# first order tetrahedra in the mesh:
element_type = gmsh.model.mesh.get_element_type("tetrahedron", 1)
edge_nodes = gmsh.model.mesh.get_element_edge_nodes(element_type)
face_nodes = gmsh.model.mesh.get_element_face_nodes(element_type, 3)

# Edges and faces are returned for each element as a list of nodes corresponding
# to the canonical orientation of the edges and faces for a given element type.

# Gmsh can also identify unique edges and faces (a single edge or face whatever
# the ordering of their nodes) and assign them a unique tag. This identification
# can be done internally by Gmsh (e.g. when generating keys for basis
# functions), or requested explicitly as follows:
gmsh.model.mesh.create_edges()
gmsh.model.mesh.create_faces()

# Edge and face tags can then be retrieved by providing their nodes:
edge_tags, edge_orientations = gmsh.model.mesh.get_edges(edge_nodes)
face_tags, face_orientations = gmsh.model.mesh.get_faces(3, face_nodes)

# Since element edge and face nodes are returned in the same order as the
# elements, one can easily keep track of which element(s) each edge or face is
# connected to:
element_tags, element_node_tags = gmsh.model.mesh.get_elements_by_type(element_type)
edges2elements: dict[int, list[int]] = {}
faces2elements: dict[int, list[int]] = {}
for i in range(len(edge_tags)):  # 6 edges per tetrahedron
    if edge_tags[i] not in edges2elements:
        edges2elements[edge_tags[i]] = [element_tags[i // 6]]
    else:
        edges2elements[edge_tags[i]].append(element_tags[i // 6])
for i in range(len(face_tags)):  # 4 faces per tetrahedron
    if face_tags[i] not in faces2elements:
        faces2elements[face_tags[i]] = [element_tags[i // 4]]
    else:
        faces2elements[face_tags[i]].append(element_tags[i // 4])

# New unique lower dimensional elements can also be easily created given the
# edge or face nodes. This is especially useful for numerical methods that
# require integrating or interpolating on internal edges or faces (like
# e.g. Discontinuous Galerkin techniques), since creating elements for the
# internal entities will make this additional mesh data readily available (see
# `x6.py'). For example, we can create a new discrete surface...
s = gmsh.model.add_discrete_entity(2)

# ... and fill it with unique triangles corresponding to the faces of the
# tetrahedra:
max_element_tag = gmsh.model.mesh.get_max_element_tag()
unique_face_tags: set[int] = set()
tags_for_triangles: list[int] = []
face_nodes_for_triangles: list[int] = []
for i in range(len(face_tags)):
    if face_tags[i] not in unique_face_tags:
        unique_face_tags.add(face_tags[i])
        tags_for_triangles.append(face_tags[i] + max_element_tag)
        face_nodes_for_triangles.append(face_nodes[3 * i])
        face_nodes_for_triangles.append(face_nodes[3 * i + 1])
        face_nodes_for_triangles.append(face_nodes[3 * i + 2])
element_type_2d = gmsh.model.mesh.get_element_type("triangle", 1)
gmsh.model.mesh.add_elements_by_type(
    s, element_type_2d, tags_for_triangles, face_nodes_for_triangles
)

# Since the tags for the triangles have been created based on the face tags,
# the information about neighboring elements can also be readily created,
# useful e.g. in Finite Volume or Discontinuous Galerkin techniques:
for t in tags_for_triangles:
    print(
        "triangle "
        + str(int(t))
        + " is connected to tetrahedra "
        + str(faces2elements[t - max_element_tag])
    )

# If all you need is the list of all edges or faces in terms of their nodes, you
# can also directly call:
edge_tags, edge_nodes = gmsh.model.mesh.get_all_edges()
face_tags, face_nodes = gmsh.model.mesh.get_all_faces(3)

# Launch the GUI to see the results:
if "-nopopup" not in sys.argv:
    gmsh.fltk.run()

gmsh.finalize()
