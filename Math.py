from Vector3 import Vector3

class Math:
    @staticmethod
    def lerp(x, y, d):
        return x + (y - x) * d

    @staticmethod
    def in_range(x, a, b):
        return a < x < b
