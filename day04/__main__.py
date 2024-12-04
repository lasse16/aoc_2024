from collections import defaultdict

grid_steps = [
    (-1, -1),
    (0, -1),
    (1, -1),
    (-1, 0),
    (1, 0),
    (-1, 1),
    (0, 1),
    (1, 1),
]


def main():
    twoDimensionalGrid, x_max, y_max = parse("input.txt")
    # twoDimensionalGrid, x_max, y_max = parse("test-input.txt")
    print(f"Solution PART1: {part1(twoDimensionalGrid,x_max,y_max)}")
    print(f"Solution PART2: {part2(twoDimensionalGrid,x_max,y_max)}")


def parse(file):
    grid = defaultdict(lambda: "")
    with open(file, "r") as file:
        for i, line in enumerate(file.readlines()):
            for j, c in enumerate(line.strip()):
                grid[(i, j)] = c
    return grid, j + 1, i + 1


def part1(grid, x_max, y_max):
    total_count = 0
    for x in range(x_max):
        for y in range(y_max):
            if grid[(x, y)] == "X":
                candidate = (x, y)
                total_count += valid_words(candidate, grid)
    return total_count


def valid_words(candidate, grid):
    count = 0
    if grid[candidate] == "X":
        for direction in grid_steps:
            if grid[__component_wise_multiplication(candidate, direction, 1)] == "M":
                if (
                    grid[__component_wise_multiplication(candidate, direction, 2)]
                    == "A"
                ):
                    if (
                        grid[__component_wise_multiplication(candidate, direction, 3)]
                        == "S"
                    ):
                        count += 1
    return count


def __component_wise_multiplication(tuple1, tuple2, multiplicator):
    result = []
    for idx, value in enumerate(tuple1):
        result += [value + multiplicator * tuple2[idx]]
    return tuple(result)


def part2(grid, x_max, y_max):
    total_count = 0
    for x in range(x_max):
        for y in range(y_max):
            if grid[(x, y)] == "A":
                candidate = (x, y)
                total_count += int(valid_xmas_cross(candidate, grid))
    return total_count


def valid_xmas_cross(candidate, grid):
    return check_if_direction_writes_mas_or_sam(
        candidate, (-1, -1), grid
    ) and check_if_direction_writes_mas_or_sam(candidate, (1, -1), grid)


def check_if_direction_writes_mas_or_sam(candidate, direction, grid):
    c_in_direction = grid[__component_wise_multiplication(candidate, direction, 1)]
    flipped_direction = __component_wise_multiplication((0, 0), direction, -1)
    c_in_flipped_direction = grid[
        __component_wise_multiplication(candidate, flipped_direction, 1)
    ]
    return (
        c_in_direction in ("M", "S")
        and c_in_flipped_direction in ("M", "S")
        and c_in_direction != c_in_flipped_direction
    )


if __name__ == "__main__":
    main()
