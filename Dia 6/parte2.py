def tiene_repetidos(lista_cuatro):
  
    n = 0
    for letrita in lista_cuatro:
        lista_cuatro[n] = 'aa'
        if letrita in lista_cuatro:
            lista_cuatro[n] = letrita
            return True
        else:
            lista_cuatro[n] = letrita      
        n = n + 1

    return False

with open('input.txt') as f:
    line = f.read()
    lista_letras = list(line)
    lista_cuatro = []
    for i in range(len(lista_letras)):
        if len(lista_cuatro) < 14:
            lista_cuatro.append(lista_letras[i])
        else:
            repetidos = tiene_repetidos(lista_cuatro)
            if repetidos: # si hay numeros repetidos
                lista_cuatro.pop(0)
                lista_cuatro.append(lista_letras[i])
            else: # si no hay repetidos
                print(i)
                break

# 3774