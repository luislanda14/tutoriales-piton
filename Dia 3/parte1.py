with open('input.txt') as f:
    lineastexto = f.readlines()
    listletrasrep = []
    for line in lineastexto:
        line = line.strip() 
        mitad = len(line) // 2
        primera_mitad = line[:mitad]
        segunda_mitad = line[mitad:]
        letras_prim_mitad = list(primera_mitad)
        letras_segu_mitad = list(segunda_mitad)
        for letra in letras_prim_mitad:
            if letra in letras_segu_mitad:
                listletrasrep.append(letra)
                break

    valor = 0
    for letrita1 in listletrasrep:
        if ord(letrita1) >= 97:
            valor = valor + ord(letrita1) - 96
        else:
            valor = valor + ord(letrita1) - 38
    print(valor)
    
    # 8243