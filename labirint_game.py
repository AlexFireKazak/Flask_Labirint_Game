import copy
import random
from threading import Lock


class Singleton:
    _instance = None
    _instance_base = None

    def __new__(cls, *args, **kwargs):
        if cls == Singleton:
            if cls._innstace_base is None:
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

    def new_start_exit(self):
        Labirint_game.world = [[0 for _ in range(3)] for i in range(3)]
        Labirint_game.exit = (random.randint(0, 3 - 1), random.randint(0, 3 - 1))
        Labirint_game.start = (random.randint(0, 3 - 1), random.randint(0, 3 - 1))
        Labirint_game.win = False

    def __init__(self, width=5, height=5):
#        super().__init__()
        self.width = width
        self.heigth = height
        self.win = False

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



class Labirint_Game:
    def __init__(self, width=3, height=3):
        self.width = width
        self.height = height
        self.world = [[0 for _ in range(self.width)] for _ in range(self.height)]
        self.exit = (random.randint(0, self.width - 1), random.randint(0, self.height - 1))
        self.start = (random.randint(0, self.width - 1), random.randint(0, self.height - 1))
        self.win = False

    def go_to(self, course, steps):
        courses = {'0': (-1, 0), '1': (0, 1), '2': (1, 0), '3': (0, -1)}
        now_travel = courses[course]
        print('now travel', now_travel)
        end_point = (
        (self.start[0] + steps * now_travel[0]) % self.width, (self.start[1] + steps * now_travel[1]) % self.height)
        print('endpoint', end_point)
        self.world[self.start[0]][self.start[1]] = 0
        self.world[end_point[0]][end_point[1]] = 1
        if end_point != self.exit:
            self.start = end_point
            print(Labirint_game.start, 'go to here')
        else:
            self.win = True
            print('win')

