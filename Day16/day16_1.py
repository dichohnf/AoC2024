from json.encoder import INFINITY

class ReindeerMazeTile:
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

def explore_neighbors(maze, current_position):
    updated_positions = []
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    for direction in directions:
        new_position = (current_position[0] + direction[0], current_position[1] + direction[1])
        if is_within_bounds(maze, new_position):
            next_tile = maze[new_position[0]][new_position[1]]
            if next_tile.tile_type in [".", "E"]:
                current_tile = maze[current_position[0]][current_position[1]]
                move_cost = calculate_move_cost(current_tile, direction)
                if next_tile.update_cost(move_cost, direction):
                    updated_positions.append(new_position)
    return updated_positions

def is_within_bounds(maze, position):
    return 0 <= position[0] < len(maze) and 0 <= position[1] < len(maze[0])

def calculate_move_cost(current_tile, direction):
    if current_tile.prev_direction == direction:
        return current_tile.cost + STRAIGHT_COST
    else:
        return current_tile.cost + STRAIGHT_COST + TURN_COST

def find_shortest_path(maze, start_position, end_position):
    positions_to_check = [start_position]
    while positions_to_check:
        current_positions = positions_to_check.copy()
        positions_to_check = [neighbor for position in current_positions
                              for neighbor in explore_neighbors(maze, position)]
    return maze[end_position[0]][end_position[1]].cost

def load_maze(file_path):
    with open(file_path) as file:
        maze_lines = file.read().splitlines()
        maze = [[ReindeerMazeTile(tile) for tile in line] for line in maze_lines]
    return maze

def main():
    global START_POSITION, END_POSITION
    maze = load_maze("../inputs/16.in")

    maze[START_POSITION[0]][START_POSITION[1]].cost = 0

    minimum_cost = find_shortest_path(maze, START_POSITION, END_POSITION)
    print(minimum_cost)

STRAIGHT_COST = 1
TURN_COST = 1000
START_POSITION = (139, 1)
END_POSITION = (1, 139)

if __name__ == "__main__":
    main()
