def search_paths(mp, start_pos):
    val = 1
    sequences = [[start_pos]]
    while val <= 9:
        sequences = [sequence + [neigh]
                             for sequence in sequences
                             for neigh in neighbors(sequence[-1], mp)
                             if int(mp[neigh[0]][neigh[1]]) == val]
        val += 1
    return len({tuple(sequence) for sequence in sequences})

def neighbors(pos, mp):
    ret = []
    if pos[0] > 0:
        ret.append((pos[0] - 1, pos[1]))
    if pos[0] < len(mp)-1:
        ret.append((pos[0] + 1, pos[1]))
    if pos[1] > 0:
        ret.append((pos[0], pos[1] - 1))
    if pos[1] < len(mp[0])-1:
        ret.append((pos[0], pos[1] + 1))
    return ret

in_map = [list(line) for line in open("../inputs/10.in").read().splitlines()]
res = sum(
    search_paths(in_map, (i, j))
    for i, line in enumerate(in_map)
    for j in range(len(line))
    if line[j] == "0")
print(res)
