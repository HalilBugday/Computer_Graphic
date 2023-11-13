# CENG 487 Assignment2 by
# Halil İbrahim Buğday
# StudentId: 280201094
# 11 2023

from math import cos, pi, sin
from .object import Object3d
from .shape import Shape
from ..vec3d import Vec3d

class Sphere(Object3d):
    def __init__(self, circle_count=4, circle_point_count=5):
        self.circle_count = circle_count
        self.circle_point_count = circle_point_count
        subdivisions = self._calculate_subdivisions()
        super().__init__(subdivisions=subdivisions)

    def _calculate_unit_points(self):
        unit_points = [self._calculate_point_on_circle(i) for i in range(self.circle_point_count)]
        return unit_points

    def _calculate_point_on_circle(self, i):
        x, z = cos(2.0 * pi * i / self.circle_point_count), sin(2.0 * pi * i / self.circle_point_count)
        return (x, z)

    def _calculate_scale_factor(self, y, circle_count):
        y_fixed = y / circle_count
        return (1 - abs(y_fixed) ** 2) ** 0.5

    def _calculate_points_for_y(self, unit_points, y, circle_count):
        y_fixed = y / circle_count
        scale_factor = self._calculate_scale_factor(y, circle_count)
        return self._calculate_current_points(unit_points, y_fixed, scale_factor)

    def _calculate_subdivisions(self):
        unit_points = self._calculate_unit_points()
        shapes = []
        previous_points = None
        for y in range(-self.circle_count, self.circle_count + 1):
            current_points = self._calculate_points_for_y(unit_points, y, self.circle_count)
            if previous_points is not None:
                shapes.extend(self._create_quadrilaterals(previous_points, current_points))
            previous_points = current_points
        return shapes

    def _calculate_current_points(self, unit_points, y_fixed, scale_factor):
        current_points = []
        for x, z in unit_points:
            current_points.append(Vec3d.point(x * scale_factor, y_fixed, z * scale_factor))
        return current_points

    def _create_quadrilaterals(self, previous_points, current_points):
        quadrilaterals = []
        previous_len = len(previous_points)
        current_len = len(current_points)

        for i in range(self.circle_point_count):
            corner_a = previous_points[i % previous_len]
            corner_b = previous_points[(i + 1) % previous_len]
            corner_c = current_points[(i + 1) % current_len]
            corner_d = current_points[i % current_len]

            new_quadrilateral = Shape.quadrilateral(
                corner_a, corner_b, corner_c, corner_d,
                color=(0.4, 0.4, 0.4),
                state=self._get_state()
            )
            quadrilaterals.append(new_quadrilateral)
        return quadrilaterals


    def _get_state(self):
        stack = self.subdivisions[0].stack if hasattr(self, "subdivisions") and len(self.subdivisions) > 0 else None
        matrix = self.subdivisions[0].matrix if hasattr(self, "subdivisions") and len(self.subdivisions) > 0 else None
        return (stack, matrix)

    def increase_subdivisions(self):
        self.circle_count += 1
        self.circle_point_count += 1
        self.update_subdivisions()

    def update_subdivisions(self):
        self.subdivisions = self._calculate_subdivisions()


    def decrease_subdivisions(self):
        if self.circle_count >= 4 and self.circle_point_count >= 6:
            self.circle_count -= 1
            self.circle_point_count -= 1
            self.update_subdivisions()

    def update_subdivisions(self):
        self.subdivisions = self._calculate_subdivisions()
