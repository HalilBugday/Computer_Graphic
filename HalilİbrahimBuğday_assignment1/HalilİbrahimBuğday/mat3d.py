# CENG 487 Assignment1 by
# Halil İbrahim Buğday
# StudentId: 280201094
# 10 2023

from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from vec3d import Vec3d
import math

class Mat3d:

    def __init__(self, *args):
        self.matrix = list(args)

    def __add__(self, other: Vec3d):
        result_matrix = []
        for i in range(4):
            result_matrix.append(self.matrix[i] + other.matrix[i])
        return Mat3d(result_matrix[0], result_matrix[1], result_matrix[2], result_matrix[3])

    def __mul__(self, other):
        result_matrix = [vec * other for vec in self.matrix]
        return Mat3d(*result_matrix)

    def __str__(self):
        result = '\n'.join(map(str, self.matrix))
        return result

    def transpose(self):
        result_matrix = [Vec3d(self.matrix[i].x, self.matrix[i].y, self.matrix[i].z, self.matrix[i].w) for i in range(4)]
        return Mat3d(*result_matrix)

    def multiplication(self, vector: Vec3d):
        result = [self.matrix[i].dot_product(vector) for i in range(4)]
        return Vec3d(*result)


class translate_matrix(Mat3d):

    def __init__(self, x, y, z):
        super().__init__(Vec3d(1, 0, 0, x), Vec3d(0, 1, 0, y), Vec3d(0, 0, 1, z), Vec3d(0, 0, 0, 1))


class xy_rotation_matrix(Mat3d):

    def __init__(self, psi):
        super().__init__(Vec3d(math.cos(psi), -math.sin(psi), 0, 0), Vec3d(math.sin(psi), math.cos(psi), 0, 0), Vec3d(0, 0, 1, 0), Vec3d(0, 0, 0, 1))

class scaling_matrix(Mat3d):
    def __init__(self, x, y, z):
       super().__init__(Vec3d(x, 0, 0, 0), Vec3d(0, y, 0, 0), Vec3d(0, 0, z, 0),Vec3d(0, 0, 0, 1))


class yz_rotation_matrix(Mat3d):
    def __init__(self, phi):
        super().__init__(Vec3d(1, 0, 0, 0), Vec3d(0, math.cos(phi), -math.sin(phi), 0), Vec3d(0, math.sin(phi), math.cos(phi), 0), Vec3d(0, 0, 0, 1))


class zx_rotation_matrix(Mat3d):
    def __init__(self, theta):
        super().__init__(Vec3d(math.cos(theta), 0, math.sin(theta), 0), Vec3d(0, 1, 0, 0), Vec3d(-math.sin(theta), 0, math.cos(theta), 0), Vec3d(0, 0, 0, 1))
