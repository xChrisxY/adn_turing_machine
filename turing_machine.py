RIGHT = 1
LEFT = -1
STAY = 0

def validar_adn(secuencia):
    
    if not secuencia.startswith("ATG"):
        return False
    
    if "TATA" not in secuencia:
        return False

    if not (secuencia.endswith("TAG") or secuencia.endswith("TAA") or secuencia.endswith("TGA")):
        return False

    return True

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

