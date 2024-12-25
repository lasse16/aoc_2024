from math import log10, floor


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
        if stone == 0:
            new_stones.append(1)
        elif digits_in_integer(stone) % 2 == 0:
            first_half, second_half = split_integer(stone)
            new_stones.append(first_half)
            new_stones.append(second_half)
        else:
            new_stones.append(stone * 2024)
    return new_stones


def digits_in_integer(integer):
    return floor(log10(integer)) + 1


def split_integer(integer, splitting_point=-1):
    if splitting_point == -1:
        splitting_point = digits_in_integer(integer) // 2
    return integer // 10**splitting_point, integer % 10**splitting_point


def part2(args):
    print(args)


if __name__ == "__main__":
    main()
