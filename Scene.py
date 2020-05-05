from Math import Math
from Camera import Camera
from Render import *
from GameObject import GameObject
import subprocess as sp
import math
import time


class Scene:

    def __init__(self):
        self.objects = {}
        self.mainCamera = ''

        # TODO: Implement a renderer.
        self.resolution = [80, 40]
        self.render_grid = {}
        self.render_grid_color = {}

    def add_object(self, object_name, object):
        if not issubclass(object, GameObject):
            return

        self.objects[object_name] = object()

    def set_camera(self, object_name):
        if not object_name in self.objects or not isinstance(self.objects[object_name], Camera):
            return

        self.mainCamera = object_name

    def get_camera(self):
        return self.objects[self.mainCamera]

    def pre_render(self):
        # Clear the screen.
        print(chr(27) + "[2J")
        self.clear_screen()

        for name, instance in self.objects.items():
            instance.pre_render(self)

    def render_at(self, coords, content):
        if not len(content) == 1:
            return

        point = coords.split(';')
        point_color = self.render_grid_color[coords]
        print("\033[%s;%sH%s" %(point[1], point[0], "%s%s" %('', content)))

    def render(self):
        for name, instance in self.objects.items():
            instance.render(self)

        for coords, item in self.render_grid.items():
            self.render_at(coords, item)

    def post_render(self):
        for name, instance in self.objects.items():
            instance.post_render(self)


    def clear_screen(self):
        for coords, item in self.render_grid.items():
            self.render_at(coords, ' ')

        self.render_grid = {}

        # for i in range(0, self.resolution.x * self.resolution.y + 1):
        #     self.render_grid.append(' ')

    def render_point(self, rel_x, rel_y, color = 39):
        if not Math.in_range(rel_x, 0, 1) or not Math.in_range(rel_y, 0, 1):
            return

        x = rel_x * (self.resolution[0] - 1)
        y = rel_y * (self.resolution[1] - 1)

        x = round(x)
        y = round(y)

        # point_address = int(round(x) + self.resolution.y * round(y))
        self.render_grid['%i;%i' %(x, y)] = '+'
        self.render_grid_color['%i;%i' %(x, y)] = "\e[%sm" %(color)
