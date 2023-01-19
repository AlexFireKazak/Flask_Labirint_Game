import copy
import random
from threading import Lock


class Singleton:
    _instance = None
    _instance_base = None

    def __new__(cls, *args, **kwargs):
        if cls == Singleton:
            if cls._instance_base is None:
                cls._instance_base = object.__new__(cls)
            return cls._instance_base
        if cls._instance is None:
            cls._instance = object.__new__(cls)
        return cls._instance

class Labirint_game(Singleton):
    world = [[0 for _ in range(3)] for i in range(3)]
    exit = (random.randint(0, 3 - 1), random.randint(0, 3 - 1))
    start = (random.randint(0, 3 - 1), random.randint(0, 3 - 1))
    win = False
    def __init__(self, width=5, height=5):
#        super().__init__()
        self.width = width
        self.heigth = height
        #self.world = self.generate_world()
        self.win = False
        #self.start = (random.randint(0, self.width - 1), random.randint(0, self.heigth - 1))

#        if self.start == self.exit:
#            while self.start == self.exit:
#                self.exit = (random.randint(0, self.width - 1), random.randint(0, self.heigth - 1))
#        self.world[self.start[0]][self.start[1]] = 1
#        print(self.start, self.exit)



    #def generate_world(self):
    #    world = [[0 for _ in range(self.width)] for i in range(self.heigth)]
    #
    #
    #    #world[self.exit[0]][self.exit[1]] = -1
    #    return world

    def go_to(self, course, steps):
        courses = {'0': (-1, 0), '1': (0, 1), '2': (1, 0), '3': (0, -1)}
        now_travel = courses[course]
        print('now travel', now_travel)
        end_point = ((self.start[0] + steps * now_travel[0])%self.width, (self.start[1] + steps * now_travel[1])%self.heigth)
        print('endpoint', end_point)
        self.world[self.start[0]][self.start[1]] = 0
        self.world[end_point[0]][end_point[1]] = 1
        if end_point != Labirint_game.exit:
            Labirint_game.start = end_point
            print(Labirint_game.start, 'go to here')
        else:
            Labirint_game.win = True
            print('win')