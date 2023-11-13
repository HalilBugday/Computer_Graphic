# CENG 487 Assignment2 by
# Halil İbrahim Buğday
# StudentId: 280201094
# 11 2023

from math import *
from ..vec3d import Vec3d
from .object import Object3d
from .shape import Shape

class Cylinder(Object3d):
    def __init__(self):
        self.count = 8
        self.subdivisions = self._calculate_subdivisions(self.count)

    def _calculate_subdivisions(self, point_count):
        top_vertices, bottom_vertices = self._generate_vertices(point_count)
        shapes = self._generate_shapes(top_vertices, bottom_vertices)
        return shapes

    def _generate_vertices(self, point_count):
        top_vertices = [Vec3d.point(cos(2.0 * pi * i / point_count), 1, sin(2.0 * pi * i / point_count)) for i in range(point_count)]
        bottom_vertices = [Vec3d.point(cos(2.0 * pi * i / point_count), -1, sin(2.0 * pi * i / point_count)) for i in range(point_count)]

        return top_vertices, bottom_vertices

    def _generate_shapes(self, top_vertices, bottom_vertices):
        shapes = []

        top_shape = self._create_shape(top_vertices, color=(0.4, 0.4, 0.4))
        bottom_shape = self._create_shape(bottom_vertices, color=(0.4, 0.4, 0.4))
        shapes.extend([top_shape, bottom_shape])

        shapes.extend([
            self._create_quadrilateral(top_vertices[i], top_vertices[(i + 1) % len(top_vertices)],
                                   bottom_vertices[(i + 1) % len(bottom_vertices)], bottom_vertices[i],
                                   color=(0.4, 0.4, 0.4))
            for i in range(len(top_vertices))
    ])

        return shapes

    def _create_shape(self, vertices, color):
        stack = self._get_stack()
        matrix = self._get_matrix()
        return Shape(vertices, color=color, state=(stack, matrix))

    def _create_quadrilateral(self, v1, v2, v3, v4, color):
        stack = self._get_stack()
        matrix = self._get_matrix()
        return Shape.quadrilateral(v1, v2, v3, v4, color=color, state=(stack, matrix))

    def _get_stack(self):
        if hasattr(self, "subdivisions") and len(self.subdivisions) > 0:
            return self.subdivisions[0].stack
        return None

    def _get_matrix(self):
        if hasattr(self, "subdivisions") and len(self.subdivisions) > 0:
            return self.subdivisions[0].matrix
        return None

    def increase_subdivisions(self):
        self.count *= 2
        self.update_subdivisions()

    def decrease_subdivisions(self):
        self.count = max(self.count // 2, 8)
        if self.count != self.count // 2:
            self.update_subdivisions()

    def update_subdivisions(self):
        self.subdivisions = self._calculate_subdivisions(self.count)

