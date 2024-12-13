rocks = open("../inputs/11.in").read().splitlines()[0].split()
rocks = {rock:rocks.count(rock) for rock in rocks}

def calc_next(rock):
        if len(rock) % 2 == 0:
            return [rock[:len(rock)//2], str(int(rock[len(rock)//2:]))]
        return '1' if rock == '0' else str(int(rock) * 2024)

for _ in range(75):
    next_rocks = {}
    for rock in rocks:
        next_rock = calc_next(rock)
        if isinstance(next_rock, str):
            next_rocks[next_rock] = next_rocks[next_rock] + rocks[rock] if next_rock in next_rocks else rocks[rock]
        else:
            for r in next_rock:
                next_rocks[r] = next_rocks[r] + rocks[rock] if r in next_rocks else rocks[rock]
    rocks = next_rocks
print(sum(rocks.values()))