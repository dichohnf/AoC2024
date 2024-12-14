import operator
from collections import defaultdict
from functools import reduce
import regex as re


class Grid:
    def __init__(self, width, height, robots_list):
        self.width = width
        self.height = height
        self.robots = robots_list

    def move_robots(self, seconds):
        for rob in self.robots:
            for _ in range(seconds):
                rob.position = rob.next_position(self.width, self.height)


class Robot:
    def __init__(self, position, speed):
        self.position = {"X": position[0], "Y": position[1]}
        self.speed = {"X": speed[0], "Y": speed[1]}

    def next_position(self, width, height):
        self.position["X"] = (self.position["X"] + self.speed["X"]) % width
        self.position["Y"] = (self.position["Y"] + self.speed["Y"]) % height
        return self.position


def get_quadrant(position, width, height):
    if position["X"] == width // 2 or position["Y"] == height // 2:
        return None
    quadrant = 0 if position["X"] < width // 2 else 2
    return quadrant if position["Y"] < height // 2 else quadrant + 1

lines = open("../inputs/14.in").read().splitlines()
robots = [Robot((int(vals[0]), int(vals[1])), (int(vals[2]), int(vals[3])))
          for line in lines for vals in [re.findall(r"-?\d+", line)]]

WIDTH, HEIGHT, SECONDS = 101, 103, 100
grid = Grid(WIDTH, HEIGHT, robots)
grid.move_robots(SECONDS)

quadrant_counts = defaultdict(int)
for robot in robots:
    quadrant = get_quadrant(robot.position, WIDTH, HEIGHT)
    if quadrant is not None:
        quadrant_counts[quadrant] += 1

print(reduce(operator.mul, quadrant_counts.values(), 1))
