# CENG 487 Assignment3 by
# Halil İbrahim Buğday
# StudentId: 280201094
# 12 2023

from typing import Iterable, List, Tuple, Union
from ..shapes import Shape, Object3d
from .camera import Camera


class Scene:
    def __init__(self, cameras: Iterable[Camera], visible=True) -> None:
     
        self.objects: List[Tuple[Union[Shape, Object3d], bool]] = []
        self.cameras: List[Camera] = list(cameras) if cameras else []
        self.active_camera: Camera = self.cameras[0] if self.cameras else None
        self.visible: bool = visible


    def draw(self, border=True):
        self.active_camera.look()
        if self.visible:
            for i in self.objects:
                obj, visible = i
                if visible:
                    if border:
                        obj.draw_border()
                    obj.draw()

    def register(self, obj: Union[Shape, Object3d], visible=True):
        entry = (obj, visible)
        self.objects.append(entry)

    def unregister(self, element: Union[Shape, Object3d]) -> bool:
        for i, (obj, _) in enumerate(self.objects):
            if obj == element:
                del self.objects[i]
                return True
        return False
