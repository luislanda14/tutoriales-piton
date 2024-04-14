with open('input.txt') as f:
    levels, instructions = [section.split("\n") for section in f.read().split("\n\n")]
    levels = [crate.replace("    ", " [X] ") for crate in levels[:-1]]  # Replace empty space with [X]
    levels = [[crate[1] for crate in level.split()] for level in levels]  # Get rid of brackets
    stacks = [[] for _ in range(len(levels[0]))]  # Create nested lists of number of vertical stacks
    for level in reversed(levels):
        for index, crate in enumerate(level):
            if crate != "X":
                stacks[index].append(crate)
    # .pop() get the top element
    # .append() add to the top
    for instruction in instructions:
        ints_only = [int(elem) for elem in instruction.split() if elem.isdigit()]
        if ints_only == []:
            break
        quantity = ints_only[0]
        from_stack = ints_only[1]-1
        to_stack = ints_only[2]-1
        if quantity == 1:
            stacks[to_stack].append(stacks[from_stack].pop())
        else:
            aux = []
            for i in range(quantity):
                aux.append(stacks[from_stack].pop())
            for element in reversed(aux):
                stacks[to_stack].append(element)
            
    solution = ''
    for stack in stacks:
        solution += str(stack[-1])

    print(solution)

    #solution = RGLVRCQSB