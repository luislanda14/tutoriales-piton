#Day 3

with open(r'C:\\Coding\\tutoriales-piton\Day 3\data.txt') as datos:
    lines = datos.readlines()
    iguales = []
    suma = 0
    for line in lines:
        match = False
        for i in range (0, (len(line) - 1) // 2 - 1):
            if match:
                continue
            for j in range((len(line) - 1) // 2, len(line) - 2):
                if match:
                    continue
                if line[i] == line [j]:
                    iguales.append(line[i])  
                    match = True

    print(len(iguales))
    
    for s in iguales:
        if s.isupper():
            suma = suma + ord(s) - ord('A') + 27
        else:
            suma = suma + ord(s) - ord('a') + 1
    print(suma)