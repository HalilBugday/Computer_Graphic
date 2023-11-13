# CENG 487 Assignment2 by
# Halil İbrahim Buğday
# StudentId: 280201094
# 11 2023

from math import pi
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from lib.shape import Torus, Box, Cylinder, Sphere, Pyramid

class Camera:
    def __init__(self):
        self.primitives = [Cylinder(), *([None] * 4)]
        self.primitives_index = 0
        self.primitive = self.primitives[self.primitives_index]
        self.mouse_x, self.mouse_y = 0, 0

    def InitGL(self, Width, Height):
        glClearDepth(5.0)
        glClearColor(0.0, 0.0, 0.0, 0.0)
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        glShadeModel(GL_SMOOTH)
        glMatrixMode(GL_MODELVIEW)
        glEnable(GL_DEPTH_TEST)
        gluPerspective(45.0, float(Width)/float(Height), 0.1, 100.0)
        glDepthFunc(GL_LESS)

    def ReSizeGLScene(self, Width, Height):
        if Height == 0:
            Height = 1
        glViewport(0, 0, Width, Height)
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        gluPerspective(45.0, float(Width)/float(Height), 0.1, 100.0)
        glMatrixMode(GL_MODELVIEW)

    def DrawGLScene(self):
        object_name = self.primitive.__class__.__name__
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glLoadIdentity()
        glTranslatef(0.0, 0.0, -5.0)
        glutSetWindowTitle(f"Halil İbrahim Buğday-280201094 [{object_name}]")
        self.primitive.draw_border()
        self.primitive.draw()
        glColor3f(1.0, 1.0, 1.0)
        glRasterPos2i(-2, -1)
        glutSwapBuffers()

    def initialize_primitive(self, index, primitive_type):
        self.primitives_index = index
        self.primitives[self.primitives_index] = self.primitives[self.primitives_index] or primitive_type()
        self.primitive = self.primitives[self.primitives_index]

    def keyboardFunc(self, key, x, y):
        if ord(key) == 27:
            glutLeaveMainLoop()
        elif key == b'1':
            self.initialize_primitive(0, Cylinder)
        elif key == b'2':
            self.initialize_primitive(1, Sphere)
        elif key == b'3':
            self.initialize_primitive(2, Torus)
        elif key == b'4':
            self.initialize_primitive(3, Box)
        elif key == b'5':
            self.initialize_primitive(4, Pyramid)
        elif key == b'+':
            self.primitive.increase_subdivisions()
        elif key == b'-':
            self.primitive.decrease_subdivisions()
        elif key == b'r':
            self.primitives[self.primitives_index] = self.primitives[self.primitives_index].__class__()
            self.primitive = self.primitives[self.primitives_index]


    def specialFunc(self, key, x, y):
        if key == GLUT_KEY_LEFT:
            self.primitive.rotate(0, -pi/8, 0)
        elif key == GLUT_KEY_RIGHT:
            self.primitive.rotate(0, +pi/8, 0)
        elif key == GLUT_KEY_UP:
            self.primitive.rotate(-pi/8, 0, 0)
        elif key == GLUT_KEY_DOWN:
            self.primitive.rotate(+pi/8, 0, 0)

    def passiveMotionFunc(self, x, y):
        if 30 <= y <= 50 and 605 <= x <= 620:
            glutSetCursor(GLUT_CURSOR_INFO)
            self.show_help = True
        else:
            glutSetCursor(GLUT_CURSOR_INHERIT)
            self.show_help = False

    def rotate_primitive(self, x, y):
        dx = (pi) * (y - self.mouse_y) / 640
        dy = (pi) * (x - self.mouse_x) / 480
        self.primitive.rotate(dy, 0, dx, "yzx")

    def scale_primitive(self, factor):
        self.primitive.scale(factor)

    def mouseFunc(self, button, state, x, y):
        if button == GLUT_LEFT_BUTTON:
            if state == GLUT_UP:
                self.rotate_primitive(x, y)
            else:
                self.mouse_x = x
                self.mouse_y = y
        elif button == GLUT_RIGHT_BUTTON and state == GLUT_UP:
            self.primitive.undo()
        elif button == GLUT_CURSOR_DESTROY and state == GLUT_UP:
            self.scale_primitive(1.5)
        elif button == GLUT_CURSOR_HELP and state == GLUT_UP:
            self.scale_primitive(0.75)

if __name__ == "__main__":
    camera = Camera()
    camera.main()
