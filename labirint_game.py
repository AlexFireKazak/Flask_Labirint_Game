import copy
import random
from threading import Lock


class SingletonMeta(type):
    _instances = {}
    _lock: Lock = Lock()

    def __call__(cls, *args, **kwargs):
        with cls._lock:
            if cls not in cls._instances or args or kwargs:
                instance = super().__call__(*args, **kwargs)
                cls._instances[cls] = instance
        return cls._instances[cls]

class Labirint_game(metaclass=SingletonMeta):
    def __init__(self, width=5, height=5):
#        super().__init__()
        self.width = width
        self.heigth = height
        self.world = self.generate_world()
        self.win = False
        self.start = (random.randint(0, self.width - 1), random.randint(0, self.heigth - 1))
        self.exit = (random.randint(0, self.width - 1), random.randint(0, self.heigth - 1))
#        if self.start == self.exit:
#            while self.start == self.exit:
#                self.exit = (random.randint(0, self.width - 1), random.randint(0, self.heigth - 1))
        self.world[self.start[0]][self.start[1]] = 1
#        print(self.start, self.exit)



    def generate_world(self):
        world = [[0 for _ in range(self.width)] for i in range(self.heigth)]


        #world[self.exit[0]][self.exit[1]] = -1
        return world

    def go_to(self, course, steps):
        courses = {0: (-1, 0), 1: (0, 1), 2: (1, 0), 3: (0, -1)}
        now_travel = courses[course]
        end_point = ((self.start[0] + steps * now_travel[0]-1)%self.width, (self.start[1] + steps * now_travel[1]-1)%self.heigth)
        self.world[self.start[0]][self.start[1]] = 0
        self.world[end_point[0]][end_point[1]] = 1
        if end_point != self.exit:
            self.start = end_point
        else:
            self.win = True