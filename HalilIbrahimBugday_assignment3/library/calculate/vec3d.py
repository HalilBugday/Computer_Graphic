# CENG 487 Assignment3 by
# Halil İbrahim Buğday
# StudentId: 280201094
# 12 2023

from math import acos, cos, pi, sqrt
from typing import Union
from ..utils import cons
from math import *
import math

class Vec3d:
    def __init__(self, x: float, y: float, z: float, w: float) -> 'Vec3d':
        for name, value in zip(['x', 'y', 'z', 'w'], [x, y, z, w]):
            cons.number(value, name)
        self.x, self.y, self.z, self.w = map(float, [x, y, z, w])
        self.order = ['x', 'y', 'z', 'w']

    @staticmethod
    def point(*args: float) -> 'Vec3d':
        if len(args) != 3:
            raise ValueError("Invalid number of arguments for point")
        return Vec3d(*args, 1)

    @staticmethod
    def vector(*args: float) -> 'Vec3d':
        if len(args) != 3:
            raise ValueError("Invalid number of arguments for vector")
        return Vec3d(*args, 0)

    def clone(self) -> 'Vec3d':
        return Vec3d(*self)

    def to_point(self, w: float = 1) -> 'Vec3d':
        cons.number(w, "w")
        result = Vec3d(self.x, self.y, self.z, w)
        return result

    def to_vector(self, w: float = 0) -> 'Vec3d':
        cons.number(w, "w")
        result = Vec3d(self.x, self.y, self.z, w)
        return result

    def __str__(self) -> str:
        return f"vec3d({self.x}, {self.y}, {self.z}, {self.w})"

    def is_point(self) -> bool:
        return math.isclose(self.w, 1)

    def is_vector(self) -> bool:
        return math.isclose(self.w, 0)

    def cast_to_point(self, w: float = 1) -> None:
        cons.number(w, "w")
        self.w = w

    def cast_to_vector(self, w: float = 0) -> None:
        cons.number(w, "w")
        self.w = w

    def dot(self, vec2: 'Vec3d') -> float:
        if not isinstance(vec2, Vec3d):
            raise TypeError(f"Invalid operand type.")

        terms = [self_coord * vec2_coord for self_coord, vec2_coord in zip(self, vec2)]
        result = sum(terms)
        return result

    def cross(self, vec2: 'Vec3d') -> 'Vec3d':
        cons.type_of(vec2, "operand", [Vec3d])
        if self.w != 0 or vec2.w != 0:
            raise TypeError("Expected vectors, not points.")

        result_x = self.y * vec2.z - self.z * vec2.y
        result_y = self.z * vec2.x - self.x * vec2.z
        result_z = self.x * vec2.y - self.y * vec2.x

        result = Vec3d(result_x, result_y, result_z, 0)
        return result

    def project(self, vec2: 'Vec3d') -> 'Vec3d':
        cos_theta = math.cos(self.angle(vec2))
        normalized_vec2 = vec2.normalize()
        length = self.length()

        result = length * cos_theta * normalized_vec2
        return result

    def angle(self, vec2: 'Vec3d', degree: bool = False) -> float:
        cons.type_of(vec2, "operand", [Vec3d])
        radian = math.acos(self.dot(vec2) / (self.length() * vec2.length()))
        result = radian * (180 / math.pi) if degree else radian
        return result

    def length(self) -> float:
        result = math.sqrt(self.dot(self))
        return result

    def normalize(self) -> 'Vec3d':
        vec_length = self.length()
        if vec_length == 0:
            raise ValueError("Cannot normalize a 0 vector.")
        result = self / vec_length
        return result

    def __add__(self, vec2: 'Vec3d') -> 'Vec3d':
        cons.type_of(vec2, "operand", [Vec3d])

        result_x = self.x + vec2.x
        result_y = self.y + vec2.y
        result_z = self.z + vec2.z
        result_w = self.w + vec2.w

        result = Vec3d(result_x, result_y, result_z, result_w)
        return result

    def __radd__(self, vec2: 'Vec3d') -> 'Vec3d':
        result = vec2 + self
        return result

    def __sub__(self, vec2: 'Vec3d') -> 'Vec3d':
        cons.type_of(vec2, "operand", [Vec3d])

        result_x = self.x - vec2.x
        result_y = self.y - vec2.y
        result_z = self.z - vec2.z
        result_w = self.w - vec2.w

        result = Vec3d(result_x, result_y, result_z, result_w)
        return result

    def __rsub__(self, o: object) -> 'Vec3d':
        result = o + (-self)
        return result

    def __neg__(self) -> 'Vec3d':
        result = Vec3d(-self.x, -self.y, -self.z, -self.w)
        return result

    def __pos__(self) -> 'Vec3d':
        return self.clone()

    def __mul__(self, scalar: Union[int, float]) -> 'Vec3d':
        cons.number(scalar, "operand")

        result_x = self.x * scalar
        result_y = self.y * scalar
        result_z = self.z * scalar
        result_w = self.w * scalar
        result = Vec3d(result_x, result_y, result_z, result_w)
        return result

    def __rmul__(self, scalar: Union[int, float]) -> 'Vec3d':
        result = scalar * self
        return result

    def __truediv__(self, scalar: Union[int, float]) -> 'Vec3d':
        result = Vec3d(self.x / scalar, self.y / scalar, self.z / scalar, self.w)
        return result

    def __floordiv__(self, scalar: Union[int, float]) -> 'Vec3d':
        result =  Vec3d(self.x // scalar, self.y // scalar, self.z // scalar, self.w)
        return result

    def __eq__(self, o: object) -> bool:
        if not isinstance(o, Vec3d):
            return False

        return self.x == o.x and \
               self.y == o.y and \
               self.z == o.z and \
               self.w == o.w

    def __abs__(self):
        result = Vec3d(abs(self.x), abs(self.y), abs(self.z), abs(self.w))
        return result

    def __round__(self, ndigits=None) -> 'Vec3d':
        if ndigits is None:
            return self
        else:
            result = self.__class__(round(self.x, ndigits), round(self.y, ndigits), round(self.z, ndigits), round(self.w, ndigits))
            return result

    def __getitem__(self, index: Union[int, slice]) -> float:
        if isinstance(index, int):
            return self.__getattribute__(self.order[index])
        result = list(map(lambda p: self.__getattribute__(p), self.order)).__getitem__(index)
        return result

    def __setitem__(self, index: int, value: float) -> None:
        self.__setattr__(self.order[index], value)
        return None

    def to_array(self):
        return [self.x, self.y, self.z, self.w]
