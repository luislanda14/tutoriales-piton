# Day 1

with open("Day 1\data.txt") as datos:
    guardaSuma = []
    suma = 0
    num = 0
    sumaTotal = 0
    guardaNum = 0

    lines = datos.readlines()
    for line in lines:
        if line == '\n':
            num = num + 1
            guardaSuma.append(suma)
            if suma == max(guardaSuma):
                guardaNum = num
            suma = 0
        else:
            suma = suma + int(line)

    print(f"The elf {guardaNum} carries {max(guardaSuma)} calories.")

    guardaSuma.sort()

    for i in range (1,4):
        sumaTotal = sumaTotal + guardaSuma[len(guardaSuma)-i]

    print(f"The top 3 carries {sumaTotal} calories.")

#The elf 123 carries 72478 calories.
#The top 3 carries 210367 calories.