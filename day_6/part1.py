with open('input.txt') as f:
    line = f.read()   
    letters = [x for x in line]
    last_4=[]
    for i in range(len(letters)):
        if len(last_4) < 4:
            last_4.append(letters[i])
        else:
            last_4.pop(0)
            last_4.append(letters[i])
            if len(set(last_4)) == len(last_4):
                print(i+1)
                break

    #solucion = 1833