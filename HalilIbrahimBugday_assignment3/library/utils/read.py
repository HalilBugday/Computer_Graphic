# CENG 487 Assignment3 by
# Halil İbrahim Buğday
# StudentId: 280201094
# 12 2023

from ..shapes import Object3d
from ..calculate import Vec3d
from ..shapes import Shape

def parse_vertex(line):
    x, y, z = map(float, line.split()[1:])
    return Vec3d.point(x, y, z)

def parse_face(line, vertices):
    face_vertices = [vertices[int(index) - 1] for index in line.split()[1:]]
    return Shape(vertices=face_vertices, color=(0.6, 0.6, 0.6))

def parse_obj(file):
    vertices = []
    faces = []

    def handle_line(line):
        nonlocal vertices, faces
        line = line.strip()

        if not line or line.startswith("#"):
            return

        cmd, *values = line.split()

        if cmd == "v":
            vertices.append(parse_vertex(line))
        elif cmd == "f":
            faces.append(parse_face(line, vertices))
        elif cmd == "o":
            pass
        else:
            raise ValueError(f"Invalid line: {line}")

    with open(file) as f:
        for line in f:
            handle_line(line)

    return Object3d(subdivisions=faces)


