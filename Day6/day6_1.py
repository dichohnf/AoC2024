import numpy as np

class PathCalculator:
    def __init__(self, input_string):
        self.area_map = [list(line) for line in input_string.splitlines()]
        # Starting position
        self.guard = Guard(
            self.area_map,
            np.array((input_string.find("^")//(len(self.area_map[0])+1), input_string.find("^")%(len(self.area_map[0])+1))), #+1 -> \n
            np.array((-1,0)))

    def __draw_path__(self):
        while self.guard.move():
            pass

    def count_path_steps(self):
        self.__draw_path__()
        return sum(row.count("X") for row in self.area_map)

class Guard:
    def __init__(self, area_map, position, direction):
        self.area_map = area_map
        self.position = position
        self.direction = direction
        self.dir_dict = {
            (-1, 0): ( 0, 1),
            ( 0, 1): ( 1, 0),
            ( 1, 0): ( 0,-1),
            ( 0,-1): (-1, 0)
        }

    def move(self):
        future_position = self.position + self.direction
        self.area_map[self.position[0]][self.position[1]] = "X"
        if not (0 <= future_position[0] < len(self.area_map) and 0 <= future_position[1] < len(self.area_map[0])):
            return False
        future_position_char = self.area_map[future_position[0]][future_position[1]]
        if future_position_char in [".", "X"]:
            self.position = future_position
        elif future_position_char == "#":
            self.direction = self.dir_dict[tuple(self.direction)]
        return True


print(PathCalculator(open("../inputs/6.in").read()).count_path_steps())