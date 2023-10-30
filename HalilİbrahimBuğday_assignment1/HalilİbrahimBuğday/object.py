# CENG 487 Assignment1 by
# Halil İbrahim Buğday
# StudentId: 280201094
# 10 2023

from typing import List
from vec3d import Vec3d
from mat3d import *

class object:
    def __init__(self, pos: Vec3d, vertices: List[Vec3d]):
        self.pos, self.x, self.y, self.z, self.vertices = pos, pos.x, pos.y, pos.z, vertices

    def vertice(self):
        return self.vertices

    def position(self):
        return Vec3d(self.x,self.y,self.z)

    def moving(self, transforms: List[Mat3d]):
        for transformation_matrix in transforms:
            for i, vertex in enumerate(self.vertices):
                self.vertices[i] = transformation_matrix.multiplication(vertex)
