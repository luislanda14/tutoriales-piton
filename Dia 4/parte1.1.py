with open('input.txt') as f:
    line = f.readlines()
    repetidos = 0
    for pareja in line:
        numeros = pareja.strip().split(",")
        numeros1 = numeros[0].split("-")
        numeros2 = numeros[1].split("-")
        if int(numeros1[0]) <= int(numeros2[0]) and int(numeros1[1]) >= int(numeros2[1]):
            repetidos = repetidos + 1
        elif int(numeros2[0]) <= int(numeros1[0]) and int(numeros2[1]) >= int(numeros1[1]):
            repetidos = repetidos + 1
    print(repetidos)

# 456 