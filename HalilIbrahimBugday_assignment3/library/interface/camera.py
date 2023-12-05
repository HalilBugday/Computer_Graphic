# CENG 487 Assignment3 by
# Halil İbrahim Buğday
# StudentId: 280201094
# 12 2023

from OpenGL.GLU import *
from OpenGL.GL import *
from ..calculate import Mat3d


class Camera:
    def __init__(self) -> None:
        self.matrix = Mat3d.translation_matrix(0, 0, -12)

    def rotate(self, x: float, y: float, z: float):
        self.matrix @=Mat3d.rotation_z_matrix(z) \
            @ Mat3d.rotation_y_matrix(y) \
            @ Mat3d.rotation_x_matrix(x)

    def reset(self):
        self.matrix = Mat3d.translation_matrix(0, 0, -12)

    def look(self):
        glLoadMatrixf(self.matrix.to_array())

