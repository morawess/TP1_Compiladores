import re
import os
import sys

class AnalizadorLexico:
    def __init__(self):
        self.tokens = []
        self.errores = []
        self.lineas_analizadas = 0

        self.patrones = [
            ('COMENTARIO',           r'//.*'),
            ('PALABRA_RESERVADA',    r'\b(if|then|else|while|for|def|return|int|float|string|bool)\b'),
            ('CADENA',               r'"[^"]*"'),
            ('NUMERO_ERROR',         r'\d+(\.\d+){2,}'),
            ('IDENTIFICADOR_ERROR',  r'\d+[a-zA-Z_][a-zA-Z0-9_]*'),
            ('CADENA_ERROR',         r'"[^"\n]*$'),
            ('NUMERO_DECIMAL',       r'\d+\.\d+'),
            ('NUMERO_ENTERO',        r'\d+'),
            ('IDENTIFICADOR',        r'[a-zA-Z_][a-zA-Z0-9_]*'),
            ('OPERADOR_RELACIONAL',  r'==|!=|>=|<=|>|<'),
            ('ASIGNACION',           r'='),
            ('OPERADOR_ARITMETICO',  r'[+\-*/]'),
            ('DELIMITADOR',          r'[()[\]{};,.]'),
            ('ESPACIO',              r'[ \t]+'),
            ('NUEVA_LINEA',          r'\n'),
            ('ERROR_LEXICO',         r'.')
        ]

        self.regex_unificada = '|'.join(f'(?P<{nombre}>{patron})' for nombre, patron in self.patrones)

    def analizar(self, codigo):
        self.tokens.clear()
        self.errores.clear()
        linea_actual = 1
        inicio_linea = 0

        for coincidencia in re.finditer(self.regex_unificada, codigo):
            tipo = coincidencia.lastgroup
            lexema = coincidencia.group(tipo)

            columna = coincidencia.start() - inicio_linea + 1

            if tipo == 'NUEVA_LINEA':
                linea_actual += 1
                inicio_linea = coincidencia.end()
            elif tipo == 'ESPACIO':
                continue
            elif tipo == 'COMENTARIO':
                self.tokens.append({'tipo': tipo, 'lexema': lexema, 'linea': linea_actual, 'columna': columna})
            elif tipo in ['ERROR_LEXICO', 'NUMERO_ERROR', 'IDENTIFICADOR_ERROR', 'CADENA_ERROR']:
                self.errores.append({'lexema': lexema, 'linea': linea_actual, 'columna': columna})
            else:
                self.tokens.append({'tipo': tipo, 'lexema': lexema, 'linea': linea_actual, 'columna': columna})

        self.lineas_analizadas = linea_actual

    def mostrar_tokens(self):
        print("\n" + "="*60)
        print(f"{'Linea':<8} {'Columna':<10} {'Token':<22} {'Lexema'}")
        print("-" * 60)
        for t in self.tokens:
            print(f"{t['linea']:<8} {t['columna']:<10} {t['tipo']:<22} {t['lexema']}")
        print("="*60)

    def mostrar_errores(self):
        print("\n" + "="*40)
        print("          ERRORES LÉXICOS")
        print("="*40)
        if not self.errores:
            print("No se encontraron errores léxicos.")
        else:
            for i, err in enumerate(self.errores, 1):
                print(f"\nError {i}")
                print(f"Tipo de error: ERROR LEXICO")
                print(f"Lexema/carácter problemático: {err['lexema']}")
                print(f"Línea: {err['linea']}")
                print(f"Columna: {err['columna']}")
                print("Acción: informar error y continuar el análisis")
        print("="*40)

    def mostrar_estadisticas(self):
        print("\n" + "="*40)
        print("       RESULTADO DEL ANÁLISIS")
        print("="*40)
        print(f"Tokens reconocidos: {len(self.tokens)}")
        print(f"Errores léxicos: {len(self.errores)}")
        print(f"Líneas analizadas: {self.lineas_analizadas}")
        print("="*40)

def menu():
    lexer = AnalizadorLexico()

    while True:
        print("\n========================================")
        print("           ANALIZADOR LÉXICO")
        print("========================================")
        print("1. Ingresar cadena")
        print("2. Analizar archivo")
        print("3. Mostrar tokens")
        print("4. Mostrar errores")
        print("5. Mostrar estadísticas")
        print("6. Salir")

        opcion = input("\nSeleccione una opción: ")

        if opcion == '1':
            codigo = input("Ingrese el código a analizar:\n")
            lexer.analizar(codigo)
            print("\n¡Análisis completado!")
        elif opcion == '2':
            ruta = input("Ingrese el nombre del archivo (ej: programa.txt): ")
            if os.path.exists(ruta):
                with open(ruta, 'r', encoding='utf-8') as archivo:
                    lexer.analizar(archivo.read())
                print("\n¡Análisis completado!")
            else:
                print("\nError: El archivo no existe.")
        elif opcion == '3':
            lexer.mostrar_tokens()
        elif opcion == '4':
            lexer.mostrar_errores()
        elif opcion == '5':
            lexer.mostrar_estadisticas()
        elif opcion == '6':
            print("Saliendo del programa...")
            sys.exit(0)
        else:
            print("Opción inválida.")

if __name__ == '__main__':
    menu()