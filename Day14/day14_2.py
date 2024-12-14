from collections import defaultdict
import regex as re

class Map:
    def __init__(self, width, height, robots_list):
        self.width = width
        self.height = height
        self.robots = robots_list
        self.positions = defaultdict(int)
        for robot in self.robots:
            self.positions[(robot.position["X"], robot.position["Y"])] += 1

    def move_robots(self, seconds):
        for _ in range(seconds):
            for robot in self.robots:
                self.positions[(robot.position["X"], robot.position["Y"])] -= 1
                robot.position = robot.next_position(self.width, self.height)
                self.positions[(robot.position["X"], robot.position["Y"])] += 1

class Robot:
    def __init__(self, position, speed):
        self.position = {"X": position[0], "Y": position[1]}
        self.speed = {"X": speed[0], "Y": speed[1]}

    def next_position(self, width, height):
        self.position["X"] = (self.position["X"] + self.speed["X"]) % width
        self.position["Y"] = (self.position["Y"] + self.speed["Y"]) % height
        return self.position

def create_map_string(robot_list, width, height):
    grid = ["." * width for _ in range(height)]
    grid = [list(row) for row in grid]
    for robot in robot_list:
        grid[robot.position["Y"]][robot.position["X"]] = "o"
    return ["".join(row) for row in grid]


lines = open("../inputs/14.in").read().splitlines()
robots = [Robot((int(x), int(y)), (int(vx), int(vy))) for line in lines for x, y, vx, vy in [re.findall(r"-?\d+", line)]]
WIDTH, HEIGHT = 101, 103
mmap = Map(WIDTH, HEIGHT, robots)
total_seconds = 0

# Ho supposto che i robot avrebbero dovuto essere tutti in posizioni
# differenti per partecipare alla generazione dell'Ester Egg in quanto partecipassero al pattern.
# La supposizione è parzialmente corretta: i robot non partecipano tutti all'EE,
# ma il pattern è visibile quando i robot sono tutti in posizioni differenti.
# (BOTTA DI CULO!)

while True:
    if sum(count for count in mmap.positions.values() if count < 2) == len(mmap.robots):
        for row in create_map_string(mmap.robots, mmap.width, mmap.height):
            print(row)
        print(total_seconds)
        break
    mmap.move_robots(1)
    total_seconds += 1