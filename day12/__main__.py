test_regions = [
    {(0, 0), (0, 1), (0, 2), (0, 3)},
    {(1, 0), (1, 1), (2, 0), (2, 1)},
    {(1, 2), (2, 2), (2, 3), (3, 3)},
    {(1, 3)},
    {(3, 0), (3, 1), (3, 2)},
]


def main():
    args = parse("input.txt")
    # args = parse("test-input.txt")
    # args = parse("test-input2.txt")

    print(f"Solution PART1: {part1(args)}")
    print(f"Solution PART2: {part2(args)}")


def parse(file):
    field_data = dict()
    with open(file, "r") as file:
        for x, line in enumerate(file.readlines()):
            for y, c in enumerate(line.strip()):
                field_data[(x, y)] = c
    return field_data


def part1(args):
    field_data = args
    regions = find_regions(field_data)
    # regions = test_regions
    total = 0
    for region in regions:
        perimeter = calculate_perimeter(region)
        area = len(region)
        print(f"perimeter {perimeter}, area {area}")
        total += perimeter * area
    return total


def calculate_perimeter(region):
    total_perimeter = 0
    for node in region:
        neighbours = get_neighbours(node)
        neighbours_in_region = [
            neighbour for neighbour in neighbours if neighbour in region
        ]
        total_perimeter += 4 - len(neighbours_in_region)
    return total_perimeter


def find_regions(field_data):
    non_visited = set(field_data.keys())
    regions = []
    while non_visited:
        node = non_visited.pop()
        region = flood_fill(node, field_data)
        non_visited -= region
        regions.append(region)
    return regions


def flood_fill(node, field_data):
    q = set()
    region = set()
    current_element = field_data[node]
    checked = set()
    q.add(node)
    while q:
        element = q.pop()
        if field_data[element] == current_element and element not in checked:
            region.add(element)
            for neighbour in get_neighbours(element):
                if neighbour not in checked:
                    q.add(neighbour)
        checked.add(element)

    return region


def get_neighbours(node):
    neighbours = []
    for direction in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        new_x = node[0] + direction[0]
        new_y = node[1] + direction[1]
        if new_x in range(140) and new_y in range(140):
            neighbours.append((new_x, new_y))
    return neighbours


def part2(args):
    pass


if __name__ == "__main__":
    main()
