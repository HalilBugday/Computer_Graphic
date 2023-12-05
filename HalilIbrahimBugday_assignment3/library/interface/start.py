# CENG 487 Assignment3 by
# Halil İbrahim Buğday
# StudentId: 280201094
# 12 2023

from abc import ABC
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from signal import signal, SIGINT

class Start(ABC):
    def __init__(self, title: str, mode=GLUT_RGBA | GLUT_DOUBLE | GLUT_DEPTH, size=(720, 680), pos=(0, 0), argv=[]) -> None:
        self.size = size
        self.argv = argv
        self.title = title
        self.mode = mode
        self.pos = pos

    def init_gl(self):
        width, height = self.size
        aspect_ratio = float(width) / float(height)
        gluPerspective(45.0, aspect_ratio, 0.1, 100.0)
        glDepthFunc(GL_LESS)
        glShadeModel(GL_SMOOTH)
        glClearColor(0.0, 0.0, 0.0, 0.0)
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        glEnable(GL_DEPTH_TEST)
        glClearDepth(5.0)
        glMatrixMode(GL_MODELVIEW)

    def start(self):
        glutInit(self.argv)
        glutInitDisplayMode(self.mode)
        glutInitWindowSize(*self.size)
        glutInitWindowPosition(*self.pos)
        glutCreateWindow(self.title)
        glutDisplayFunc(self.on_display)
        glutIdleFunc(self.on_idle)
        glutReshapeFunc(self.on_resize)
        glutKeyboardFunc(self.on_key_press)
        glutSpecialFunc(self.on_special_key_press)
        glutMotionFunc(self.on_mouse_drag)
        glutPassiveMotionFunc(self.on_mouse_move)
        self.init_gl()
        signal(SIGINT, lambda *_: glutLeaveMainLoop())
        glutMainLoop()

    def on_display(self):
        # TODO:
        pass

    def on_idle(self):
        # TODO:
        pass

    def on_resize(self, width, height):
        if height == 0:
            height = 1
        self.size = (width, height)
        glViewport(0, 0, width, height)
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        gluPerspective(45.0, float(width)/float(height), 0.1, 100.0)
        glMatrixMode(GL_MODELVIEW)

    def on_key_press(self, key, x, y):
        if ord(key) == 27:
            glutLeaveMainLoop()

    def on_mouse_drag(self, x, y):
        # TODO:
        pass

    def on_special_key_press(self, key, x, y):
        # TODO:
        pass

    def on_mouse_move(self, x, y):
        # TODO:
        pass

    def on_display(self):
        # TODO:
        pass

    def on_idle(self):
        # TODO:
        pass
