import re

def demostrar_prioridad(codigo):
    patrones = [
        ('OPERADOR_RELACIONAL', r'==|!=|>=|<=|>|<'),
        ('ASIGNACION',          r'='),
        ('IDENTIFICADOR',       r'[a-zA-Z_]+'),
        ('DELIMITADOR',         r';'),
        ('ESPACIO',             r'\s+')
    ]
    regex = '|'.join(f'(?P<{n}>{p})' for n, p in patrones)

    for match in re.finditer(regex, codigo):
        if match.lastgroup != 'ESPACIO':
            print(f"{match.lastgroup:<20} | {match.group(match.lastgroup)}")

print("Caso 1 (Asignación):")
demostrar_prioridad('A = B;')
print("\nCaso 2 (Relacional):")
demostrar_prioridad('A == B;')