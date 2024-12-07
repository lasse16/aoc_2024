from operator import add, mul


def main():
    args = parse("input.txt")
    # args = parse("test-input.txt")

    print(f"Solution PART1: {part1(args)}")
    print(f"Solution PART2: {part2(args)}")


def parse(file):
    result = []
    with open(file, "r") as file:
        for line in file.readlines():
            line = line.strip()
            result_raw, values_raw = line.split(":")
            values = list(map(int, values_raw.strip().split()))
            result.append((int(result_raw), values))
    return result


def part1(args):
    total_sum_of_valid = 0
    for equation in args:
        if is_valid(equation):
            total_sum_of_valid += equation[0]
    return total_sum_of_valid


def is_valid(equation):
    result, values = equation

    # Generate a list of all possible values by applying all operators to all possible values at each step
    # This essentially is dynamic programming
    possible_values = [values[0]]
    for other_value in values[1:]:
        possible_values = [op(value, other_value) for value in possible_values for op in (add, mul)]

    return result in possible_values


def part2(args):
    pass


if __name__ == "__main__":
    main()
