from GameObject import *
from Time import Time


class Animation(GameComponent):

    def __init__(self, game_object):
        super(Animation, self).__init__(game_object)

    def pre_render(self, scene):
        self.game_object.transform.rotation.y += Time.delta * 0.5

        pass

    def render(self, scene):
        pass

    def post_render(self, scene):
        pass


class AnimationFov(GameComponent):

    def __init__(self, game_object):
        super(AnimationFov, self).__init__(game_object)

    def pre_render(self, scene):
        current_fov = self.game_object.fov
        self.game_object.set_fov(current_fov + Time.delta * 10)
        pass

    def render(self, scene):
        pass

    def post_render(self, scene):
        pass


class AnimationCam(GameComponent):

    def __init__(self, game_object):
        super(AnimationCam, self).__init__(game_object)
        self.period = 0
        self.magnitude = 1

    def pre_render(self, scene):
        self.period = (self.period + Time.delta) % 1
        self.game_object.transform.position += Vector3(0, 0, math.sin(math.pi * self.period) * self.magnitude)

    def render(self, scene):
        pass

    def post_render(self, scene):
        pass
