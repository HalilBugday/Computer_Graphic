# CENG 487 Assignment2 by
# Halil İbrahim Buğday
# StudentId: 280201094
# 11 2023

from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from signal import signal, SIGINT
from lib.shape import Camera

class Assignment2(Camera):
    def __init__(self):
        super().__init__()

    print("")
    print("CENG487 Homework#2")
    print("")
    print("***USER'S MANUAL***")

    print("-> 1.", "Cylinder")
    print("-> 2.", "Sphere")
    print("-> 3.", "Torus")
    print("-> 4.", "Box")
    print("-> 5.", "Pyramid")

    print("")

    print("KEYBOARD OPERATIONS:")
    print("-> +", "increase number of subdivisions")
    print("-> -", "decrease number of subdivisions")
    print("-> Up Arrow", "rotate the object around x-axis")
    print("-> Down Arrow", "rotate the object around x-axis")
    print("-> Right Arrow", "rotate the object around y-axis")
    print("-> Left Arrow", "rotate the object around y-axis")
    print("-> R", "reset the object")
    print("")


    print("MOUSE OPERATIONS:")
    print("-> Left click - drag and drop ", "rotate rotate the object around xyz-axis")
    print("-> Right click", "undo last transformation")
    print("-> Wheel Up", "zoom -")
    print("-> Wheel Down", "zoom +")



    def main(self):
        glutInit(sys.argv)
        glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_DEPTH)
        glutInitWindowSize(780, 640)
        glutInitWindowPosition(0, 0)
        glutCreateWindow("Halil Ibrahim Bugday")
        glutIdleFunc(self.DrawGLScene)
        glutKeyboardFunc(self.keyboardFunc)
        glutReshapeFunc(self.ReSizeGLScene)
        glutSpecialFunc(self.specialFunc)
        glutPassiveMotionFunc(self.passiveMotionFunc)
        glutDisplayFunc(self.DrawGLScene)
        glutMouseFunc(self.mouseFunc)
        self.InitGL(780, 640)
        signal(SIGINT, lambda *_: glutLeaveMainLoop())
        glutMainLoop()

if __name__ == "__main__":
    assignment2 = Assignment2()
    assignment2.main()
