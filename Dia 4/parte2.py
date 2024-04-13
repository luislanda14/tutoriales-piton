with open('input.txt') as f:
    line = f.readlines()
    repetidos = 0
    for pareja in line:
        numeros = pareja.strip().split(",")
        numeros1 = numeros[0].split("-")
        numeros2 = numeros[1].split("-")
        listanumeros1 = []
        listanumeros2 = []
        for num in range(int(numeros1[0]), int(numeros1[1]) + 1):
            listanumeros1.append(num)
        for num in range(int(numeros2[0]), int(numeros2[1]) + 1):
            listanumeros2.append(num)
        for num1 in listanumeros1:
            if num1 in listanumeros2:
                repetidos = repetidos + 1
                break
    print(repetidos)

# 808