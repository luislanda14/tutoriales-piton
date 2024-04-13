import argparse

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


def generate_range(range_repr: str) -> list:
    """El input es un string que representa un rango:
        2-4    
    """
    range_repr = range_repr.split('-')
    start   = int(range_repr[0])
    stop    = int(range_repr[1]) +1 # Para que incluya el ultimo elemento

    return list(range(start, stop))

def is_contained(listA: list, listB: list) -> bool:
    """Comprueba si la lista B está contenida en la lista A.
        La lista B debe tener menos o los mismos elementos que la A
    """

    for a in listA:
        try:
            listB.remove(a)
        except:
            # a no está en la lista. Continuamos
            pass
    
    return len(listB) == 0

def main(input_path):
    datos = procesar_archivo(input_path)

    # Procesar los datos de entrada
    count = 0
    for line in datos:
        line = line.strip().strip().split(',')

        # Generamos los rangos para poder iterarlos
        elfA = generate_range(line[0])
        elfB = generate_range(line[1])
        
        esta_contenida = False
        if len(elfA) >= len(elfB):
            esta_contenida = is_contained(elfA, elfB)
        else:
            esta_contenida = is_contained(elfB, elfA)

        if esta_contenida:
            count += 1

    print(count)
    #guardar_archivo(final_score)

if __name__ == "__main__":
    #Argumentos de entrada
    parser = argparse.ArgumentParser(description='Script para Advent of Code Día 4 parte 1')
    parser.add_argument('input', type=str, help='Archivo de entrada de datos')
    
    args = parser.parse_args()

    main(args.input)
