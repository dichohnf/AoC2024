def calculate_region_positions(position):
    char = char_map[position[0]][position[1]]
    positions = {position}
    to_check = {position}
    to_add = 1
    while to_add :
        to_add = set()
        for position in to_check:
            for pos in [neigh
                        for neigh in neighbors(position, char_map)
                        if neigh not in positions
                        and char_map[neigh[0]][neigh[1]] == char]:
                    to_add.add(pos)
        to_check = to_add
        positions = positions.union(to_check)
    return positions

class Region:
    def __init__(self, char, positions):
        global char_map
        self.char = char
        self.positions = positions
        self.area = len(positions)
        self.perimeter = sum(4 - sum([char == char_map[pos[0]][pos[1]] for pos in neighbors(position, char_map)]) for position in positions)

def neighbors(position, mp):
    ret = []
    if position[0] > 0:
        ret.append((position[0] - 1, position[1]))
    if position[0] < len(mp)-1:
        ret.append((position[0] + 1, position[1]))
    if position[1] > 0:
        ret.append((position[0], position[1] - 1))
    if position[1] < len(mp[0])-1:
        ret.append((position[0], position[1] + 1))
    return ret

char_map = [list(line) for line in open("../inputs/12.in").read().splitlines()]
regions = []
for row in range(len(char_map)):
    for col in range(len(char_map[row])):
        if (row, col) not in [pos for region in regions for pos in region.positions]:
            regions.append(Region(char_map[row][col], calculate_region_positions((row, col))))
print(sum(region.area*region.perimeter for region in regions))
