def ceres_search_pt1(puzzle):
    height, width = len(puzzle[0]), len(puzzle)
    x = y = 0
    res = 0
    while x < width:
        y = 0
        while y < height:
            if puzzle[x][y] == "X":
                # check upwards
                if y >= 3:
                    if puzzle[x][y-1] == "M" and puzzle[x][y-2] == "A" and puzzle[x][y-3] == "S":
                        res += 1 
                # check downwards
                if y < height - 3:
                    if puzzle[x][y+1] == "M" and puzzle[x][y+2] == "A" and puzzle[x][y+3] == "S":
                        res += 1 
                # check leftwards
                if x >= 3:
                    if puzzle[x-1][y] == "M" and puzzle[x-2][y] == "A" and puzzle[x-3][y] == "S":
                        res += 1 
                # check rightwards
                if x < width - 3:
                    if puzzle[x+1][y] == "M" and puzzle[x+2][y] == "A" and puzzle[x+3][y] == "S":
                        res += 1 
                # check leftup
                if x >= 3 and y >= 3:
                    if puzzle[x-1][y-1] == "M" and puzzle[x-2][y-2] == "A" and puzzle[x-3][y-3] == "S":
                        res += 1 
                # check leftdown
                if x >= 3 and y < height - 3:
                    if puzzle[x-1][y+1] == "M" and puzzle[x-2][y+2] == "A" and puzzle[x-3][y+3] == "S":
                        res += 1 
                # check rightup
                if x < width - 3 and y >= 3:
                    if puzzle[x+1][y-1] == "M" and puzzle[x+2][y-2] == "A" and puzzle[x+3][y-3] == "S":
                        res += 1 
                # check rightdown
                if x < width - 3 and y < height - 3:
                    if puzzle[x+1][y+1] == "M" and puzzle[x+2][y+2] == "A" and puzzle[x+3][y+3] == "S":
                        res += 1 

            y += 1
        x += 1

    return res


def ceres_search_pt2(puzzle):
    height, width = len(puzzle[0]), len(puzzle)
    x = y = 0
    res = 0
    while x < width:
        y = 0
        while y < height:
            if puzzle[x][y] == "A" and x > 0 and x < width - 1 and y > 0 and y < height - 1:
                # check Ss on left, Ms on right
                if puzzle[x-1][y-1] == "S" and puzzle[x-1][y+1] == "S" and puzzle[x+1][y-1] == "M" and puzzle[x+1][y+1] == "M":
                    res += 1
                # check Ms on left, Ss on right
                if puzzle[x-1][y-1] == "M" and puzzle[x-1][y+1] == "M" and puzzle[x+1][y-1] == "S" and puzzle[x+1][y+1] == "S":
                    res += 1
                # check Ss on top, Ms on bottom
                if puzzle[x-1][y-1] == "S" and puzzle[x+1][y-1] == "S" and puzzle[x-1][y+1] == "M" and puzzle[x+1][y+1] == "M":
                    res += 1
                # check Ms on top, Ss on bottom
                if puzzle[x-1][y-1] == "M" and puzzle[x+1][y-1] == "M" and puzzle[x-1][y+1] == "S" and puzzle[x+1][y+1] == "S":
                    res += 1
            y += 1
        x += 1

    return res


# reading input
with open("input.txt") as f:
    puzzle = [line.strip() for line in f.readlines()]
    

print("Part 1 Solution: " + str(ceres_search_pt1(puzzle)))
print("Part 2 Solution: " + str(ceres_search_pt2(puzzle)))