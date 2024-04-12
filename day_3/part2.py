import string

lowercase_dict = {char: index for index, char in enumerate(string.ascii_lowercase, start=1)}
uppercase_dict = {char: index for index, char in enumerate(string.ascii_uppercase, start=27)}
combined_dict = {**lowercase_dict, **uppercase_dict}


with open('input.txt') as f:
    lines = f.readlines()
    # divide the lines in groups of 3
    groups = [lines[i:i + 3] for i in range(0, len(lines), 3)]
    suma = 0
    for group in groups:
        for char in group[0]:
            if char in group[1] and char in group[2]:
                suma += combined_dict[char]
                break
    print(suma)
    

    # solucion parte 2: 2515