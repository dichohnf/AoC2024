class Map:
    def __init__(self, matrix):
        self.positions = [[Position(self, (i,j), char) for j, char in enumerate(row)] for i, row in enumerate(matrix)]

    def __calculate_antinode_unique_positions__(self):
        [position.writable_antinode() for row in self.positions for position in row]

    def count_unique_positions(self):
        self.__calculate_antinode_unique_positions__()
        return sum(position.antinode for row in self.positions for position in row)

class Position:
    def __init__(self, map, position, char):
        self.map = map
        self.position = position
        self.char = char
        self.antinode = False

    def writable_antinode(self):
        if self.char == '.':
            return
        for i, row in enumerate(self.map.positions):
            for j, position in enumerate(row):
                if position.char == self.char and (i,j) != self.position:
                    antinode_row = 2*i - self.position[0]
                    antinode_col = 2*j - self.position[1]
                    if 0<= antinode_row < len(self.map.positions) and 0<= antinode_col < len(self.map.positions[0]):
                        self.map.positions[antinode_row][antinode_col].antinode = True

list_map = [line for line in open("../inputs/8.in").read().splitlines()]
print(Map(list_map).count_unique_positions())