with open('test.txt') as f:
    line = f.readlines()
    listfirstpart = []
    totalrepetidos = 0
    for pareja in line:
        listpairs = list(pareja)
        i = 0
        for element in listpairs:
            if element != ',':
                i = i + 1
            elif element == ',':
                nfirstpart = i   
        listfirstpart = listpairs[:nfirstpart]
        listsecpart = listpairs[nfirstpart + 1:]
        n1 = 0
        for element in listfirstpart:
            if element != '-':
                n1 = n1 + 1
            elif element == '-':
                elementn1 = n1
        primernum = ''.join(listfirstpart[:elementn1])
        segundonum = ''.join(listfirstpart[elementn1 + 1:])
        lista1 = []
        for num in range(int(primernum), int(segundonum) + 1):
            lista1.append(num)
        n2 = 0
        for element in listsecpart:
            if element != '-':
                n2 = n2 + 1
            elif element == '-':
                elementn2 = n2
        primernum = ''.join(listsecpart[:elementn2])
        segundonum = ''.join(listsecpart[elementn2 + 1:])
        lista2 = []
        for num in range(int(primernum), int(segundonum) + 1):
            lista2.append(num)
        print(lista1)
        print(lista2)
        repetido1 = 0
        for numero in lista1:
            if numero in lista2:
                repetido1 = repetido1 + 1
        if repetido1 == len(lista2):
            totalrepetidos = totalrepetidos + 1

        repetido2 = 0
        for numero in lista2:
            if numero in lista1:
                repetido2 = repetido2 + 1
        if repetido2 == len(lista1):
            totalrepetidos = totalrepetidos + 1
        print(totalrepetidos)