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
    if current != 0:
        calories_list.append(current)
    
    calories_list.sort()
    top3 = calories_list[-3] + calories_list[-2] + calories_list[-1]
    print(top3)
    

    #solucion parte 2: 199357
       
        