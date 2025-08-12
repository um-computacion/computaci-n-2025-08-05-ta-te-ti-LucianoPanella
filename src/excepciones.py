class SimboloInvalidoError(Exception):
    """El símbolo del jugador no es válido (debe ser 'X' o 'O')."""
    pass

class CasilleroOcupadoError(Exception):
    """Se intenta jugar en un casillero ya ocupado."""
    pass

class MovimientoInvalidoError(Exception):
    """El movimiento está fuera del tablero o no es permitido."""
    pass