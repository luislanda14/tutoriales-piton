import argparse
import string

def procesar_archivo(input_path):
    datos = None
    with open(input_path, 'r') as f:
        datos = f.readlines()
    
    if datos is None:
        print("No se pudo leer el archivo")
        return

    return [d.strip() for d in datos]

def guardar_archivo(datos):
    file_name = "salida.out"
    with open(file_name, 'w') as f:
        f.write(str(datos))
    
    print(f"Resultados guardados en '{file_name}'.")


def main(input_path):
    datos = procesar_archivo(input_path)

    # Comprobación inicial
    num_items_group = 3 # Numero de elementos de cada grupo
    if len(datos) % num_items_group != 0:
        print("El numero de lineas no es divisible entre el numero de elementos por grupo")
        exit(1)

    # Generamos la tabla de puntuaciones
    abcdario = string.ascii_lowercase + string.ascii_uppercase
    punt_table = {}
    for i, elm in enumerate(abcdario):
        punt_table[elm] = i+1
    #print(punt_table)

    # Creamos los grupos de elfos
    grupos = []
    grupo = []    
    for line in datos:
        line = line.strip()
        grupo.append(line)

        if len(grupo) == num_items_group:
            grupos.append(grupo)
            grupo = [] # Nuevo grupo
    
    final_score = 0
    for grupo in grupos:
        
        # Calculamos las apariciones de los carácteres
        apariciones = {}
        for bolsa in grupo:
            aux = {}
            for e in bolsa:
                # recorremos los carácteres de cada bolsa
                if e not in aux:
                    if e not in apariciones:
                        apariciones[e] = 1
                    else:
                        apariciones[e] +=1
                    aux[e]= None
                

        comunes = []
        for a in apariciones:
            if apariciones[a] == num_items_group:
                comunes.append(a)

        # Calculamos la puntuación
        score = 0
        for elm in comunes:
            score += punt_table[elm]
        
        final_score += score
    
    print(final_score)
    #guardar_archivo(final_score)

if __name__ == "__main__":
    #Argumentos de entrada
    parser = argparse.ArgumentParser(description='Script para Advent of Code Día 3 parte 2')
    parser.add_argument('input', type=str, help='Archivo de entrada de datos')
    
    args = parser.parse_args()

    main(args.input)
