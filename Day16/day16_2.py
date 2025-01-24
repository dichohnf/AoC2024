from json.encoder import INFINITY

class MazeTile:
    def __init__(self, tile_type):
        self.tile_type = tile_type
        self.cost = INFINITY
        self.prev_direction = None

    def update_cost(self, cost, direction):
        if cost < self.cost:
            self.cost = cost
            self.prev_direction = direction
            return True
        return False

def is_within_bounds(maze, position):
    rows, cols = len(maze), len(maze[0])
    return 0 <= position[0] < rows and 0 <= position[1] < cols

def calculate_move_cost(current_tile, direction):
    if current_tile.prev_direction == direction:
        return current_tile.cost + STRAIGHT_COST
    return current_tile.cost + STRAIGHT_COST + TURN_COST

def explore_neighbors(maze, current_position):
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    current_tile = maze[current_position[0]][current_position[1]]
    neighbors = []

    for direction in directions:
        new_position = (current_position[0] + direction[0], current_position[1] + direction[1])
        if is_within_bounds(maze, new_position):
            next_tile = maze[new_position[0]][new_position[1]]
            if next_tile.tile_type in [".", "E"]:
                move_cost = calculate_move_cost(current_tile, direction)
                if next_tile.update_cost(move_cost, direction):
                    neighbors.append(new_position)
    return neighbors

def build_best_paths(maze):
    positions_to_check = [START_POSITION]
    while positions_to_check:
        current_positions = positions_to_check.copy()
        positions_to_check = [neighbor for pos in current_positions
                              for neighbor in explore_neighbors(maze, pos)]

def add_neighbors(maze, visited, current_position):
    mmax = maze[current_position[0]][current_position[1]].cost
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    if current_position != START_POSITION:
        old_dir = maze[current_position[0]][current_position[1]].prev_direction
        directions.append((-2*old_dir[0], -2*old_dir[1]))
    neighbors = []

    for direction in directions:
        new_position = (current_position[0] + direction[0], current_position[1] + direction[1])
        if is_within_bounds(maze, new_position):
            next_tile = maze[new_position[0]][new_position[1]]
            if next_tile.tile_type in [".", "S"]:
                neighbors.append(new_position)
    added = set()
    for neighbor in neighbors:
        if maze[neighbor[0]][neighbor[1]].cost in [mmax - 1, mmax - 2, mmax - 1001] and neighbor not in visited:
            added.add(neighbor)
            maze[neighbor[0]][neighbor[1]].tile_type = "O"
    return added

def count_tiles(maze):
    visited = {END_POSITION}
    positions_to_check = {END_POSITION}
    while positions_to_check:
        current_positions = positions_to_check.copy()
        positions_to_check = [neighbor for pos in current_positions
                              for neighbor in add_neighbors(maze, visited, pos)]
        visited.update(positions_to_check)
    return len(visited)

def load_maze(file_path):
    with open(file_path) as file:
        lines = file.read().splitlines()
        maze = [[MazeTile(char) for char in line] for line in lines]
    return maze

def main():
    global START_POSITION, END_POSITION
    maze = load_maze("../inputs/16.in")
    maze[START_POSITION[0]][START_POSITION[1]].cost = 0

    build_best_paths(maze)
    total_tiles = count_tiles(maze)

    print(total_tiles)

STRAIGHT_COST = 1
TURN_COST = 1000
START_POSITION = (139, 1)
END_POSITION = (1, 139)

if __name__ == "__main__":
    main()