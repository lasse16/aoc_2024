def main():
    rules, updates = parse("input.txt")
    # rules, updates = parse("test-input.txt")

    print(f"Solution PART1: {part1(rules, updates)}")
    # print(f"Solution PART2: {part2(twoDimensionalGrid,x_max,y_max)}")


def parse(file):
    rules = dict()
    updates = list()
    with open(file, "r") as file:
        file_text = file.read()
        rules_raw, updates_raw = file_text.split("\n\n")
        for rule in rules_raw.splitlines():
            number_before, number_after = map(int, rule.strip().split("|"))
            enry = rules.get(number_before)
            if not enry:
                enry = []
                rules[number_before] = enry

            enry.append(number_after)
        for update in updates_raw.splitlines():
            numbers  = list(map(int, update.strip().split(",")))
            updates.append(numbers)
    return rules, updates


def part1(rules, updates):
    total_count = 0
    for update in updates:
        if is_valid(update,rules):
            total_count += update[len(update) // 2]
    return total_count

def is_valid(update,rules):
    previous_chars = []
    for page in update:
        pages_that_must_be_after = rules.get(page,[])
        for c in previous_chars:
            if c in pages_that_must_be_after:
                return False
        previous_chars.append(page)
    return True

def part2(grid, x_max, y_max):
    pass


if __name__ == "__main__":
    main()
