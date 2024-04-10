with open('input.txt') as f:
    lines = f.readlines()
    suma  = 0
    listasumas = []
    for line in lines:
        if line!='\n':
            suma = suma + int(line)   
        else:
            listasumas.append(suma)
            suma = 0
    if suma!=0:
        listasumas.append(suma)
listasumas.sort(reverse=True)
suma3mayores = listasumas[0] + listasumas[1] + listasumas[2]
print(suma3mayores)