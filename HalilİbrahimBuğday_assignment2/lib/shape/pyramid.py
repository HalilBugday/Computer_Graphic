# CENG 487 Assignment2 by
# Halil İbrahim Buğday
# StudentId: 280201094
# 11 2023

from .object import Object3d
from .shape import Shape
from ..vec3d import Vec3d

class Pyramid(Object3d):
    def __init__(self):
        self.subdivisions = self.create_pyramid_subdivisions()
        super().__init__(subdivisions=self.subdivisions)

    def create_pyramid_subdivisions(self):
        points = [
            [Vec3d.point(1.0, -1.0, 1.0), Vec3d.point(-1.0, -1.0, 1.0), Vec3d.point(-1.0, -1.0, -1.0), Vec3d.point(1.0, -1.0, -1.0)],
            [Vec3d.point(1.0, -1.0, -1.0), Vec3d.point(0.0, 1.0, 0.0), Vec3d.point(-1.0, -1.0, -1.0)],
            [Vec3d.point(1.0, -1.0, 1.0), Vec3d.point(0.0, 1.0, 0.0), Vec3d.point(1.0, -1.0, -1.0)],
            [Vec3d.point(-1.0, -1.0, 1.0), Vec3d.point(0.0, 1.0, 0.0), Vec3d.point(1.0, -1.0, 1.0)],
            [Vec3d.point(-1.0, -1.0, -1.0), Vec3d.point(0.0, 1.0, 0.0), Vec3d.point(-1.0, -1.0, 1.0)]
        ]

        bottom_plane_points = [
            Vec3d.point(1.0, -1.0, 1.0),
            Vec3d.point(-1.0, -1.0, 1.0),
            Vec3d.point(-1.0, -1.0, -1.0),
            Vec3d.point(1.0, -1.0, -1.0)
        ]

        bottom_plane = Shape.quadrilateral(*bottom_plane_points, color=(0.4, 0.4, 0.4))

        subdivisions = [Shape.triangle(*points[i], color=(0.4, 0.4, 0.4)) for i in range(1, 5)]
        subdivisions.append(bottom_plane)
        return subdivisions

    def increase_subdivisions(self):
        new_subdivisions = []

        for subdivision in self.subdivisions[1:]:
            halved_subdivision = self._halve_subdivision(subdivision)
            translated_subdivisions = self._translate_subdivision(halved_subdivision)
            new_subdivisions.extend(translated_subdivisions)
        new_subdivisions.insert(0, self.subdivisions[0])
        self.subdivisions = new_subdivisions

    def _halve_subdivision(self, subdivision):
        halved = subdivision.clone()
        x = 0.5
        y = 0.5
        z = 0.5
        halved.scale(x, y, z)
        return halved

    def _translate_subdivision(self, subdivision):
        translated_subdivisions = []
        for vertice in subdivision:
            new_subdivision = subdivision.clone()
            new_subdivision.translate(*vertice[:-1])
            translated_subdivisions.append(new_subdivision)
        return translated_subdivisions

    def decrease_subdivisions(self):
        if len(self.subdivisions) <= 5:
            return
        merged_subdivisions = []
        for i in range(0, len(self.subdivisions[1:]), 3):
            doubled = self._double_subdivision(self.subdivisions[i + 1])
            merged_subdivisions.append(doubled)
        bottom_edges = self.subdivisions[0].edges
        for edge in bottom_edges:
            self.draw_line(edge[0], edge[1], color=(1.0, 1.0, 1.0))
        merged_subdivisions.insert(0, self.subdivisions[0])
        self.subdivisions = merged_subdivisions

    def _double_subdivision(self, subdivision):
        doubled = subdivision.clone()
        doubled.scale(2.0, 2.0, 2.0)
        doubled.translate(*(-subdivision[0])[:-1])
        return doubled