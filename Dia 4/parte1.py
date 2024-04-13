with open('input.txt') as f:
    line = f.readlines()
    listfirstpart = []
    repetidos = 0
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
        
        if int(lista1[0]) <= int(lista2[0]) and int(lista1[-1]) >= int(lista2[-1]):
            repetidos = repetidos + 1
        elif int(lista2[0]) <= int(lista1[0]) and int(lista2[-1]) >= int(lista1[-1]):
            repetidos = repetidos + 1
    print(repetidos)

# 456