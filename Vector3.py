import math
import copy


class Vector3:

    @staticmethod
    def up():
        return Vector3(0, 1, 0)

    @staticmethod
    def dot_relative(a, b):
        return Vector3(math.atan2(b.y, b.z) - math.atan2(a.y, a.z),
                       math.atan2(b.z, b.x) - math.atan2(a.z, a.x),
                       math.atan2(b.y, b.x) - math.atan2(a.y, a.x))

    @staticmethod
    def dot(a, b):
        return (a.x * b.x) + (a.y * b.y) + (a.z * b.z)

    @staticmethod
    def rotate_y(v, d):
        matrix = [
            Vector3(math.cos(d), 0, math.sin((d))),
            Vector3(0, 1, 0),
            Vector3(-math.sin(d), 0, math.cos(d))
        ]

        return Vector3(
            Vector3.dot(v, matrix[0]),
            Vector3.dot(v, matrix[1]),
            Vector3.dot(v, matrix[2]),
        )

    def __init__(self, x = 0.0, y = 0.0, z = 0.0):
        self.x = float(x)
        self.y = float(y)
        self.z = float(z)

    def __add__(self, other):
        return Vector3(self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other):
        return Vector3(self.x - other.x, self.y - other.y, self.z - other.z)

    def __mul__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            other = Vector3(other, other, other)

        return Vector3(self.x * other.x, self.y * other.y, self.z * other.z)

    def __str__(self):
        return 'x:%f y:%f z:%f' %(self.x, self.y, self.z)

    def magnitude(self):
        return math.sqrt(self.x**2 + self.y**2 + self.z**2)

    def normalize(self):
        vmax = float(max(abs(self.x), abs(self.y), abs(self.z)))
        if vmax == 0:
            return self

        return Vector3(self.x / vmax, self.y / vmax, self.z / vmax)

    # As of now the rotation will be represented as a vector, but
    # maybe i'll implement the quaternions later on.
    def rotation(self):
        return Vector3(math.atan2(self.y, self.z), math.atan2(self.z, self.x), math.atan2(self.y, self.x))

    def rotation_deg(self):
        rot = self.rotation()
        rad = 180 / math.pi

        return Vector3(rot.x * rad, rot.y * rad, rot.z * rad)


