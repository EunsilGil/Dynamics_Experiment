from vpython import *

class Simulator:
    __t = 0 # 현재 시간
    dt = 0.1 # 관찰 시간 간격

    __objects = [] # 그릴 목록

    def getCurrentTime(self):
        return self.__t

    def addObject(self, obj):
        self.__objects.append(obj)

    def run(self):
        while True:
            rate(1 / self.dt)
            for obj1 in range(len(self.__objects)):
                for obj2 in range(obj1 + 1, len(self.__objects)):
                    self.__objects[obj1].collision(self.__objects[obj2])

            for obj in self.__objects:
                obj.update(self.dt)

            self.__t += self.dt