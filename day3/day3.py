import re


def mull_it_over_pt1(puzzle):
    pattern = r"mul\((\d+),(\d+)\)"

    # Find all occurrences of mul(x, y)
    matches = re.findall(pattern, puzzle)

    res = 0

    for match in matches:
        res += int(match[0]) * int(match[1])

    return res

def mull_it_over_pt2(puzzle):
    patternDisable = r"don't\(\).*?do\(\)"
    puzzle = re.sub(patternDisable, "", puzzle)

    dontPattern = r"don't\(\).*"
    puzzle = re.sub(dontPattern, "", puzzle)


    pattern = r"mul\((\d+),(\d+)\)"
    matches = re.findall(pattern, puzzle)

    

    res = 0
    for match in matches:
        res += int(match[0]) * int(match[1])

    return res


# reading input
with open("input.txt") as f:
    puzzle = f.readlines() 
    puzzle = "".join(puzzle).replace('\n', "")
    print(puzzle)  



print("Part 1 Solution: " + str(mull_it_over_pt1(puzzle)))
print("Part 2 Solution: " + str(mull_it_over_pt2(puzzle)))
