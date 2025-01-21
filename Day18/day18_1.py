def corrupt_byte(b_map, byte):
    b_map[byte[0]][byte[1]] = "#"


def print_map(b_map):
    print("\n".join("".join(char for char in row ) for row in b_map))


def collect_neighbours(b_map, position):
    neighbors = []
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    for direction in directions:
        new_position = (position[0] + direction[0], position[1] + direction[1])
        if (0 <= new_position[0] < len(b_map)
                and 0 <= new_position[1] < len(b_map[0])):
            if b_map[new_position[0]][new_position[1]] == ".":
                neighbors.append(new_position)
    return neighbors


def search_path(b_map, visited, last_added, num, end):
    uncorrupted_neighbours = [neighbour for node in last_added for neighbour in collect_neighbours(b_map, node)]
    last_added.clear()
    for neighbour in uncorrupted_neighbours:
        if neighbour not in visited:
            visited[neighbour] = num
            last_added.append(neighbour)


def search_minimum_path(b_map):
    start = (0,0)
    end = (70,70)
    i = 0
    visited = {start:i}
    last_added = [start]
    while end not in visited:
        i += 1
        search_path(b_map, visited, last_added, i, end)
    return visited[end]


def main():
    global BYTES_FALLEN
    global MAP_DIMENSION

    with open("../inputs/18.in") as file:
        fallen = [line.split(",") for line in file.read().splitlines()]
        fallen = [(int(fal[0]), int(fal[1])) for fal in fallen]

    bytes_map = [["." for _ in range(MAP_DIMENSION)] for _ in range(MAP_DIMENSION)]
    for i in range(BYTES_FALLEN):
        corrupt_byte(bytes_map, fallen[i])

    minimum = search_minimum_path(bytes_map)
    print(minimum)


BYTES_FALLEN = 1024
MAP_DIMENSION = 71
if __name__ == "__main__":
    main()