with open('input.txt') as f:
    lines = f.readlines()
    current= 0
    calories_list = []
    for line in lines:
        if line != '\n':
            current += int(line)
        else :
            calories_list.append(current)
            current = 0
    
    print(max(calories_list))

    #solucion parte 1: 67450
       
        