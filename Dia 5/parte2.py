with open('input.txt') as f:
    line = f.readlines()
    salto = line.index('\n')
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
    parar = False
    ns = 0
    while not parar:
        sublista = listas_hor1[0 + len(numeros)*ns:len(numeros) + len(numeros)*ns]
        ns = ns + 1
        if len(sublista) != 0:
            listas_hor2.append(sublista)
        else:
            parar = True
    resultfinal = []
    listas_verticales = [[] for _ in range(len(numeros))]
    for linea in listas_hor2:
        n = 0
        for elemento in linea:
            if elemento != ' ':
                listas_verticales[n].append(elemento)
            n = n + 1
    for lista in listas_verticales:
        lista.reverse()
    for movimiento in move:
        lista_mov = movimiento.split()
        n = lista_mov[1]
        de = lista_mov[3]
        a = lista_mov[5]
        listas_cambios = []
        for _ in range(int(n)):
            elem = listas_verticales[int(de) - 1].pop()
            listas_cambios.append(elem)
        listas_cambios.reverse()
        for change in listas_cambios:
            listas_verticales[int(a) - 1].append(change)
    for n in numeros:
        resultn = listas_verticales[int(n) - 1].pop()
        resultfinal.append(resultn)
    print(''.join(resultfinal))

# RNLFDJMCT