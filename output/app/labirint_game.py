import random


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


class Labirint_Game(Singleton):
    def __init__(self, width=4, height=4):
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
            print(self.start, 'go to here')
        else:
            self.win = True
            print('win')

    def new_start_exit(self):
        self.world = [[0 for _ in range(3)] for i in range(3)]
        self.exit = (random.randint(0, 3 - 1), random.randint(0, 3 - 1))
        self.start = (random.randint(0, 3 - 1), random.randint(0, 3 - 1))
        self.win = False