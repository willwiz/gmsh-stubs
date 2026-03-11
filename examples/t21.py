# /// script
# dependencies = []
# ///

import sys

import gmsh

# Gmsh can partition meshes using different algorithms, e.g. the graph
# partitioner Metis or the `SimplePartition' plugin. For all the partitioning
# algorithms, the relationship between mesh elements and mesh partitions is
# encoded through the creation of new (discrete) elementary entities, called
# "partition entities".
#
# Partition entities behave exactly like other discrete elementary entities; the
# only difference is that they keep track of both a mesh partition index and
# their parent elementary entity.
#
# The major advantage of this approach is that it allows to maintain a full
# boundary representation of the partition entities, which Gmsh creates
# automatically if `Mesh.PartitionCreateTopology' is set.

gmsh.initialize()

# Let us start by creating a simple geometry with two adjacent squares sharing
# an edge:
gmsh.model.add("t21")
gmsh.model.occ.add_rectangle(0, 0, 0, 1, 1, 1)
gmsh.model.occ.add_rectangle(1, 0, 0, 1, 1, 2)
gmsh.model.occ.fragment([(2, 1)], [(2, 2)])
gmsh.model.occ.synchronize()
gmsh.model.mesh.set_size(gmsh.model.get_entities(0), 0.05)

# We create one physical group for each square, and we mesh the resulting
# geometry:
gmsh.model.add_physical_group(2, [1], 100, "Left")
gmsh.model.add_physical_group(2, [2], 200, "Right")
gmsh.model.mesh.generate(2)

# We now define several ONELAB parameters to fine-tune how the mesh will be
# partitioned:
gmsh.onelab.set("""[
  {
    "type":"number",
    "name":"Parameters/0Mesh partitioner",
    "values":[0],
    "choices":[0, 1],
    "valueLabels":{"Metis":0, "SimplePartition":1}
  },
  {
    "type":"number",
    "name":"Parameters/1Number of partitions",
    "values":[3],
    "min":1,
    "max":256,
    "step":1
  },
  {
    "type":"number",
    "name":"Parameters/2Create partition topology (BRep)?",
    "values":[1],
    "choices":[0, 1]
  },
  {
    "type":"number",
    "name":"Parameters/3Create ghost cells?",
    "values":[0],
    "choices":[0, 1]
  },
  {
    "type":"number",
    "name":"Parameters/3Create new physical groups?",
    "values":[0],
    "choices":[0, 1]
  },
  {
    "type":"number",
    "name":"Parameters/3Write file to disk?",
    "values":[1],
    "choices":[0, 1]
  },
  {
    "type":"number",
    "name":"Parameters/4Write one file per partition?",
    "values":[0],
    "choices":[0, 1]
  }
]""")


def partition_mesh() -> None:
    # Number of partitions
    n = int(gmsh.onelab.get_number("Parameters/1Number of partitions")[0])

    # Should we create the boundary representation of the partition entities?
    gmsh.option.set_number(
        "Mesh.PartitionCreateTopology",
        gmsh.onelab.get_number("Parameters/2Create partition topology (BRep)?")[0],
    )

    # Should we create ghost cells?
    gmsh.option.set_number(
        "Mesh.PartitionCreateGhostCells",
        gmsh.onelab.get_number("Parameters/3Create ghost cells?")[0],
    )

    # Should we automatically create new physical groups on the partition
    # entities?
    gmsh.option.set_number(
        "Mesh.PartitionCreatePhysicals",
        gmsh.onelab.get_number("Parameters/3Create new physical groups?")[0],
    )

    # Should we keep backward compatibility with pre-Gmsh 4, e.g. to save the
    # mesh in MSH2 format?
    gmsh.option.set_number("Mesh.PartitionOldStyleMsh2", 0)

    # Should we save one mesh file per partition?
    gmsh.option.set_number(
        "Mesh.PartitionSplitMeshFiles",
        gmsh.onelab.get_number("Parameters/4Write one file per partition?")[0],
    )

    if gmsh.onelab.get_number("Parameters/0Mesh partitioner")[0] == 0:
        # Use Metis to create N partitions
        gmsh.model.mesh.partition(n)
        # Several options can be set to control Metis: `Mesh.MetisAlgorithm' (1:
        # Recursive, 2: K-way), `Mesh.MetisObjective' (1: min. edge-cut, 2:
        # min. communication volume), `Mesh.PartitionTriWeight' (weight of
        # triangles), `Mesh.PartitionQuadWeight' (weight of quads), ...
    else:
        # Use the `SimplePartition' plugin to create chessboard-like partitions
        gmsh.plugin.set_number("SimplePartition", "NumSlicesX", n)
        gmsh.plugin.set_number("SimplePartition", "NumSlicesY", 1)
        gmsh.plugin.set_number("SimplePartition", "NumSlicesZ", 1)
        gmsh.plugin.run("SimplePartition")

    # Save mesh file (or files, if `Mesh.PartitionSplitMeshFiles' is set):
    if gmsh.onelab.get_number("Parameters/3Write file to disk?")[0] == 1:
        gmsh.write("t21.msh")

    # Iterate over partitioned entities and print some info (see the first
    # extended tutorial `x1.py' for additional information):
    entities = gmsh.model.get_entities()
    for e in entities:
        partitions = gmsh.model.get_partitions(e[0], e[1])
        if len(partitions):
            print("Entity " + str(e) + " of type " + gmsh.model.get_type(e[0], e[1]))
            print(" - Partition(s): " + str(partitions))
            print(" - Parent: " + str(gmsh.model.get_parent(e[0], e[1])))
            print(" - Boundary: " + str(gmsh.model.get_boundary([e])))


partition_mesh()


# Launch the GUI and handle the "check" event to re-partition the mesh according
# to the choices made in the GUI
def check_for_event() -> bool:
    action = gmsh.onelab.get_string("ONELAB/Action")
    if len(action) and action[0] == "check":
        gmsh.onelab.set_string("ONELAB/Action", [""])
        partition_mesh()
        gmsh.graphics.draw()
    return True


if "-nopopup" not in sys.argv:
    gmsh.fltk.initialize()
    while gmsh.fltk.is_available() and check_for_event():
        gmsh.fltk.wait()

gmsh.finalize()
