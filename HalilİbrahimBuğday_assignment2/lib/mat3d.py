# CENG 487 Assignment2 by
# Halil İbrahim Buğday
# StudentId: 280201094
# 11 2023

from typing import Union
from math import sin, cos
from .utils import cons
from .vec3d import Vec3d

class Mat3d:
    def __init__(self, *rows):
        for row in rows:
            cons.type_of(row, f"r{rows.index(row) + 1}", [Vec3d])
        self.matrix = list(rows)

    @staticmethod
    def translation_matrix(tx: float, ty: float, tz: float) -> 'Mat3d':
        result_matrix = Mat3d(Vec3d(1, 0, 0, tx), Vec3d(0, 1, 0, ty), Vec3d(0, 0, 1, tz), Vec3d(0, 0, 0, 1))
        return result_matrix

    @staticmethod
    def scaling_matrix(sx: float, sy: float, sz: float) -> 'Mat3d':
        result_matrix = Mat3d(Vec3d(sx, 0, 0, 0),Vec3d(0, sy, 0, 0), Vec3d(0, 0, sz, 0), Vec3d(0, 0, 0, 1))
        return result_matrix

    @staticmethod
    def rotation_x_matrix(theta: float) -> 'Mat3d':
        result_matrix = Mat3d(Vec3d(1, 0, 0, 0), Vec3d(0, cos(theta), -sin(theta), 0), Vec3d(0, sin(theta), cos(theta), 0), Vec3d(0, 0, 0, 1))
        return result_matrix

    @staticmethod
    def rotation_y_matrix(theta: float) -> 'Mat3d':
        result_matrix = Mat3d(Vec3d(cos(theta), 0, sin(theta), 0),Vec3d(0, 1, 0, 0),Vec3d(-sin(theta), 0, cos(theta), 0),Vec3d(0, 0, 0, 1))
        return result_matrix

    @staticmethod
    def rotation_z_matrix(theta: float) -> 'Mat3d':
        result_matrix = Mat3d(Vec3d(cos(theta), -sin(theta), 0, 0),Vec3d(sin(theta), cos(theta), 0, 0),Vec3d(0, 0, 1, 0),Vec3d(0, 0, 0, 1))
        return result_matrix

    def clone(self) -> 'Mat3d':
        return Mat3d(*[row.clone() for row in self.matrix])

    def __add__(self, mat2: 'Mat3d') -> 'Mat3d':
        cons.type_of(mat2, "operand", [Mat3d])
        result_matrix = []
        for row1, row2 in zip(self.matrix, mat2.matrix):
            result_matrix.append(row1 + row2)
        return Mat3d(*result_matrix)

    def __radd__(self, mat2: 'Mat3d') -> 'Mat3d':
        result_matrix = self + mat2
        return result_matrix

    def __sub__(self, mat2: 'Mat3d') -> 'Mat3d':
        cons.type_of(mat2, "operand", [Mat3d])
        result_matrix = self + mat2.negate()
        return result_matrix

    def __rsub__(self, mat2: 'Mat3d') -> 'Mat3d':
        result_matrix = self - mat2
        return result_matrix

    def __mul__(self, scalar: Union[int, float]) -> 'Mat3d':
        cons.number(scalar, "operand")
        result_matrix = Mat3d(*[row * scalar for row in self.matrix])
        return result_matrix

    def __rmul__(self, scalar: Union[int, float]) -> 'Mat3d':
        result_matrix = self * scalar
        return result_matrix

    def __truediv__(self, scalar: Union[int, float]) -> 'Mat3d':
        result_matrix = self * (1 / scalar)
        return result_matrix

    def __matmul__(self, mat2: Union['Mat3d', 'Vec3d']) -> 'Mat3d':
        cons.type_of(mat2, "mat", [Vec3d, Mat3d])
        if isinstance(mat2, Vec3d):
            result_vector = Vec3d(*[row.dot(mat2) for row in self.matrix])
            return result_vector
        mat_T = mat2.transpose()
        result_matrix = Mat3d(*[Vec3d(*[row.dot(row_T) for row_T in mat_T]) for row in self.matrix])
        return result_matrix

    def transpose(self) -> 'Mat3d':
        transposed_matrix = Mat3d(*[Vec3d(*column) for column in zip(*self.matrix)])
        return transposed_matrix

    def __eq__(self, o: object) -> bool:
        if isinstance(o, Mat3d):
            return all(row_self == row_other for row_self, row_other in zip(self.matrix, o.matrix))
        return False

    def __getitem__(self, index: int) -> Vec3d:
        return self.matrix[index]

    def __setitem__(self, index: int, value: Vec3d) -> None:
        self.matrix[index] = value

    def __neg__(self) -> 'Mat3d':
        negated_matrix = -1 * self
        return negated_matrix

    def __pos__(self) -> 'Mat3d':
        return self.clone()

    def __str__(self) -> str:
        return "mat3d(" + ",\n      ".join(map(str, self.matrix)) + ")"

    @staticmethod
    def identity():
        result_matrix = Mat3d(Vec3d(1, 0, 0, 0),Vec3d(0, 1, 0, 0),Vec3d(0, 0, 1, 0),Vec3d(0, 0, 0, 1))
        return result_matrix
