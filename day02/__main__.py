def main():
    lines = parse("input.txt")
    part1(lines)
    part2(lines)


def parse(file):
    lines = []
    with open(file, "r") as file:
        for line in file.readlines():
            columns = line.split(" ")
            columns = list(map(int, columns))
            lines.append(columns)

    return lines


def part1(lines):
    total_safe_count = 0
    for line in lines:
        if is_safe(line):
            total_safe_count += 1
    print(total_safe_count)


def part2(lines):
    total_safe_count = 0
    for line in lines:
        if is_safe_with_removal(line):
            total_safe_count += 1
    print(total_safe_count)


def is_safe(line):
    first_difference_sign = sign(line[0] - line[1])

    # skip last number
    for i in range(len(line) - 1):
        difference = line[i] - line[i + 1]
        if (
            sign(difference) != first_difference_sign
            or abs(difference) == 0
            or abs(difference) > 3
        ):
            return False

    return True


def is_safe_with_removal(line):
    # Split into two because most are going to be fine without removal so no need to calculate sublists
    if is_safe(line):
        return True
    for sublist in sublists_with_element_removed(line):
        if is_safe(sublist):
            return True
    return False


def sublists_with_element_removed(full_list):
    for i in range(len(full_list)):
        yield full_list[:i] + full_list[i + 1 :]


def sign(number):
    if number > 0:
        return 1
    elif number < 0:
        return -1
    else:
        return 0


if __name__ == "__main__":
    main()
