from simulator import Simulator
from sphere import Sphere
from cube import Cube
from vpython import *

env = Simulator()

obj1 = Sphere(vec(0, 0, 0), radius = 1, v = vec(1, 0, 0))
env.addObject(obj1)

obj2 = Sphere(vec(5, 0, 0), radius = 1, v = vec(-1, 0, 0))
env.addObject(obj2)

env.addObject(Sphere(vec(1, 0, 0), radius = 0.5, v = vec(-1, 0, 0)))
env.addObject(Sphere(vec(0, 1, 0), radius = 0.2, v = vec(0, 1, 0)))
env.addObject(Cube(vec(0,0,0), size=(1, 1, 1), v = vec(0, 0, 0)))

env.run()