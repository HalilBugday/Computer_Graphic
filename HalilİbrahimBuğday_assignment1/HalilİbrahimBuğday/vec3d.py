# CENG 487 Assignment1 by
# Halil İbrahim Buğday
# StudentId: 280201094
# 10 2023

import math

class Vec3d:
    # Constructer
    def __init__(self, x: float, y: float, z: float, t: float = 0):
        self.x, self.y, self.z, self.t = x, y, z, t

    # Vector + Vector
    def __add__(self, other):
        result = Vec3d(self.x + other.x, self.y + other.y, self.z + other.z)
        return result

    # Vector - Vector
    def __sub__(self, other):
        result = Vec3d(self.x - other.x, self.y - other.y, self.z - other.z)
        return result

    # Scaler x Vector
    def __mul__(self, other: float):
        result = Vec3d(self.x * other.x, self.y * other.y, self.z * other.z)
        return result

    # Vector / Scaler
    def __truediv__(self, other: float):
        if other == 0:
            raise ZeroDivisionError("Division by zero is not allowed.")
        return Vec3d(self.x / other, self.y / other, self.z / other, self.w / other)

    # |A| of Vector
    def abs(self):
        result =  math.sqrt(self.x ** 2 + self.y ** 2 + self.z ** 2 + self.t **2)
        return result

    # Str representation of the Vector
    def __repr__(self):
        result = f"Custom_repr({str(self)})"
        return result

    # Str form of the Vector
    def __str__(self):
        result = '(%g, %g, %g, %g)' % (self.x, self.y, self.z, self.t)
        return result

    # Cross Product
    def cross_product(self, vector):
        x = self.y * vector.z - self.z * vector.y
        y = self.z * vector.x - self.x * vector.z
        z = self.x * vector.y - self.y * vector.x
        result = Vec3d(x, y, z)
        return result

    # Dot Product
    def dot_product(self, other):
        result =  self.x * other.x + self.y * other.y + self.z * other.z + self.t * other.t
        return result

   # Degree of two Vectors
    def angle(self, other):
        dot_product = self.dot_product(other)
        magnitude_product = self.abs * other.abs
        if magnitude_product == 0:
            return 0  #if mag. is zero so, deg=0
        result = math.acos(dot_product / magnitude_product)
        return math.degrees(result)

    # Projection
    def matrix_projection(self, other):
        dot_product = self.dot_product(other)
        other_dot_product = other.dot_product(other)
        if other_dot_product == 0:
            return Vec3d(0, 0, 0)  # if dot = 0 so, projection = 0
        result = other * (dot_product / other_dot_product)
        return result

