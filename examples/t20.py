# /// script
# dependencies = []
# ///

import math
import os
import sys
from pathlib import Path

import gmsh


def main(direction: str) -> None:
    gmsh.initialize()

    gmsh.model.add("t20")

    # Load a STEP file (using `importShapes' instead of `merge' allows to directly
    # retrieve the tags of the highest dimensional imported entities):
    path = Path(__file__).parent
    v = gmsh.model.occ.import_shapes(str(path / os.pardir / "t20_data.step"))

    # If we had specified
    #
    # gmsh.option.setString('Geometry.OCCTargetUnit', 'M')
    #
    # before merging the STEP file, OpenCASCADE would have converted the units to
    # meters (instead of the default, which is millimeters).

    # Get the bounding box of the volume:
    xmin, ymin, zmin, xmax, ymax, zmax = gmsh.model.occ.get_bounding_box(v[0][0], v[0][1])

    # We want to slice the model into N slices, and either keep the volume slices
    # or just the surfaces obtained by the cutting:

    n = 5  # Number of slices
    surf = False  # Keep only surfaces?

    dx = xmax - xmin
    dy = ymax - ymin
    dz = zmax - zmin
    ll = dz if (direction == "X") else dx
    h = dz if (direction == "Y") else dy

    # Create the first cutting plane:
    s: list[tuple[int, int]] = []
    s.append((2, gmsh.model.occ.add_rectangle(xmin, ymin, zmin, ll, h)))
    if direction == "X":
        gmsh.model.occ.rotate([s[0]], xmin, ymin, zmin, 0, 1, 0, -math.pi / 2)
    elif direction == "Y":
        gmsh.model.occ.rotate([s[0]], xmin, ymin, zmin, 1, 0, 0, math.pi / 2)
    tx = dx / n if (direction == "X") else 0
    ty = dy / n if (direction == "Y") else 0
    tz = dz / n if (direction == "Z") else 0
    gmsh.model.occ.translate([s[0]], tx, ty, tz)

    # Create the other cutting planes:
    for i in range(1, n - 1):
        s.extend(gmsh.model.occ.copy([s[0]]))
        gmsh.model.occ.translate([s[-1]], i * tx, i * ty, i * tz)

    # Fragment (i.e. intersect) the volume with all the cutting planes:
    gmsh.model.occ.fragment(v, s)

    # Now remove all the surfaces (and their bounding entities) that are not on the
    # boundary of a volume, i.e. the parts of the cutting planes that "stick out" of
    # the volume:
    gmsh.model.occ.remove(gmsh.model.occ.get_entities(2), recursive=True)

    gmsh.model.occ.synchronize()

    if surf:
        # If we want to only keep the surfaces, retrieve the surfaces in bounding
        # boxes around the cutting planes...
        eps = 1e-4
        s = []
        for i in range(1, n):
            xx = xmin if (direction == "X") else xmax
            yy = ymin if (direction == "Y") else ymax
            zz = zmin if (direction == "Z") else zmax
            s.extend(
                gmsh.model.get_entities_in_bounding_box(
                    xmin - eps + i * tx,
                    ymin - eps + i * ty,
                    zmin - eps + i * tz,
                    xx + eps + i * tx,
                    yy + eps + i * ty,
                    zz + eps + i * tz,
                    2,
                )
            )
        # ...and remove all the other entities (here directly in the model, as we
        # won't modify any OpenCASCADE entities later on):
        dels = gmsh.model.get_entities(2)
        for e in s:
            dels.remove(e)
        gmsh.model.remove_entities(gmsh.model.get_entities(3))
        gmsh.model.remove_entities(dels)
        gmsh.model.remove_entities(gmsh.model.get_entities(1))
        gmsh.model.remove_entities(gmsh.model.get_entities(0))

    # Finally, let's specify a global mesh size and mesh the partitioned model:
    gmsh.option.set_number("Mesh.MeshSizeMin", 3)
    gmsh.option.set_number("Mesh.MeshSizeMax", 3)
    gmsh.model.mesh.generate(3)
    gmsh.write("t20.msh")

    # Launch the GUI to see the results:
    if "-nopopup" not in sys.argv:
        gmsh.fltk.run()

    gmsh.finalize()


if __name__ == "__main__":
    direction: str = "X"  # Direction: 'X', 'Y' or 'Z'
    main(direction)
