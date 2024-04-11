# Day 2

with open('Day 2/data.txt') as datos:
    lines = datos.readlines()

    score1 = 0
    score2 = 0

    for line in lines:
        if line[0] == 'A':
            if line[2] == 'X':
                score1 = score1 + 4
                score2 = score2 + 3
            elif line[2] == 'Y':
                score1 = score1 + 8
                score2 = score2 + 4
            elif line[2] == 'Z':
                score1 = score1 + 3
                score2 = score2 + 8
        if line[0] == 'B':
            if line[2] == 'X':
                score1 = score1 + 1
                score2 = score2 + 1
            elif line[2] == 'Y':
                score1 = score1 + 5
                score2 = score2 + 5
            elif line[2] == 'Z':
                score1 = score1 + 9
                score2 = score2 + 9
        if line[0] == 'C':
            if line[2] == 'X':
                score1 = score1 + 7
                score2 = score2 + 2
            elif line[2] == 'Y':
                score1 = score1 + 2
                score2 = score2 + 6
            elif line[2] == 'Z':
                score1 = score1 + 6
                score2 = score2 + 7
print(f'El score 1 es: {score1}\nEl score 2 es: {score2}')

# El score 1 es: 13682
# El score 2 es: 12881