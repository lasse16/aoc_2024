from collections import defaultdict

directions = [
    (-1, 0),
    (0, 1),
    (1, 0),
    (0, -1),
]


def main():
    grid, guard_start = parse("input.txt")
    # rules, updates = parse("test-input.txt")

    print(f"Solution PART1: {part1(grid, guard_start)}")
    # print(f"Solution PART2: {part2(grid, guard_start)}")


def parse(file):
    grid = dict()
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
    return grid, guard_start


def part1(grid, guard_start):
    visited_nodes = set()
    current_direction_index = 0
    current_position = guard_start
    in_grid = True
    while in_grid:
        print("still_running")
        visited_nodes.add(current_position)
        potential_position = __tuple_add(
            current_position, directions[current_direction_index]
        )
        # Not proud on using exceptions to do business logic
        try:
            if grid[potential_position]:
                current_direction_index += 1
                current_direction_index %= len(directions)
            else:
                current_position = potential_position
        except KeyError:
            in_grid = False

    return len(visited_nodes)


def __tuple_add(tuple1, tuple2):
    res = []
    for idx, x in enumerate(tuple1):
        res.append(x + tuple2[idx])
    return tuple(res)


def part2(rules, updates):
    pass


if __name__ == "__main__":
    main()
