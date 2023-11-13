# CENG 487 Assignment2 by
# Halil İbrahim Buğday
# StudentId: 280201094
# 11 2023

from math import *
from lib.mat3d import Mat3d
from .object import Object3d
from .shape import Shape
from ..vec3d import Vec3d

class Torus(Object3d):
    def __init__(self, circle_count=7, circle_point_count=6):
        self.circle_count = circle_count
        self.circle_point_count = circle_point_count
        subdivisions = self._calculate_subdivisions()
        super().__init__(subdivisions=subdivisions)
        self.rotate_torus()

    def _calculate_subdivisions(self):
        shapes = []
        previous_points = None
        stack, matrix = self._get_stack_matrix()
        theta_x, theta_y = self._calculate_theta_values()
        for i in range(self.circle_count+1):
            theta_xi = theta_x * i
            center_x, center_z = self._calculate_center_coordinates(theta_xi)
            current_points = self._calculate_current_points(theta_y, theta_xi, center_x, center_z)
            if previous_points is not None:
                shapes.extend(self._create_quadrilaterals(previous_points, current_points, stack, matrix))
            previous_points = current_points
        return shapes

    def _get_stack_matrix(self):
        stack = matrix = None
        if hasattr(self, "subdivisions") and len(self.subdivisions) > 0:
            stack = self.subdivisions[0].stack
            matrix = self.subdivisions[0].matrix
        return stack, matrix

    def _calculate_theta_values(self):
        theta_x = 2.0 * pi / self.circle_count
        theta_y = 2.0 * pi / self.circle_point_count
        return theta_x, theta_y

    def _calculate_center_coordinates(self, theta_xi):
        center_x = 0.75 * cos(theta_xi)
        center_z = 0.75 * sin(theta_xi)
        return center_x, center_z

    def _calculate_current_points(self, theta_y, theta_xi, center_x, center_z):
        current_points = []
        for j in range(self.circle_point_count):
            theta_yj = theta_y * j
            point = self._calculate_point(theta_yj, theta_xi, center_x, center_z)
            current_points.append(point)
        return current_points

    def _calculate_point(self, theta_yj, theta_xi, center_x, center_z):
        p_center = Vec3d.vector(center_x, 0, center_z)
        p_origin = Vec3d.point(0.25 * cos(theta_yj), 0.25 * sin(theta_yj), 0)
        return p_center + Mat3d.rotation_y_matrix(-theta_xi) @ p_origin

    def _create_quadrilaterals(self, previous_points, current_points, stack, matrix):
        quadrilaterals = []
        for i in range(self.circle_point_count):
            next_index = (i + 1) % self.circle_point_count
            p1 = previous_points[i]
            p2 = previous_points[next_index]
            p3 = current_points[next_index]
            p4 = current_points[i]
            quadrilaterals.append(
                Shape.quadrilateral(
                    p1, p2, p3, p4,
                    color=(0.4, 0.4, 0.4),
                    state=(stack, matrix)
                )
            )
        return quadrilaterals

    def rotate_torus(self):
        self.rotate(pi/2, 0, 0)

    def increase_subdivisions(self):
        self.circle_count += 1
        self.circle_point_count += 1
        self.update_subdivisions()

    def update_subdivisions(self):
        self.subdivisions = self._calculate_subdivisions()

    def decrease_subdivisions(self):
        if self.circle_count > 7 and self.circle_point_count > 6:
            self.circle_count -= 1
            self.circle_point_count -= 1
            self.update_subdivisions()

    def update_subdivisions(self):
        self.subdivisions = self._calculate_subdivisions()
