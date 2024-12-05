def historican_hysteria_pt1(puzzle):
    first_list = []
    second_list = []
    for line in puzzle:
        line = line.split(" ")
        first, second = line[0], line[3]
        first_list.append(int(first))
        second_list.append(int(second))

    first_list = sorted(first_list)
    second_list = sorted(second_list)

    pointer, n = 0, len(first_list)
    res = 0
    while pointer < n:
        res += abs(first_list[pointer] - second_list[pointer])
        pointer += 1
    return res

def historican_hysteria_pt2(puzzle):
    first_list = []
    count = {}
    for line in puzzle:
        line = line.split(" ")
        first, second = int(line[0]), int(line[3])
        first_list.append(first)

        if second not in count:
            count[second] = 1
        else:
            count[second] += 1

    pointer, n = 0, len(first_list)
    res = 0
    while pointer < n:
        if first_list[pointer] in count:
            res += first_list[pointer] * count[first_list[pointer]]
        pointer += 1
    return res

# reading input
with open("input.txt") as f:
    puzzle = f.readlines()

print("Part 1 Solution: " + str(historican_hysteria_pt1(puzzle)))
print("Part 2 Solution: " + str(historican_hysteria_pt2(puzzle)))
