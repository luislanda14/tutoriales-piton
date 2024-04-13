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


# 0 loose | 3 draw | 6 win
win_table = {
    ("A", "X"): 3,
    ("A", "Y"): 6,
    ("A", "Z"): 0,
    ("B", "X"): 0,
    ("B", "Y"): 3,
    ("B", "Z"): 6,
    ("C", "X"): 6,
    ("C", "Y"): 0,
    ("C", "Z"): 3,
}

result_table = {
    "X": 0,
    "Y": 3,
    "Z": 6
}

# 1 rock \ 2 paper | 3 scissors
choose_table = {
    "X": 1,
    "Y": 2,
    "Z": 3
}

def main(input_path):
    datos = procesar_archivo(input_path)

    score = 0
    for line in datos:
        line = line.strip().split()
        opponent = line[0]
        result   = result_table[line[1]]
        player = None

        for elm in win_table:
            if win_table[elm] == result and elm[0] == opponent:
                player = elm[1]
                break
        
        score += choose_table[player] + result

    print(score)
    #guardar_archivo(score)

if __name__ == "__main__":
    #Argumentos de entrada
    parser = argparse.ArgumentParser(description='Script para Advent of Code Día 2 parte 2')
    parser.add_argument('input', type=str, help='Archivo de entrada de datos')
    
    args = parser.parse_args()

    main(args.input)
