from math import log10, floor
from functools import cache


def main():
    args = parse("input.txt")
    # args = parse("test-input.txt")

    print(f"Solution PART1: {part1(args)}")
    print(f"Solution PART2: {part2(args)}")


def parse(file):
    stones = []
    with open(file, "r") as file:
        file_text = file.read().split()
        stones = list(map(int, file_text))
    return stones


def part1(args):
    stones = args
    step_count = 25
    for i in range(step_count):
        stones = simulate_step(stones)
    return len(stones)


def simulate_step(stones):
    new_stones = []
    for stone in stones:
        updated = simulate_stone(stone)
        new_stones += updated
    return new_stones


def simulate_stone(stone):
    if stone == 0:
        return [1]
    elif digits_in_integer(stone) % 2 == 0:
        first_half, second_half = split_integer(stone)
        return [first_half, second_half]
    else:
        return [stone * 2024]


def digits_in_integer(integer):
    return floor(log10(integer)) + 1


def split_integer(integer, splitting_point=-1):
    if splitting_point == -1:
        splitting_point = digits_in_integer(integer) // 2
    return integer // 10**splitting_point, integer % 10**splitting_point


@cache
def simulate_stone_for_count(stone, count):
    if count == 0:
        return 1

    count -= 1
    if stone == 0:
        result = simulate_stone_for_count(1, count)
    elif digits_in_integer(stone) % 2 == 0:
        left, right = split_integer(stone)
        result = simulate_stone_for_count(left, count) + simulate_stone_for_count(
            right, count
        )
    else:
        result = simulate_stone_for_count(stone * 2024, count)

    return result


def part2(args):
    stones = args
    step_count = 75

    total_stone_count = 0

    # All stones are independent from each other as order is preserved
    for stone in stones:
        total_stone_count += simulate_stone_for_count(stone, step_count)

    return total_stone_count


if __name__ == "__main__":
    main()
