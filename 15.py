import os

def analizar_archivo(ruta_archivo):

    with open(ruta_archivo, 'w') as f:
        f.write("int contador = 10;\nfloat precio = 25.50;\ncontador = contador + 1;\n@")

    print(f"Leyendo archivo: {ruta_archivo}...")
    if os.path.exists(ruta_archivo):
        with open(ruta_archivo, 'r') as archivo:
            codigo_fuente = archivo.read()
            print("Contenido leído con éxito.")
    else:
        print("Error: Archivo no encontrado.")

analizar_archivo("programa.txt")