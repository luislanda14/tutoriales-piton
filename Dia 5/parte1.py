with open('test.txt') as f:
    line = f.readlines()
    salto=line.index('\n')
    parte_1 = line[:salto]
    numeros = parte_1[-1].split()
    move = line[salto + 1:]
    lista_hor = []
    for x in parte_1[:-1]:
        lista_hor.append([x])
    listas_hor1 = []
    listas_hor2 = []
    for i in lista_hor:
        for el in i:
            for n in range(len(numeros)):
                listas_hor1.append(el[1 + 4*n])
    parar = 0
    ns = 0
    while parar == 0:
        sublista = listas_hor1[0 + len(numeros)*ns:len(numeros) + len(numeros)*ns]
        ns = ns + 1
        listas_hor2.append(sublista)
        if len(sublista) == 0:
            parar = 1 
        
    resultfinal = []
    listas_hor2.pop()
    print((listas_hor2))
    lista_ver = []
    for n in numeros:
        sublista_ver1 = []
        for l in numeros:
            sublista_ver = listas_hor2[int(l) - 1][int(n) - 1]
            sublista_ver1.append(sublista_ver)
        print(sublista_ver1, 'aaaa')
        lista_ver.append(sublista_ver)
        

    """for movimiento in move:
        n = movimiento[5]
        de = movimiento[12]
        a = movimiento[17]
        for _ in range(int(n)):
            elem = listas_ver1[int(de) - 1].pop()
            listas_ver1[int(a) -1].append(elem)
    for n in numeros:
        resultn = listas_ver1[int(n) - 1].pop()
        resultfinal.append(resultn)
    print(''.join(resultfinal))"""
    
    
        
       

    
            