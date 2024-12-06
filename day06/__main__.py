from collections import defaultdict

directions = [
    (-1, 0),
    (0, 1),
    (1, 0),
    (0, -1),
]


def main():
    grid, guard_start, max_x, max_y = parse("input.txt")
    # grid, guard_start, max_x, max_y = parse("test-input.txt")

    print(f"Solution PART1: {part1(grid, guard_start,max_x,max_y)}")
    print(f"Solution PART2: {part2(grid, guard_start,max_x,max_y)}")


def parse(file):
    grid = defaultdict(lambda: False)
    guard_start = -1
    with open(file, "r") as file:
        for x, line in enumerate(file.readlines()):
            for y, field in enumerate(line):
                if field == "#":
                    grid[(x, y)] = True
                if field == "^":
                    guard_start = (x, y)
                    grid[(x, y)] = False
                if field == ".":
                    grid[(x, y)] = False
    # need to correct for last line
    # in y direction \n is counted
    # in x last line is not counted
    return grid, guard_start, x + 1, y


def part1(grid, guard_start, max_x, max_y):
    visited_nodes, _ = __move_guard(grid, guard_start, max_x, max_y)
    return len(visited_nodes)


def __tuple_add(tuple1, tuple2):
    res = []
    for idx, x in enumerate(tuple1):
        res.append(x + tuple2[idx])
    return tuple(res)


def __move_guard(grid, guard_start, max_x, max_y):
    visited_nodes = set()
    visited_nodes_with_direction = defaultdict(set)
    current_direction_index = 0
    current_position = guard_start
    while current_position[0] in range(max_x) and current_position[1] in range(max_y):
        visited_nodes.add(current_position)
        directions_node_was_visited_with = visited_nodes_with_direction[
            current_position
        ]
        if current_direction_index in directions_node_was_visited_with:
            return visited_nodes, True
        directions_node_was_visited_with.add(current_direction_index)

        potential_position = __tuple_add(
            current_position, directions[current_direction_index]
        )
        if grid[potential_position]:
            current_direction_index += 1
            current_direction_index %= len(directions)
        else:
            current_position = potential_position
    return visited_nodes, False

# Correct solution but about 10s run time
def part2(grid, guard_start, max_x, max_y):
    default_path, _ = __move_guard(grid, guard_start, max_x, max_y)
    loop_counter= 0
    for potentially_looping_obstruction in default_path:
        modified_grid = grid.copy()
        modified_grid[potentially_looping_obstruction] = True
        _, loop = __move_guard(modified_grid, guard_start, max_x, max_y)
        if loop:
            loop_counter += 1
    return loop_counter


if __name__ == "__main__":
    main()
