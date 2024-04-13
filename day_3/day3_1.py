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

    # Generamos la tabla de puntuaciones
    abcdario = string.ascii_lowercase + string.ascii_uppercase
    punt_table = {}
    for i, elm in enumerate(abcdario):
        punt_table[elm] = i+1
    #print(punt_table)

    # Procesamos los datos de entrada
    final_score = 0
    for line in datos:
        line = line.strip()

        # Encontrar los items que se repiten
        num_items = len(line)
        if num_items % 2 != 0:
            print("El numero de items es impar")
            exit(1)

        center_index = int(num_items / 2)
        bolsillo_A = line[:center_index]
        bolsillo_B = line[center_index:]

        # Búsqueda cuadrática
        comunes = {}
        for a in bolsillo_A:
            for b in bolsillo_B:
                if a == b:
                    # igual lo preguntan en el apartado 2
                    if a not in comunes:
                        comunes[a] = 0
                    else:
                        comunes[a] += 1

        # Calculamos la puntuación
        score = 0
        for elm in comunes:
            score += punt_table[elm]
        
        final_score += score
    
    print(final_score)
    #guardar_archivo(final_score)

if __name__ == "__main__":
    #Argumentos de entrada
    parser = argparse.ArgumentParser(description='Script para Advent of Code Día 3 parte 1')
    parser.add_argument('input', type=str, help='Archivo de entrada de datos')
    
    args = parser.parse_args()

    main(args.input)
