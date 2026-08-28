import re

def analisis_integral(codigo):
    patrones = [
        ('COMENTARIO',           r'//.*'),
        ('PALABRA_RESERVADA',    r'\b(if|int|float)\b'),
        ('CADENA_ERROR',         r'"[^"\n]*$'),                 # Cadena sin comilla de cierre
        ('CADENA',               r'"[^"]*"'),
        ('NUMERO_ERROR',         r'\d+(\.\d+){2,}'),            # Ej: 12.5.8
        ('IDENTIFICADOR_ERROR',  r'\d+[a-zA-Z_][a-zA-Z0-9_]*'), # Ej: 123abc
        ('NUMERO_DECIMAL',       r'\d+\.\d+'),
        ('NUMERO_ENTERO',        r'\d+'),
        ('IDENTIFICADOR',        r'[a-zA-Z_]\w*'),
        ('OPERADOR_RELACIONAL',  r'==|!=|>=|<=|>|<'),
        ('ASIGNACION',           r'='),
        ('OPERADOR_ARITMETICO',  r'[+\-*/]'),
        ('DELIMITADOR',          r'[()[\]{};,.]'),
        ('ESPACIO',              r'[ \t]+'),
        ('NUEVA_LINEA',          r'\n'),
        ('ERROR_LEXICO',         r'.') # Caracteres no permitidos (ej. @, #)
    ]
    regex = '|'.join(f'(?P<{n}>{p})' for n, p in patrones)

    tokens = []
    errores = []
    linea = 1
    inicio_linea = 0

    for m in re.finditer(regex, codigo):
        tipo = m.lastgroup
        lexema = m.group(tipo)
        columna = m.start() - inicio_linea + 1

        if tipo == 'NUEVA_LINEA':
            linea += 1
            inicio_linea = m.end()
        elif tipo == 'ESPACIO':
            continue
        elif 'ERROR' in tipo or tipo == 'ERROR_LEXICO':
            errores.append({'lexema': lexema, 'linea': linea, 'columna': columna, 'tipo': 'ERROR LEXICO'})
        else:
            tokens.append({'lexema': lexema, 'linea': linea, 'columna': columna, 'tipo': tipo})

    # Salida 1: Tabla de tokens (Ej. 17)
    print("=" * 60 + "\nTABLA DE TOKENS (Válidos)\n" + "=" * 60)
    for t in tokens:
        print(f"Línea: {t['linea']:<3} Col: {t['columna']:<3} | {t['tipo']:<20} | {t['lexema']}")

    # Salida 2: Reporte de errores (Ej. 18)
    print("\n" + "=" * 60 + "\nREPORTE DE ERRORES (Casos inválidos)\n" + "=" * 60)
    for e in errores:
        print(f"Entrada problematica: {e['lexema']}")
        print(f"Tipo de error:        {e['tipo']}")
        print(f"Línea: {e['linea']}, Columna: {e['columna']}")
        print("Acción:               Informar error y continuar el análisis\n" + "-"*40)

#prueba + casos inválidos
codigo_prueba = """int edad = 25;
float altura = 1.83;

if edad >= 18 {
    edad = edad + 1;
}
// Fin del programa

123abc
@usuario
"Hola
12.5.8
#contador
"""

analisis_integral(codigo_prueba)