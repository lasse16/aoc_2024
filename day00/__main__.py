def main():
    args = parse("input.txt")
    args = parse("test-input.txt")

    print(f"Solution PART1: {part1(args)}")
    print(f"Solution PART2: {part2(args)}")


def parse(file):
    with open(file, "r") as file:
        file_text = file.read()
    return file_text


def part1(args):
    print(args)


def part2(args):
    print(args)


if __name__ == "__main__":
    main()
