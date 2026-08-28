import re

def analizar_posiciones(codigo):
    patrones = [
        ('PALABRA_RESERVADA', r'\b(?:int|float)\b'),
        ('IDENTIFICADOR',     r'[a-zA-Z_]\w*'),
        ('NUMERO',            r'\d+(\.\d+)?'),
        ('ASIGNACION',        r'='),
        ('DELIMITADOR',       r';'),
        ('NUEVA_LINEA',       r'\n'),
        ('ESPACIO',           r'[ \t]+')
    ]
    regex = '|'.join(f'(?P<{n}>{p})' for n, p in patrones)

    linea = 1
    inicio_linea = 0

    print(f"{'LINEA':<6} | {'COLUMNA':<8} | {'TOKEN':<18} | {'LEXEMA'}")
    for match in re.finditer(regex, codigo):
        tipo = match.lastgroup
        lexema = match.group(tipo)
        columna = match.start() - inicio_linea + 1

        if tipo == 'NUEVA_LINEA':
            linea += 1
            inicio_linea = match.end()
        elif tipo not in ['ESPACIO']:
            print(f"{linea:<6} | {columna:<8} | {tipo:<18} | {lexema}")

analizar_posiciones("int contador = 10;\nfloat precio = 25.50;")