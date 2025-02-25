from math import prod
import sys
import re


def main():
    args = parse("input.txt")
    # args = parse("test-input.txt")

    print(f"Solution PART1: {part1(args)}")
    print(f"Solution PART2: {part2(args)}")


def parse(file):
    robots = []
    with open(file, "r") as file:
        for line in file.readlines():
            pattern = r"-?\d+"
            robot = tuple(map(int, re.findall(pattern, line)))
            robots.append(robot)
    return robots


def part1(args):
    max_x = 101
    max_y = 103
    step_count = 100
    robots = args
    end_positions = robots_at_step(robots, step_count, max_x, max_y)
    return prod(count_quadrants(end_positions, max_x, max_y))


def visualize(positions, max_x, max_y):
    res = [[0] * max_x for _ in range(max_y)]
    for x, y in positions:
        res[y][x] += 1
    r = "\n".join(
        ["".join(map(lambda x: str(x) if x else ".", sublist)) for sublist in res]
    )
    return r


def count_quadrants(positions, max_x, max_y):
    top_left = top_right = bot_left = bot_right = 0
    limit_x = max_x // 2
    limit_y = max_y // 2
    for x, y in positions:
        if x == limit_x or y == limit_y:
            continue
        if x > limit_x:
            if y > limit_y:
                top_left += 1
            else:
                top_right += 1
        else:
            if y > limit_y:
                bot_left += 1
            else:
                bot_right += 1

    return top_left, top_right, bot_left, bot_right


def part2(args):
    ##### ASSUMING ALL ROBOTS ARE IN THE SAME QUADRANT DURING THE EASTER EGG #####
    max_x = 101
    max_y = 103
    min_security_factor = (-1, sys.maxsize)
    for i in range(max_x * max_y):
        step_count = i
        end_positions = robots_at_step(args, step_count, max_x, max_y)

        safety_factor = prod(count_quadrants(end_positions, max_x, max_y))
        if safety_factor < min_security_factor[1]:
            min_security_factor = (step_count, safety_factor)
    print(
        visualize(
            robots_at_step(args, min_security_factor[0], max_x, max_y), max_x, max_y
        )
    )
    return min_security_factor[0]


def robots_at_step(robots, step_count, max_x, max_y):
    end_positions = []
    for robot in robots:
        start_pos = robot[:2]
        direction = robot[2:]
        movements = tuple(map(lambda x: x * step_count, direction))
        end_positions.append(
            (
                (start_pos[0] + movements[0]) % max_x,
                (start_pos[1] + movements[1]) % max_y,
            )
        )
    return end_positions


if __name__ == "__main__":
    main()
