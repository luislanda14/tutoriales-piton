with open('input.txt') as f:
    lines = f.readlines()
    puntos = 0
    for line in lines:
        lineas = line.split()
        
        if lineas[1] == 'X':
            if lineas[0] == 'A':
                puntos = puntos + 3
            elif  lineas[0] == 'B':
                puntos = puntos + 1
            elif  lineas[0] == 'C':
                puntos = puntos + 2
            puntos = puntos + 0

        elif lineas[1] == 'Y':
            if lineas[0] == 'A':
                puntos = puntos + 1
            elif  lineas[0] == 'B':
                puntos = puntos + 2
            elif  lineas[0] == 'C':
                puntos = puntos + 3
            puntos = puntos + 3
        elif lineas[1] == 'Z':
            if lineas[0] == 'A':
                puntos = puntos + 2
            elif  lineas[0] == 'B':
                puntos = puntos + 3
            elif  lineas[0] == 'C':
                puntos = puntos + 1      
            puntos = puntos + 6

print(puntos)

# 10238