# CENG 487 Assignment3 by
# Halil İbrahim Buğday
# StudentId: 280201094
# 12 2023

from typing import List, Tuple, Union

from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

from ..calculate import Vec3d, Mat3d


class Shape:
    def __init__(
        self,
        vertices: List[Vec3d],
        origin: Vec3d = Vec3d.point(0, 0, 0),
        color: Union[Tuple[int, int, int],List[Tuple[int, int, int]]] = (1.0, 1.0, 1.0),
        state=(None, None)
    ):
        self.vertices = vertices
        self.origin = origin
        self.color = color
        self._initialize_stack_and_matrix(state)

    def _initialize_stack_and_matrix(self, state):
        self.stack = (state[0] or []).copy()
        self.matrix = state[1] or Mat3d.identity()

        if state[0] is not None:
            self._transform_vertices()

    def _transform_vertices(self):
        self.vertices = [self.matrix @ vertice for vertice in self.vertices]

    def draw(self):
        self._set_polygon_mode()
        self._draw_vertices(GL_POLYGON)

    def draw_border(self):
        glLineWidth(2)
        glColor3f(0, 0, 255)
        self._draw_vertices(GL_LINE_LOOP)

    def _set_polygon_mode(self):
        is_multicolored = isinstance(self.color, list)
        if is_multicolored:
            glEnable(GL_COLOR_MATERIAL)
        else:
            glDisable(GL_COLOR_MATERIAL)
            glColor3f(*self.color)

    def _draw_vertices(self, mode):
        glBegin(mode)
        for vertice in self.vertices:
            position = vertice + self.origin
            if isinstance(self.color, list):
                glColor3f(*self._get_next_color())
            glVertex3f(position.x, position.y, position.z)
        glEnd()

    def _get_next_color(self):
        color_itr = iter(self.color)
        return next(color_itr)

    def __getitem__(self, index: Union[int, slice]) -> List[Vec3d]:
        return self._get_vertices(index)

    def _get_vertices(self, index: Union[int, slice]) -> List[Vec3d]:
        return self.vertices[index]

    def rotate(self, theta_0: float, theta_1: float, theta_2: float, order="xyz") -> None:
        rotation_matrices = self._get_rotation_matrices(theta_0, theta_1, theta_2, order)
        R = self._calculate_combined_rotation_matrix(rotation_matrices)
        self._apply_rotation(R)

        self._update_stack_with_rotation(order, theta_0, theta_1, theta_2)

    def _get_rotation_matrices(self, theta_0: float, theta_1: float, theta_2: float, order: str):
        rotation_matrix_functions = [getattr(Mat3d, f'rotation_{axis}_matrix') for axis in order]
        return [rotation_matrix(theta) for rotation_matrix, theta in zip(rotation_matrix_functions, (theta_0, theta_1, theta_2))]

    def _calculate_combined_rotation_matrix(self, rotation_matrices):
        combined_rotation_matrix = rotation_matrices[2] @ rotation_matrices[1] @ rotation_matrices[0]
        return combined_rotation_matrix

    def _apply_rotation(self, R):
        self.matrix = R @ self.matrix
        self.vertices = [R @ vertice for vertice in self.vertices]

    def _update_stack_with_rotation(self, order, theta_0, theta_1, theta_2):
        self.stack.append(('R', order, theta_0, theta_1, theta_2))

    def translate(self, tx: float, ty: float, tz: float) -> None:
        translation_matrix = self._get_translation_matrix(tx, ty, tz)
        self._apply_translation(translation_matrix)

        self._update_stack_with_translation(tx, ty, tz)

    def _get_translation_matrix(self, tx: float, ty: float, tz: float):
        return Mat3d.translation_matrix(tx, ty, tz)

    def _apply_translation(self, T):
        self.matrix = T @ self.matrix
        self.vertices = [T @ vertice for vertice in self.vertices]

    def _update_stack_with_translation(self, tx, ty, tz):
        self.stack.append(('T', tx, ty, tz))

    def scale(self, sx: float, sy: float, sz: float) -> None:
        scaling_matrix = self._get_scaling_matrix(sx, sy, sz)
        self._apply_scaling(scaling_matrix)

        self._update_stack_with_scaling(sx, sy, sz)

    def _get_scaling_matrix(self, sx: float, sy: float, sz: float):
        return Mat3d.scaling_matrix(sx, sy, sz)

    def _apply_scaling(self, S):
        self.matrix = S @ self.matrix
        self.vertices = [S @ vertice for vertice in self.vertices]

    def _update_stack_with_scaling(self, sx, sy, sz):
        self.stack.append(('S', sx, sy, sz))

    def clone(self) -> 'Shape':
        cloned = Shape(
            self.vertices[::],
            self.origin.clone(),
            self.color[::])
        cloned.stack = self.stack[::]

        return cloned

    def __str__(self) -> str:
        return self.__class__.__name__ + "(" + ", ".join(map(str, self.vertices)) + ")"

    @staticmethod
    def quadrilateral(vertice1: Vec3d, vertice2: Vec3d, vertice3: Vec3d, vertice4: Vec3d,
                 origin: Vec3d = Vec3d.point(0, 0, 0),
                 color: Tuple[int, int, int] = None,
                 color1: Tuple[int, int, int] = (1.0, 1.0, 1.0),
                 color2: Tuple[int, int, int] = (1.0, 1.0, 1.0),
                 color3: Tuple[int, int, int] = (1.0, 1.0, 1.0),
                 color4: Tuple[int, int, int] = (1.0, 1.0, 1.0),
                 state=(None, None)):
        return Shape([vertice1, vertice2, vertice3, vertice4],
                 origin, color or [color1, color2, color3, color4], state)

