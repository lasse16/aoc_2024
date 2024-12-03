import re
import math


def main():
    # file_as_string = parse("test_input.txt")
    file_as_string = parse("input.txt")
    print(f"Solution PART1: {part1(file_as_string)}")
    print(f"Solution PART2: {part2(file_as_string)}")


def parse(file):
    with open(file, "r") as file:
        return file.read()


def part1(string):
    total_count = 0
    regex_pattern = re.compile(r"mul\((\d{1,3}),(\d{1,3})\)")
    matches = regex_pattern.findall(string)
    print(len(matches))
    for m in matches:
        total_count += math.prod(map(int, m))
    return total_count


# 115930653 too high
# 146718064 too high
# 82857512 correct
def part2(string):
    total_count = 0
    regex_pattern = re.compile(r'''(don't\(\))|(do\(\))|(mul\((\d+),(\d+)\))''')
    matches = regex_pattern.findall(string)

    do = True
    for m in matches:
        print(m)
        if m[1] == "do()":
            do = True
            continue
        elif m[0] == "don't()":
            do = False
            continue
        if do:
            m = m[3:]
            total_count += math.prod(map(int, m))
    return total_count


if __name__ == "__main__":
    main()
