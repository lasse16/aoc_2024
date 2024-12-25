from collections import defaultdict

grid_steps = [
    (0, -1),
    (-1, 0),
    (1, 0),
    (0, 1),
]


def main():
    args = parse("input.txt")
    # args = parse("test-input.txt")

    print(f"Solution PART1: {part1(args)}")
    print(f"Solution PART2: {part2(args)}")


def parse(file):
    grid = defaultdict(int)
    with open(file, "r") as file:
        for x, line in enumerate(file.readlines()):
            for y, c in enumerate(line.strip()):
                grid[(x, y)] = int(c)
    return grid, x + 1, y + 1


def part1(args):
    grid, max_x, max_y = args
    sum_of_valid_trails = 0
    for x in range(max_x):
        for y in range(max_y):
            start = (x, y)
            if grid[start] == 0:
                trailhead_score = len(set(get_trail_ends(grid, start)))
                print(f"trail-head: {start} with score: {trailhead_score}")
                sum_of_valid_trails += trailhead_score
    return sum_of_valid_trails


def get_trail_ends(grid, start, current_num=0):
    if grid[start] != current_num:
        return []

    if grid[start] == 9:
        return [start]

    trailheads = []
    for direction in grid_steps:
        trailheads += get_trail_ends(
            grid, __comp_add(start, direction), current_num + 1
        )
    return trailheads


def part2(args):
    grid, max_x, max_y = args
    sum_of_valid_trails = 0
    for x in range(max_x):
        for y in range(max_y):
            start = (x, y)
            if grid[start] == 0:
                trailhead_rating = len(get_trail_ends(grid, start))
                print(f"trail-head: {start} with rating: {trailhead_rating}")
                sum_of_valid_trails += trailhead_rating
    return sum_of_valid_trails


def __comp_add(tuple1, tuple2):
    return (tuple1[0] + tuple2[0], tuple1[1] + tuple2[1])


if __name__ == "__main__":
    main()
