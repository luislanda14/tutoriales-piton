with open('input.txt') as f:
    lineastexto = f.readlines()
    listletrasrep = []

    grupos_de_tres = []
    for i in range(0, len(lineastexto), 3):
        grupo = lineastexto[i:i+3]  # Obtener los siguientes tres elementos
        grupos_de_tres.append(grupo)  # Agregar el grupo a la lista de grupos

    for group in grupos_de_tres: 
        primero = group[0]
        segundo = group[1]
        tercero = group[2]
        letras_prim= list(primero)
        letras_segu = list(segundo)
        letras_terc = list(tercero)
        for letra in letras_prim:
            if letra in letras_segu and letra in letras_terc:
                listletrasrep.append(letra)
                break

    valor = 0
    for letrita1 in listletrasrep:
        if ord(letrita1) >= 97:
            valor = valor + ord(letrita1) - 96
        else:
            valor = valor + ord(letrita1) - 38
    print(valor)

    # 2631