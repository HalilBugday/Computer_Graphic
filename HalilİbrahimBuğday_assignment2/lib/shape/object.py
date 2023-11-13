# CENG 487 Assignment2 by
# Halil İbrahim Buğday
# StudentId: 280201094
# 11 2023

from abc import ABC, abstractmethod
from typing import List
from .shape import Shape
from ..mat3d import Mat3d
from ..vec3d import Vec3d

class Object3d(ABC):
    def __init__(self, subdivisions: List[Shape], x=0, y=0, z=0) -> None:
        super().__init__()
        self.subdivisions = subdivisions
        self.vertices = []
        self.x = x
        self.y = y
        self.z = z

    def draw(self):
        [division.draw() for division in self.subdivisions]

    def draw_border(self):
        [division.draw_border() for division in self.subdivisions]

    def rotate(self, theta_0, theta_1, theta_2, order="xyz"):
        [division.rotate(theta_0, theta_1, theta_2, order) for division in self.subdivisions]

    def scale(self, factor):
        [division.scale(factor, factor, factor) for division in self.subdivisions]


    def undo(self):
        [division.undo() for division in self.subdivisions]


    def vertice(self):
        vertices = self.vertices
        return vertices


    def position(self):
        x, y, z = self.x, self.y, self.z
        return Vec3d(x, y, z)

    def moving(self, transforms: List[Mat3d]):
        for transformation_matrix in transforms:
            for i, vertex in enumerate(self.vertices):
                self.vertices[i] = transformation_matrix.multiplication(vertex)

    @abstractmethod
    def increase_subdivisions(self):
        pass

    @abstractmethod
    def decrease_subdivisions(self):
        pass