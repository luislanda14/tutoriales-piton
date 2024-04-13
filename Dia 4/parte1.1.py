with open('input.txt') as f:
    line = f.readlines()
    repetidos = 0
    for pareja in line:
        numeros = pareja.strip().split(",")
        numeros1 = numeros[0].split("-")
        numeros2 = numeros[1].split("-")
        if numeros1[0] <= numeros2[0] and numeros1[1] >= numeros2[1]:
            repetidos = repetidos + 1
        elif numeros2[0] <= numeros1[0] and numeros2[1] >= numeros1[1]:
            repetidos = repetidos + 1
    print(repetidos)