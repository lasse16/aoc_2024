import re


def main():
    args = parse("input.txt")
    # args = parse("test-input.txt")

    print(f"Solution PART1: {part1(args)}")
    # print(f"Solution PART2: {part2(args)}")


def parse(file):
    machines = []
    with open(file, "r") as file:
        machines_raw = file.read().split("\n\n")
        for machine in machines_raw:
            machine = machine.strip()
            a, b, prize = machine.split("\n")
            ax, ay = map(int, re.findall(r"-?\d+", a))
            bx, by = map(int, re.findall(r"-?\d+", b))
            px, py = map(int, re.findall(r"-?\d+", prize))
            machines.append((ax, bx, ay, by, px, py))
    return machines


def part1(args):
    cost_a_button = 3
    cost_b_button = 1
    max_button_presses = 100
    machines = args
    solutions = solve_machines(machines)

    total_cost = 0
    for solution in solutions:
        a, b = solution
        if a in range(max_button_presses) and b in range(max_button_presses):
            total_cost += a * cost_a_button + b * cost_b_button
    return total_cost


def part2(args):
    print(args)


def solve_machines(machines):
    solutions = []
    for machine in machines:
        solution = solve_machine(*machine)
        if solution:
            solutions.append(solution)

    return solutions


def solve_machine(Ax, Bx, Ay, By, x, y):
    det = Ax * By - Ay * Bx
    if det == 0:
        return None
    a = (x * By - Bx * y) / det
    b = (y * Ax - Ay * x) / det

    return a, b


if __name__ == "__main__":
    main()
