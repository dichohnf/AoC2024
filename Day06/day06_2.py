import numpy as np

class PathCalculator:
    def __init__(self, input_matrix):
        self.area_map = input_matrix
        # Starting position
        self.guard = Guard(
            self.area_map,
            np.array([[i,j] for i, row in enumerate(input_matrix) for j, char in enumerate(row) if char == "^"]),
            np.array((-1,0)))
    def has_loop(self):
        while True:
            flag = self.guard.move()
            if flag == -1:
                return 0
            if flag == 1:
                return 1

class Guard:
    def __init__(self, area_map, start_position, direction):
        self.area_map = area_map
        self.positions_list = [[Position() for _ in row] for row in area_map]
        self.position = start_position.squeeze()
        self.direction = direction
        self.change_dir_dict = {
            (-1, 0): ( 0, 1),
            ( 0, 1): ( 1, 0),
            ( 1, 0): ( 0,-1),
            ( 0,-1): (-1, 0)
        }
    def move(self):
        if self.positions_list[self.position[0]][self.position[1]].already_traveled_direction(self.direction):
            return 1
        future_position = self.position + self.direction
        if not (0 <= future_position[0] < len(self.area_map) and 0 <= future_position[1] < len(self.area_map[0])):
            return -1
        self.positions_list[self.position[0]][self.position[1]].add_direction(self.direction)
        future_position_char = self.area_map[future_position[0]][future_position[1]]
        if future_position_char == "#":
            self.direction = self.change_dir_dict[tuple(self.direction)]
        else:
            self.position = self.position + self.direction
        return 0

class Position:
    def __init__(self):
        self.directions = []
        self.dict = {
            (-1, 0): "^",
            ( 0, 1): ">",
            ( 1, 0): "v",
            ( 0,-1): "<"
        }
    def add_direction(self, direction):
        self.directions.append(self.dict[tuple(direction)])
    def already_traveled_direction(self, direction):
        return self.dict[tuple(direction)] in self.directions

in_list = [list(line) for line in open("../inputs/6.in").read().splitlines()]
cnt = 0
for i in range(len(in_list)):
    for j, char in enumerate(in_list[i]):
        cp_list = [row[:] for row in in_list]
        if char not in ["#", "^"]:
            cp_list[i][j] = "#"
            cnt += PathCalculator(cp_list).has_loop()
print(cnt)


