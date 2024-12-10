def guard_gallivant_pt1(puzzle):
    height = len(puzzle)
    width = len(puzzle[0])

    i = 0
    while i < width:
        j = 0
        while j < height:
            if puzzle[j][i] == "^":  
                x = i
                y = j
            j += 1
        i += 1

    print(x,y)
    print(height,width)
    res = 1
    puzzle[y][x] = "*"
    direction = "up"
    while x < width and y < height and x >= 0 and y >= 0:
        print(x,y)
        if direction == "up":
            if y - 1 < 0:
                break
            elif puzzle[y-1][x] == ".":
                y = y - 1
                res += 1
                puzzle[y][x] = "*"
            elif puzzle[y-1][x] == "*":
                y = y - 1
            elif puzzle[y-1][x] == "#":
                direction = "right"
        elif direction == "right":
            if x + 1 >= width:
                break
            elif puzzle[y][x+1] == ".":
                x = x + 1
                res += 1
                puzzle[y][x] = "*"
            elif puzzle[y][x+1] == "*":
                x = x + 1
            elif puzzle[y][x+1] == "#":
                direction = "down"
        elif direction == "down":
            if y + 1 >= height:
                break
            elif puzzle[y+1][x] == ".":
                y = y + 1
                res += 1
                puzzle[y][x] = "*"
            elif puzzle[y+1][x] == "*":
                y = y + 1
            elif puzzle[y+1][x] == "#":
                direction = "left"
        elif direction == "left":
            if x - 1 < 0:
                break
            elif puzzle[y][x-1] == ".":
                x = x - 1
                res += 1
                puzzle[y][x] = "*"
            elif puzzle[y][x-1] == "*":
                x = x - 1
            elif puzzle[y][x-1] == "#":
                direction = "up"
    print(puzzle)
    return res
        

def guard_gallivant_pt2(puzzle):
    pass

        


# reading input
with open("input.txt") as f:
    puzzle = [list(line.strip()) for line in f.readlines()]

print("Part 1 Solution: " + str(guard_gallivant_pt1(puzzle)))
print("Part 2 Solution: " + str(guard_gallivant_pt2(puzzle)))