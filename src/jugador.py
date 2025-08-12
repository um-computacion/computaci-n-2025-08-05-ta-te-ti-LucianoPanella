class jugador:
    def __init__(self, nombre, simbolo):
        """
        Inicializa un jugador con nombre y símbolo (X o O).
        """
        self.nombre = nombre
        self.simbolo = simbolo

    def __str__(self):
        return f"Jugador: {self.nombre} Ficha: ({self.simbolo})"
        juego.tablero.poner_la_ficha(0,0,"X")