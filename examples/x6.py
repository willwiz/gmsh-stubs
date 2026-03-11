# /// script
# dependencies = []
# ///

import sys

import gmsh

gmsh.initialize(sys.argv)

gmsh.model.add("x6")

# The API provides access to all the elementary building blocks required to
# implement finite-element-type numerical methods. Let's create a simple 2D
# model and mesh it:
gmsh.model.occ.add_rectangle(0, 0, 0, 1, 0.1)
gmsh.model.occ.synchronize()
gmsh.model.mesh.set_transfinite_automatic()
gmsh.model.mesh.generate(2)

# Set the element order and the desired interpolation order:
element_order = 1
interpolation_order = 2
gmsh.model.mesh.set_order(element_order)


def pp(label: str, v: list[float], mult: float) -> None:
    print(" * " + str(len(v) / mult) + " " + label + ": " + str(v))


# Iterate over all the element types present in the mesh:
element_types = gmsh.model.mesh.get_element_types()

for t in element_types:
    # Retrieve properties for the given element type
    element_name, dim, order, num_nodes, local_node_coord, num_prim_nodes = (
        gmsh.model.mesh.get_element_properties(t)
    )
    print("\n** " + element_name + " **\n")

    # Retrieve integration points for that element type, enabling exact
    # integration of polynomials of order "interpolationOrder". The "Gauss"
    # integration family returns the "economical" Gauss points if available, and
    # defaults to the "CompositeGauss" (tensor product) rule if not.
    local_coords, weights = gmsh.model.mesh.get_integration_points(
        t, "Gauss" + str(interpolation_order)
    )
    pp(
        "integration points to integrate order " + str(interpolation_order) + " polynomials",
        local_coords,
        3,
    )

    # Return the basis functions evaluated at the integration points. Selecting
    # "Lagrange" and "GradLagrange" returns the isoparamtric basis functions and
    # their gradient (in the reference space of the given element type). A
    # specific interpolation order can be requested using "LagrangeN" and
    # "GradLagrangeN" with N = 1, 2, ... Other supported function spaces include
    # "H1LegendreN", "GradH1LegendreN", "HcurlLegendreN", "CurlHcurlLegendreN".
    num_components, basis_functions, num_orientations = gmsh.model.mesh.get_basis_functions(
        t, local_coords, "Lagrange"
    )
    pp("basis functions at integration points", basis_functions, 1)
    num_components, basis_functions, num_orientations = gmsh.model.mesh.get_basis_functions(
        t, local_coords, "GradLagrange"
    )
    pp("basis function gradients at integration points", basis_functions, 3)

    # Compute the Jacobians (and their determinants) at the integration points
    # for all the elements of the given type in the mesh. Beware that the
    # Jacobians are returned "by column": see the API documentation for details.
    jacobians, determinants, coords = gmsh.model.mesh.get_jacobians(t, local_coords)
    pp("Jacobian determinants at integration points", determinants, 1)

gmsh.finalize()
