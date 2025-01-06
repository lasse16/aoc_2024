from operator import add

directions = {
    "<": (-1, 0),
    ">": (1, 0),
    "^": (0, -1),
    "v": (0, 1),
}


def main():
    args = parse("input.txt")
    # args = parse("test-input.txt")
    # args = parse("test-input2.txt")

    print(f"Solution PART1: {part1(args)}")
    # print(f"Solution PART2: {part2(args)}")


def parse(file):
    boxes = set()
    walls = set()
    instructions = ""
    with open(file, "r") as file:
        file_text = file.read()
        grid, instructions_lines = file_text.split("\n\n")
        instructions = instructions_lines.replace("\n", "")
        for y, line in enumerate(grid.splitlines()):
            for x, c in enumerate(line.strip()):
                if c == "#":
                    walls.add((x, y))
                if c == "O":
                    boxes.add((x, y))
                if c == "@":
                    start_position = (x, y)
    return boxes, walls, start_position, instructions, x + 1, y + 1


def part1(args):
    boxes, walls, start_position, instructions, max_x, max_y = args
    position = start_position
    for instruction in instructions:
        direction = directions[instruction]
        potential_pos = tuple(map(add, position, direction))
        if potential_pos in walls:
            continue
        if potential_pos in boxes:
            # MOVABLE?
            next_pos = tuple(map(add, potential_pos, direction))
            while next_pos in boxes:
                next_pos = tuple(map(add, next_pos, direction))
            if next_pos in walls:
                continue
            else:
                # MOVE BOX
                # Moving a box is just swapping the first with the free position
                boxes.add(next_pos)
                boxes.remove(potential_pos)
        position = potential_pos
        state = boxes, walls, position, instruction, max_x, max_y

    return sum(get_box_values(boxes))


def part2(args):
    print(args)


def visualize(args):
    boxes, walls, position, _, max_x, max_y = args
    lines = [["."] * max_x for _ in range(max_y)]
    for x, y in boxes:
        lines[y][x] = "O"
    for x, y in walls:
        lines[y][x] = "#"
    lines[position[1]][position[0]] = "@"

    return "\n".join(["".join(line) for line in lines])


def get_box_values(boxes):
    result = []
    for x, y in boxes:
        result += [x + y * 100]
    return result


if __name__ == "__main__":
    main()
