import re

def analizar_errores(codigo):
    patrones = [
        ('ASIGNACION',    r'='),
        ('NUMERO',        r'\d+'),
        ('IDENTIFICADOR', r'[a-zA-Z_][a-zA-Z0-9_]*'),
        ('DELIMITADOR',   r';'),
        ('ESPACIO',       r'\s+'),
        ('ERROR_LEXICO',  r'.') #xualquier carácter que no hizo match arriba
    ]
    regex = '|'.join(f'(?P<{n}>{p})' for n, p in patrones)

    for match in re.finditer(regex, codigo):
        tipo = match.lastgroup
        lexema = match.group(tipo)
        if tipo == 'ESPACIO': continue

        if tipo == 'ERROR_LEXICO':
            print(f"ERROR LEXICO: Carácter no reconocido '{lexema}'")
            print("Acción: informar error y continuar el análisis\n")
        else:
            print(f"{tipo:<20} | {lexema}")

# Prueba con el caso del TP
analizar_errores('A = 10 @ B;')