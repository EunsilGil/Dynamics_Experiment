from vpython import *
from rigidbody import RigidBody

class Sphere(RigidBody):
    def __init__(self, position, radius, v = vec(0, 0, 0), m = 1):
        super().__init__(v, m, radius)
        super().setObject(sphere(pos = position, radius=radius))