# CENG 487 Assignment3 by
# Halil İbrahim Buğday
# StudentId: 280201094
# 12 2023

import operator
from functools import reduce
from typing import List
from .shape import Shape
from ..calculate import Vec3d

class Object3d:

    def draw(self):
        [division.draw() for division in self.subdivisions]

    def draw_border(self):
        [division.draw_border() for division in self.subdivisions]

    def position(self):
        x, y, z = self.x, self.y, self.z
        return Vec3d(x, y, z)


    def __str__(self) -> str:
        subdivisions_str = ', '.join(map(str, self.subdivisions))
        return f"{self.__class__.__name__}(subdivisions=[{subdivisions_str}])"

    def __init__(self, subdivisions: List[Shape]) -> None:
        self.subdivisions = subdivisions
        self.level = 0

    def increase_subdivisions(self):
        new_subdivisions = []
        for subdivision in self.subdivisions:
            center = self.calculate_center(subdivision.vertices)
            vertices = self.calculate_new_vertices(subdivision.vertices)
            new_subdivisions.extend(
                self.create_quadrilaterals(vertices, center)
            )
        self.subdivisions = new_subdivisions
        self.level += 1

    def calculate_center(self, vertices):
        return reduce(operator.add, vertices) / len(vertices)

    def calculate_new_vertices(self, vertices):
        new_vertices = []
        for i in range(4):
            new_vertices.append(vertices[i])
            new_vertices.append(
                (vertices[i] + vertices[(i+1) % 4]) / 2
            )
        return new_vertices

    def create_quadrilaterals(self, vertices, center):
        quadrilaterals = []
        for i in range(0, 8, 2):
            quadrilaterals.append(
                Shape.quadrilateral(vertices[i], vertices[i+1], center, vertices[(i-1) % 8], color=(0.6, 0.6, 0.6)
                )
            )
        return quadrilaterals

    def decrease_subdivisions(self):
        if self.level == 0:
            return

        new_subdivisions = []
        for s1, s2, s3, s4 in zip(self.subdivisions[0::4], self.subdivisions[1::4], self.subdivisions[2::4], self.subdivisions[3::4]):
            new_subdivisions.append(
                Shape.quadrilateral(
                    s1.vertices[0],
                    s2.vertices[0],
                    s3.vertices[0],
                    s4.vertices[0],
                    color=(0.6, 0.6, 0.6)
                )
            )

        self.subdivisions = new_subdivisions
        self.level -= 1