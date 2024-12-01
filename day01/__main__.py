from collections import Counter

def main():
    left_column, right_column = parse("input.txt")
    part1(left_column, right_column)
    part2(left_column, right_column)

def parse(file):
    left_column = []
    right_column = []

    with open(file, 'r') as file:
        for line in file.readlines():
            columns = line.split("   ")
            left_column.append(int(columns[0]))
            right_column.append(int(columns[1]))

    return left_column,right_column

def part1(left, right):
    left.sort()
    right.sort()
    total_distance = 0
    for i in range(len(left)):
        total_distance += abs(left[i] - right[i])
    print(total_distance)

def part2(left, right):
    similarity_score = 0
    c = Counter(right)
    for id in left:
        similarity_score += c[id] * id
    print(similarity_score)

if __name__ == "__main__":
    main()
