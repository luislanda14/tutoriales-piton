import string

lowercase_dict = {char: index for index, char in enumerate(string.ascii_lowercase, start=1)}
uppercase_dict = {char: index for index, char in enumerate(string.ascii_uppercase, start=27)}
combined_dict = {**lowercase_dict, **uppercase_dict}


with open('input.txt') as f:
    lines = f.readlines()
    suma = 0
    for line in lines:
        line = line.strip()
        first_half = line[:len(line)//2]
        second_half = line[len(line)//2:]
        for char in first_half:
            if char in second_half:
                suma += combined_dict[char]
                break  
    print(suma)

    # socucion parte 1 : 8085

    