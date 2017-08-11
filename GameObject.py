from Vector3 import Vector3
from Vector2 import Vector2
from Render import *
import math
from random import random


class Transform:

    def __init__(self):
        # As written previously, note that quaternions will actually
        # be implemented later on, I guess.
        self.position = Vector3(0, 0, 0)
        self.rotation = Vector3(0, 0, 0)
        self.scale = 1


class GameComponent(Renderable):

    def __init__(self, game_object):
        self.game_object = game_object


class GameObject(Renderable):

    def __init__(self):
        self.transform = Transform()
        self.components = {}

    def add_component(self, component_name, component):
        if issubclass(component, GameComponent):
            self.components[component_name] = component(game_object = self)

        return self

    def pre_render(self, scene):
        for key, instance in self.components.items():
            instance.pre_render(scene)

    def render(self, scene):
        for key, instance in self.components.items():
            instance.render(scene)

    def post_render(self, scene):
        for key, instance in self.components.items():
            instance.post_render(scene)


class MeshComponent(GameComponent):

    def __init__(self, game_object):
        super(MeshComponent, self).__init__(game_object)
        self.points = []
        self.triangles = {}
        self.color = Vector3(random() * 255,
                             random() * 255,
                             random() * 255)

    def transpose_points(self):
        result = []
        for point in self.points:
            new_point = Vector3.rotate_y(point, self.game_object.transform.rotation.y)
            new_point = (new_point * self.game_object.transform.scale) + self.game_object.transform.position

            result.append(new_point)

        return result

    def pre_render(self, scene):
        pass

    def render(self, scene):
        # Render the mesh points.
        cam = scene.get_camera()
        points = self.transpose_points()

        # Cast every point to a cameras' screen.
        for point in points:
            point_vector = point - cam.transform.position
            point_rad = Vector3.dot_relative(point_vector.normalize(), cam.direction)

            # Assume projection 1:1 ratio.
            cam_rad = cam.fov_rad
            point_x = (point_rad.y + cam_rad / 2.0) / cam_rad
            point_y = (point_rad.x + cam_rad / 2.0) / cam_rad

            scene.render_point(point_x, point_y)

        pass

    def post_render(self, scene):
        pass
