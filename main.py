#!/usr/bin/env python

from Vector3 import Vector3
from Render import *
from GameObject import *
from Camera import Camera
from Scene import Scene
from Animation import *
from Time import Time
from ObjReader import ObjReader
import time
import sys


# Define a renderable scene.
scene = Scene()

# geometry = ObjReader.load('bunny.obj')
if len(sys.argv) > 1:
    geometry = ObjReader.load(sys.argv[1])

    scene.add_object('object', GameObject)
    for key, item in geometry.items():
       scene.objects['object'].add_component(key, MeshComponent)
       scene.objects['object'].components[key].points = item.vertices

    scene.objects['object'].transform.position = Vector3(0, -0.8, 150)
    scene.objects['object'].transform.scale = 150
    scene.objects['object'].add_component('animation', Animation)

scene.add_object('cube', GameObject)
scene.add_object('sphere', GameObject)

scene.objects['cube'].add_component('animation', Animation)
scene.objects['cube'].transform.position = Vector3(0, 0, 200)
scene.objects['cube'].transform.scale = 50
scene.objects['cube'].add_component('cubeMesh', MeshComponent)
scene.objects['cube'].components['cubeMesh'].points = [
    Vector3(-1, 1, -1), Vector3(1, 1, -1),
    Vector3(-1, -1, -1), Vector3(1, -1, -1),
    Vector3(-1, 1, 1), Vector3(1, 1, 1),
    Vector3(-1, -1, 1), Vector3(1, -1, 1)
]

#scene.objects['cube'].add_component('sphere', MeshComponent)
#scene.objects['cube'].components['sphere'].points = ObjReader.load('test_c.obj')['default'].vertices

# Define a camera.
scene.add_object('mainCamera', Camera)
scene.objects['mainCamera'].set_fov(120)
scene.objects['mainCamera'].transform.position = Vector3(0, 0, -10)
#scene.objects['mainCamera'].add_component('camAnimation', AnimationCam)

scene.set_camera('mainCamera')

while True:
    # Measure dTime.
    start = time.clock()

    scene.pre_render()
    scene.render()
    scene.post_render()

    sleep = 0.025
    time.sleep(sleep)
    start -= sleep
    Time.delta = time.clock() - start

