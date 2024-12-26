test_regions = [
    {(0, 0), (0, 1), (0, 2), (0, 3)},
    {(1, 0), (1, 1), (2, 0), (2, 1)},
    {(1, 2), (2, 2), (2, 3), (3, 3)},
    {(1, 3)},
    {(3, 0), (3, 1), (3, 2)},
]

# clockwise-ordering
directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
directions_8_neighbours = [
    (-1, 0),
    (-1, 1),
    (0, 1),
    (1, 1),
    (1, 0),
    (1, -1),
    (0, -1),
    (-1, -1),
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


def part2(args):
    field_data = args
    regions = find_regions(field_data)
    # regions = test_regions
    total = 0
    for region in regions:
        sides = calculate_sides(region)
        area = len(region)
        total += sides * area
    return total


def calculate_sides(region):
    sides = 0

    for cell in region:
        cell_corners = 0
        # get all neightbouras
        neighbours = [(cell[0] + i, cell[1] + j) for i, j in directions_8_neighbours]
        # collect triples of neighbours
        for neighbour1, neighbour2, neighbour3 in [
            (neighbours[x], neighbours[(x + 1) % 8], neighbours[(x + 2) % 8])
            for x in range(0, 8, 2)
        ]:
            # exterior corners
            if neighbour1 not in region and neighbour3 not in region:
                cell_corners += 1

            # interior corners
            if (
                neighbour1 in region
                and neighbour2 not in region
                and neighbour3 in region
            ):
                cell_corners += 1

        sides += cell_corners

    return sides


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
    for direction in directions:
        new_x = node[0] + direction[0]
        new_y = node[1] + direction[1]
        dimension = 140
        if new_x in range(dimension) and new_y in range(dimension):
            neighbours.append((new_x, new_y))
    return neighbours


if __name__ == "__main__":
    main()
