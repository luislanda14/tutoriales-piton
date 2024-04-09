with open('input.txt', 'r') as f:
    lines = f.readlines()
    score=0
    for line in lines:
        chars = line.split()
        if chars[1] == 'X': # need to lose
            if chars[0] == 'A': # opponent plays Rock
                score += 3+0
            elif chars[0] == 'B': # opponent plays Paper
                score += 1+0
            elif chars[0] == 'C': # opponent plays Scissors
                score += 2+0
        elif chars[1] == 'Y': # need to draw
            if chars[0] == 'A': # opponent plays Rock
                score += 1+3
            elif chars[0] == 'B': # opponent plays Paper
                score += 2+3
            elif chars[0] == 'C': # opponent plays Scissors
                score += 3+3
        elif chars[1] == 'Z': # need to win
            if chars[0] == 'A': # opponent plays Rock
                score += 2+6
            elif chars[0] == 'B': # opponent plays Paper
                score += 3+6
            elif chars[0] == 'C': # opponent plays Scissors
                score += 1+6

    print(score)

    # solucion parte 2: 13726