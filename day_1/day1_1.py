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

def main(input_path):
    datos = procesar_archivo(input_path)
    

    # Elfs
    elfs = []
    cur_elf = 0
    for d in datos:        
        if d == '':
            elfs.append(cur_elf)
            cur_elf = 0
            continue

        cur_elf += int(d)

    # Elf with most calories
    print(max(elfs))
    #guardar_archivo(max(elfs))
    


if __name__ == "__main__":
    #Argumentos de entrada
    parser = argparse.ArgumentParser(description='Script para Advent of Code Día 1 parte 1')
    parser.add_argument('input', type=str, help='Archivo de entrada de datos')
    
    args = parser.parse_args()

    main(args.input)
