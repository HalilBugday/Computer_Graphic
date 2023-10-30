# CENG 487 Assignment1 by
# Halil İbrahim Buğday
# StudentId: 280201094
# 10 2023

from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from mat3d import *
from vec3d import Vec3d
from object import object
import sys

window = 0
past_time = 0

# Creating square
square = object(pos=Vec3d(2.5, 0, 0,0), vertices=[Vec3d(-1, 1, 0, 1), Vec3d(1, 1, 0, 1), Vec3d(1, -1, 0, 1), Vec3d(-1, -1, 0, 1)])

# Creating triangle
triangle = object(pos=Vec3d(-1.5, 0, 0, 0), vertices=[Vec3d(0, 1, 0, 1), Vec3d(1, -1, 0, 1), Vec3d(-1, -1, 0, 1)])

def InitGL(Width, Height):
    glClearColor(0.0, 0.0, 0.0, 0.0)
    glClearDepth(1.0)
    glDepthFunc(GL_LESS)
    glEnable(GL_DEPTH_TEST)
    glShadeModel(GL_SMOOTH)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(45.0, float(Width) / float(Height), 0.1, 100.0)
    glMatrixMode(GL_MODELVIEW)

def ReSizeGLScene(Width, Height):
    if Height == 0:
        Height = 1

    glViewport(0, 0, Width, Height)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(45.0, float(Width) / float(Height), 0.1, 100.0)
    glMatrixMode(GL_MODELVIEW)

def DrawGLScene():
    global past_time
    dif = glutGet(GLUT_ELAPSED_TIME) - past_time
    past_time = glutGet(GLUT_ELAPSED_TIME)
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    glTranslatef(0, 0.0, -10.0)
    glBegin(GL_POLYGON)
    glColor3f(255.0,0.0,0.0)

    triangle.moving([translate_matrix(-1, 1, 0), xy_rotation_matrix(dif/300), translate_matrix(1, -1, 0)])

    for i in triangle.vertice():
        position=triangle.position()+i
        glVertex3f(position.x, position.y, position.z)
    glEnd()

    glBegin(GL_POLYGON)
    glColor3f(1.0,1.0,0.0)

    square.moving(
       [translate_matrix(1, 1, 0), xy_rotation_matrix(dif/300), translate_matrix(-1, -1, 0)])

    for j in square.vertice():
        position=square.position()+j
        glVertex3f(position.x, position.y, position.z)
    glEnd()

    glutSwapBuffers()



def keyPressed(key, x, y):
	if ord(key) == 27:
		return


def main():

    global window

    glutInit(sys.argv)

    glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_DEPTH)

    glutInitWindowSize(640, 480)

    glutInitWindowPosition(0, 0)

    window = glutCreateWindow("CENG487 Assigment1")

    glutDisplayFunc(DrawGLScene)

    glutIdleFunc(DrawGLScene)

    glutReshapeFunc(ReSizeGLScene)

    glutKeyboardFunc(keyPressed)

    InitGL(640, 480)

    glutMainLoop()

print("Hit ESC key to quit.")
main()
