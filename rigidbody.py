from vpython import *

class RigidBody:
    __obj = None

    def __init__(self, v = vec(0, 0, 0), m = 1, boundingSphereRadius = 1):
        self.v = v
        self.mass = m
        self.r = boundingSphereRadius

    def getPosition(self):
        return self.__obj.pos

    def setObject(self, obj):
        self.__obj = obj

    def addForce(self, f: vec):
        self.v += f / self.mass

    def update(self, dt):
        self.__obj.pos += self.v * dt

    def collision(self, obj2):
        n = self.getPosition() - obj2.getPosition() 
        n_hat = norm(n)
        dist = mag(n)

        v_relm = dot(self.v - obj2.v, n_hat) # 멀어지는 상황
        if v_relm > 0:
            return
        
        tot_radius = self.r + obj2.r
        if dist > tot_radius:
            return
        else:
            j = -2*v_relm
            j = j/(1/self.mass+1/obj2.mass)
            self.v = self.v + j*n_hat/self.mass
            obj2.v = obj2.v - j*n_hat/obj2.mass