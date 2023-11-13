# CENG 487 Assignment2 by
# Halil İbrahim Buğday
# StudentId: 280201094
# 11 2023

from ..vec3d import Vec3d
from ..mat3d import Mat3d
from .shape import Shape
from .object import Object3d

class Box(Object3d):
    def __init__(self):
        self.subdivisions = self.create_box_subdivisions()
        super().__init__(subdivisions=self.subdivisions)

    def create_box_subdivisions(self):
        points = [
            [Vec3d.point(1.0, 1.0, -1.0), Vec3d.point(-1.0, 1.0, -1.0), Vec3d.point(-1.0, 1.0, 1.0), Vec3d.point(1.0, 1.0, 1.0)],  # Top
            [Vec3d.point(1.0, -1.0, 1.0), Vec3d.point(-1.0, -1.0, 1.0), Vec3d.point(-1.0, -1.0, -1.0), Vec3d.point(1.0, -1.0, -1.0)],  # Bottom
            [Vec3d.point(1.0, 1.0, 1.0), Vec3d.point(-1.0, 1.0, 1.0), Vec3d.point(-1.0, -1.0, 1.0), Vec3d.point(1.0, -1.0, 1.0)],  # Front
            [Vec3d.point(1.0, -1.0, -1.0), Vec3d.point(-1.0, -1.0, -1.0), Vec3d.point(-1.0, 1.0, -1.0), Vec3d.point(1.0, 1.0, -1.0)],  # Back
            [Vec3d.point(-1.0, 1.0, 1.0), Vec3d.point(-1.0, 1.0, -1.0), Vec3d.point(-1.0, -1.0, -1.0), Vec3d.point(-1.0, -1.0, 1.0)],  # Left
            [Vec3d.point(1.0, 1.0, -1.0), Vec3d.point(1.0, 1.0, 1.0), Vec3d.point(1.0, -1.0, 1.0), Vec3d.point(1.0, -1.0, -1.0)]  # Right
        ]

        subdivisions = [Shape.quadrilateral(*points[i], color=(0.4, 0.4, 0.4)) for i in range(6)]
        return subdivisions

    def increase_subdivisions(self):
        new_subdivisions = []

        for subdivision in self.subdivisions:
            halved_subdivision = self._halve_subdivision(subdivision)
            translated_subdivisions = self._translate_subdivision(halved_subdivision)
            new_subdivisions.extend(translated_subdivisions)

        self.subdivisions = new_subdivisions

    def _halve_subdivision(self, subdivision):
        halved = subdivision.clone()
        x=0.5
        y=0.5
        z=0.5
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
        if len(self.subdivisions) <= 6:
            return

        merged_subdivisions = []

        for i in range(0, len(self.subdivisions), 4):
            doubled = self._double_subdivision(self.subdivisions[i])
            merged_subdivisions.append(doubled)

        self.subdivisions = merged_subdivisions

    def _double_subdivision(self, subdivision):
        doubled = subdivision.clone()
        doubled.scale(2.0, 2.0, 2.0)
        doubled.translate(*(-subdivision[0])[:-1])
        return doubled

