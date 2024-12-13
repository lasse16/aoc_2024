def main():
    args = parse("input.txt")
    # args = parse("test-input.txt")

    print(f"Solution PART1: {part1(args)}")
    print(f"Solution PART2: {part2(args)}")


def parse(file):
    with open(file, "r") as file:
        file_text = file.read().strip()
        return [int(c) for c in file_text]


def part1(args):
    layout = visualize_layout(args)
    forward_pointer = 0
    backwards_pointer = len(layout) - 1
    while forward_pointer < backwards_pointer:
        if layout[forward_pointer] == "." and layout[backwards_pointer] != ".":
            layout[forward_pointer] = layout[backwards_pointer]
            layout[backwards_pointer] = "."
            backwards_pointer -= 1
            forward_pointer += 1
        else:
            if layout[backwards_pointer] == ".":
                backwards_pointer -= 1
            else:
                forward_pointer += 1
    return checksum(layout)


def checksum(layout):
    total_checksum = 0
    for idx, c in enumerate(layout):
        if c == ".":
            return total_checksum
        total_checksum += idx * c
    return total_checksum


def part2(args):
    pass

def visualize_layout(parsed_map):
    layout = []
    file_id = 0
    for i, length in enumerate(parsed_map):
        if i % 2 == 0:  # File
            layout.extend([file_id] * length)
            file_id += 1
        else:  # Free space
            layout.extend(["."] * length)
    return layout


if __name__ == "__main__":
    main()
