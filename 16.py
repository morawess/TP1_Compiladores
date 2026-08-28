def generar_tabla(lista_tokens):
    print("=" * 60)
    print(f"{'Linea':<8} | {'Columna':<8} | {'Token':<22} | {'Lexema'}")
    print("=" * 60)
    for t in lista_tokens:
        print(f"{t['linea']:<8} | {t['columna']:<8} | {t['tipo']:<22} | {t['lexema']}")
    print("-" * 60)

tokens_simulados = [
    {'linea': 1, 'columna': 1, 'tipo': 'PALABRA_RESERVADA', 'lexema': 'int'},
    {'linea': 1, 'columna': 5, 'tipo': 'IDENTIFICADOR', 'lexema': 'contador'},
    {'linea': 1, 'columna': 14, 'tipo': 'ASIGNACION', 'lexema': '='},
    {'linea': 1, 'columna': 16, 'tipo': 'NUMERO', 'lexema': '10'}
]

generar_tabla(tokens_simulados)