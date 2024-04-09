with open('input.txt', 'r') as f:
    lines = f.readlines()
    score=0
    for line in lines:
        chars = line.split()
        if chars[1] == 'X': # i play Rock
            if chars[0] == 'A': # opponent plays Rock
                score += 4
            elif chars[0] == 'B': # opponent plays Paper
                score += 1
            elif chars[0] == 'C': # opponent plays Scissors
                score += 7
        elif chars[1] == 'Y': # i play Paper
            if chars[0] == 'A': # opponent plays Rock
                score += 8
            elif chars[0] == 'B': # opponent plays Paper
                score += 5
            elif chars[0] == 'C': # opponent plays Scissors
                score += 2
        elif chars[1] == 'Z': # i play Scissors
            if chars[0] == 'A': # opponent plays Rock
                score += 3
            elif chars[0] == 'B': # opponent plays Paper
                score += 9
            elif chars[0] == 'C': # opponent plays Scissors
                score += 6

    print(score)

    # solucion parte 1 : 12855