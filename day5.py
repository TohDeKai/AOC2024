def print_queue_pt1(puzzle):
    """
    approach
    while iterating through the front part, the rules
    save it in a dictionary where right will be the key and left will be the value

    then when it reaches the pages
    for every line
    have a dict to count occurrence of number
    at each number, check the rule dict. if it is in rule dict, find the value.
    check if value has occurred. if not, break. if yes continue.
    if it reaches the end, find middle number add to res
    """
    rules_dict = {}

    # Find the index of the empty string
    empty_index = puzzle.index('')

    # Split the list
    rules = puzzle[:empty_index]
    pages = puzzle[empty_index + 1:]

    res = 0
    for pair in rules:
        if pair == "":
            break
        pair = pair.split("|")
        left, right = pair[0], pair[1]

        if right not in rules_dict:
            rules_dict[right] = []
        rules_dict[right].append(left)
    
    for line in pages:
        line = line.split(",")
        count = {}
        correct = True
        for num in line:
            if num not in count:
                count[num] = 0
        
        for num in line:
            count[num] = 1
            if num in rules_dict:
                for i in rules_dict[num]:
                    if i in count and count[i] == 0:
                        correct = False
                        break
                
        if correct:
            res += int(line[len(line)//2])

    return res
        


def print_queue_pt2(puzzle):
    pass

        


# reading input
with open("input.txt") as f:
    puzzle = [line.strip() for line in f.readlines()]


print("Part 1 Solution: " + str(print_queue_pt1(puzzle)))
print("Part 2 Solution: " + str(print_queue_pt2(puzzle)))