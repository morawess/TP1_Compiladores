import re

def analizar_base(codigo):
    patrones = [
        ('COMENTARIO',          r'//.*'),
        ('CADENA',              r'"[^"]*"'),
        ('OPERADOR_RELACIONAL', r'==|!=|>=|<=|>|<'),
        ('ASIGNACION',          r'='),
        ('OPERADOR_ARITMETICO', r'[+\-*/]'),
        ('NUMERO',              r'\d+(\.\d+)?'),
        ('IDENTIFICADOR',       r'[a-zA-Z_][a-zA-Z0-9_]*'),
        ('DELIMITADOR',         r'[()[\]{};,.]'),
        ('ESPACIO',             r'\s+')
    ]
    regex = '|'.join(f'(?P<{nombre}>{patron})' for nombre, patron in patrones)

    print(f"{'TOKEN':<20} | {'LEXEMA'}")
    print("-" * 40)
    for match in re.finditer(regex, codigo):
        tipo = match.lastgroup
        lexema = match.group(tipo)

        if tipo in ['ESPACIO', 'COMENTARIO']:#manejo de espacios y comentarios
            continue
        print(f"{tipo:<20} | {lexema}")

analizar_base('nombre = "Juan"; // Asignacion\nedad >= 18;')