# CENG 487 Assignment3 by
# Halil İbrahim Buğday
# StudentId: 280201094
# 12 2023

# TO RUN -> python assignment3.py library/ecube.obj
# TO RUN -> python assignment3.py library/tori.obj

from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from sys import argv
from os.path import basename
from math import *
from library.utils.read import parse_obj
from library.interface import Start, Camera, Scene
from library.shapes import Object3d

class Assignment3Application(Start):
    def __init__(self, obj: Object3d, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.camera_model = Camera()
        self.camera_ui = Camera()
        self.scene_model = Scene(cameras=(self.camera_model,))
        self.scene_model.register(obj)
        self.scene_ui = Scene(cameras=(self.camera_ui,))
        self.mouse_x = 0
        self.mouse_y = 0

    def draw_gl_scene(self):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        level = self.scene_model.objects[0][0].level
        self.scene_model.draw()
        self.scene_ui.draw()
        glutSwapBuffers()

    def on_display(self):
        return self.draw_gl_scene()

    def on_idle(self):
        return self.draw_gl_scene()

    def on_mouse_drag(self, x, y):
        width, height = self.size
        dx = (pi/2) * (y - self.mouse_y)/width
        dy = (pi/2) * (x - self.mouse_x)/height
        self.mouse_x = x
        self.mouse_y = y
        self.scene_model.active_camera.rotate(dy, dx, 0)

    def on_key_press(self, key, x, y):
        super().on_key_press(key, x, y)

        if key == b'+':
            for obj in self.scene_model.objects:
                obj[0].increase_subdivisions()
            current_level = self.scene_model.objects[0][0].level
            print("Current subdivision Level:", current_level)
        elif key == b'-':
            for obj in self.scene_model.objects:
                obj[0].decrease_subdivisions()
            current_level = self.scene_model.objects[0][0].level
            print("Current subdivision Level:", current_level)
        elif key == b'r':
            self.scene_model.active_camera.reset()

    def on_special_key_press(self, key, x, y):
        if key == GLUT_KEY_LEFT:
            self.scene_model.active_camera.rotate(0, -pi/8, 0)
        elif key == GLUT_KEY_RIGHT:
            self.scene_model.active_camera.rotate(0, +pi/8, 0)
        elif key == GLUT_KEY_UP:
            self.scene_model.active_camera.rotate(-pi/8, 0, 0)
        elif key == GLUT_KEY_DOWN:
            self.scene_model.active_camera.rotate(+pi/8, 0, 0)


def main():
    print("")
    print("CENG487 Homework#3")
    print("")
    print("***USER'S MANUAL***")
    print("")
    print("-> +", "increase number of subdivisions")
    print("-> -", "decrease number of subdivisions")
    print("-> Up Arrow", "rotate the object around x-axis")
    print("-> Down Arrow", "rotate the object around x-axis")
    print("-> Right Arrow", "rotate the object around y-axis")
    print("-> Left Arrow", "rotate the object around y-axis")
    print("-> Drag while Mouse clicked", "rotate the object around xyz-axis")
    print("-> R", "reset position the object")
    print("")
    print("Current subdivision Level: 0")

    argc = len(argv)
    obj = None

    if argc < 2:
        print("error! Object file does not exist.")
        exit(1)
    try:
        obj = parse_obj(argv[1])
    except FileNotFoundError:
        print("error! File does not exist.")
        exit(2)
    except Exception as e:
        print("error: Parse Error because : ", e)
        exit(3)

    app = Assignment3Application(
        obj,
        "IZTECH CENG487 - ASSIGNMENT3 [" + basename(argv[1]) + "]",
        argv=argv[:2]
    )
    app.start()

if __name__ == "__main__":
    main()