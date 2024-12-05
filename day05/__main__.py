from collections import defaultdict


def main():
    rules, updates = parse("input.txt")
    # rules, updates = parse("test-input.txt")

    print(f"Solution PART1: {part1(rules, updates)}")
    print(f"Solution PART2: {part2(rules, updates)}")


def parse(file):
    rules = defaultdict(list)
    updates = list()
    with open(file, "r") as file:
        file_text = file.read()
        rules_raw, updates_raw = file_text.split("\n\n")
        for rule in rules_raw.splitlines():
            number_before, number_after = map(int, rule.strip().split("|"))
            entry = rules[number_before]
            entry.append(number_after)
            rules[number_before] = entry
        for update in updates_raw.splitlines():
            numbers = list(map(int, update.strip().split(",")))
            updates.append(numbers)
    return rules, updates


def part1(rules, updates):
    total_count = 0
    for update in updates:
        if is_valid(update, rules):
            total_count += update[len(update) // 2]
    return total_count


def is_valid(update, rules):
    previous_chars = []
    for page in update:
        pages_that_must_be_after = rules.get(page, [])
        for c in previous_chars:
            if c in pages_that_must_be_after:
                return False
        previous_chars.append(page)
    return True


def part2(rules, updates):
    total_count = 0
    for update in updates:
        if not is_valid(update, rules):
            update = topological_sort(update, rules)
            total_count += update[len(update) // 2]
    return total_count


def topological_sort(update, rules):
    # Kahn's algorithm
    in_degree = {node: 0 for node in update}
    for node in update:
        for neighbor in rules[node]:
            if neighbor in update:
                in_degree[neighbor] += 1

    queue = [node for node in update if in_degree[node] == 0]
    result = []

    while queue:
        node = queue.pop(0)
        result.append(node)
        for neighbor in rules[node]:
            if neighbor in update:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)
    #  order  is flipped but does not matter for middle number
    return result


if __name__ == "__main__":
    main()
