RIGHT = 1
LEFT = -1
STAY = 0

def validar_adn(secuencia):
    estado = 'q0'
    cinta = list(secuencia) + ['□']
    cabezal = 0

    transiciones_validacion = {
        ('q0', 'A'): ('q0', 'A', RIGHT),
        ('q0', 'T'): ('q0', 'T', RIGHT),
        ('q0', 'C'): ('q0', 'C', RIGHT),
        ('q0', 'G'): ('q0', 'G', RIGHT),
        ('q0', '□'): ('q_accept', '□', STAY),
    }

    while estado != 'q_accept' and estado != 'q_reject':
        simbolo_actual = cinta[cabezal]
        if (estado, simbolo_actual) in transiciones_validacion:
            nuevo_estado, simbolo_escrito, direccion = transiciones_validacion[(estado, simbolo_actual)]
            cinta[cabezal] = simbolo_escrito
            estado = nuevo_estado
            cabezal += direccion
        else:
            estado = 'q_reject'

    return estado == 'q_accept'

def encontrar_patron(secuencia, patron):
    if not validar_adn(secuencia):
        print("La secuencia de ADN no es válida.")
        return False

    if patron in secuencia:
        print(f"Patrón '{patron}' encontrado en la secuencia.")
        return True
    else:
        print(f"Patrón '{patron}' no encontrado en la secuencia.")
        return False
