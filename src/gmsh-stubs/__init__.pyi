from collections.abc import Callable, Sequence
from typing import Any

import numpy as np
from _typeshed import Incomplete

GMSH_API_VERSION: str
GMSH_API_VERSION_MAJOR: int
GMSH_API_VERSION_MINOR: int
GMSH_API_VERSION_PATCH: int
__version__ = GMSH_API_VERSION
type _ToTag = int | np.integer[Any]
type _ToDim = int | np.integer[Any]
type _ToName = str | np.str_
type _API_RESULT_ = int
type _SizeCallBackProtocol_ = Callable[[int, int, float, float, float, float], float]
type _DIM_TAGS_ = list[tuple[int, int]]
type _FILE_IO_ = str
type _Size_ = int
type _TAG_ = int
# Dimension
type _DIM_ = int
type _RGB_ = tuple[int, int, int, int]
type _S1D = tuple[int]
type _S2D = tuple[int, int]
type _S3D = tuple[int, int, int]
type _VectorInt_[D: _S1D | _S2D | _S3D = _S1D] = Sequence[int] | np.ndarray[D, np.dtype[np.integer]]
type _VectorFloat_[D: _S1D | _S2D | _S3D = _S1D] = (
    Sequence[float] | np.ndarray[D, np.dtype[np.floating]]
)
type _VectorString_[D: _S1D | _S2D | _S3D = _S1D] = Sequence[str] | np.ndarray[D, np.dtype[np.str_]]

type _Method_ = str
type _ElemFamily_ = str
type _ElemType_ = int
type _FACE_TYPE_ = int
type _FuncSpace_ = str
type _Int1D_[I: np.integer = np.intp] = np.ndarray[tuple[int], np.dtype[I]]
type _Int2D_[I: np.integer = np.intp] = list[_Int1D_[I]]
type _Float1D_[F: np.floating = np.float64] = np.ndarray[tuple[int], np.dtype[F]]
type _Float2D_[F: np.floating = np.float64] = list[_Float1D_[F]]
type _String1D_ = np.ndarray[tuple[int, int], np.dtype[np.str_]]

def initialize(
    argv: Sequence[str] = [],
    *,
    readConfigFiles: bool = True,
    run: bool = False,
    interruptible: bool = True,
) -> None: ...
def is_initialized() -> int: ...
def finalize() -> None: ...
def open(fileName: _FILE_IO_) -> None: ...
def merge(fileName: _FILE_IO_) -> None: ...
def write(fileName: _FILE_IO_) -> None: ...
def clear() -> None: ...

class option:
    @staticmethod
    def set_number(name: _ToName, value: float) -> None: ...
    @staticmethod
    def get_number(name: _ToName) -> float: ...
    @staticmethod
    def set_string(name: _ToName, value: str) -> None: ...
    @staticmethod
    def get_string(name: _ToName) -> str: ...
    @staticmethod
    def set_color(name: _ToName, r: int, g: int, b: int, a: int = 255) -> None: ...
    @staticmethod
    def get_color(name: _ToName) -> _RGB_: ...
    @staticmethod
    def restore_defaults() -> None: ...

class model:
    @staticmethod
    def add(name: _ToName) -> None: ...
    @staticmethod
    def remove() -> None: ...
    @staticmethod
    def list() -> _String1D_: ...
    @staticmethod
    def get_current() -> str: ...
    @staticmethod
    def set_current(name: str) -> None: ...
    @staticmethod
    def get_file_name() -> str: ...
    @staticmethod
    def set_file_name(fileName: _FILE_IO_) -> None: ...
    @staticmethod
    def get_entities(dim: _ToDim = -1) -> _DIM_TAGS_: ...
    @staticmethod
    def set_entity_name(dim: _ToDim, tag: _ToTag, name: str) -> None: ...
    @staticmethod
    def get_entity_name(dim: _ToDim, tag: _ToTag) -> str: ...
    @staticmethod
    def remove_entity_name(name: str) -> None: ...
    @staticmethod
    def get_physical_groups(dim: _ToDim = -1) -> _DIM_TAGS_: ...
    @staticmethod
    def get_physical_groups_entities(
        dim: _ToDim = -1,
    ) -> tuple[_DIM_TAGS_, list[_DIM_TAGS_]]: ...
    @staticmethod
    def get_entities_for_physical_group(dim: _ToDim, tag: _ToTag) -> _Int1D_: ...
    @staticmethod
    def get_entities_for_physical_name(name: str) -> _DIM_TAGS_: ...
    @staticmethod
    def get_physical_groups_for_entity(dim: _ToDim, tag: _ToTag) -> _Int1D_: ...
    @staticmethod
    def add_physical_group(
        dim: _ToDim, tags: _VectorInt_, tag: _ToTag = -1, name: str = ""
    ) -> int: ...
    @staticmethod
    def remove_physical_groups(dimTags: _DIM_TAGS_ = []) -> None: ...
    @staticmethod
    def set_physical_name(dim: _ToDim, tag: _ToTag, name: str) -> None: ...
    @staticmethod
    def get_physical_name(dim: _ToTag, tag: _ToTag) -> str: ...
    @staticmethod
    def remove_physical_name(name: str) -> None: ...
    @staticmethod
    def set_tag(dim: _ToDim, tag: _ToTag, newTag: int) -> None: ...
    @staticmethod
    def get_boundary(
        dimTags: _DIM_TAGS_,
        *,
        combined: bool = True,
        oriented: bool = False,
        recursive: bool = False,
    ) -> _DIM_TAGS_: ...
    @staticmethod
    def get_adjacencies(dim: _ToDim, tag: _ToTag) -> _DIM_TAGS_: ...
    @staticmethod
    def is_entity_orphan(dim: _ToDim, tag: _ToTag) -> _API_RESULT_: ...
    @staticmethod
    def get_entities_in_bounding_box(
        xmin: float,
        ymin: float,
        zmin: float,
        xmax: float,
        ymax: float,
        zmax: float,
        dim: _ToDim = -1,
    ) -> _DIM_TAGS_: ...
    @staticmethod
    def get_bounding_box(
        dim: _ToDim, tag: _ToTag
    ) -> tuple[float, float, float, float, float, float]: ...
    @staticmethod
    def get_dimension() -> _DIM_: ...
    @staticmethod
    def add_discrete_entity(dim: _ToDim, tag: _ToTag = -1, boundary: _VectorInt_ = []) -> int: ...
    @staticmethod
    def remove_entities(dimTags: _DIM_TAGS_, *, recursive: bool = False) -> None: ...
    @staticmethod
    def get_entity_type(dim: _ToDim, tag: _ToTag) -> str: ...
    @staticmethod
    def get_type(dim: _ToDim, tag: _ToTag) -> str: ...
    @staticmethod
    def get_entity_properties(dim: _ToDim, tag: _ToTag) -> tuple[_DIM_, _TAG_]: ...
    @staticmethod
    def get_parent(dim: _ToDim, tag: _ToTag) -> tuple[_DIM_, _TAG_]: ...
    @staticmethod
    def get_number_of_partitions() -> int: ...
    @staticmethod
    def get_partitions(dim: _ToDim, tag: _ToTag) -> _Int1D_: ...
    @staticmethod
    def get_value(dim: _ToDim, tag: _ToTag, parametricCoord: _VectorFloat_) -> _Float1D_: ...
    @staticmethod
    def get_derivative(dim: _ToDim, tag: _ToTag, parametricCoord: _VectorFloat_) -> _Float1D_: ...
    @staticmethod
    def get_second_derivative(
        dim: _ToDim, tag: _ToTag, parametricCoord: _VectorFloat_
    ) -> _Float1D_: ...
    @staticmethod
    def get_curvature(dim: _ToDim, tag: _ToTag, parametricCoord: _VectorFloat_) -> _Float1D_: ...
    @staticmethod
    def get_principal_curvatures(
        tag: _ToTag, parametricCoord: _VectorFloat_
    ) -> tuple[_VectorFloat_, _VectorFloat_, _VectorFloat_, _VectorFloat_]: ...
    @staticmethod
    def get_normal(tag: _ToTag, parametricCoord: _VectorFloat_) -> _VectorFloat_: ...
    @staticmethod
    def get_parametrization(dim: _ToDim, tag: _ToTag, coord: _VectorFloat_) -> _Float1D_: ...
    @staticmethod
    def get_parametrization_bounds(dim: _ToDim, tag: _ToTag) -> tuple[_Float1D_, _Float1D_]: ...
    @staticmethod
    def is_inside(
        dim: _ToDim, tag: _ToTag, coord: _VectorFloat_, parametric: bool = False
    ) -> _API_RESULT_: ...
    @staticmethod
    def get_closest_point(
        dim: _ToDim, tag: _ToTag, coord: _VectorFloat_
    ) -> tuple[_Float1D_, _Float1D_]: ...
    @staticmethod
    def reparametrize_on_surface(
        dim: _ToDim, tag: _ToTag, parametricCoord: _VectorFloat_, surfaceTag: _ToTag, which: int = 0
    ) -> _VectorFloat_: ...
    @staticmethod
    def set_visibility(dimTags: _DIM_TAGS_, value: int, recursive: bool = False) -> None: ...
    @staticmethod
    def get_visibility(dim: _ToDim, tag: _ToTag) -> _API_RESULT_: ...
    @staticmethod
    def set_visibility_per_window(value: int, windowIndex: int = 0) -> None: ...
    @staticmethod
    def set_color(
        dimTags: _DIM_TAGS_, r: int, g: int, b: int, a: int = 255, recursive: bool = False
    ) -> None: ...
    @staticmethod
    def get_color(dim: _ToDim, tag: _ToTag) -> _RGB_: ...
    @staticmethod
    def set_coordinates(tag: _ToTag, x: float, y: float, z: float) -> None: ...
    @staticmethod
    def set_attribute(name: _ToName, values: _VectorString_) -> None: ...
    @staticmethod
    def get_attribute(name: _ToName) -> _String1D_: ...
    @staticmethod
    def get_attribute_names() -> _String1D_: ...
    @staticmethod
    def remove_attribute(name: _ToName) -> None: ...
    class mesh:
        @staticmethod
        def generate(dim: _ToDim = 3) -> None: ...
        @staticmethod
        def partition(
            numPart: int, elementTags: _VectorInt_ = [], partitions: _VectorInt_ = []
        ) -> None: ...
        @staticmethod
        def unpartition() -> None: ...
        @staticmethod
        def optimize(
            method: str = "", force: bool = False, niter: int = 1, dimTags: _DIM_TAGS_ = []
        ) -> None: ...
        @staticmethod
        def recombine() -> None: ...
        @staticmethod
        def refine() -> None: ...
        @staticmethod
        def set_order(order: int) -> None: ...
        @staticmethod
        def get_last_entity_error() -> _DIM_TAGS_: ...
        @staticmethod
        def get_last_node_error() -> _Int1D_: ...
        @staticmethod
        def clear(dimTags: _DIM_TAGS_ = []) -> None: ...
        @staticmethod
        def remove_elements(dim: _ToDim, tag: _ToTag, elementTags: _VectorInt_ = []) -> None: ...
        @staticmethod
        def reverse(dimTags: _DIM_TAGS_ = []) -> None: ...
        @staticmethod
        def reverse_elements(elementTags: _VectorInt_) -> None: ...
        @staticmethod
        def affine_transform(affineTransform: _VectorFloat_, dimTags: _DIM_TAGS_ = []) -> None: ...
        @staticmethod
        def get_nodes(
            dim: _ToDim = -1,
            tag: _ToTag = -1,
            includeBoundary: bool = False,
            returnParametricCoord: bool = True,
        ) -> tuple[_Int1D_, _Float1D_, _Float1D_]: ...
        @staticmethod
        def get_nodes_by_element_type(
            elementType: _ElemType_, tag: _ToTag = -1, returnParametricCoord: bool = True
        ) -> tuple[_Int1D_, _Float1D_, _Float1D_]: ...
        @staticmethod
        def get_node(nodeTag: _Size_) -> tuple[_VectorFloat_, _VectorFloat_, _DIM_, _TAG_]: ...
        @staticmethod
        def set_node(
            nodeTag: _Size_, coord: _VectorFloat_, parametricCoord: _VectorFloat_
        ) -> None: ...
        @staticmethod
        def rebuild_node_cache(onlyIfNecessary: bool = True) -> None: ...
        @staticmethod
        def rebuild_element_cache(onlyIfNecessary: bool = True) -> None: ...
        @staticmethod
        def get_nodes_for_physical_group(dim: _ToDim, tag: _ToTag) -> tuple[_Int1D_, _Float1D_]: ...
        @staticmethod
        def get_max_node_tag() -> _Size_: ...
        @staticmethod
        def add_nodes(
            dim: _ToDim,
            tag: _ToTag,
            nodeTags: _VectorInt_,
            coord: _VectorFloat_,
            parametricCoord: _VectorFloat_ = [],
        ) -> None: ...
        @staticmethod
        def reclassify_nodes() -> None: ...
        @staticmethod
        def relocate_nodes(dim: _ToDim = -1, tag: _ToTag = -1) -> None: ...
        @staticmethod
        def get_elements(
            dim: _ToDim = -1, tag: _ToTag = -1
        ) -> tuple[_Int1D_, _Int2D_, _Int2D_]: ...
        @staticmethod
        def get_element(elementTag: _Size_) -> tuple[_ElemType_, _Int1D_, _DIM_, _TAG_]: ...
        @staticmethod
        def get_element_by_coordinates(
            x: float, y: float, z: float, dim: _ToDim = -1, strict: bool = False
        ) -> tuple[_Size_, _ElemType_, _Int1D_, float, float, float]: ...
        @staticmethod
        def get_elements_by_coordinates(
            x: float, y: float, z: float, dim: _ToDim = -1, strict: bool = False
        ) -> _Int1D_: ...
        @staticmethod
        def get_local_coordinates_in_element(
            elementTag: _Size_, x: float, y: float, z: float
        ) -> tuple[float, float, float]: ...
        @staticmethod
        def get_element_types(dim: _ToDim = -1, tag: _ToTag = -1) -> _Int1D_: ...
        @staticmethod
        def get_element_type(
            familyName: _ElemFamily_, order: int, serendip: bool = False
        ) -> _ElemType_: ...
        @staticmethod
        def get_element_properties(
            elementType: _ToTag,
        ) -> tuple[str, _DIM_, int, int, _VectorFloat_, int]: ...
        @staticmethod
        def get_elements_by_type(
            elementType: _ElemType_, tag: _ToTag = -1, task: int = 0, numTasks: int = 1
        ) -> tuple[_Int1D_, _Int1D_]: ...
        @staticmethod
        def get_max_element_tag() -> _Size_: ...
        @staticmethod
        def get_element_qualities(
            elementTags: _VectorInt_, qualityName: str = "minSICN", task: int = 0, numTasks: int = 1
        ) -> _Float1D_: ...
        @staticmethod
        def add_elements(
            dim: _ToDim,
            tag: _ToTag,
            elementTypes: _VectorInt_,
            elementTags: Sequence[_VectorInt_],
            nodeTags: Sequence[_VectorInt_],
        ) -> None: ...
        @staticmethod
        def add_elements_by_type(
            tag: _ToTag, elementType: int, elementTags: _VectorInt_, nodeTags: _VectorInt_
        ) -> None: ...
        @staticmethod
        def get_integration_points(
            elementType: _ToTag, integrationType: str
        ) -> tuple[_Float1D_, _Float1D_]: ...
        @staticmethod
        def get_jacobians(
            elementType: _ToTag,
            localCoord: _VectorFloat_,
            tag: _ToTag = -1,
            task: int = 0,
            numTasks: int = 1,
        ) -> tuple[_Float1D_, _Float1D_, _Float1D_]: ...
        @staticmethod
        def get_jacobian(
            elementTag: _Size_, localCoord: _VectorFloat_
        ) -> tuple[_Float1D_, _Float1D_, _Float1D_]: ...
        @staticmethod
        def get_basis_functions(
            elementType: _ToTag,
            localCoord: _VectorFloat_,
            functionSpaceType: _FuncSpace_,
            wantedOrientations: _VectorInt_ = [],
        ) -> tuple[_Size_, _Float1D_, _Size_]: ...
        @staticmethod
        def get_basis_functions_orientation(
            elementType: _ElemType_,
            functionSpaceType: _FuncSpace_,
            tag: _ToTag = -1,
            task: int = 0,
            numTasks: int = 1,
        ) -> _Int1D_: ...
        @staticmethod
        def get_basis_functions_orientation_for_element(
            elementTag: _Size_, functionSpaceType: _FuncSpace_
        ) -> int: ...
        @staticmethod
        def get_number_of_orientations(
            elementType: _ElemType_, functionSpaceType: _FuncSpace_
        ) -> _Size_: ...
        @staticmethod
        def get_edges(nodeTags: _VectorInt_) -> tuple[_Int1D_, _Int1D_]: ...
        @staticmethod
        def get_faces(faceType: _FACE_TYPE_, nodeTags: _VectorInt_) -> tuple[_Int1D_, _Int1D_]: ...
        @staticmethod
        def create_edges(dimTags: _DIM_TAGS_ = []) -> None: ...
        @staticmethod
        def create_faces(dimTags: _DIM_TAGS_ = []) -> None: ...
        @staticmethod
        def get_all_edges() -> tuple[_Int1D_, _Int1D_]: ...
        @staticmethod
        def get_all_faces(faceType: _FACE_TYPE_) -> tuple[_Int1D_, _Int1D_]: ...
        @staticmethod
        def add_edges(edgeTags: _VectorInt_, edgeNodes: _VectorInt_) -> None: ...
        @staticmethod
        def add_faces(
            faceType: _FACE_TYPE_, faceTags: _VectorInt_, faceNodes: _VectorInt_
        ) -> None: ...
        @staticmethod
        def get_keys(
            elementType: _ElemType_,
            functionSpaceType: _FuncSpace_,
            tag: _ToTag = -1,
            returnCoord: bool = True,
        ) -> tuple[_Int1D_, _Int1D_, _Float1D_]: ...
        @staticmethod
        def get_keys_for_element(
            elementTag: _Size_, functionSpaceType: _FuncSpace_, returnCoord: bool = True
        ) -> tuple[_Int1D_, _Int1D_, _Float1D_]: ...
        @staticmethod
        def get_number_of_keys(
            elementType: _ElemType_, functionSpaceType: _FuncSpace_
        ) -> _Size_: ...
        @staticmethod
        def get_keys_information(
            typeKeys: _VectorInt_,
            entityKeys: _VectorInt_,
            elementType: _ElemType_,
            functionSpaceType: _FuncSpace_,
        ) -> list[tuple[int, int]]: ...
        @staticmethod
        def get_barycenters(
            elementType: _ElemType_,
            tag: _ToTag,
            fast: bool,
            primary: bool,
            task: int = 0,
            numTasks: int = 1,
        ) -> _Float1D_: ...
        @staticmethod
        def get_element_edge_nodes(
            elementType: _ElemType_,
            tag: _ToTag = -1,
            primary: bool = False,
            task: int = 0,
            numTasks: int = 1,
        ) -> _Int1D_: ...
        @staticmethod
        def get_element_face_nodes(
            elementType: _ElemType_,
            faceType: _FACE_TYPE_,
            tag: _ToTag = -1,
            primary: bool = False,
            task: int = 0,
            numTasks: int = 1,
        ) -> _Int1D_: ...
        @staticmethod
        def get_ghost_elements(dim: _ToDim, tag: _ToTag) -> tuple[_Int1D_, _Int1D_]: ...
        @staticmethod
        def set_size(dimTags: _DIM_TAGS_, size: float) -> None: ...
        @staticmethod
        def get_sizes(dimTags: _DIM_TAGS_) -> _Float1D_: ...
        @staticmethod
        def set_size_at_parametric_points(
            dim: _ToDim, tag: _ToTag, parametricCoord: _VectorFloat_, sizes: _VectorFloat_
        ) -> None: ...
        @staticmethod
        def set_size_callback(callback: _SizeCallBackProtocol_) -> None: ...
        @staticmethod
        def remove_size_callback() -> None: ...
        @staticmethod
        def set_transfinite_curve(
            tag: _ToTag, numNodes: int, meshType: str = "Progression", coef: float = 1.0
        ) -> None: ...
        @staticmethod
        def set_transfinite_surface(
            tag: _ToTag, arrangement: str = "Left", cornerTags: _VectorInt_ = []
        ) -> None: ...
        @staticmethod
        def set_transfinite_volume(tag: _ToTag, cornerTags: _VectorInt_ = []) -> None: ...
        @staticmethod
        def set_transfinite_automatic(
            dimTags: _DIM_TAGS_ = [], cornerAngle: float = 2.35, recombine: bool = True
        ) -> None: ...
        @staticmethod
        def set_recombine(dim: _ToDim, tag: _ToTag, angle: float = 45.0) -> None: ...
        @staticmethod
        def set_smoothing(dim: _ToDim, tag: _ToTag, val: int) -> None: ...
        @staticmethod
        def set_reverse(dim: _ToDim, tag: _ToTag, val: bool = True) -> None: ...
        @staticmethod
        def set_algorithm(dim: _ToDim, tag: _ToTag, val: int) -> None: ...
        @staticmethod
        def set_size_from_boundary(dim: _ToDim, tag: _ToTag, val: int) -> None: ...
        @staticmethod
        def set_compound(dim: _ToDim, tags: _VectorInt_) -> None: ...
        @staticmethod
        def set_outward_orientation(tag: _ToTag) -> None: ...
        @staticmethod
        def remove_constraints(dimTags: _DIM_TAGS_ = []) -> None: ...
        @staticmethod
        def embed(dim: _ToDim, tags: _VectorInt_, inDim: int, inTag: int) -> None: ...
        @staticmethod
        def remove_embedded(dimTags: _DIM_TAGS_, dim: _ToDim = -1) -> None: ...
        @staticmethod
        def get_embedded(dim: _ToDim, tag: _ToTag) -> _DIM_TAGS_: ...
        @staticmethod
        def reorder_elements(
            elementType: _ElemType_, tag: _ToTag, ordering: _VectorInt_
        ) -> None: ...
        @staticmethod
        def compute_renumbering(
            method: str = "RCMK", elementTags: _VectorInt_ = []
        ) -> tuple[_Int1D_, _Int1D_]: ...
        @staticmethod
        def renumber_nodes(oldTags: _VectorInt_ = [], newTags: _VectorInt_ = []) -> None: ...
        @staticmethod
        def renumber_elements(oldTags: _VectorInt_ = [], newTags: _VectorInt_ = []) -> None: ...
        @staticmethod
        def set_periodic(
            dim: _ToDim, tags: _VectorInt_, tagsMaster: _VectorInt_, affineTransform: _VectorFloat_
        ) -> None: ...
        @staticmethod
        def get_periodic(dim: _ToDim, tags: _VectorInt_) -> _Int1D_: ...
        @staticmethod
        def get_periodic_nodes(
            dim: _ToDim, tag: _ToTag, includeHighOrderNodes: bool = False
        ) -> tuple[_TAG_, _Int1D_, _Int1D_, _Float1D_]: ...
        @staticmethod
        def get_periodic_keys(
            elementType: _ElemType_,
            functionSpaceType: _FuncSpace_,
            tag: _ToTag,
            returnCoord: bool = True,
        ) -> tuple[_TAG_, _Int1D_, _Int1D_, _Int1D_, _Int1D_, _Float1D_, _Float1D_]: ...
        @staticmethod
        def import_stl() -> None: ...
        @staticmethod
        def get_duplicate_nodes(dimTags: _DIM_TAGS_ = []) -> _Int1D_: ...
        @staticmethod
        def remove_duplicate_nodes(dimTags: _DIM_TAGS_ = []) -> None: ...
        @staticmethod
        def remove_duplicate_elements(dimTags: _DIM_TAGS_ = []) -> None: ...
        @staticmethod
        def split_quadrangles(quality: float = 1.0, tag: _ToTag = -1) -> None: ...
        @staticmethod
        def set_visibility(elementTags: _VectorInt_, value: int) -> None: ...
        @staticmethod
        def get_visibility(elementTags: _VectorInt_) -> _Int1D_: ...
        @staticmethod
        def classify_surfaces(
            angle: float,
            boundary: bool = True,
            forReparametrization: bool = False,
            curveAngle: float = ...,
            exportDiscrete: bool = True,
        ) -> None: ...
        @staticmethod
        def create_geometry(dimTags: _DIM_TAGS_ = []) -> None: ...
        @staticmethod
        def create_topology(
            makeSimplyConnected: bool = True, exportDiscrete: bool = True
        ) -> None: ...
        @staticmethod
        def add_homology_request(
            type: str = "Homology",
            domainTags: _VectorInt_ = [],
            subdomainTags: _VectorInt_ = [],
            dims: _VectorInt_ = [],
        ) -> None: ...
        @staticmethod
        def clear_homology_requests() -> None: ...
        @staticmethod
        def compute_homology() -> _DIM_TAGS_: ...
        @staticmethod
        def compute_cross_field() -> _Int1D_: ...
        class field:
            @staticmethod
            def add(fieldType: str, tag: _ToTag = -1) -> int: ...
            @staticmethod
            def remove(tag: _ToTag) -> None: ...
            @staticmethod
            def list() -> _Int1D_: ...
            @staticmethod
            def get_type(tag: _ToTag) -> _FILE_IO_: ...
            @staticmethod
            def set_number(tag: _ToTag, option: _Method_, value: float) -> None: ...
            @staticmethod
            def get_number(tag: _ToTag, option: _Method_) -> float: ...
            @staticmethod
            def set_string(tag: _ToTag, option: _Method_, value: _Method_) -> None: ...
            @staticmethod
            def get_string(tag: _ToTag, option: _Method_) -> str: ...
            @staticmethod
            def set_numbers(tag: _ToTag, option: _Method_, values: _VectorInt_) -> None: ...
            @staticmethod
            def get_numbers(tag: _ToTag, option: _Method_) -> _Float1D_: ...
            @staticmethod
            def set_as_background_mesh(tag: _ToTag) -> None: ...
            @staticmethod
            def set_as_boundary_layer(tag: _ToTag) -> None: ...

    class geo:
        @staticmethod
        def add_point(
            x: float, y: float, z: float, meshSize: float = 0.0, tag: _ToTag = -1
        ) -> int: ...
        @staticmethod
        def add_line(startTag: int, endTag: int, tag: _ToTag = -1) -> int: ...
        @staticmethod
        def add_circle_arc(
            startTag: _ToTag,
            centerTag: _ToTag,
            endTag: _ToTag,
            tag: _ToTag = -1,
            nx: float = 0.0,
            ny: float = 0.0,
            nz: float = 0.0,
        ) -> _API_RESULT_: ...
        @staticmethod
        def add_ellipse_arc(
            startTag: _ToTag,
            centerTag: _ToTag,
            majorTag: _ToTag,
            endTag: _ToTag,
            tag: _ToTag = -1,
            nx: float = 0.0,
            ny: float = 0.0,
            nz: float = 0.0,
        ) -> _API_RESULT_: ...
        @staticmethod
        def add_spline(pointTags: _VectorInt_, tag: _ToTag = -1) -> int: ...
        @staticmethod
        def add_bspline(pointTags: _VectorInt_, tag: _ToTag = -1) -> int: ...
        @staticmethod
        def add_bezier(pointTags: _VectorInt_, tag: _ToTag = -1) -> _TAG_: ...
        @staticmethod
        def add_polyline(pointTags: _VectorInt_, tag: _ToTag = -1) -> _TAG_: ...
        @staticmethod
        def add_compound_spline(
            curveTags: _VectorInt_, numIntervals: int = 5, tag: _ToTag = -1
        ) -> _TAG_: ...
        @staticmethod
        def add_compound_bspline(
            curveTags: _VectorInt_, numIntervals: int = 20, tag: _ToTag = -1
        ) -> _TAG_: ...
        @staticmethod
        def add_curve_loop(
            curveTags: _VectorInt_, tag: _ToTag = -1, reorient: bool = False
        ) -> _TAG_: ...
        @staticmethod
        def add_curve_loops(curveTags: _VectorInt_) -> _TAG_: ...
        @staticmethod
        def add_plane_surface(wireTags: _VectorInt_, tag: _ToTag = -1) -> int: ...
        @staticmethod
        def add_surface_filling(
            wireTags: _VectorInt_, tag: _ToTag = -1, sphereCenterTag: int = -1
        ) -> int: ...
        @staticmethod
        def add_surface_loop(surfaceTags: _VectorInt_, tag: _ToTag = -1) -> _TAG_: ...
        @staticmethod
        def add_volume(shellTags: _VectorInt_, tag: _ToTag = -1) -> _TAG_: ...
        @staticmethod
        def add_geometry(
            geometry: str,
            numbers: _VectorFloat_ = [],
            strings: _VectorString_ = [],
            tag: _ToTag = -1,
        ) -> _API_RESULT_: ...
        @staticmethod
        def add_point_on_geometry(
            geometryTag: _ToTag,
            x: float,
            y: float,
            z: float = 0.0,
            meshSize: float = 0.0,
            tag: _ToTag = -1,
        ) -> _TAG_: ...
        @staticmethod
        def extrude(
            dimTags: _DIM_TAGS_,
            dx: float,
            dy: float,
            dz: float,
            numElements: _VectorInt_ = [],
            heights: _VectorFloat_ = [],
            recombine: bool = False,
        ) -> _DIM_TAGS_: ...
        @staticmethod
        def revolve(
            dimTags: _DIM_TAGS_,
            x: float,
            y: float,
            z: float,
            ax: float,
            ay: float,
            az: float,
            angle: float,
            numElement: _VectorInt_ = [],
            heights: _VectorFloat_ = [],
            *,
            recombine: bool = False,
        ) -> _DIM_TAGS_: ...
        @staticmethod
        def twist(
            dimTags: _DIM_TAGS_,
            x: float,
            y: float,
            z: float,
            dx: float,
            dy: float,
            dz: float,
            ax: float,
            ay: float,
            az: float,
            angle: float,
            numElements: _VectorInt_ = [],
            heights: _VectorFloat_ = [],
            recombine: bool = False,
        ) -> _DIM_TAGS_: ...
        @staticmethod
        def extrude_boundary_layer(
            dimTags: _DIM_TAGS_,
            numElements: _VectorInt_ = [1],
            heights: _VectorFloat_ = [],
            recombine: bool = False,
            second: bool = False,
            viewIndex: int = -1,
        ) -> _DIM_TAGS_: ...
        @staticmethod
        def translate(dimTags: _DIM_TAGS_, dx: float, dy: float, dz: float) -> None: ...
        @staticmethod
        def rotate(
            dimTags: _DIM_TAGS_,
            x: float,
            y: float,
            z: float,
            ax: float,
            ay: float,
            az: float,
            angle: float,
        ) -> None: ...
        @staticmethod
        def dilate(
            dimTags: _DIM_TAGS_, x: float, y: float, z: float, a: float, b: float, c: float
        ) -> None: ...
        @staticmethod
        def mirror(dimTags: _DIM_TAGS_, a: float, b: float, c: float, d: float) -> None: ...
        @staticmethod
        def symmetrize(dimTags: _DIM_TAGS_, a: float, b: float, c: float, d: float) -> None: ...
        @staticmethod
        def copy(dimTags: _DIM_TAGS_) -> _DIM_TAGS_: ...
        @staticmethod
        def remove(dimTags: _DIM_TAGS_, recursive: bool = False) -> None: ...
        @staticmethod
        def remove_all_duplicates() -> None: ...
        @staticmethod
        def split_curve(tag: _ToTag, pointTags: _VectorInt_) -> _Int1D_: ...
        @staticmethod
        def get_max_tag(dim: _ToDim) -> _DIM_: ...
        @staticmethod
        def set_max_tag(dim: _ToDim, maxTag: _ToTag) -> None: ...
        @staticmethod
        def add_physical_group(
            dim: _ToDim, tags: _VectorInt_, tag: _ToTag = -1, name: str = ""
        ) -> _API_RESULT_: ...
        @staticmethod
        def remove_physical_groups(dimTags: _DIM_TAGS_ = []) -> None: ...
        @staticmethod
        def synchronize() -> None: ...
        class mesh:
            @staticmethod
            def set_size(dimTags: _DIM_TAGS_, size: float) -> None: ...
            @staticmethod
            def set_transfinite_curve(
                tag: _ToTag, nPoints: int, meshType: str = "Progression", coef: float = 1.0
            ) -> None: ...
            @staticmethod
            def set_transfinite_surface(
                tag: _ToTag, arrangement: str = "Left", cornerTags: _VectorInt_ = []
            ) -> None: ...
            @staticmethod
            def set_transfinite_volume(tag: _ToTag, cornerTags: _VectorInt_ = []) -> None: ...
            @staticmethod
            def set_recombine(dim: _ToDim, tag: _ToTag, angle: float = 45.0) -> None: ...
            @staticmethod
            def set_smoothing(dim: _ToDim, tag: _ToTag, val: int) -> None: ...
            @staticmethod
            def set_reverse(dim: _ToDim, tag: _ToTag, val: bool = True) -> None: ...
            @staticmethod
            def set_algorithm(dim: _ToDim, tag: _ToTag, val: int) -> None: ...
            @staticmethod
            def set_size_from_boundary(dim: _ToDim, tag: _ToTag, val: int) -> None: ...

    class occ:
        @staticmethod
        def add_point(
            x: float, y: float, z: float, meshSize: float = 0.0, tag: _ToTag = -1
        ) -> _API_RESULT_: ...
        @staticmethod
        def add_line(startTag: int, endTag: int, tag: _ToTag = -1) -> _API_RESULT_: ...
        @staticmethod
        def add_circle_arc(
            startTag: int, middleTag: int, endTag: int, tag: _ToTag = -1, center: bool = True
        ) -> _API_RESULT_: ...
        @staticmethod
        def add_circle(
            x: float,
            y: float,
            z: float,
            r: float,
            tag: _ToTag = -1,
            angle1: float = 0.0,
            angle2: float = ...,
            zAxis: _VectorFloat_ = [],
            xAxis: _VectorFloat_ = [],
        ) -> _API_RESULT_: ...
        @staticmethod
        def add_ellipse_arc(
            startTag: int, centerTag: int, majorTag: int, endTag: int, tag: _ToTag = -1
        ) -> _API_RESULT_: ...
        @staticmethod
        def add_ellipse(
            x: float,
            y: float,
            z: float,
            r1: float,
            r2: float,
            tag: _ToTag = -1,
            angle1: float = 0.0,
            angle2: float = ...,
            zAxis: _VectorFloat_ = [],
            xAxis: _VectorFloat_ = [],
        ) -> _TAG_: ...
        @staticmethod
        def add_spline(
            pointTags: _VectorInt_, tag: _ToTag = -1, tangents: _VectorFloat_ = []
        ) -> _API_RESULT_: ...
        @staticmethod
        def add_bspline(
            pointTags: _VectorInt_,
            tag: _ToTag = -1,
            degree: int = 3,
            weights: _VectorFloat_ = [],
            knots: _VectorFloat_ = [],
            multiplicities: _VectorInt_ = [],
        ) -> _API_RESULT_: ...
        @staticmethod
        def add_bezier(pointTags: _VectorInt_, tag: _ToTag = -1) -> _API_RESULT_: ...
        @staticmethod
        def add_wire(
            curveTags: _VectorInt_, tag: _ToTag = -1, checkClosed: bool = False
        ) -> _API_RESULT_: ...
        @staticmethod
        def add_curve_loop(curveTags: _VectorInt_, tag: _ToTag = -1) -> _API_RESULT_: ...
        @staticmethod
        def add_rectangle(
            x: float,
            y: float,
            z: float,
            dx: float,
            dy: float,
            tag: _ToTag = -1,
            roundedRadius: float = 0.0,
        ) -> _API_RESULT_: ...
        @staticmethod
        def add_disk(
            xc: float,
            yc: float,
            zc: float,
            rx: float,
            ry: float,
            tag: _ToTag = -1,
            zAxis: _VectorFloat_ = [],
            xAxis: _VectorFloat_ = [],
        ) -> _API_RESULT_: ...
        @staticmethod
        def add_plane_surface(wireTags: _VectorInt_, tag: _ToTag = -1) -> _API_RESULT_: ...
        @staticmethod
        def add_surface_filling(
            wireTag: int,
            tag: _ToTag = -1,
            pointTags: _VectorInt_ = [],
            degree: int = 2,
            numPointsOnCurves: int = 15,
            numIter: int = 2,
            anisotropic: bool = False,
            tol2d: float = 1e-05,
            tol3d: float = 0.0001,
            tolAng: float = 0.01,
            tolCurv: float = 0.1,
            maxDegree: int = 8,
            maxSegments: int = 9,
        ) -> _API_RESULT_: ...
        @staticmethod
        def add_bspline_filling(wireTag: int, tag: _ToTag = -1, type: str = "") -> _API_RESULT_: ...
        @staticmethod
        def add_bezier_filling(wireTag: int, tag: _ToTag = -1, type: str = "") -> _API_RESULT_: ...
        @staticmethod
        def add_bspline_surface(
            pointTags: _VectorInt_,
            numPointsU: int,
            tag: _ToTag = -1,
            degreeU: int = 3,
            degreeV: int = 3,
            weights: _VectorFloat_ = [],
            knotsU: _VectorFloat_ = [],
            knotsV: _VectorFloat_ = [],
            multiplicitiesU: _VectorInt_ = [],
            multiplicitiesV: _VectorInt_ = [],
            wireTags: _VectorInt_ = [],
            wire3D: bool = False,
        ) -> _API_RESULT_: ...
        @staticmethod
        def add_bezier_surface(
            pointTags: _VectorInt_,
            numPointsU: int,
            tag: _ToTag = -1,
            wireTags: _VectorInt_ = [],
            wire3D: bool = False,
        ) -> _API_RESULT_: ...
        @staticmethod
        def add_trimmed_surface(
            surfaceTag: int, wireTags: _VectorInt_ = [], wire3D: bool = False, tag: _ToTag = -1
        ) -> _API_RESULT_: ...
        @staticmethod
        def add_surface_loop(
            surfaceTags: _VectorInt_, tag: _ToTag = -1, sewing: bool = False
        ) -> _API_RESULT_: ...
        @staticmethod
        def add_volume(shellTags: _VectorInt_, tag: _ToTag = -1) -> _API_RESULT_: ...
        @staticmethod
        def add_sphere(
            xc: float,
            yc: float,
            zc: float,
            radius: float,
            tag: _ToTag = -1,
            angle1: float = ...,
            angle2: float = ...,
            angle3: float = ...,
        ) -> _API_RESULT_: ...
        @staticmethod
        def add_box(
            x: float, y: float, z: float, dx: float, dy: float, dz: float, tag: _ToTag = -1
        ) -> int: ...
        @staticmethod
        def add_cylinder(
            x: float,
            y: float,
            z: float,
            dx: float,
            dy: float,
            dz: float,
            r: float,
            tag: _ToTag = -1,
            angle: float = ...,
        ) -> _TAG_: ...
        @staticmethod
        def add_cone(
            x: float,
            y: float,
            z: float,
            dx: float,
            dy: float,
            dz: float,
            r1: float,
            r2: float,
            tag: _ToTag = -1,
            angle: float = ...,
        ) -> _TAG_: ...
        @staticmethod
        def add_wedge(
            x: float,
            y: float,
            z: float,
            dx: float,
            dy: float,
            dz: float,
            tag: _ToTag = -1,
            ltx: float = 0.0,
            zAxis: _VectorFloat_ = [],
        ) -> _TAG_: ...
        @staticmethod
        def add_torus(
            x: float,
            y: float,
            z: float,
            r1: float,
            r2: float,
            tag: _ToTag = -1,
            angle: float = ...,
            zAxis: _VectorFloat_ = [],
        ) -> _TAG_: ...
        @staticmethod
        def add_thru_sections(
            wireTags: _VectorInt_,
            tag: _ToTag = -1,
            *,
            makeSolid: bool = True,
            makeRuled: bool = False,
            maxDegree: int = -1,
            continuity: str = "",
            parametrization: str = "",
            smoothing: bool = False,
        ) -> _Int1D_: ...
        @staticmethod
        def add_thick_solid(
            volumeTag: _ToTag, excludeSurfaceTags: _VectorInt_, offset: float, tag: _ToTag = -1
        ) -> _TAG_: ...
        @staticmethod
        def extrude(
            dimTags: _DIM_TAGS_,
            dx: float,
            dy: float,
            dz: float,
            numElements: _VectorInt_ = [],
            heights: _VectorFloat_ = [],
            recombine: bool = False,
        ) -> _DIM_TAGS_: ...
        @staticmethod
        def revolve(
            dimTags: _DIM_TAGS_,
            x: float,
            y: float,
            z: float,
            ax: float,
            ay: float,
            az: float,
            angle: float,
            numElements: _VectorInt_ = [],
            heights: _VectorFloat_ = [],
            recombine: bool = False,
        ) -> _DIM_TAGS_: ...
        @staticmethod
        def add_pipe(dimTags: _DIM_TAGS_, wireTag: int, trihedron: str = "") -> _DIM_TAGS_: ...
        @staticmethod
        def fillet(
            volumeTags: _VectorInt_,
            curveTags: _VectorInt_,
            radii: _VectorFloat_,
            *,
            removeVolume: bool = True,
        ) -> _DIM_TAGS_: ...
        @staticmethod
        def chamfer(
            volumeTags: _VectorInt_,
            curveTags: _VectorInt_,
            surfaceTags: _VectorInt_,
            distances: _VectorFloat_,
            removeVolume: bool = True,
        ) -> _DIM_TAGS_: ...
        @staticmethod
        def defeature(
            volumeTags: _VectorInt_, surfaceTags: _VectorInt_, removeVolume: bool = True
        ) -> _DIM_TAGS_: ...
        @staticmethod
        def fillet2_d(
            edgeTag1: _ToTag,
            edgeTag2: _ToTag,
            radius: float,
            tag: _ToTag = -1,
            pointTag: int = -1,
            reverse: bool = False,
        ) -> _TAG_: ...
        @staticmethod
        def chamfer2_d(
            edgeTag1: _ToTag, edgeTag2: _ToTag, distance1: float, distance2: float, tag: _ToTag = -1
        ) -> _TAG_: ...
        @staticmethod
        def offset_curve(curveLoopTag: _ToTag, offset: float) -> _DIM_TAGS_: ...
        @staticmethod
        def get_distance(
            dim1: _ToDim, tag1: _ToTag, dim2: _ToDim, tag2: _ToTag
        ) -> tuple[float, float, float, float, float, float]: ...
        @staticmethod
        def get_closest_entities(
            x: float, y: float, z: float, dimTags: _DIM_TAGS_, n: int = 1
        ) -> tuple[_DIM_TAGS_, _Float1D_, _Float1D_]: ...
        @staticmethod
        def fuse(
            objectDimTags: _DIM_TAGS_,
            toolDimTags: _DIM_TAGS_,
            tag: _ToTag = -1,
            removeObject: bool = True,
            removeTool: bool = True,
        ) -> tuple[_DIM_TAGS_, list[_DIM_TAGS_]]: ...
        @staticmethod
        def intersect(
            objectDimTags: _DIM_TAGS_,
            toolDimTags: _DIM_TAGS_,
            tag: _ToTag = -1,
            removeObject: bool = True,
            removeTool: bool = True,
        ) -> tuple[_DIM_TAGS_, list[_DIM_TAGS_]]: ...
        @staticmethod
        def cut(
            objectDimTags: _DIM_TAGS_,
            toolDimTags: _DIM_TAGS_,
            tag: _ToTag = -1,
            removeObject: bool = True,
            removeTool: bool = True,
        ) -> tuple[_DIM_TAGS_, list[_DIM_TAGS_]]: ...
        @staticmethod
        def fragment(
            objectDimTags: _DIM_TAGS_,
            toolDimTags: _DIM_TAGS_,
            tag: _ToTag = -1,
            removeObject: bool = True,
            removeTool: bool = True,
        ) -> tuple[_DIM_TAGS_, list[_DIM_TAGS_]]: ...
        @staticmethod
        def translate(dimTags: _DIM_TAGS_, dx: float, dy: float, dz: float) -> None: ...
        @staticmethod
        def rotate(
            dimTags: _DIM_TAGS_,
            x: float,
            y: float,
            z: float,
            ax: float,
            ay: float,
            az: float,
            angle: float,
        ) -> None: ...
        @staticmethod
        def dilate(
            dimTags: _DIM_TAGS_, x: float, y: float, z: float, a: float, b: float, c: float
        ) -> None: ...
        @staticmethod
        def mirror(dimTags: _DIM_TAGS_, a: float, b: float, c: float, d: float) -> None: ...
        @staticmethod
        def symmetrize(dimTags: _DIM_TAGS_, a: float, b: float, c: float, d: float) -> None: ...
        @staticmethod
        def affine_transform(dimTags: _DIM_TAGS_, affineTransform: _VectorFloat_) -> None: ...
        @staticmethod
        def copy(dimTags: _DIM_TAGS_) -> _DIM_TAGS_: ...
        @staticmethod
        def remove(dimTags: _DIM_TAGS_, *, recursive: bool = False) -> None: ...
        @staticmethod
        def remove_all_duplicates() -> None: ...
        @staticmethod
        def heal_shapes(
            dimTags: _DIM_TAGS_ = [],
            tolerance: float = 1e-08,
            fixDegenerated: bool = True,
            fixSmallEdges: bool = True,
            fixSmallFaces: bool = True,
            sewFaces: bool = True,
            makeSolids: bool = True,
        ) -> _DIM_TAGS_: ...
        @staticmethod
        def convert_to_nurbs(dimTags: _DIM_TAGS_) -> None: ...
        @staticmethod
        def import_shapes(
            fileName: _FILE_IO_, highestDimOnly: bool = True, format: str = ""
        ) -> _DIM_TAGS_: ...
        @staticmethod
        def import_shapes_native_pointer(
            shape: Incomplete, highestDimOnly: bool = True
        ) -> _DIM_TAGS_: ...
        @staticmethod
        def get_entities(dim: _ToDim = -1) -> _DIM_TAGS_: ...
        @staticmethod
        def get_entities_in_bounding_box(
            xmin: float,
            ymin: float,
            zmin: float,
            xmax: float,
            ymax: float,
            zmax: float,
            dim: _ToDim = -1,
        ) -> _DIM_TAGS_: ...
        @staticmethod
        def get_bounding_box(
            dim: _ToDim, tag: _ToTag
        ) -> tuple[float, float, float, float, float, float]: ...
        @staticmethod
        def get_curve_loops(surfaceTag: _ToTag) -> tuple[_Int1D_, _Int2D_]: ...
        @staticmethod
        def get_surface_loops(volumeTag: _ToTag) -> tuple[_Int1D_, _Int2D_]: ...
        @staticmethod
        def get_mass(dim: _ToDim, tag: _ToTag) -> float: ...
        @staticmethod
        def get_center_of_mass(dim: _ToDim, tag: _ToTag) -> tuple[float, float, float]: ...
        @staticmethod
        def get_matrix_of_inertia(dim: _ToDim, tag: _ToTag) -> _Float1D_: ...
        @staticmethod
        def get_max_tag(dim: _ToDim) -> _Size_: ...
        @staticmethod
        def set_max_tag(dim: _ToDim, maxTag: _ToTag) -> None: ...
        @staticmethod
        def synchronize() -> None: ...
        class mesh:
            @staticmethod
            def set_size(dimTags: _DIM_TAGS_, size: float) -> None: ...

class view:
    @staticmethod
    def add(name: str, tag: _ToTag = -1) -> int: ...
    @staticmethod
    def remove(tag: _ToTag) -> None: ...
    @staticmethod
    def get_index(tag: _ToTag) -> int: ...
    @staticmethod
    def get_tags() -> _Int1D_: ...
    @staticmethod
    def add_model_data(
        tag: _ToTag,
        step: int,
        modelName: str,
        dataType: str,
        tags: _VectorInt_,
        data: Sequence[_VectorFloat_],
        time: float = 0.0,
        numComponents: int = -1,
        partition: int = 0,
    ) -> None: ...
    @staticmethod
    def add_homogeneous_model_data(
        tag: _ToTag,
        step: int,
        modelName: str,
        dataType: str,
        tags: _VectorInt_,
        data: _VectorFloat_,
        time: float = 0.0,
        numComponents: int = -1,
        partition: int = 0,
    ) -> None: ...
    @staticmethod
    def get_model_data(tag: _ToTag, step: _Size_) -> tuple[str, _Int1D_, _Float2D_, float, int]: ...
    @staticmethod
    def get_homogeneous_model_data(
        tag: _ToTag, step: int
    ) -> tuple[str, _Int1D_, _Float1D_, float, int]: ...
    @staticmethod
    def add_list_data(tag: _ToTag, dataType: str, numEle: int, data: _VectorFloat_) -> None: ...
    @staticmethod
    def get_list_data(
        tag: _ToTag, returnAdaptive: bool = False
    ) -> tuple[_String1D_, _Int1D_, _Float2D_]: ...
    @staticmethod
    def add_list_data_string(
        tag: _ToTag, coord: _VectorFloat_, data: _VectorString_, style: _VectorString_ = []
    ) -> None: ...
    @staticmethod
    def get_list_data_strings(
        tag: _ToTag, dim: _ToDim
    ) -> tuple[_VectorFloat_, _VectorString_, _VectorString_]: ...
    @staticmethod
    def set_interpolation_matrices(
        tag: _ToTag,
        type: str,
        d: int,
        coef: _VectorFloat_,
        exp: _VectorFloat_,
        dGeo: int = 0,
        coefGeo: _VectorFloat_ = [],
        expGeo: _VectorFloat_ = [],
    ) -> None: ...
    @staticmethod
    def add_alias(refTag: _ToTag, copyOptions: bool = False, tag: _ToTag = -1) -> _TAG_: ...
    @staticmethod
    def combine(
        what: _Method_, how: _Method_, remove: bool = True, copyOptions: bool = True
    ) -> None: ...
    @staticmethod
    def probe(
        tag: _ToTag,
        x: float,
        y: float,
        z: float,
        step: int = -1,
        numComp: int = -1,
        gradient: bool = False,
        distanceMax: float = 0.0,
        xElemCoord: _VectorFloat_ = [],
        yElemCoord: _VectorFloat_ = [],
        zElemCoord: _VectorFloat_ = [],
        dim: _ToDim = -1,
    ) -> tuple[_VectorFloat_, float]: ...
    @staticmethod
    def write(tag: _ToTag, fileName: _FILE_IO_, append: bool = False) -> None: ...
    @staticmethod
    def set_visibility_per_window(tag: _ToTag, value: int, windowIndex: int = 0) -> None: ...
    class option:
        @staticmethod
        def set_number(tag: _ToTag, name: _ToName, value: float) -> None: ...
        @staticmethod
        def get_number(tag: _ToTag, name: _ToName) -> float: ...
        @staticmethod
        def set_string(tag: _ToTag, name: _ToName, value: str) -> None: ...
        @staticmethod
        def get_string(tag: _ToTag, name: _ToName) -> str: ...
        @staticmethod
        def set_color(tag: _ToTag, name: _ToName, r: int, g: int, b: int, a: int = 255) -> None: ...
        @staticmethod
        def get_color(tag: _ToTag, name: _ToName) -> _RGB_: ...
        @staticmethod
        def copy(refTag: _ToTag, tag: _ToTag) -> None: ...

class algorithm:
    @staticmethod
    def triangulate(coordinates: _VectorFloat_, edges: _VectorInt_ = []) -> _Int1D_: ...
    @staticmethod
    def tetrahedralize(
        coordinates: _VectorFloat_, triangles: _VectorInt_ = []
    ) -> tuple[_Int1D_, _Float1D_]: ...

class plugin:
    @staticmethod
    def set_number(name: str, option: str, value: float) -> None: ...
    @staticmethod
    def set_string(name: str, option: str, value: str) -> None: ...
    @staticmethod
    def run(name: str) -> _API_RESULT_: ...

class graphics:
    @staticmethod
    def draw() -> None: ...

class fltk:
    @staticmethod
    def initialize() -> None: ...
    @staticmethod
    def finalize() -> None: ...
    @staticmethod
    def wait(time: float = -1.0) -> None: ...
    @staticmethod
    def update() -> None: ...
    @staticmethod
    def awake(action: str = "") -> None: ...
    @staticmethod
    def lock() -> None: ...
    @staticmethod
    def unlock() -> None: ...
    @staticmethod
    def run(optionFileName: str = "") -> None: ...
    @staticmethod
    def is_available() -> _API_RESULT_: ...
    @staticmethod
    def select_entities(dim: _ToDim = -1) -> tuple[int, _DIM_TAGS_]: ...
    @staticmethod
    def select_elements() -> tuple[int, _Int1D_]: ...
    @staticmethod
    def select_views() -> tuple[int, _Int1D_]: ...
    @staticmethod
    def split_current_window(how: str = "v", ratio: float = 0.5) -> None: ...
    @staticmethod
    def set_current_window(windowIndex: int = 0) -> None: ...
    @staticmethod
    def set_status_message(message: str, graphics: bool = False) -> None: ...
    @staticmethod
    def show_context_window(dim: _ToDim, tag: _ToTag) -> None: ...
    @staticmethod
    def open_tree_item(name: str) -> None: ...
    @staticmethod
    def close_tree_item(name: str) -> None: ...

class parser:
    @staticmethod
    def get_names(search: str = "") -> _String1D_: ...
    @staticmethod
    def set_number(name: _ToName, value: _VectorFloat_) -> None: ...
    @staticmethod
    def set_string(name: _ToName, value: _VectorString_) -> None: ...
    @staticmethod
    def get_number(name: _ToName) -> _Float1D_: ...
    @staticmethod
    def get_string(name: _ToName) -> _String1D_: ...
    @staticmethod
    def clear(name: str = "") -> None: ...
    @staticmethod
    def parse(fileName: _ToName) -> None: ...

class onelab:
    @staticmethod
    def set(data: str, format: str = "json") -> None: ...
    @staticmethod
    def get(name: str = "", format: str = "json") -> str: ...
    @staticmethod
    def get_names(search: str = "") -> _String1D_: ...
    @staticmethod
    def set_number(name: str, value: _VectorFloat_) -> None: ...
    @staticmethod
    def set_string(name: str, value: _VectorString_) -> None: ...
    @staticmethod
    def get_number(name: str) -> _Float1D_: ...
    @staticmethod
    def get_string(name: str) -> _String1D_: ...
    @staticmethod
    def get_changed(name: str) -> _API_RESULT_: ...
    @staticmethod
    def set_changed(name: str, value: int) -> None: ...
    @staticmethod
    def clear(name: str = "") -> None: ...
    @staticmethod
    def run(name: str = "", command: str = "") -> None: ...

class logger:
    @staticmethod
    def write(message: str, level: str = "info") -> None: ...
    @staticmethod
    def start() -> None: ...
    @staticmethod
    def get() -> _String1D_: ...
    @staticmethod
    def stop() -> None: ...
    @staticmethod
    def get_wall_time() -> float: ...
    @staticmethod
    def get_cpu_time() -> float: ...
    @staticmethod
    def get_memory() -> float: ...
    @staticmethod
    def get_total_memory() -> float: ...
    @staticmethod
    def get_last_error() -> str: ...
