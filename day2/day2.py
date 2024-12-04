def is_safe_sequence(level):
    # Checks if a sequence of levels is safe without removal of any level
    n = len(level)
    if n <= 1:
        return True
    
    # Check whether the sequence is increasing or decreasing
    if level[0] < level[1]:
        increasing = True
    elif level[0] > level[1]:
        increasing = False
    else:
        return False
    
    pointer = 1
    while pointer < n:
        if abs(level[pointer] - level[pointer-1]) < 1 or abs(level[pointer] - level[pointer-1]) > 3:
            return False
        if increasing:
            if level[pointer] < level[pointer-1]:
                return False
        else:
            if level[pointer] > level[pointer-1]:
                return False
        pointer += 1
    return True

def red_nose_reports_pt1(puzzle):
    res = 0
    for level in puzzle:
        level = [int(i) for i in level.split()]
        if is_safe_sequence(level):
            res += 1
    return res

def red_nose_reports_pt2(puzzle):
    res = 0
    for level in puzzle:
        level = [int(i) for i in level.split()]
        
        if is_safe_sequence(level):
            res += 1
            continue
        
        n = len(level)
        safe_with_removal = False
        for i in range(n):
            # Create a new sequence with the i-th element removed
            new_level = level[:i] + level[i+1:]
            if is_safe_sequence(new_level):
                safe_with_removal = True
                break
        
        if safe_with_removal:
            res += 1

    return res

# reading input
with open("input.txt") as f:
    puzzle = f.readlines()

print("Part 1 Solution: " + str(red_nose_reports_pt1(puzzle)))
print("Part 2 Solution: " + str(red_nose_reports_pt2(puzzle)))
