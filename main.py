import time
import copy
import random
import os

random.seed(0)


class World:
    def __init__(self, height, lenght):
        self.height = height
        self.lenght = lenght
        self.cur_gen = [[False for _ in range(self.lenght)] for row in range(self.height)]
        self.prv_gen = list(copy.deepcopy(self.cur_gen))
        self.gen_count = 0

    def clone_pop(self, field):
        self.feild = field

    def pop_count(self):
        return sum([sum(row) for row in self.cur_gen])

    def isEnd(self):
        return self.pop_count() == 0 or self.cur_gen in self.prv_gen

    def rand_pop(self, populaiton):
        for _ in range(populaiton):
            x = random.randint(0, self.height - 1)
            y = random.randint(0, self.lenght - 1)
            self.cur_gen[x][y] = True

    def draw(self, symbol='X'):
        for row in self.cur_gen:
            for el in row:
                if el:
                    print(symbol, end='')
                else:
                    print(' ', end='')
            print()

    def get_neib_count(self, pos_x, pos_y):
        delta = [-1, 0, 1]
        res = sum(
            [self.cur_gen[(pos_x + delta_x) % self.height][(pos_y + delta_y) % self.lenght] for delta_x in delta for
             delta_y in delta])
        if self.cur_gen[pos_x][pos_y]:
            res -= 1
        return res

    def new_cell_state(self, x, y):
        neibs = self.get_neib_count(x, y)
        if self.cur_gen[x][y] and (neibs > 3 or neibs < 2):
            return False
        elif not self.cur_gen[x][y] and neibs == 3:
            return True
        return self.cur_gen[x][y]

    def next_generation(self):
        new_gen = []
        for x in range(self.height):
            new_gen.append([])
            for y in range(self.lenght):
                new_gen[x].append(self.new_cell_state(x, y))
        self.prv_gen.append(self.cur_gen)
        self.cur_gen = new_gen
        self.gen_count += 1


world = World(30, 30)
world.rand_pop(100)

while True:
    # os.system('cls')
    world.next_generation()
    world.draw(symbol='O')
    print(world.pop_count())
    if world.isEnd(): break
    time.sleep(1)
print(world.gen_count)