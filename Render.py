from abc import *


class Renderable:
    __metaclass__ = ABCMeta

    @abstractmethod
    def pre_render(self, scene):
        pass

    @abstractmethod
    def render(self, scene):
        pass

    @abstractmethod
    def post_render(self, scene):
        pass
