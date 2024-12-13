from collections import defaultdict


def main():
    args = parse("input.txt")
    # args = parse("test-input.txt")
    # args = parse("test-input2.txt")

    print(f"Solution PART1: {part1(args)}")
    print(f"Solution PART2: {part2(args)}")


def parse(file):
    antennae_with_frequency = defaultdict(list)
    with open(file, "r") as file:
        for x, line in enumerate(file.readlines()):
            for y, c in enumerate(line):
                if c.isalnum():
                    antennae_with_frequency[c].append((x, y))
    return antennae_with_frequency, x + 1, y


def part1(args):
    antennae_with_frequency, max_x, max_y = args
    unique_antinodes = set()
    for antennae in antennae_with_frequency.values():
        for idx, antenna in enumerate(antennae):
            for other_antenna in antennae[idx + 1 :]:
                # Implicit ordering from parsing
                # antenna 0 is going to be lower x than antenna 1
                x_diff = antenna[0] - other_antenna[0]
                y_diff = antenna[1] - other_antenna[1]

                top_antinode = (antenna[0] + x_diff, antenna[1] + y_diff)
                bottom_antinode = (other_antenna[0] - x_diff, other_antenna[1] - y_diff)

                for node in (top_antinode, bottom_antinode):
                    if __point_in_grid(node, max_x, max_y):
                        unique_antinodes.add(node)

    return len(unique_antinodes)


def __point_in_grid(point, max_x, max_y):
    return point[0] in range(max_x) and point[1] in range(max_y)


def part2(args):
    antennae_with_frequency, max_x, max_y = args
    unique_antinodes = set()
    for antennae in antennae_with_frequency.values():
        for idx, antenna in enumerate(antennae):
            for other_antenna in antennae[idx + 1 :]:
                # Implicit ordering from parsing
                # antenna 0 is going to be lower x than antenna 1
                x_diff = antenna[0] - other_antenna[0]
                y_diff = antenna[1] - other_antenna[1]

                curr_point = antenna
                while __point_in_grid(curr_point, max_x, max_y):
                    unique_antinodes.add(curr_point)
                    curr_point = (curr_point[0] + x_diff, curr_point[1] + y_diff)

                curr_point = other_antenna
                while __point_in_grid(curr_point, max_x, max_y):
                    unique_antinodes.add(curr_point)
                    curr_point = (curr_point[0] - x_diff, curr_point[1] - y_diff)

    return len(unique_antinodes)


if __name__ == "__main__":
    main()
