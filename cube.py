from vpython import *
from rigidbody import RigidBody
import math

class Cube(RigidBody):
    def __init__(self, position, size, v, m = 1):
        super().__init__(v, m, math.sqrt(sum([ i ** 2 for i in size ]))/2 )
        super().setObject(box(pos = position, width = size[0], height = size[1], length=size[2]))