from GameObject import *
import math


class Camera(GameObject):

    def __init__(self, hfov = 180.0):
        # Set horizontal fov.
        super(Camera, self).__init__()
        self.set_fov(hfov)
        self.direction = Vector3(0, 0, 1)

    def set_fov(self, fov):
        self.fov = fov
        self.fov_rad = fov / (180 / math.pi)

    def get_direction(self):
        return (self.transform.position + self.direction).normalize()
